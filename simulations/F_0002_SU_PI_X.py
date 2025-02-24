import itertools
import jinja_sim_utils as ju
from pathlib import Path

# TODO: Compare to F_0000_SU_X_plots

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
        Lz = 5,
        tstop = 250,
        t_dataDump = 50,
    ),
    turb = dict(  # can only provide one turbine right now - update when needed
        # if not provided, default_inputs will be used
        # surge_freq = 0.15,
        # surge_amplitude = 0.25,
        useCorrection = True,
        cT = 1.0,
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

# simulation setup parameters
nx = [160, 384]
ny = [80, 192]
nz = [80, 192]
# filter delta/D = 3h/2D -> delta = 3h/2 since D = 1 and h = sqrt(dx^2 + dy^2 + dz^2)
filterWidth = [ju.find_filter_width(nx[i], ny[i], nz[i], single_inputs) for i, _ in enumerate(nx)]

# moving turbine parameters 
sf = [0, 1]
sa = [0, 0]
pa = [0, 5.0]

varied_inputs = itertools.product(itertools.zip_longest(nx, ny, nz, filterWidth), itertools.zip_longest(sf, sa, pa))
# add appropriate dt as the first element for all iterations
CFL = 0.8
varied_inputs = [(ju.find_min_dt(CFL, vin[0][0], vin[0][1], vin[0][2], vin[1][0], single_inputs, v = 0.0, w = 0.0), ) + vin for vin in varied_inputs]
varied_header = ["dt", "nx", "ny", "nz", "filterWidth", "surge_freq", "surge_amplitude", "pitch_amplitude"]
# write needed simulation files
ju.write_padeops_suite(single_inputs, varied_inputs, varied_header = varied_header, default_input = default_inputs,
    sim_template = sim_template, run_template = run_template, turb_template = turb_template)