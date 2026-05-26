# TODO

# Raondmised tests with outputs compared against Python Reference Model

import cocotb
from cocotb.triggers import Timer

from reference_model import reference_model

# Design under test
@cocotb.test()
async def random_reference_cases(dut):
    pass