`timescale 1ns / 1ps

module top_pipeline_tb();

    reg [31:0] message;
    wire [3:0] value_a;
    wire [3:0] value_b;
    wire [3:0] reject_reason;

    initial begin
        message = 32'b0000_0000_11111111_00001111_00000000; #10 // valid
        message = 32'b0000_0000_11110000_11110000_00000000; #10 // valid
        message = 32'b0000_0000_01010101_10101010_00000000; #10 // valid
        message = 32'b0001_0000_01010101_10101010_00000000; #10 // invalid
        message = 32'b0001_0000_11110000_00001111_00000000; // invalid
    end

    top_pipeline uut (
        .message(message),
        .value_a(value_a),
        .value_b(value_b),
        .reject_reason(reject_reason)
    );

endmodule
