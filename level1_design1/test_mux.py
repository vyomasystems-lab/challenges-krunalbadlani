# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""
    await Timer(10, units='ns')
    A = 0b01100
    B = 0b11
    await Timer(2, units='ns')
    dut.sel.value = A
    dut.inp12.value = B
    await Timer(2, units='ns')
    dut._log.info(f'A={A:05} B={B:05} DUT={int(dut.out.value):05}')
    
    assert dut.out.value == B,"Mux test failed with select input :- {A} as  input is {B} but the output is {SUM}".format(
            A=int(dut.sel.value), B=int(dut.inp12.value), SUM=int(dut.out.value))
    
    print ("Mux test passed with select input :- {A} and  input {B} and output as {SUM},which are equal".format( A=int(dut.sel.value), B=int(dut.inp12.value), SUM=int(dut.out.value)))
           
    

@cocotb.test()
async def test_mux2(dut):
    """Test for mux2"""
    await Timer(10, units='ns')
    A = 0b11110
    B = 0b11
    await Timer(2, units='ns')
    dut.sel.value = A
    dut.inp30.value = B
    await Timer(2, units='ns')
    dut._log.info(f'A={A:05} B={B:05} DUT={int(dut.out.value):05}')
    
    assert dut.out.value == B,"Mux test failed with select input :- {A} as  input is {B} but the output is {SUM}".format(
            A=int(dut.sel.value), B=int(dut.inp30.value), SUM=int(dut.out.value))
    
    print ("Mux test passed with select input :- {A} and  input {B} and output as {SUM}, which are equal".format( A=int(dut.sel.value), B=int(dut.inp30.value), SUM=int(dut.out.value)))
           
    
   

