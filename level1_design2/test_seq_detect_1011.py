# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

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
    ##cocotb.log.info(f'A={int(dut.inp_bit.value):05} DUT={int(dut.seq_seen.value):05}')
    ##print("the value of output is {A} ".format(A=dut.seq_seen.value))
   
    assert dut.seq_seen.value == 0b1,"the output of the sequence detector is wrong for the input bits "
    print("the value of output is {A} ".format(A=dut.seq_seen.value))
