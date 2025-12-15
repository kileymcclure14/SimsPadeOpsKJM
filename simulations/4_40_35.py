import jinja_sim_utils as ju
import os
from pathlib import Path

# TODO: need to add in scratch path so the run scripts have the right file path

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
        # if not provided, default_inputs will be used
        t_dataDump = 1000,
        CFL = 1.0,
        tstop = 400,
        nx = 192,
        ny = 128,
        nz = 128,
        Lx = 38.4,
        Ly = 1.497,
        Lz = 1.497,
        do_budgets = True,
        budgets_dir = ju.DATA_PATH + curr_script_name + "_Files"

    ),
    turb = dict(  # can only provide one turbine right now - update when needed
        # if not provided, default_inputs will be used
        cT = 4,
        yaw = 40,
        useCorrection = True,
        xLoc = 5,
        yLoc = 0.7485,
        zLoc = 0.7585,
    ),
    run = dict(
        # always need to provide the filepaths (no defaults)
        problem_dir = "turbines",
        problem_name = "AD_coriolis_shear",
        job_name = "10deg_mblock_kjm",
        # if not provided, default_inputs will be used
        n_hrs = 24,
    )
)
single_inputs["turb"]["filterWidth"] = ju.find_filter_width(single_inputs)

ju.write_padeops_files(single_inputs, default_input = default_inputs,
    sim_template = sim_template, run_template = run_template, turb_template = turb_template)