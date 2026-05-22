`timescale 1ns / 1ps

module output_formatter(
        input wire [7:0] input_val_a,
        input wire [7:0] input_val_b,
        input wire message_valid,
        output reg [7:0] value_a,
        output reg [7:0] value_b
    );

    // based on filter output, define the outputs
    always @ (*) begin
        if (message_valid == 1) begin
            value_a = input_val_a;
            value_b = input_val_b;
        end
        else begin
            value_a = 0;
            value_b = 0;
        end
    end
endmodule
