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

The current tests reproduce the original Verilog testbench cases and compare the RTL output against either manually specified expected values or a Python reference model.

- [x] Recreate Verilog TB in Python
- [x] Write a Python Software Reference Model to compare to the hardware model
- [ ] Randomised testing & edge-case testing against software model

## Files

| File                       | Purpose                                                       |
| -------------------------- | ------------------------------------------------------------- |
| `test_direct_cases.py`     | Fixed input cases with manually specified expected outputs    |
| `test_reference_cases.py`  | Fixed input cases checked against Python reference model      |
| `test_random_reference.py` | Randomised input cases checked against Python reference model |
| `reference_model.py`       | Python software model of the expected RTL behaviour           |
