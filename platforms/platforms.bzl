load("@bazel_arm_toolchains//toolchains:toolchain_info.bzl", "ALL_CPU", "AVAILABLE_TOOLCHAINS")

def all_platforms():
    for toolchain in AVAILABLE_TOOLCHAINS:
        for cpu in ALL_CPU:
            name = "{}-{}-{}-{}".format(toolchain["host_os"], cpu, toolchain["target_os"], toolchain["version"])

            # Bazel uses "macos" instead of "darwin" in @platforms; however, arm refers to the toolchain
            # host as "darwin". We chose to use "darwin" in this repository to follow arms convention and do a
            # simple string replacement here to be compatible with bazel.
            os_constraint_name = toolchain["target_os"].replace("darwin", "macos")

            native.platform(
                name = name,
                constraint_values = [
                    "//platforms/cpu:{}".format(cpu),
                    "@platforms//os:{}".format(os_constraint_name),
                    "//platforms/toolchain_version:{}".format(toolchain["version"]),
                ],
                visibility = ["//visibility:public"],
            )
