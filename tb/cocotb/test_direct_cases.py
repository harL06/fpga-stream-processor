# Fixed tests from Verilog Testbench, manually checked output

import cocotb
from cocotb.triggers import Timer, RisingEdge, ClockCycles, ReadOnly
from cocotb.clock import Clock

import reference_model

# Design under test
@cocotb.test()
async def fixed_direct_cases(dut):

    # set up a 10ns cycle clock
    clk = Clock(dut.clk, 10, "ns")
    clk.start()

    # set reset HIGH for start
    dut.reset.value = 1
    dut.input_valid.value = 0
    dut.message.value = 0

    await ClockCycles(dut.clk, 2) # wait two clock cycles, holding reset HIGH

    dut.reset.value = 0 # disable reset signal

    # === Test Case 1 ==== #
    message = 0b0000_0000_11111111_00001111_00000000
    dut.message.value = message
    dut.input_valid.value = 1

    await RisingEdge(dut.clk) # wait until posedge for input to be sampled

    dut.input_valid.value = 0 # don't read input after prev was sampled

    await RisingEdge(dut.clk) # wait for next posedge, output updated
    await ReadOnly() # wait for values to settle and sim to enter "read only" stage

    value_a = int(dut.value_a.value) #255
    value_b = int(dut.value_b.value) #15
    reject_reason = int(dut.reject_reason.value) #invalid - A too high

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 2

    # === Test Case 2 ==== #
    await RisingEdge(dut.clk) # set next message at next rising edge
    dut.message.value = 0b0000_0000_11110000_11110000_00000000
    dut.input_valid.value = 1

    await RisingEdge(dut.clk) # wait until posedge for input to be sampled

    dut.input_valid.value = 0 # don't read input after prev was sampled

    await RisingEdge(dut.clk) # wait for next posedge, output updated
    await ReadOnly() # wait for values to settle and sim to enter "read only" stage

    value_a = int(dut.value_a.value) #240
    value_b = int(dut.value_b.value) #240
    reject_reason = int(dut.reject_reason.value) #invalid - A too high (checks A first)

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 2

    # === Test Case 3 ==== #
    await RisingEdge(dut.clk) # set next message at next rising edge
    dut.message.value = 0b0000_0000_01010101_11001101_00000000
    dut.input_valid.value = 1

    await RisingEdge(dut.clk) # wait until posedge for input to be sampled

    dut.input_valid.value = 0 # don't read input after prev was sampled

    await RisingEdge(dut.clk) # wait for next posedge, output updated
    await ReadOnly() # wait for values to settle and sim to enter "read only" stage

    value_a = int(dut.value_a.value) #85
    value_b = int(dut.value_b.value) #205
    reject_reason = int(dut.reject_reason.value) #invalid - B too high

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 3

    # === Test Case 4 ==== #
    await RisingEdge(dut.clk) # set next message at next rising edge
    dut.message.value = 0b0000_0000_00000101_00000011_00000000
    dut.input_valid.value = 1

    await RisingEdge(dut.clk) # wait until posedge for input to be sampled

    dut.input_valid.value = 0 # don't read input after prev was sampled

    await RisingEdge(dut.clk) # wait for next posedge, output updated
    await ReadOnly() # wait for values to settle and sim to enter "read only" stage

    value_a = int(dut.value_a.value) #5
    value_b = int(dut.value_b.value) #3
    reject_reason = int(dut.reject_reason.value) #valid - passes filter

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 5
    assert value_b == 3
    assert reject_reason == 0

    # === Test Case 5 ==== #
    await RisingEdge(dut.clk) # set next message at next rising edge
    dut.message.value = 0b0000_0000_11001000_11001000_00000000
    dut.input_valid.value = 1

    await RisingEdge(dut.clk) # wait until posedge for input to be sampled

    dut.input_valid.value = 0 # don't read input after prev was sampled

    await RisingEdge(dut.clk) # wait for next posedge, output updated
    await ReadOnly() # wait for values to settle and sim to enter "read only" stage

    value_a = int(dut.value_a.value) #200
    value_b = int(dut.value_b.value) #200
    reject_reason = int(dut.reject_reason.value) #valid - passes filter

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 200
    assert value_b == 200
    assert reject_reason == 0

    # === Test Case 6 ==== #
    await RisingEdge(dut.clk) # set next message at next rising edge
    dut.message.value = 0b0001_0000_01010101_10101010_00000000
    dut.input_valid.value = 1

    await RisingEdge(dut.clk) # wait until posedge for input to be sampled

    dut.input_valid.value = 0 # don't read input after prev was sampled

    await RisingEdge(dut.clk) # wait for next posedge, output updated
    await ReadOnly() # wait for values to settle and sim to enter "read only" stage

    value_a = int(dut.value_a.value) #200
    value_b = int(dut.value_b.value) #200
    reject_reason = int(dut.reject_reason.value) #invalid - wrong type

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 1

    # === Test Case 7 ==== #
    await RisingEdge(dut.clk) # set next message at next rising edge
    dut.message.value = 0b0001_0000_11110000_00001111_00000000
    dut.input_valid.value = 1

    await RisingEdge(dut.clk) # wait until posedge for input to be sampled

    dut.input_valid.value = 0 # don't read input after prev was sampled

    await RisingEdge(dut.clk) # wait for next posedge, output updated
    await ReadOnly() # wait for values to settle and sim to enter "read only" stage

    value_a = int(dut.value_a.value)
    value_b = int(dut.value_b.value)
    reject_reason = int(dut.reject_reason.value) #invalid - wrong type

    cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason)

    assert value_a == 0
    assert value_b == 0
    assert reject_reason == 1