`timescale 1ns / 1ps

module message_filter
    #(parameter MAX_A = 200, parameter MAX_B = 200)
    (
        input wire [3:0] message_type,
        input wire [7:0] value_a,
        input wire [7:0] value_b,

        output reg message_valid,
        output reg [3:0] reject_reason
    );

    always @ (*) begin
        if (message_type != 0) begin
            message_valid = 0;
            reject_reason = 4'b0001; // invalid type
        end
        else if (value_a > MAX_A) begin
            message_valid = 0;
            reject_reason = 4'b0010; // value A over the limit
        end
        else if (value_b > MAX_B) begin
            message_valid = 0;
            reject_reason = 4'b0011; // value B over the limit
        end
        else begin
            message_valid = 1;
            reject_reason = 4'b0000; // passes through filter
        end 
    end

endmodule
