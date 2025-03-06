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
        t_dataDump = 50,
        CFL = 1.0,
    ),
    turb = dict(  # can only provide one turbine right now - update when needed
        # if not provided, default_inputs will be used
    ),
    run = dict(
        # always need to provide the filepaths (no defaults)
        problem_dir = "turbines",
        problem_name = "AD_coriolis_shear",
        job_name = "unblocked_ctprime_kjm",
        # if not provided, default_inputs will be used
        n_hrs = 4,
    )
)

varied_inputs = dict(turb = dict(cT = [1.0, 1.5, 2.0, 2.5]))  # below and above the Betz limit


ju.write_padeops_suite(single_inputs, varied_inputs, nested = True, default_input = default_inputs,
    sim_template = sim_template, run_template = run_template, turb_template = turb_template)