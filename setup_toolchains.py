import argparse
import os

_AVAILABLE_TOOLCHAINS = [
    {
        'host_arch': 'x86_64',
        'host_os': 'linux',
        'target': 'arm-none-eabi',
        'version': '12.3.rel1',
        'sha256': '12a2815644318ebcceaf84beabb665d0924b6e79e21048452c5331a56332b309',
    },
]

# GCC cpu options: https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html#index-mcpu-2
_ALL_CPU = [
    'cortex-m0',
    'cortex-m0plus',
    'cortex-m1',
    'cortex-m3',
    'cortex-m4',
    'cortex-m7',
    'cortex-m7+nofp.dp',
    'cortex-a8',
    'cortex-a9',
]

_ALL_TOOLS = [
    'ar',
    'as',
    'cpp',
    'gcc',
    'gcov',
    'gdb',
    'ld',
    'nm',
    'objcopy',
    'objdump',
    'readelf',
    'strip',
]


def create_wrappers(toolchain_dir, root_dir):
  for toolchain in _AVAILABLE_TOOLCHAINS:
    host_os_name = '' if toolchain['host_os'] == 'linux' else "-" + toolchain['host_os']
    name = ('arm-gnu-toolchain-' +
            f'{toolchain["version"]}-{toolchain["host_arch"]}{host_os_name}-{toolchain["target"]}')
    toolchain['name'] = name

    target_os = 'linux' if 'linux' in toolchain['target'] else 'none'
    toolchain['target_os'] = target_os

    wrapper_dir = os.path.join(toolchain_dir, 'tool_wrappers', toolchain['host_arch'],
                               toolchain['host_os'], toolchain['target'], toolchain['version'])
    try:
      os.makedirs(wrapper_dir)
    except FileExistsError:
      pass

    # Populate empty BUILD files.
    wrapper_dirs = os.path.relpath(wrapper_dir, toolchain_dir).split(os.path.sep)
    for i in range(1, len(wrapper_dirs)):
      with open(os.path.join(toolchain_dir, *wrapper_dirs[:-i], 'BUILD'), 'w') as f:
        pass

    toolchain['wrapper_dir'] = os.path.relpath(wrapper_dir, root_dir)
    toolchain['wrapper_paths'] = {}

    build_file = '''\
filegroup(
    name = "wrappers",
    srcs = glob(["*"]),
    visibility = ["//visibility:public"],
)

'''

    for tool in _ALL_TOOLS:
      tool_name = f'{toolchain["target"]}-{tool}'
      wrapper_path = os.path.join(wrapper_dir, tool_name)
      toolchain['wrapper_paths'][tool] = os.path.relpath(wrapper_path, toolchain_dir)

      build_file += f'''\
sh_binary(
    name = "{tool}",
    srcs = [":{tool_name}"],
    data = ["@{name}//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

'''

      with open(wrapper_path, 'w') as f:
        f.write(f'''\
#!/bin/bash

TOOL_PATH={name}/bin/{tool_name}

# First check if we can find the executable directly and then revert to runfiles.
# This is necessary because when used in the toolchain, the runfiles library is not available.
if [[ -f external/${{TOOL_PATH}} ]]; then
  exec external/${{TOOL_PATH}} $@
fi

# --- begin runfiles.bash initialization v3 ---
# Copy-pasted from the Bazel Bash runfiles library v3.
set -uo pipefail; set +e; f=bazel_tools/tools/bash/runfiles/runfiles.bash
source "${{RUNFILES_DIR:-/dev/null}}/$f" 2>/dev/null || \\
  source "$(grep -sm1 "^$f " "${{RUNFILES_MANIFEST_FILE:-/dev/null}}" | cut -f2- -d' ')" 2>/dev/null || \\
  source "$0.runfiles/$f" 2>/dev/null || \\
  source "$(grep -sm1 "^$f " "$0.runfiles_manifest" | cut -f2- -d' ')" 2>/dev/null || \\
  source "$(grep -sm1 "^$f " "$0.exe.runfiles_manifest" | cut -f2- -d' ')" 2>/dev/null || \\
  {{ echo>&2 "ERROR: cannot find $f"; exit 1; }}; f=; set -e
# --- end runfiles.bash initialization v3 ---

exec $(rlocation ${{TOOL_PATH}}) $@\n')
''')

      os.chmod(wrapper_path, 0o777)

    build_path = os.path.join(wrapper_dir, 'BUILD')
    with open(build_path, 'w') as f:
      f.write(build_file[:-2])


def write_toolchain_info(filename):
  with open(filename, 'w') as f:
    f.write(f'AVAILABLE_TOOLCHAINS = {_AVAILABLE_TOOLCHAINS}\n')
    f.write(f'ALL_CPU = {_ALL_CPU}\n')


def write_test_script(filename):
  with open(filename, 'w') as f:
    f.write('#!/bin/bash\n')
    f.write('set -e\n')
    f.write('set -o xtrace\n\n')

    f.write('bazel clean\n')
    for toolchain in _AVAILABLE_TOOLCHAINS:
      for cpu in _ALL_CPU:
        platform = f'//platforms:{cpu}-{toolchain["target_os"]}-{toolchain["version"]}'
        f.write(f'bazel build -s --verbose_failures --platforms={platform} //test:test_cpp\n')
        f.write(f'bazel build -s --verbose_failures --platforms={platform} //test:test_c\n')

    f.write('bazel run --verbose_failures //test:objdump -- --help\n')
    f.write(
        'bazel build -s --verbose_failures --platforms=//platforms:cortex-m0plus-none-12.3.rel1 //test:objdump_output\n'
    )

  os.chmod(filename, 0o777)


def main():
  parser = argparse.ArgumentParser(description='Generate wrapper scripts for Bazel toolchains.')
  args = parser.parse_args()

  root_dir = os.path.dirname(os.path.realpath(__file__))

  create_wrappers(os.path.join(root_dir, 'toolchains'), root_dir)
  write_toolchain_info(os.path.join(root_dir, 'toolchains/toolchain_info.bzl'))
  write_test_script(os.path.join(root_dir, 'test_build_all.sh'))


if __name__ == '__main__':
  main()
