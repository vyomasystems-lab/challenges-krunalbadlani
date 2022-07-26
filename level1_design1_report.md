# **STAGE 2 REPORT**
## **level1_design1 - MUX**
---
The verification is setup using Vyoma's UpTickPro provided for the hackathon.

![Gitpod screenshot](https://github.com/krunalbadlani/muximages/blob/main/gitpod_screen.png)


### **Verification Environment**
---
The CocoTb based python test is developed as explained. The test drives inputs to the Design Under Test(Mux module here) which takes in a select input 'sel' of 5 bit and one of the 31 inputs (inp0-inp30) of 2 bits each present in the DUT and gives a 2 bit output 'out'. 

The values to the select input and the input port are given using

Case1 :- Select input = 12 , input12 = 3
``` python
    A = 0b01100
    B = 0b11
    dut.sel.value = A
    dut.inp12.value = B
```
Case2 :- Select input = 30 , input30 = 3
```python
    A = 0b11110
    B = 0b11
    dut.sel.value = A
    dut.inp30.value = B
```
The assert statement is used for comparing the mux's output with the  expected output.

The following error is seen:

Case1 :-

```
assert dut.out.value == B,"Mux test failed with select input :- {A} as  input is {B} but the output is {SUM}".format(
                     AssertionError: Mux test failed with select input :- 12 as  input is 3 but the output is 0
```

Case2 :-

```
assert dut.out.value == B,"Mux test failed with select input :- {A} as  input is {B} but the output is {SUM}".format(
                     AssertionError: Mux test failed with select input :- 30 as  input is 3 but the output is 0
```


### **Test scenario**
---

Case1 :-
- Test inputs: sel = 12 , input12 = 3
- Expected output: out = 3
- Observed output in the DUT dut.out = 0

Case2 :-
- Test inputs: sel = 30 , input30 = 3
- Expected output: out = 3
- Observed output in the DUT dut.out = 0

Output mismatches for the above inputs proving that there are 2 design bugs

### **Design Bugs**
Based on the above test output and analysing the design,
we see the following

---
Bug1 :-
```verilog
5'b01101: out = inp12; //BUG1
```
Bug2 :-
```verilog
5'b11101: out = inp29;
//case for inp30 is missing //BUG2
default: out = 0;
```
### **Design Fix**
---
Updating the design and re-running the test makes the test pass.

![mux_corrected](https://github.com/krunalbadlani/muximages/blob/main/mux%20correct%20output.png)

The updated design is checked in as mux.v in the folder level1_design1_corrected.

### **Verification Strategy**
---

Mux is a combinational circuit which passes a particular input as the output based on the select input. In the design in question a 31:1 mux is used, i.e. the inputs will be from input 0 to input 30 and the select input would be of 5 bits so that we can get 2^5 = 32 cases out of which 31 can be used to select the inputs to be passed on t0 the output. Therefore to test the circuit, I gave  0-30 to the select input and at the same time I gave the 2 bit input '3' to the corresponding input line. During the process it was found that on select input 12 the output came 0 which is the default output, which implied that the case for select input 12 i.e 01100 in binary is missing, moving forward, similar situation was seen for the select input 30 i.e. 11110 in binary. This verification strategy made sure that all the 0-30 i.e. all the 31 select inputs were checked.


### **Is the verification complete?**
---
The functionality of the 31:1 mux in question is fully verified here, hence yes it is complete
