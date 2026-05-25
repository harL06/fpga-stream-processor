# Verilog Testbenches

This folder contains simple verilog simulation testbenches for the RTL modules.

## Current status

The current testbench inputs fixed 32-bit messages into `top_pipeline.v` and checks the parsed fields in simulation.
Outputs are compared against expected values and a count for the number of passes/fails is tracked.
