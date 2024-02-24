cc_test(
    name = "test_cpp",
    srcs = ["test_cpp.cc"],
    linkopts = ["-nostartfiles"],
)

cc_test(
    name = "test_c",
    srcs = ["test_c.c"],
    linkopts = ["-nostartfiles"],
)

alias(
    name = "objdump",
    actual = "@bazel_arm_toolchains//toolchains/tool_wrappers/x86_64/linux/arm-none-eabi/12.3.rel1:objdump",
)

genrule(
    name = "objdump_output",
    testonly = True,
    srcs = [":test_cpp"],
    outs = ["objdump_output.txt"],
    cmd = "$(location :objdump) -x $< > $@",
    tools = [":objdump"],
)
