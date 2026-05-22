`timescale 1ns / 1ps

module message_parser(
        input wire [31:0] message,

        output wire [3:0] message_type,
        output wire [3:0] channel_id,
        output wire [7:0] value_a,
        output wire [7:0] value_b,
        output wire [7:0] flags
    );

    // break up message into sections as output wires
    assign message_type = message[31:28];
    assign channel_id   = message[27:24];
    assign value_a      = message[23:16];
    assign value_b      = message[15:8];
    assign flags        = message[7:0];

endmodule
