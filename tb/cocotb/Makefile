# defaults from Quickstart Guide

SIM ?= icarus
TOPLEVEL_LANG ?= verilog


# load in verilog sources from rtl dir
VERILOG_SOURCES += $(PWD)/../../rtl/message_parser.v
VERILOG_SOURCES += $(PWD)/../../rtl/message_filter.v
VERILOG_SOURCES += $(PWD)/../../rtl/output_formatter.v
VERILOG_SOURCES += $(PWD)/../../rtl/top_pipeline.v

# COCOTB_TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
COCOTB_TOPLEVEL = top_pipeline

# COCOTB_TEST_MODULES is the basename of the Python test file(s)
COCOTB_TEST_MODULES = test_top_pipeline

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim