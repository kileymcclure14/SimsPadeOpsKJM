# PadeOpsSims

Simulations run on PadeOps.

Simulation setups use templates for input (both general and turbine) and run files, which are then filled in with Jinja. Thus, the most important files are actually the files that define the paramters that are then filled into the templetes - these are in the `simulations` folder. These is also a `default` folder that holds files that contains good default parameters for most of the simulation values. There are what will be used if alteratives are not provided within the simulation file itself. There is also an `analysis` folder that hold some basic code for plotting and data access.

You can create both single runs and whole simulations with the `write_padeops_files` and `write_pardeops_suite`, respectively, which are both in the `jinja_sim_utils.py` file.

The basic workflow is as follows:

### Installation
1. Fork this repository and clone it into your `scratch` folder.
2. Make a `Data` folder also in the `scratch` folder.

Remember that scratch is periodically deleted!! So make sure to push your changes! And save your data that you need!

### Usage
1. Decide which defaults file fits best for your simulation - or make a new one!
2. Write a new simulations.py file that defines the parameters you want different from the defaults and calls one of the two functions to write the needed files.
3. Run the simulation file you made to generate PadeOps input files and a bash run script

    ```
    cd $SCRATCH
    python SimsPadeOps/simulations/<your_file.py>
    ```

4. Check that the needed files were created in the Data `folder`.
5. Compile PadeOps.
6. Run the generated bash script using `sbatch`, which is in the created sub-folder of `Data`.

See the README in the simulations folder for a log of all the simulations run. 


