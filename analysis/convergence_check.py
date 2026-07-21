import analysis_utils as au
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import padeopsIO as pio
import cmcrameri.cm as cmc
import time

data_path = Path(au.DATA_PATH)

# Load Data
print("\n[1/4] Initializing BudgetIO...")
init_start = time.perf_counter()
sim = pio.BudgetIO("Data/HIT_Filter/CTP_2/TI_3/10PCT", padeops=True, runid=3)
print(sim)
print
init_time = time.perf_counter() - init_start
print(f"✓ BudgetIO initialized in {init_time:.2f}s")


ubar = sim.slice(budget_terms=["ubar"], ylim = 1.4)

ubar["ubar"].imshow()
plt.title('HIT Filter Domain, 20% Blockage, CTP = 2, TI = 3')
plt.savefig('10PCTf_23.png', dpi=300)


