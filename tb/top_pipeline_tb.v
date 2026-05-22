`timescale 1ns / 1ps

module top_pipeline_tb();

    reg [31:0] message;
    wire [7:0] value_a;
    wire [7:0] value_b;
    wire [3:0] reject_reason;

    reg [7:0] test_value_a;
    reg [7:0] test_value_b;
    reg [3:0] test_reject_reason;

    reg clk;
    initial
        clk = 0;
    always
        #5 clk = ~clk; //setup simple testbench clock

    reg [7:0] fail_count;
    reg [7:0] pass_count;
    initial begin
        fail_count = 0;
        pass_count = 0;
    end

    always @ (posedge clk) begin
        if (value_a == test_value_a &&
            value_b == test_value_b &&
            reject_reason == test_reject_reason)
            // keep track of num failing and passing test cases

            pass_count <= pass_count + 1;
        else
            fail_count <= fail_count + 1;
    end

    initial begin
        message = 32'b0000_0000_11111111_00001111_00000000;
        test_value_a = 8'b11111111;
        test_value_b = 8'b00001111;
        test_reject_reason = 4'b0000;
        #10 // valid

        message = 32'b0000_0000_11110000_11110000_00000000;
        test_value_a = 8'b11110000;
        test_value_b = 8'b11110000;
        test_reject_reason = 4'b0000;
        #10 // valid

        message = 32'b0000_0000_01010101_10101010_00000000;
        test_value_a = 8'b01010101;
        test_value_b = 8'b10101010;
        test_reject_reason = 4'b0000;
        #10 // valid

        message = 32'b0001_0000_01010101_10101010_00000000;
        test_value_a = 8'b00000000;
        test_value_b = 8'b00000000;
        test_reject_reason = 4'b0001;
        #10 // invalid

        message = 32'b0001_0000_11110000_00001111_00000000;
        test_value_a = 8'b00000000;
        test_value_b = 8'b00000000;
        test_reject_reason = 4'b0001;  // invalid
        #10

        $display("Passes: %0d, Fails: %0d", pass_count, fail_count); // finish sim and display results
        $finish;
    end

    top_pipeline uut (
        .message(message),
        .value_a(value_a),
        .value_b(value_b),
        .reject_reason(reject_reason)
    );

endmodule
