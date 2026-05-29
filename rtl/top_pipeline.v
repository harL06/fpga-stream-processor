`timescale 1ns / 1ps

module top_pipeline(
        input clk,
        input reset,
        input input_valid, // should input be ignored
        input wire [31:0] message,

        output reg output_valid, // should output be ignored
        output reg [7:0] value_a,
        output reg [7:0] value_b,
        output reg [3:0] reject_reason
    );

    reg [31:0] reg_message;
    reg reg_message_valid;

    wire [7:0] value_a_wire;
    wire [7:0] value_b_wire;

    wire message_accept;
    wire [3:0] reject_reason_wire;

    always @ (posedge clk) begin // synchronous logic
        // input sampling logic
        if (reset) begin // reset HIGH
            reg_message <= 0;
            reg_message_valid <= 0; // current reg message is invalid
        end
        else if (input_valid) begin
            reg_message <= message; // sample input on clk edge if its valid
            reg_message_valid <= 1; // reg message is valid
        end
        else begin // if input invalid, ignore the input
            reg_message <= 0;
            reg_message_valid <= 0;
        end

        // output sampling logic
        output_valid <= reg_message_valid; // output valid based on prev message valid

        if (reset) begin // reset HIGH
            output_valid <= 0; // output invalid during reset
            value_a <= 0;
            value_b <= 0;
            reject_reason <= 0;
        end
        else if (reg_message_valid) begin // if current reg message is valid, sample output
            value_a <= value_a_wire; //outputs will be based on prev cycle input
            value_b <= value_b_wire;
            reject_reason <= reject_reason_wire;
        end
        else begin //outputs zeroed if reg input is invalid
            value_a <= 0;
            value_b <= 0;
            reject_reason <= 0;
        end
    end

    // parse diferent vars from the input message
    wire [7:0] input_val_a, input_val_b;
    wire [3:0] message_type;
    wire [3:0] channel_id; // will be used in fut ver
    wire [7:0] flags;      // will be used in fut ver
    message_parser parser (
        .message(reg_message), // input the most recent sampled input
        .value_a(input_val_a),
        .value_b(input_val_b),
        .message_type(message_type),
        .channel_id(channel_id),
        .flags(flags)
    );

    // pass parsed values into message filter
    message_filter filter (
        .message_type(message_type),
        .message_valid(message_accept),
        .reject_reason(reject_reason_wire),
        .value_a(input_val_a),
        .value_b(input_val_b)
    );

    // set outputs only if the message is valid
    output_formatter out_format (
        .input_val_a(input_val_a),
        .input_val_b(input_val_b),
        .message_valid(message_accept),
        .value_a(value_a_wire),
        .value_b(value_b_wire)
    );

endmodule
