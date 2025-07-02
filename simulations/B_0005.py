import jinja_sim_utils as ju
import os
from pathlib import Path

sim_template = ju.TEMPLATE_PATH.joinpath("sim_template.jinja")
turb_template = ju.TEMPLATE_PATH.joinpath("turb_template.jinja")
run_template = ju.TEMPLATE_PATH.joinpath("run_template.jinja")
default_inputs = ju.DEFAULTS_PATH.joinpath("fixed_defaults.json")

# file name based on current script name
curr_script_name = Path(__file__).with_suffix('').name

single_inputs = dict(
    sim = dict(
        # always need to provide the filepaths (no defaults)
        inputdir = ju.DATA_PATH + curr_script_name + "_Files",
        outputdir = ju.DATA_PATH + curr_script_name + "_Files",
        # if not provided, default_inputs will be used
       CFL = 1.0,
       nx = 192,
       ny = 128,
       nz = 128,
       Lx = 38.4,
       Ly = 12.8,
       Lz = 2.857,
       do_budgets = True,
       budgets_dir = ju.DATA_PATH + curr_script_name + "_Files",

    ),
    turb = dict(  # can only provide one turbine right now - update when needed
        # if not provided, default_inputs will be used
        useCorrection = True,
        xLoc = 5,
        zLoc = 1.4285,
    ),
    run = dict(
        # always need to provide the filepaths (no defaults)
        problem_dir = "turbines",
        problem_name = "AD_coriolis_shear",
        job_name = "hblocked_budgets_kjm",
        # if not provided, default_inputs will be used
        n_hrs = 24,
    )
)

varied_inputs = dict(turb = dict(cT = [-4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0] ))  # below and above the Betz limit


ju.write_padeops_suite(single_inputs, varied_inputs, nested = True, default_input = default_inputs,
    sim_template = sim_template, run_template = run_template, turb_template = turb_template)