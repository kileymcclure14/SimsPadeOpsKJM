"""
Helper functions for writing input files

Skylar Gering
2025 Janudary 16
"""
import csv
import itertools
import jinja2
import json
import os
from pathlib import Path

# paths to folders
BASE = Path(__file__).parent.parent
TEMPLATE_PATH = BASE.joinpath("templates")
DEFAULTS_PATH = BASE.joinpath("defaults")
SIMS_PATH = BASE.joinpath("simulations")
DATA_PATH = os.environ['SCRATCH'] + "/Data/"

# important constants
TASKS_PER_NODE = 48  # skx nodes on Stampede3

def safe_mkdir(dst, quiet=False):
    """Make output directory without overwriting files."""
    dst_path = Path(dst)
    dst_path.mkdir(parents=True, exist_ok=True)
    if not quiet:
        print("\tCreated directory", dst_path.resolve())
    return dst_path

def get_nnodes(inputs):
    """
    Computes the ideal number of nodes for PadeOps.
    Rounds to an even number.
    """
    nx = inputs["nx"]
    ny = inputs["ny"]
    nz = inputs["nz"]
    # compute n_nodes; round to nearest even number
    n_nodes = 2 * round(nx * ny * nz / 32**3 / TASKS_PER_NODE / 2)
    return n_nodes

def update_inputs(new_inputs, curr_inputs):
    """Updates current (default) input values with user-provided new_inputs"""
    for name, val in new_inputs.items():
        curr_inputs[name] = val

def fill_template(inputs, template_path, file_path):
    with open(template_path, "r") as f:
        template = jinja2.Template(f.read(), undefined=jinja2.StrictUndefined)
    # render output
    out = template.render(inputs)
    with open(file_path, "w") as f:
        f.write(out)

def write_sim(new_inputs, curr_inputs, template_path, out_path, quiet):
    update_inputs(new_inputs, curr_inputs)
    fill_template(curr_inputs, template_path, out_path.joinpath(curr_inputs["sim_file_name"]))
    if not quiet:
        print("\tDone writing simulation .dat file.")

def write_turb(new_inputs, curr_inputs, template_path, out_turb_path, quiet, n_turbs):
    """Writes a turbine file by copying ActuatorDisk_0001_input.j2"""
    if n_turbs > 1: raise NotImplementedError
    update_inputs(new_inputs, curr_inputs)
    # note that this should only happen for the first turbine once we implement more (but needs to happen after update_inputs!
    file_path = out_turb_path.joinpath(f"ActuatorDisk_{n_turbs:04d}_input.inp")
    fill_template(curr_inputs, template_path, file_path)
    if not quiet:
        print(f"\tDone writing ActuatorDisk_{n_turbs:04d}_input.inp file")

def write_run(new_inputs, curr_inputs, template_path, out_path, quiet, n_nodes, node_cap):
    # TODO: set the right file path for the .e and .o files so I don't need to CD into them
    update_inputs(new_inputs, curr_inputs)
    curr_inputs["inputdir"] = str(out_path)  # add the output path for input files for template
    curr_inputs["n_hrs"] = int(curr_inputs["n_hrs"])
    curr_inputs["n_nodes"] = int(max(min(n_nodes, node_cap), 1))
    curr_inputs["job_path"] = out_path.joinpath(curr_inputs["job_name"])
    fill_template(curr_inputs, template_path, out_path.joinpath(curr_inputs["run_file_name"]))
    if not quiet:
        print("\tDone writing run file.")

def write_padeops_files(new_inputs, *, default_input,
    sim_template, run_template, turb_template = None,
    n_turbs = 1, quiet = False, node_cap = 128
):
    # load default parameters
    with Path(default_input).open(mode = 'r') as file:
        curr_inputs = json.load(file)
    # make input directory directory (user required to provide 'inputdir')
    inputdir = safe_mkdir(new_inputs["sim"]["inputdir"], quiet=quiet)
    # inputdir and outputdir must be the same for PadeOpsIO to work
    new_inputs["sim"]["outputdir"] = new_inputs["sim"]["inputdir"]
    # load turbine template and write simulation's .ini files (if there are turbines)
    if n_turbs > 0:
        turb_path = safe_mkdir(inputdir.joinpath(curr_inputs["sim"]["turb_dirname"]), quiet=quiet)
        curr_inputs["sim"]["turb_dirname"] = turb_path
        write_turb(new_inputs["turb"], curr_inputs["turb"], Path(turb_template), turb_path, quiet, n_turbs)
    # load sim template and write simulation's .dat file
    write_sim(new_inputs["sim"], curr_inputs["sim"], Path(sim_template), inputdir, quiet)
    # load run template and write .sh file to run simulation
    write_run(new_inputs["run"], curr_inputs["run"], Path(run_template), inputdir,
              quiet, get_nnodes(curr_inputs["sim"]), node_cap)  

def write_pardeops_suite(single_inputs, varied_inputs, quiet = False, nested = False, **kwargs):
    # grab path for simulation input and output
    inputdir = safe_mkdir(single_inputs["sim"]["inputdir"], quiet=quiet)
    jobname = single_inputs["run"]["job_name"]
    # define needed values for CSV
    row_header = ["id"]
    input_type_list = []
    value_lists = []

    for input_type in ["sim", "turb", "run"]:
        # skip input type if not in the varied_inputs dictionary
        if not input_type in varied_inputs: continue
        inputs = varied_inputs[input_type]
        row_header += inputs.keys()
        input_type_list += itertools.repeat(input_type, len(inputs))
        value_lists += inputs.values()
    # write CSV header
    csv_key_path = inputdir.joinpath('sim_ids.csv')
    with open(csv_key_path, 'w', newline='') as csv_key:
        writer = csv.writer(csv_key)
        writer.writerow(row_header)

    # write the files for each simulation
    suite_iter = itertools.product(*value_lists) if nested else itertools.zip_longest(*value_lists)
    for i, input_prod in enumerate(suite_iter):
        id = f"{i:04d}"
        # update needed values
        for j, val in enumerate(input_prod):
            input_key = row_header[j + 1]
            input_type = input_type_list[j]
            single_inputs[input_type][input_key] = val
        # create sub-directory
        single_inputs['sim']['inputdir'] = inputdir.joinpath(f"Sim_{id}")
        # set run ID
        single_inputs['sim']["RunID"] = id
        # update job name
        single_inputs["run"]["job_name"] = jobname + f"_{id}"
        # write files
        write_padeops_files(single_inputs, **kwargs)
        # add simulation to CSV
        with open(csv_key_path, "a") as csv_key:
            writer = csv.writer(csv_key)
            writer.writerow((id,) + input_prod)
    return

### Functions from Kirby I don't need yet! ###

# def find_last_restart(inputs, return_frameangle=True):
#     """
#     Finds the final restart file and gleans the TID
#     and frame angle, if requested
#     """
#     basedir = Path(inputs["restart_dir"])
#     RID = inputs["restart_rid"]
#     restart_files = basedir.glob(f"RESTART_Run{RID:02d}_info*")

#     # find the last restart file; largest TID
#     filename = None
#     tid = -1
#     for file in restart_files:
#         new_tid = int(
#             re.findall(r"info.(\d+)$", str(file))[0]
#         )  # glean the TID from the string
#         if new_tid > tid:
#             tid = new_tid
#             filename = file

#     if tid == 0:
#         # this did not find any files
#         warnings.warn(
#             "find_last_restart(): no restart files found, defaulting to TID 0"
#         )

#     if not return_frameangle:
#         return tid
#     else:
#         print(filename)
#         data = np.genfromtxt(filename, dtype=None)
#         if len(data) < 2:
#             frameangle = 0
#         else:
#             frameangle = -data[1]

#         return tid, frameangle

# def write_upsample(
#     inputs,
#     dst=None,
#     quiet=False,
#     inputfile_name="input_upsample.dat",
# ):
#     """
#     Writes upsampled fields inputs

#     nx, ny in `inputs` are the FINAL number of points in x and y, after upsampling
#     """

#     # update inputs
#     update_upsample_inputs(inputs)

#     # make output directory
#     OUTPUT = safe_mkdir(dst or inputs['dirname'], quiet=quiet)

#     # load spinup template and write template:
#     with open(TEMPLATE_UPSAMPLE, "r") as f:
#         template = jinja2.Template(f.read(), undefined=jinja2.StrictUndefined)

#     # render output
#     out = template.render(inputs)
#     with open(OUTPUT / inputfile_name, "w") as f:
#         f.write(out)

#     if not quiet:
#         print("\tDone writing upsampling files")


# def update_upsample_inputs(inputs):
#     """Glean the restart TID from the restart RID"""
#     TID = find_last_restart(inputs, return_frameangle=False)
#     inputs["restart_tid"] = TID
#     return  # updates dictionary, returns nothing


# def write_rotate(
#     inputs,
#     dst=None,
#     quiet=False,
#     inputfile_name="input_rotate.dat",
#     n_hrs=6,
# ):
#     """
#     Writes inputs for the rotation phase
#     """

#     # adds frame angle line to RESTART file
#     prep_rotation(inputs, quiet=quiet)

#     # make output directory
#     OUTPUT = safe_mkdir(dst or inputs['dirname'], quiet=quiet)

#     # load spinup template and write template:
#     with open(TEMPLATE_ROTATE, "r") as f:
#         template = jinja2.Template(f.read(), undefined=jinja2.StrictUndefined)

#     # render output
#     out = template.render(inputs)
#     with open(OUTPUT / inputfile_name, "w") as f:
#         f.write(out)

#     # make submit.sh file
#     with open(OUTPUT / "submit_rotation.sh", "w") as f:
#         f.write(
#             sbatch_write_file(
#                 inputs, inputfile_name, problem_name="neutral_pbl", n_hrs=n_hrs
#             )
#         )

#     if not quiet:
#         print("\tDone writing rotation files")


# def prep_rotation(inputs, rid=2, tid=0, frameangle=0.0, quiet=False):
#     """Appends frame angle line to rotation restart files"""
#     fname = Path(inputs["restart_dir"]) / f"RESTART_Run{rid:02d}_info.{tid:06d}"

#     try:
#         data = np.genfromtxt(fname, dtype=None)
#         if len(np.atleast_1d(data)) > 1:
#             return  # frame angle line already exists
#     except FileNotFoundError:
#         raise

#     with open(fname, "a") as src:
#         src.write(f"{frameangle:11.1f}")

#     if not quiet:
#         print("Added frame angle to retart files for rotation phase")


# def write_concurrent(
#     inputs,
#     dst=None,
#     quiet=False,
#     n_hrs=24,
# ):
#     """
#     Write concurrent files, main function. Calls helper function
#     _write_concurrent() after gleaning the restart TID and frame angle
#     from restart files.
#     """

#     # make output directory
#     OUTPUT = safe_mkdir(dst or inputs['dirname'], quiet=quiet)
#     # finish populating restart_tid, frame_angle fields
#     tid, frameangle = find_last_restart(inputs, return_frameangle=True)
#     inputs.update(frameangle=frameangle, restart_tid=tid)

#     for _template, name in zip(
#         [TEMPLATE_PRIMARY, TEMPLATE_PRECURSOR, TEMPLATE_CONCURRENT],
#         ["primary", "precursor", "main"],
#     ):
#         # load spinup template and write template:
#         with open(_template, "r") as f:
#             template = jinja2.Template(f.read(), undefined=jinja2.StrictUndefined)

#         # render output
#         out = template.render(inputs)
#         with open(OUTPUT / f"input_{name}.dat", "w") as f:
#             f.write(out)

#         if not quiet:
#             print(f"\tDone writing {name} files")

#     # make submit.sh file
#     with open(OUTPUT / "submit_concurrent.sh", "w") as f:
#         f.write(
#             sbatch_write_file(
#                 inputs,
#                 "input_main.dat",
#                 problem_name="neutral_pbl_concurrent",
#                 n_hrs=n_hrs,
#             )
#         )

if __name__ == "__main__":
    pass
