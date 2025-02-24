import itertools
import jinja_sim_utils as ju
from pathlib import Path

# The purpose of this simulation was to study how different domain sizes in y and z
# would affect the value of Cp, especially compared to the analytical value,
# due to blockage causing speedups especially compared to the analytical value.

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
        filterWidth = 0.032,
        useCorrection = False,
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
y_dim = [15, 5, 10, 20]  # added in large first value to replace 2.5, which produced all NaNs
z_dim = y_dim
factor = 10.0 / 128.0  # middle of the road resolution used in F_0002_X simulations
ny = [y / factor for y in y_dim]
nz = ny
varied_inputs = itertools.zip_longest(y_dim, z_dim, ny, nz)
varied_header = ["Ly", "Lz", "ny", "nz"]
# write needed simulation files
ju.write_padeops_suite(single_inputs, varied_inputs, varied_header = varied_header, default_input = default_inputs,
    sim_template = sim_template, run_template = run_template, turb_template = turb_template)