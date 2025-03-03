import analysis_utils as au
import quick_metadata_plots as mplts

mplts.plot_run_power(au.DATA_PATH + "U_00008_Files", label = "cT = 3.0")

mplts.plot_suite_power(au.DATA_PATH + "U_0008_Files")