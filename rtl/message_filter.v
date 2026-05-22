`timescale 1ns / 1ps

module message_filter(
        input wire [3:0] message_type,
        input wire [7:0] value_a,
        input wire [7:0] value_b,

        output reg message_valid,
        output reg [3:0] reject_reason
    );

    always @ (*) begin
        if (message_type == 0) begin
            message_valid = 1;
            reject_reason = 4'b0000; // passes
        end
        else begin
            message_valid = 0;
            reject_reason = 4'b0001; // invalid type
        end
    end

endmodule
