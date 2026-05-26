# cocotb Testbenches

This folder contains cocotb testbenches and simulations for the RTL modules.

## Run the tests

From the repo root:

```bash
source .venv/bin/activate
cd tb/cocotb
make
```

This runs the cocotb tests using Icarus Verilog and writes simulator output to the terminal.

## Requirements

Python packages (run in repo root):

```bash
pip install -r requirements.txt
```

System packages:

```bash
sudo apt install iverilog
```

## Current status

Current verification includes fixed cocotb tests, a Python reference model, and randomised RTL vs model testing.

- [x] Recreate Verilog TB in Python
- [x] Write a Python software reference model to compare to the hardware Verilog design
- [x] Randomised input testing against reference model
- [ ] Edge case testing

## Files

| File                       | Purpose                                                       |
| -------------------------- | ------------------------------------------------------------- |
| `test_direct_cases.py`     | Fixed input cases with manually specified expected outputs    |
| `test_reference_cases.py`  | Fixed input cases checked against Python reference model      |
| `test_random_reference.py` | Randomised input cases checked against Python reference model |
| `reference_model.py`       | Python software model of the expected RTL behaviour           |
| `message_generator.py`     | Generates randomised input messages for testing               |
