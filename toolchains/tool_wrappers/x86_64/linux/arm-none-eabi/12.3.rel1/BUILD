filegroup(
    name = "wrappers",
    srcs = glob(["*"]),
    visibility = ["//visibility:public"],
)

sh_binary(
    name = "ar",
    srcs = [":arm-none-eabi-ar"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "as",
    srcs = [":arm-none-eabi-as"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "cpp",
    srcs = [":arm-none-eabi-cpp"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "gcc",
    srcs = [":arm-none-eabi-gcc"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "gcov",
    srcs = [":arm-none-eabi-gcov"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "gdb",
    srcs = [":arm-none-eabi-gdb"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "ld",
    srcs = [":arm-none-eabi-ld"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "nm",
    srcs = [":arm-none-eabi-nm"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "objcopy",
    srcs = [":arm-none-eabi-objcopy"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "objdump",
    srcs = [":arm-none-eabi-objdump"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "readelf",
    srcs = [":arm-none-eabi-readelf"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

sh_binary(
    name = "strip",
    srcs = [":arm-none-eabi-strip"],
    data = ["@arm-gnu-toolchain-12.3.rel1-x86_64-arm-none-eabi//:all_files"],
    visibility = ["//visibility:public"],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)