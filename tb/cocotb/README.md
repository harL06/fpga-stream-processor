# cocotb Testbenches

This folder contains cocotb testbenches and simulations for the RTL modules.

## Requirements

Python packages:

```bash
pip install -r requirements.txt
```

System packages:

```bash
sudo apt install iverilog
```

## Current status

Testbench with fixed testcases, mirroring those in the initial verilog tb.

- [x] Recreate Verilog TB in Python
- [ ] Write a Python Software Reference Model to compare to the hardware model
- [ ] Randomised testing & edge-case testing against software model
