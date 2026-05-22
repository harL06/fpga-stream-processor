`timescale 1ns / 1ps

module top_pipeline(
        input wire [31:0] message,
        output wire [7:0] value_a,
        output wire [7:0] value_b,
        output wire [3:0] reject_reason
    );

    // parse diferent vars from the input message
    wire [7:0] input_val_a, input_val_b;
    wire [3:0] message_type;
    message_parser parser (
        .message(message),
        .value_a(input_val_a),
        .value_b(input_val_b),
        .message_type(message_type)
    );

    // pass parsed values into message filter
    wire message_valid;
    message_filter filter (
        .message_type(message_type),
        .message_valid(message_valid),
        .reject_reason(reject_reason)
    );

    // set outputs only if the message is valid
    output_formatter out_format (
        .input_val_a(input_val_a),
        .input_val_b(input_val_b),
        .message_valid(message_valid),
        .value_a(value_a),
        .value_b(value_b)
    );

endmodule
