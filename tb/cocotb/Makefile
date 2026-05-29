# simulated using iverilog
SIM ?= icarus
TOPLEVEL_LANG ?= verilog


# load in all verilog sources from rtl dir
VERILOG_SOURCES += $(PWD)/../../rtl/message_parser.v
VERILOG_SOURCES += $(PWD)/../../rtl/message_filter.v
VERILOG_SOURCES += $(PWD)/../../rtl/output_formatter.v
VERILOG_SOURCES += $(PWD)/../../rtl/top_pipeline.v

# define the top-level design file from verilog sources
COCOTB_TOPLEVEL = top_pipeline

# ================================
# select which test should be used
# ================================
COCOTB_TEST_MODULES = test_direct_cases,test_reference_cases,test_random_reference
# COCOTB_TEST_MODULES = test_reference_cases
# COCOTB_TEST_MODULES = test_direct_cases

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim