# Fixed tests from Verilog Testbench

import cocotb
from cocotb.triggers import Timer

# Design under test
@cocotb.test()
async def fixed_test_top_pipeline(dut):

    # === Test Case 1 ==== #
    dut.message.value = 0b0000_0000_11111111_00001111_00000000
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #255
    value_b = int(dut.value_b.value) #15
    reject_reason = int(dut.reject_reason.value) #invalid - A too high

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 2

    # === Test Case 2 ==== #
    dut.message.value = 0b0000_0000_11110000_11110000_00000000
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #240
    value_b = int(dut.value_b.value) #240
    reject_reason = int(dut.reject_reason.value) #invalid - A too high (checks A first)

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 2

    # === Test Case 3 ==== #
    dut.message.value = 0b0000_0000_01010101_11001101_00000000
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #85
    value_b = int(dut.value_b.value) #205
    reject_reason = int(dut.reject_reason.value) #invalid - B too high

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 3

    # === Test Case 4 ==== #
    dut.message.value = 0b0000_0000_00000101_00000011_00000000
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #5
    value_b = int(dut.value_b.value) #3
    reject_reason = int(dut.reject_reason.value) #valid - passes filter

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 5
    assert value_b == 3
    assert reject_reason == 0

    # === Test Case 5 ==== #
    dut.message.value = 0b0000_0000_11001000_11001000_00000000
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #200
    value_b = int(dut.value_b.value) #200
    reject_reason = int(dut.reject_reason.value) #valid - passes filter

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 200
    assert value_b == 200
    assert reject_reason == 0

    # === Test Case 6 ==== #
    dut.message.value = 0b0001_0000_01010101_10101010_00000000
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #200
    value_b = int(dut.value_b.value) #200
    reject_reason = int(dut.reject_reason.value) #invalid - wrong type

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 1

    # === Test Case 7 ==== #
    dut.message.value = 0b0001_0000_11110000_00001111_00000000
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value)
    value_b = int(dut.value_b.value)
    reject_reason = int(dut.reject_reason.value) #invalid - wrong type

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 1