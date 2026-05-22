`timescale 1ns / 1ps

module message_parser_tb();

    // generate some simple test messages, opnly changing values of a and b
    reg [31:0] message;
    initial begin
        message = 32'b0000_0000_11111111_00001111_00000000; #10
        message = 32'b0000_0000_11110000_11110000_00000000; #10
        message = 32'b0000_0000_00000000_00000000_00000000;
    end

    // read out the 2 values only for tb
    wire [7:0] value_a;
    wire [7:0] value_b;

    // feed input and outputs relevant vars
    message_parser uut (.value_a(value_a), .value_b(value_b), .message(message));


endmodule
