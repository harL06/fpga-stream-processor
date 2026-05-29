# Raondmised tests with outputs compared against Python Reference Model

import cocotb
from cocotb.triggers import RisingEdge, ClockCycles, ReadOnly
from cocotb.clock import Clock

from reference_model import reference_model
import message_generator

NUM_TESTS = 10_000 # number of testcases to generate

# Design under test
@cocotb.test()
async def random_reference_cases(dut):
    # set up a 10ns cycle clock
    clk = Clock(dut.clk, 10, "ns")
    clk.start()

    # set reset HIGH for start
    dut.reset.value = 1
    dut.input_valid.value = 0
    dut.message.value = 0

    await ClockCycles(dut.clk, 2) # wait two clock cycles, holding reset HIGH

    dut.reset.value = 0 # disable reset signal

    # begin test cases
    for i in range(NUM_TESTS):
        # generate random message, only allowing message type of 0 or 1
        message = message_generator.generate_paramaterised_random_message(type_limit=1)
        dut.message.value = message

        dut.input_valid.value = 1
        await RisingEdge(dut.clk) # wait until posedge for input to be sampled allow message input value to settle before reading output

        dut.input_valid.value = 0 # don't read input after prev was sampled

        await RisingEdge(dut.clk) # wait for next posedge, output updated
        await ReadOnly() # wait for values to settle and sim to enter "read only" stage

        # record output values from sim
        value_a = int(dut.value_a.value)
        value_b = int(dut.value_b.value)
        reject_reason = int(dut.reject_reason.value)

        # cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason) # log results for debug

        ref_results = reference_model(message) # run message through reference model
        # cocotb.log.info("ref results=%s", ref_results) # log reference results for debug

        # compare sim results to reference model (pass/fail criteria)
        assert value_a == ref_results["a"], \
            f"FAIL: simulated value_a ({value_a}) =/= model value_a ({ref_results['a']})"
        assert value_b == ref_results["b"], \
            f"FAIL: simulated value_b ({value_b}) =/= model value_b ({ref_results['b']})"
        assert reject_reason == ref_results["reject_reason"], \
            f"FAIL: simulated reject_reason ({reject_reason}) =/= model reject_reason ({ref_results['reject_reason']})"

        await RisingEdge(dut.clk) # set next message at next rising edge


    cocotb.log.info(f"{NUM_TESTS} tests ran successfully...")
    cocotb.log.info(f"{i+1}/{NUM_TESTS}: PASS")