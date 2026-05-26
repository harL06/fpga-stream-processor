# Raondmised tests with outputs compared against Python Reference Model

import cocotb
from cocotb.triggers import Timer

from reference_model import reference_model
import message_generator

NUM_TESTS = 1000 # number of testcases to generate

# Design under test
@cocotb.test()
async def random_reference_cases(dut):

    for i in range(NUM_TESTS):
        # generate random message, only allowing message type of 0 or 1
        message = message_generator.generate_paramaterised_random_message(type_limit=1)

        dut.message.value = message
        await Timer(1, unit="ns") # allow message input value to settle before reading output

        # record output values from sim
        value_a = int(dut.value_a.value)
        value_b = int(dut.value_b.value)
        reject_reason = int(dut.reject_reason.value)

        cocotb.log.info("a=%s b=%s reason=%s", value_a, value_b, reject_reason) # log results for debug

        ref_results = reference_model(message) # run message through reference model
        cocotb.log.info("ref results=%s", ref_results) # log reference results for debug

        assert value_a == ref_results["a"] # compare sim results to reference model (pass/fail criteria)
        assert value_b == ref_results["b"]
        assert reject_reason == ref_results["reject_reason"]