import analysis_utils as au
from pathlib import Path
import os
import math
import padeopsIO as pio
import matplotlib.pyplot as plt
import numpy as np
from padeopsIO import turbine

sim = pio.BudgetIO("Data/HIT_AD/CTP_2/TI_3/20PCT", padeops = True, runid = 5)

u = sim.slice(budget_terms=["ubar"], ylim = 0.99)

u["ubar"].imshow()
plt.title('HIT Empty Domain, Spinup')
plt.savefig('20PCT.png', dpi=300)
