# **STAGE 2 REPORT**
## **level1_design2 - Sequence detector**
---
The verification is setup using Vyoma's UpTickPro provided for the hackathon.

![Gitpod screenshot](https://github.com/krunalbadlani/muximages/blob/main/gitpod_screen.png)


### **Verification Environment**
---
The CocoTb based python test is developed as explained. The test drives inputs to the Design Under Test(seq_detect_1011 module here) which takes in bitwise input 'inp_bit' on every positive edge of an another input named 'clk' or the clock signal. One additional input named reset is also given to initialize the design when needed. This combination yields the bitwise output named 'seq_seen'. 

The values to the input inp_bit, clk, and the reset are given as follows:-


``` python
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b0
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')


    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b0
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b0
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'A={(dut.inp_bit.value)} DUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
```



The assert statement is used for comparing the sequence detector's output with the  expected output.

The following error is seen:



```
 25000.00ns INFO     A=1 DUT=0
 35000.00ns INFO     A=0 DUT=0
 45000.00ns INFO     A=1 DUT=0
 55000.00ns INFO     A=1 DUT=1
 65000.00ns INFO     A=1 DUT=0
 75000.00ns INFO     A=1 DUT=0
 85000.00ns INFO     A=1 DUT=0
 95000.00ns INFO     A=0 DUT=0
105000.00ns INFO     A=1 DUT=0
115000.00ns INFO     A=1 DUT=0
125000.00ns INFO     A=0 DUT=0
135000.00ns INFO     A=1 DUT=0
145000.00ns INFO     A=1 DUT=0
145000.00ns INFO     test_seq_bug1 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-krunalbadlani/level1_design2/test_seq_detect_1011.py", line 88, in test_seq_bug1
                         assert dut.seq_seen.value == 0b1,"the output of the sequence detector is wrong for the input bits "
                     AssertionError: the output of the sequence detector is wrong for the input bits 
```




### **Test scenario**
---

- inp_bits: 1,0,1,1,1,1,1,0,1,1,0,1,1
- Expected output: seq_seen = 0,0,0,1,0,0,0,0,0,1,0,0,1
- Observed output in the DUT = dut.seq_seen = 0,0,0,1,0,0,0,0,0,0,0,0,0



Output mismatches for the above inputs proving that there are design bugs

### **Design Bugs**
---
Based on the above test output and analysing the design,
we see the following


Bugs :-
```verilog
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            /*BUG1 :- the state SEQ_11 is missing, therefore the code fails when the sequence has more than 2 1's.*/ 
            SEQ_10 = 2, 
            SEQ_101 =  4,
            SEQ_1011 =  5;

  reg [2:0] current_state, next_state;

  
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

  
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;
        else
          next_state = SEQ_10;
      end
    //BUG1 :- SEQ_11 missing

      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;
      end
      SEQ_1011:
      begin
        next_state = IDLE; /* BUG2 :- No redirection t0 SEQ_10 to enable the overlapping functionality*/ 
      end
    endcase
  end
endmodule
```


### **Design Fix**
---
Updating the design 
```verilog
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_11 = 2,//change
            SEQ_10  = 3,
            SEQ_101 = 4,
            SEQ_1011 = 5;

  reg [2:0] current_state, next_state;

  
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

 
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_11;
        else
          next_state = SEQ_10;
      end

      SEQ_11://change
      begin
        if(inp_bit == 1)
          next_state = IDLE;
        else
          next_state = SEQ_10;
      end
      
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;
      end
      SEQ_1011:
      begin
        if(inp_bit == 0) //change
          next_state = SEQ_10; //change
        else //change
          next_state = IDLE;
      end
     
    endcase
  end
endmodule






```
and re-running the test makes the test pass.

![seq_detect_1011_corrected](https://github.com/krunalbadlani/muximages/blob/main/seq_detector_coreect.png)

The updated design is checked in as seq_detect_1011.v in the folder level1_design2_corrected.

### **Verification Strategy**
---

The design in question is an overlapping sequence detector, which means the design should always return a 1 as output whenever it sees the sequence '1011' anywhere in the sequence. The sequence of inputs that I have chosen is such that it has the correct sequence at the beginning then it is followed by some 1's which is followed by the correct sequence again. This is done to check whether the design is able to detect the sequence after some ones. Lastly this is followed by another correct sequence which means the overlap is checked as well (input sequence :- 1011111011011). The DUT output is logged at every input which helps us to see whether each and every sequence is detected or not. So the python testbench along with this particular input sequence is my verification strategy.


### **Is the verification complete?**
---
The functionality of the sequence detector along with its overlapping condition is fully verified here, hence yes it is complete in that sense.
