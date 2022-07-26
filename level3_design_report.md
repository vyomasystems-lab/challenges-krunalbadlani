# **STAGE 2 REPORT**
## **level3_design - LCD interfacing circuit**
---
The verification is setup using Vyoma's UpTickPro provided for the hackathon.

![Gitpod screenshot](https://github.com/krunalbadlani/muximages/blob/main/gitpod_screen.png)


### **Verification Environment**
---
The CocoTb based python test is developed as explained. The test drives inputs to the Design Under Test(lcd module here) which takes an input named 'clk' or the clock signal. This  yields the output 'dout' as a sequence of control signals followed by the ASCII representation for the word 'verilog'. 

The values to the input 'clk' is given as follows:-


``` python
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
```



The assert statement is used for comparing the sequence detector's output with the expected output.




The following error is seen:



```
 expected value = 0x38
  5000.00ns INFO     DUT output = 0x38
expected value = 0x01
 15000.00ns INFO     DUT output = 0x1
expected value = 0x0E
 25000.00ns INFO     DUT output = 0xe
expected value = 0x06
 35000.00ns INFO     DUT output = 0x6
expected value = 0x80
 45000.00ns INFO     DUT output = 0x80
expected value = 0x76
 55000.00ns INFO     DUT output = 0x76
expected value = 0x65
 65000.00ns INFO     DUT output = 0x65
expected value = 0x72
 75000.00ns INFO     DUT output = 0x72
expected value = 0x69
 85000.00ns INFO     DUT output = 0x69
expected value = 0x6C
 95000.00ns INFO     DUT output = 0x6c
expected value = 0x6F
105000.00ns INFO     DUT output = 0x6f
expected value = 0x67
115000.00ns INFO     DUT output = 0x0
115000.00ns INFO     test_lcd_bug1 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-krunalbadlani/level3_design/test_lcd.py", line 84, in test_lcd_bug1
                         assert dut.dout.value == 0x67,"the output {K} of the lcd is wrong, it should be 0x67 ".format(K = hex(dut.dout.value))
                     AssertionError: the output 0x0 of the lcd is wrong, it should be 0x67 
```

![des3_err](https://github.com/krunalbadlani/muximages/blob/main/des3err.png)


### **Test scenario**
---

- input = clk
- Expected output (in hex):38,01,0E,06,80,76,65,72,69,6C,6F
- Observed output in the DUT= dout (in hex)= 38,01,0E,06,80,76,65,72,69,6C,'00'



Output mismatches for the above inputs proving that there are design bugs

### **Design Bugs**
---
Based on the above test output and analysing the design,
we see the following


Bug :-
```verilog
module lcd(
   input clk, 
   output reg [7:0] dout
    );
 
integer count = 0;
integer  i = 0;
reg rs, rw;
reg en; 
parameter send_cmd  = 0;
parameter send_data = 1;
reg state = send_cmd;
 
reg [7:0] data [11:0];

 
initial begin
 
///////////command for LCD , rs = 0
data[0] <= 8'h38; /////2 Lines 5 x 7 matrix
data[1] <= 8'h01; /////CLEAR DISPLAY
data[2] <= 8'h0E;// Display On Cursor Blinking
data[3] <= 8'h06; ////increment cursor from left to right
data[4] <= 8'h80;///// force cursor from beginning of first line
 
////////Data for LCD, rs = 1
data[5]  <= 8'h76; /////ascii value for v
data[6]  <= 8'h65;  ///e
data[7]  <= 8'h72;  ///r
data[8]  <= 8'h69; ///i
data[9]  <= 8'h6c; ///l
data[10] <= 8'h6f; /// o
data[11] <= 8'h67; ///g
end

 
 
always@(posedge clk)
begin
case(state)
send_cmd : 
begin
  if(i <= 4) 
   begin
    rs <= 1'b0;
    rw <= 1'b0;
    dout <= data[i];
    i <= i + 1;
   end
  else
    begin
    state <= send_data;
    dout <= data[i];
    i <= i + 1;
    end
end
 
send_data : 
begin
  if(i < 11) // THE BUG
   begin
    rs   <= 1'b1;
    rw   <= 1'b0; 
    dout <= data[i];
    i <= i + 1; 
   end
 else
   begin
   i <= 0;
   state <= send_cmd;
   rs    <= 1'b0;
   rw    <= 1'b0;
   dout  <= 8'h00;
   end
end
 
endcase
 
end
 
assign en = clk;

endmodule
```


### **Design Fix**
---
Updating the design 
```verilog
module lcd(
   input clk, 
   output reg [7:0] dout
    );
 
integer count = 0;
integer  i = 0;
reg rs, rw;
reg en; 
parameter send_cmd  = 0;
parameter send_data = 1;
reg state = send_cmd;
 
reg [7:0] data [11:0];

 
initial begin
 
///////////command for LCD , rs = 0
data[0] <= 8'h38; /////2 Lines 5 x 7 matrix
data[1] <= 8'h01; /////CLEAR DISPLAY
data[2] <= 8'h0E;// Display On Cursor Blinking
data[3] <= 8'h06; ////increment cursor from left to right
data[4] <= 8'h80;///// force cursor from beginning of first line
 
////////Data for LCD, rs = 1
data[5]  <= 8'h76; /////ascii value for v
data[6]  <= 8'h65;  ///e
data[7]  <= 8'h72;  ///r
data[8]  <= 8'h69; ///i
data[9]  <= 8'h6c; ///l
data[10] <= 8'h6f; /// o
data[11] <= 8'h67; ///g
end

 
 
always@(posedge clk)
begin
case(state)
send_cmd : 
begin
  if(i <= 4) 
   begin
    rs <= 1'b0;
    rw <= 1'b0;
    dout <= data[i];
    i <= i + 1;
   end
  else
    begin
    state <= send_data;
    dout <= data[i];
    i <= i + 1;
    end
end
 
send_data : 
begin
  if(i <= 11) // change
   begin
    rs   <= 1'b1;
    rw   <= 1'b0; 
    dout <= data[i];
    i <= i + 1; 
   end
 else
   begin
   i <= 0;
   state <= send_cmd;
   rs    <= 1'b0;
   rw    <= 1'b0;
   dout  <= 8'h00;
   end
end
 
endcase
 
end
 
assign en = clk;

endmodule






```
and re-running the test makes the test pass.

![des3fix](https://github.com/krunalbadlani/muximages/blob/main/des3fix.png)

The updated design is checked in as lcd.v in the folder level3_design_corrected.

### **Verification Strategy**
---

The design here is of a LCD interfacing circuit. The circuit takes input as clock. It then displays the output on the lcd screen (dout) as per the data on its data lines. Here the data lines have the word 'verilog' which is to be displayed on the LCD screen. It uses ASCII letters of the letters to display them. To successfully display the word, the display has to have some control output to set the lcd for displaying, and then the ASCII values of the characters have to be followed as output to successfully display them. To verify this operation, I have given a clock and at each falling edge of the clock I have logged the value of dout. I have asserted the ASCII value of the last letter 'g' to be equal to dout exactly at that falling edge. If there is no error we can be assured that the data is coming in correct sequence, and additionally that can be verified by the logged data. The result of the test suggests that the last ASCII value doesnt match with that of 'g' and is rather 00 which is the value that should be after displaying the word. This implies that there is a bug in the part of the design which is dealing with the letter 'g'. This is the strategy adopted.


### **Is the verification complete?**
---
The functionality of the LCD interfacing circuit for the word 'verilog' to be displayed is completely verified here.
