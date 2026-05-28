# RTL

This folder contains the Verilog design files for the project.

## Current status

The setup includes a simple message parser, a filter to check for an invalid type and a pipeline to connect these and decide the output based on the parsed input and filter result.

The top-level pipeline is also now synchronous, with registered input/output behaviour and `input_valid` / `output_valid` signalling.

```text
                ┌────────────────┐   message type    ┌────────────────┐                              
    message     │                ├──────────────────►│                │  reject reason               
───────────────►│ message_parser │                   │ message_filter ├───────────►                  
                │                ├──────────────────►│                │                              
                └────────────────┘    values a&b     └────┬────┬──────┘                              
                                                          │    │                                     
                                                          │    │                                     
                                                          │    │                                     
                                                          │    │                                     
                                                          │    │                                     
                                                 input a&b│    │ valid message?                      
                                                          │    │    ┌───────────────────┐  output a&b
                                                          │    └───►│                   │            
                                                          │         │ output_formatter  ├───────────►
                                                          └────────►│                   │            
                                                                    └───────────────────┘            
```

## Message format

The current message is 32 bits wide:

| Bits  | Field          | Width  |
| ----- | -------------- | ------ |
| 31:28 | `message_type` | 4 bits |
| 27:24 | `channel_id`   | 4 bits |
| 23:16 | `value_a`      | 8 bits |
| 15:8  | `value_b`      | 8 bits |
| 7:0   | `flags`        | 8 bits |

## Rejection Reasons

| Rejection Number | Reason              |
| ---------------- | ------------------- |
| 0                | not rejected        |
| 1                | invalid type        |
| 2                | value A above limit |
| 3                | value B above limit |
