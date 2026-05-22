# RTL

This folder contains the Verilog design files for the project.

## Current status

The current first module is a simple message parser. It takes a fixed-width input message and breaks it into separate fields.

## Message format

The current message is 32 bits wide:

| Bits  | Field          | Width  |
| ----- | -------------- | ------ |
| 31:28 | `message_type` | 4 bits |
| 27:24 | `channel_id`   | 4 bits |
| 23:16 | `value_a`      | 8 bits |
| 15:8  | `value_b`      | 8 bits |
| 7:0   | `flags`        | 8 bits |
