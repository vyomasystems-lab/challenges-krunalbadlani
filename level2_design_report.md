# **STAGE 2 REPORT**
## **level2_design - bitmanipulation coprocessor**
---
The verification is setup using Vyoma's UpTickPro provided for the hackathon.

![Gitpod screenshot](https://github.com/krunalbadlani/muximages/blob/main/gitpod_screen.png)


### **Verification Environment**
---
The CocoTb based python test is developed as explained. The test drives inputs to the Design Under Test(mkbitmanip module here) which takes in 4, 32 bit inputs, namely mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2 and mav_putvalue_src3. This combination yields the 32 bit output named dut_output . 

The values to the inputs are given as follows:-

- As the inputs are of size 32 bit, I have randomized the inputs mav_putvalue_src1 and mav_putvalue_src2 to a value between 0 and 2^32.
- mav_putvalue_src3 is set to 0 for the sake of simplicity.
- mav_putvalue_instr is given values from a python list 'instr' containing all instructions given in the reference model in 32 bit format.
``` python
    for j in range(1):

        A = random.randint(0, 4294967295)
        B = random.randint(0, 4294967295)
        
    
    mav_putvalue_src1 = A
    mav_putvalue_src2 = B
    print("input1 = {A} , input2 = {B}".format(A=hex(mav_putvalue_src1),B=hex(mav_putvalue_src2)))
    mav_putvalue_src3 = 0x0
    ##mav_putvalue_instr = 0x101010B3
    instr =[0x40006033,0x40004033,0x20001033,0x20005033,0x60001033,0x60005033,
    0x20002033,0x20004033,0x20006033,0x48001033,0x28001033,0x68001033,0x48005033,
    0x28005033,0x68005033,0x6001033,0x6005033,0x4001033,0x4005033,0x60001013,
    0x60101013,0x60201013,0x60401013,0x60501013,0x61001013,0x61101013,0x61201013,0x61801013,
    0x61901013,0x61A01013,0xA001033,0xA003033,0xA002033,0xA004033,0xA005033,0xA006033,
    0xA007033,0x48006033,0x8006033,0x8004033,0x48004033,0x8007033,0x20001013,0x22005013,0x62005013,
    0x48001013,0x28001013,0x68001013,0x48005013,0x8001033,0x8005033,0x8001013,0x8005013,0x2A005013,
    0x6A005013,0x4005013,0x48007033,0x40007033]
    for i in instr:
        print("The instruction executed is = {K}".format(K = bin(i)))
        mav_putvalue_instr = i
```



The assert statement is used for comparing the sequence detector's output with the expected output.




The following error is seen:



```
input1 = 0xf335cf95 , input2 = 0xb1655892
The instruction executed is = 0b1000000000000000110000000110011
--ORN 2
     0.01ns INFO     DUT OUTPUT=0x1ff7fdffb
     0.01ns INFO     EXPECTED OUTPUT=0x1ff7fdffb
The instruction executed is = 0b1000000000000000100000000110011
--XNOR 3
     0.01ns INFO     DUT OUTPUT=0x17b5ed1f1
     0.01ns INFO     EXPECTED OUTPUT=0x17b5ed1f1
The instruction executed is = 0b100000000000000001000000110011
--SLO  4
     0.01ns INFO     DUT OUTPUT=0x7cafffff
     0.01ns INFO     EXPECTED OUTPUT=0x7cafffff
The instruction executed is = 0b100000000000000101000000110011
--SRO  5
     0.01ns INFO     DUT OUTPUT=0x1fffff99b
     0.01ns INFO     EXPECTED OUTPUT=0x1fffff99b
The instruction executed is = 0b1100000000000000001000000110011
--ROL  6
     0.01ns INFO     DUT OUTPUT=0x7caf99af
     0.01ns INFO     EXPECTED OUTPUT=0x7caf99af
The instruction executed is = 0b1100000000000000101000000110011
--ROR  7
     0.02ns INFO     DUT OUTPUT=0xe7caf99b
     0.02ns INFO     EXPECTED OUTPUT=0xe7caf99b
The instruction executed is = 0b100000000000000010000000110011
--SH1ADD  8
     0.02ns INFO     DUT OUTPUT=0x12fa1ef79
     0.02ns INFO     EXPECTED OUTPUT=0x12fa1ef79
The instruction executed is = 0b100000000000000100000000110011
--SH2ADD  9
     0.02ns INFO     DUT OUTPUT=0xfc792dcd
     0.02ns INFO     EXPECTED OUTPUT=0xfc792dcd
The instruction executed is = 0b100000000000000110000000110011
--SH3ADD  10
     0.02ns INFO     DUT OUTPUT=0x9627aa75
     0.02ns INFO     EXPECTED OUTPUT=0x9627aa75
The instruction executed is = 0b1001000000000000001000000110011
--SBCLR   11
     0.02ns INFO     DUT OUTPUT=0x1e6639f2b
     0.02ns INFO     EXPECTED OUTPUT=0x1e6639f2b
The instruction executed is = 0b101000000000000001000000110011
--SBSET   12
     0.02ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.02ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1101000000000000001000000110011
--SBINV  13
     0.02ns INFO     DUT OUTPUT=0x1e6639f2b
     0.02ns INFO     EXPECTED OUTPUT=0x1e6639f2b
The instruction executed is = 0b1001000000000000101000000110011
--SBEXT  14
     0.02ns INFO     DUT OUTPUT=0x3
     0.02ns INFO     EXPECTED OUTPUT=0x3
The instruction executed is = 0b101000000000000101000000110011
--GORC 15 (check)
     0.02ns INFO     DUT OUTPUT=0x1ffebffeb
     0.02ns INFO     EXPECTED OUTPUT=0x1ffebffeb
The instruction executed is = 0b1101000000000000101000000110011
--GREV  16 (should check)
     0.03ns INFO     DUT OUTPUT=0x7ecbf98b
     0.03ns INFO     EXPECTED OUTPUT=0x7ecbf98b
The instruction executed is = 0b110000000000001000000110011
--CMIX  17
     0.03ns INFO     DUT OUTPUT=0x1624a9121
     0.03ns INFO     EXPECTED OUTPUT=0x1624a9121
The instruction executed is = 0b110000000000101000000110011
--CMOV 18
     0.03ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.03ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b100000000000001000000110011
--FSL 19
     0.03ns INFO     DUT OUTPUT=0x7ca80001
     0.03ns INFO     EXPECTED OUTPUT=0x7ca80001
The instruction executed is = 0b100000000000101000000110011
--FSR  20(check)
     0.03ns INFO     DUT OUTPUT=0x799b
     0.03ns INFO     EXPECTED OUTPUT=0x799b
The instruction executed is = 0b1100000000000000001000000010011
--CLZ   21
     0.03ns INFO     DUT OUTPUT=0x1
     0.03ns INFO     EXPECTED OUTPUT=0x1
The instruction executed is = 0b1100000000100000001000000010011
--CTZ    22
     0.03ns INFO     DUT OUTPUT=0x1
     0.03ns INFO     EXPECTED OUTPUT=0x1
The instruction executed is = 0b1100000001000000001000000010011
--PCNT   23
     0.03ns INFO     DUT OUTPUT=0x29
     0.03ns INFO     EXPECTED OUTPUT=0x29
The instruction executed is = 0b1100000010000000001000000010011
--SEXT.B  24
     0.03ns INFO     DUT OUTPUT=0x1ffffff2b
     0.03ns INFO     EXPECTED OUTPUT=0x1ffffff2b
The instruction executed is = 0b1100000010100000001000000010011
--SEXT.H  25
     0.03ns INFO     DUT OUTPUT=0x1ffff9f2b
     0.03ns INFO     EXPECTED OUTPUT=0x1ffff9f2b
The instruction executed is = 0b1100001000000000001000000010011
--CRC32.B 26
     0.04ns INFO     DUT OUTPUT=0x1012ca409
     0.04ns INFO     EXPECTED OUTPUT=0x1012ca409
The instruction executed is = 0b1100001000100000001000000010011
--CRC32.H  27
     0.04ns INFO     DUT OUTPUT=0xfdaa497
     0.04ns INFO     EXPECTED OUTPUT=0xfdaa497
The instruction executed is = 0b1100001001000000001000000010011
--CRC32.W  28
     0.04ns INFO     DUT OUTPUT=0x12dd143f7
     0.04ns INFO     EXPECTED OUTPUT=0x12dd143f7
The instruction executed is = 0b1100001100000000001000000010011
--CRC32C.B 29
     0.04ns INFO     DUT OUTPUT=0x14f55bb89
     0.04ns INFO     EXPECTED OUTPUT=0x14f55bb89
The instruction executed is = 0b1100001100100000001000000010011
--CRC32C.H  30
     0.04ns INFO     DUT OUTPUT=0x960360d
     0.04ns INFO     EXPECTED OUTPUT=0x960360d
The instruction executed is = 0b1100001101000000001000000010011
--CRC32C.W  31
     0.04ns INFO     DUT OUTPUT=0x1c03073ad
     0.04ns INFO     EXPECTED OUTPUT=0x1c03073ad
The instruction executed is = 0b1010000000000001000000110011
--CLMUL  32
     0.04ns INFO     DUT OUTPUT=0x19b2229f5
     0.04ns INFO     EXPECTED OUTPUT=0x19b2229f5
The instruction executed is = 0b1010000000000011000000110011
--CLMULH  33
     0.04ns INFO     DUT OUTPUT=0xd03b2e6d
     0.04ns INFO     EXPECTED OUTPUT=0xd03b2e6d
The instruction executed is = 0b1010000000000010000000110011
--CLMULR  34
     0.04ns INFO     DUT OUTPUT=0x1a0765cdb
     0.04ns INFO     EXPECTED OUTPUT=0x1a0765cdb
The instruction executed is = 0b1010000000000100000000110011
--MIN  35
     0.04ns INFO     DUT OUTPUT=0x162cab125
     0.04ns INFO     EXPECTED OUTPUT=0x162cab125
The instruction executed is = 0b1010000000000101000000110011
--MAX 36
     0.04ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.04ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1010000000000110000000110011
--MINU  37
     0.05ns INFO     DUT OUTPUT=0x162cab125
     0.05ns INFO     EXPECTED OUTPUT=0x162cab125
The instruction executed is = 0b1010000000000111000000110011
--MAXU 38
     0.05ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.05ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1001000000000000110000000110011
--BDEP 39
     0.05ns INFO     DUT OUTPUT=0x22c82105
     0.05ns INFO     EXPECTED OUTPUT=0x22c82105
The instruction executed is = 0b1000000000000110000000110011
--BEXT 40
     0.05ns INFO     DUT OUTPUT=0x7bdd
     0.05ns INFO     EXPECTED OUTPUT=0x7bdd
The instruction executed is = 0b1000000000000100000000110011
--PACK 41
     0.05ns INFO     DUT OUTPUT=0xb1259f2b
     0.05ns INFO     EXPECTED OUTPUT=0xb1259f2b
The instruction executed is = 0b1001000000000000100000000110011
--PACKU 42
     0.05ns INFO     DUT OUTPUT=0x162cbe66b
     0.05ns INFO     EXPECTED OUTPUT=0x162cbe66b
The instruction executed is = 0b1000000000000111000000110011
--PACKH 45
     0.05ns INFO     DUT OUTPUT=0x1252b
     0.05ns INFO     EXPECTED OUTPUT=0x1252b
The instruction executed is = 0b100000000000000001000000010011
--SLOI  46
     0.05ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.05ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b100010000000000101000000010011
--SROI 47
     0.05ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.05ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1100010000000000101000000010011
--RORI  48
     0.06ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.06ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1001000000000000001000000010011
--SBCLRI   49
     0.06ns INFO     DUT OUTPUT=0x1e66b9f29
     0.06ns INFO     EXPECTED OUTPUT=0x1e66b9f29
The instruction executed is = 0b101000000000000001000000010011
--SBSETI   50
     0.06ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.06ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1101000000000000001000000010011
--SBINVI  51
     0.06ns INFO     DUT OUTPUT=0x1e66b9f29
     0.06ns INFO     EXPECTED OUTPUT=0x1e66b9f29
The instruction executed is = 0b1001000000000000101000000010011
--SBEXTI  52
     0.06ns INFO     DUT OUTPUT=0x3
     0.06ns INFO     EXPECTED OUTPUT=0x3
The instruction executed is = 0b1000000000000001000000110011
--SHFL  53
     0.06ns INFO     DUT OUTPUT=0x19e3be72b
     0.06ns INFO     EXPECTED OUTPUT=0x19e3be72b
The instruction executed is = 0b1000000000000101000000110011
--UNSHFL  54
     0.06ns INFO     DUT OUTPUT=0x19e3be72b
     0.06ns INFO     EXPECTED OUTPUT=0x19e3be72b
The instruction executed is = 0b1000000000000001000000010011
--SHFLI  55 (check)
     0.06ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.06ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1000000000000101000000010011
--UNSHFLI  56  (check)
     0.06ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.06ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b101010000000000101000000010011
--GORCI 57
     0.06ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.06ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1101010000000000101000000010011
--GREVI  58
     0.07ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.07ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b100000000000101000000010011
--_FSRI  59
     0.07ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.07ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1001000000000000111000000110011
--BFP  60
--SLO function
     0.07ns INFO     DUT OUTPUT=0x1e66b9f2b
     0.07ns INFO     EXPECTED OUTPUT=0x1e66b9f2b
The instruction executed is = 0b1000000000000000111000000110011
--ANDN 1
     0.07ns INFO     DUT OUTPUT=0x1624a9121
     0.07ns INFO     EXPECTED OUTPUT=0x84210e0b
     0.07ns INFO     run_test failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-krunalbadlani/level2_design/test_mkbitmanip.py", line 82, in run_test
                         assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x1624a9121 does not match MODEL = 0x84210e0b
     0.07ns INFO     

 
```
![Error_ss](https://github.com/krunalbadlani/muximages/blob/main/des2_err.png)



### **Test scenario**
---

- inputs: src1 = 0xf335cf95 , src2 = 0xb1655892, src3 = 0x0, instructions = all values from the list 'instr'
- Expected output: 'PASS' for all instructions whose expected values are taken by the test from the reference model.
- Observed output in the DUT = FAIL for 'ANDN 1'' instruction and PASS for all other instructions.



Output mismatches for the above inputs prove that there are design bugs

### **Design Bugs**
---
Based on the above test output and analysing the design,
we see the following


From the output of the test, it can be seen that there is a bug in the design for the operation 'ANDN 1`'.








### **Verification Strategy**
---

The design in question is a very complex design of a bit manipulation coprocessor. The verification problem here requires us to check the design for a specific set of instruction that this coprocessor can perform. I have randomly given 32 bit inputs to the src1 and src2 inputs and 0 to the src3 input. Then I have created a list of all the specific 32 bit instructions that need to be tested in proper format to match the reference file. Then I have given the instr input from the list in an ordered fashion and the output is compared to the output from the reference model file. The mismatch case of the ANDN instruction is purposefully kept last to check the other instructions before it making the test fail, and all the other instructions dont fail which can be seen from the log values.Hence,the ANDN operation is the one which is needed to be rectified in the design.


### **Is the verification complete?**
---
As this is a very small instance of the bitmanipulation coprocessor, the verification might not be complete. 
