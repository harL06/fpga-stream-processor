# Verilog Testbenches

This folder contains simple verilog simulation testbenches for the RTL modules.

## Current status

The top-level testbench applies fixed 32-bit messages to the synchronous pipeline and checks the registered output values and reject reasons.
Outputs are compared against expected values and a count for the number of passes/fails is tracked.
