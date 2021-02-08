# NATS sample
#
# Optimal Synthesis Inc.
#
# Oliver Chen
# 09.27.2019
#
# Demo of gate-to-gate trajectory simulation.
#
# The aircraft starts from the origin gate, goes through departing taxi plan, takes off, goes through different flight phases to the destination airport, and finally reaches the destination gate.
import sys
sys.path.append('/home/dyn.datasys.swri.edu/mhartnett/NASA_ULI/NASA_ULI_InfoFusion/src/NATS/Client/')

from NATS_header import NATS_Config
from NATS_MonteCarlo_Interface import NATS_MonteCarlo_Interface
from sys import argv
import time
import numpy as np
import time

def main(arg):
    trx, mfl = "share/tg/trxSwRI/TRX_DEMO_Combined_GateToGate.trx", "share/tg/trxSwRI/TRX_DEMO_Combined_GateToGate_mfl.trx"
    config = NATS_Config(duration=7200, interval=1, track_file = trx, max_flt_lev_file = mfl)
    MC_interface = NATS_MonteCarlo_Interface(config)

    filename = MC_interface.runMCSimWithPause(arg)
    return filename
