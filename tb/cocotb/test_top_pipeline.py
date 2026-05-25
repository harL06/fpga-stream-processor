# Test from Quickstart Guide

import cocotb
from cocotb.triggers import Timer

# Design under test
@cocotb.test()
async def my_first_test(dut):
    """Try accessing the design."""

    for _ in range(10):
        dut.message.value = 0
        await Timer(1, unit="ns")
        dut.message.value = 1
        await Timer(1, unit="ns")

    cocotb.log.info("reject_reason is %s", dut.reject_reason.value)
    assert dut.reject_reason.value == 0