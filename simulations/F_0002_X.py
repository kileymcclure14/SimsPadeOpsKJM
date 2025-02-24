import itertools
import jinja_sim_utils as ju
from pathlib import Path

# The purpose of this simulation was to study how different filter widths,
# along with turning the correction calculation on and off, would effect the value of Cp,
# especially compared to the analytical value.

sim_template = ju.TEMPLATE_PATH.joinpath("sim_template.jinja")
turb_template = ju.TEMPLATE_PATH.joinpath("turb_template.jinja")
run_template = ju.TEMPLATE_PATH.joinpath("run_template.jinja")
default_inputs = ju.DEFAULTS_PATH.joinpath("floating_defaults.json")

# file name based on current script name
curr_script_name = Path(__file__).with_suffix('').name

single_inputs = dict(
    sim = dict(
        # always need to provide the filepaths (no defaults)
        inputdir = ju.DATA_PATH + curr_script_name + "_Files",
        outputdir = ju.DATA_PATH + curr_script_name + "_Files",
        # if not provided, default_inputs will be used
        Lx = 25,
        Ly = 10,
        Lz = 10,
        nx = 256,
        ny = 128,
        nz = 128,
        tstop = 250,
        t_dataDump = 50,
    ),
    turb = dict(  # can only provide one turbine right now - update when needed
        # if not provided, default_inputs will be used
        cT = 1.0,
        surge_freq = 0.0,
        surge_amplitude = 0.0,
        pitch_amplitude = 0.0,
    ),
    run = dict(
        # always need to provide the filepaths (no defaults)
        problem_dir = "turbines",
        problem_name = "AD_coriolis_shear",
        job_name = "grid_resolution_test_sg",
        # if not provided, default_inputs will be used
        n_hrs = 4,
    )
)
single_inputs["sim"]["dt"] = ju.find_min_dt(1.0, 256, 128, 128, 0.0, single_inputs, v = 0.0, w = 0.0)
factor_list = [0.25, 1.5, 2.75, 4.0]
filterWidth = [ ju.find_filter_width(single_inputs, factor = f) for f in factor_list]
useCorrection = [True, False]
varied_inputs = itertools.product(useCorrection, filterWidth)
varied_header = ["useCorrection", "filterWidth"]
# write needed simulation files
ju.write_padeops_suite(single_inputs, varied_inputs, varied_header = varied_header, default_input = default_inputs,
    sim_template = sim_template, run_template = run_template, turb_template = turb_template)