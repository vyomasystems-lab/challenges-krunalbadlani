# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_lcd_bug1(dut):
    """Test for lcd interfacing """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    await FallingEdge(dut.clk)
    print("expected value = 0x38")
    dut_output = dut.dout.value
    cocotb.log.info(f'DUT output = {hex(dut_output)}')

    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x01")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')

    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x0E")
    dut_output = dut.dout.value
    cocotb.log.info(f'DUT output = {hex(dut_output)}')

    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x06")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')

    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x80")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')
    
    
   #v
    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x76")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')
   #e 
    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x65")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')
   #r 
    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x72")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')
   #i 
    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x69")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')
   #l 
    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x6C")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')
   #o 
    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x6F")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')
   #g 
    await FallingEdge(dut.clk)
    dut_output = dut.dout.value
    print("expected value = 0x67")
    cocotb.log.info(f'DUT output = {hex(dut_output)}')

    
    assert dut.dout.value == 0x67,"the output {K} of the lcd is wrong, it should be 0x67 ".format(K = hex(dut.dout.value))
    print("the value of output is {A} ".format(A=hex(dut.dout.value)))
