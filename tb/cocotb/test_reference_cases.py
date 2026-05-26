# Fixed tests from Verilog Testbench, output checked against Python reference model

import cocotb
from cocotb.triggers import Timer

from reference_model import reference_model

# Design under test
@cocotb.test()
async def fixed_reference_cases(dut):

    # === Test Case 1 ==== #
    message = 0b0000_0000_11111111_00001111_00000000

    dut.message.value = message
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #255
    value_b = int(dut.value_b.value) #15
    reject_reason = int(dut.reject_reason.value) #invalid - A too high

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    ref_results = reference_model(message) # run message through reference model
    cocotb.log.info("ref results=%s", ref_results)

    assert value_a == ref_results["a"] # compare sim results to reference model
    assert value_b == ref_results["b"]
    assert reject_reason == ref_results["reject_reason"]

    # === Test Case 2 ==== #
    message = 0b0000_0000_11110000_11110000_00000000

    dut.message.value = message
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #240
    value_b = int(dut.value_b.value) #240
    reject_reason = int(dut.reject_reason.value) #invalid - A too high (checks A first)

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    ref_results = reference_model(message) # run message through reference model
    cocotb.log.info("ref results=%s", ref_results)

    assert value_a == ref_results["a"] # compare sim results to reference model
    assert value_b == ref_results["b"]
    assert reject_reason == ref_results["reject_reason"]

    # === Test Case 3 ==== #
    message = 0b0000_0000_01010101_11001101_00000000

    dut.message.value = message
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #85
    value_b = int(dut.value_b.value) #205
    reject_reason = int(dut.reject_reason.value) #invalid - B too high

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    ref_results = reference_model(message) # run message through reference model
    cocotb.log.info("ref results=%s", ref_results)

    assert value_a == ref_results["a"] # compare sim results to reference model
    assert value_b == ref_results["b"]
    assert reject_reason == ref_results["reject_reason"]

    # === Test Case 4 ==== #
    message = 0b0000_0000_00000101_00000011_00000000

    dut.message.value = message
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #5
    value_b = int(dut.value_b.value) #3
    reject_reason = int(dut.reject_reason.value) #valid - passes filter

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    ref_results = reference_model(message) # run message through reference model
    cocotb.log.info("ref results=%s", ref_results)

    assert value_a == ref_results["a"] # compare sim results to reference model
    assert value_b == ref_results["b"]
    assert reject_reason == ref_results["reject_reason"]

    # === Test Case 5 ==== #
    message = 0b0000_0000_11001000_11001000_00000000

    dut.message.value = message
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #200
    value_b = int(dut.value_b.value) #200
    reject_reason = int(dut.reject_reason.value) #valid - passes filter

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    ref_results = reference_model(message) # run message through reference model
    cocotb.log.info("ref results=%s", ref_results)

    assert value_a == ref_results["a"] # compare sim results to reference model
    assert value_b == ref_results["b"]
    assert reject_reason == ref_results["reject_reason"]

    # === Test Case 6 ==== #
    message = 0b0001_0000_01010101_10101010_00000000

    dut.message.value = message
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value) #200
    value_b = int(dut.value_b.value) #200
    reject_reason = int(dut.reject_reason.value) #invalid - wrong type

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    ref_results = reference_model(message) # run message through reference model
    cocotb.log.info("ref results=%s", ref_results)

    assert value_a == ref_results["a"] # compare sim results to reference model
    assert value_b == ref_results["b"]
    assert reject_reason == ref_results["reject_reason"]

    # === Test Case 7 ==== #
    message = 0b0001_0000_11110000_00001111_00000000

    dut.message.value = message
    await Timer(1, unit="ns") # allow message value to settle

    value_a = int(dut.value_a.value)
    value_b = int(dut.value_b.value)
    reject_reason = int(dut.reject_reason.value) #invalid - wrong type

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    ref_results = reference_model(message) # run message through reference model
    cocotb.log.info("ref results=%s", ref_results)

    assert value_a == ref_results["a"] # compare sim results to reference model
    assert value_b == ref_results["b"]
    assert reject_reason == ref_results["reject_reason"]