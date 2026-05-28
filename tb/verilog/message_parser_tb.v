`timescale 1ns / 1ps

module top_pipeline_tb();

    reg [31:0] message;
    wire [7:0] value_a;
    wire [7:0] value_b;
    wire [3:0] reject_reason;

    reg [7:0] test_value_a;
    reg [7:0] test_value_b;
    reg [3:0] test_reject_reason;
    wire output_valid;

    reg clk;
    initial
        clk = 0;
    always
        #5 clk = ~clk; //setup simple testbench clock

    reg reset, input_valid;
    initial begin // set reset HIGH for one clock cycle on start
        reset = 1;
        #10

        reset = 0;
    end

    reg [7:0] fail_count;
    reg [7:0] pass_count;
    initial begin
        fail_count = 0;
        pass_count = 0;
    end

    always @ (*) begin // pass/fail checks sampled
        if (!reset & output_valid) begin
            if (value_a == test_value_a &&
                value_b == test_value_b &&
                reject_reason == test_reject_reason)
                // keep track of num failing and passing test cases

                pass_count <= pass_count + 1;
            else
                fail_count <= fail_count + 1;
        end
        #20;
    end

    initial begin
        input_valid = 0; #10
        input_valid = 1;

        message = 32'b0000_0000_11111111_00001111_00000000;

        test_value_a = 8'b00000000; //255
        test_value_b = 8'b00000000; //15
        test_reject_reason = 4'b0010;
        #10 // invalid - A too high

        input_valid = 0; #10
        input_valid = 1;


        message = 32'b0000_0000_11110000_11110000_00000000;

        test_value_a = 8'b00000000; //240
        test_value_b = 8'b00000000; //240
        test_reject_reason = 4'b0010;
        #10 // invalid - A too high (checks A first)

        input_valid = 0; #10
        input_valid = 1;

        message = 32'b0000_0000_01010101_11001101_00000000;

        test_value_a = 8'b00000000; //85
        test_value_b = 8'b00000000; //205
        test_reject_reason = 4'b0011;
        #10 // invalid - B too high

        input_valid = 0; #10
        input_valid = 1;

        message = 32'b0000_0000_00000101_00000011_00000000;

        test_value_a = 8'b00000101; //5
        test_value_b = 8'b00000011; //3
        test_reject_reason = 4'b0000;
        #10 // valid - passes filter

        input_valid = 0; #10
        input_valid = 1;

        message = 32'b0000_0000_11001000_11001000_00000000;

        test_value_a = 8'b11001000; //200
        test_value_b = 8'b11001000; //200
        test_reject_reason = 4'b0000;
        #10 // valid - passes filter

        input_valid = 0; #10
        input_valid = 1;

        message = 32'b0001_0000_01010101_10101010_00000000;

        test_value_a = 8'b00000000;
        test_value_b = 8'b00000000;
        test_reject_reason = 4'b0001;
        #10 // invalid - wrong type

        input_valid = 0; #10
        input_valid = 1;

        message = 32'b0001_0000_11110000_00001111_00000000;

        test_value_a = 8'b00000000;
        test_value_b = 8'b00000000;
        test_reject_reason = 4'b0001;  // invalid - wrong type
        #10

        input_valid = 0; #10

        $display("Passes: %0d, Fails: %0d", pass_count, fail_count); // finish sim and display results
        $finish;
    end

    top_pipeline uut (
        .clk(clk),
        .reset(reset),
        .input_valid(input_valid),
        .output_valid(output_valid),
        .message(message),
        .value_a(value_a),
        .value_b(value_b),
        .reject_reason(reject_reason)
    );

endmodule
