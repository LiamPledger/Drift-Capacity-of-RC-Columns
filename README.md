# Drift-Capacity-of-RC-Columns
This repository uses existing data for cyclic tests of RC columns to train a Gradient-Boosted Decision Tree (GBDT) machine learning algorithm to estimate drift capacity. 

A total of 498 RC column tests  from the ACI-369 database (326 rectangular columns, and 172 circular columns) are used to train the algorithm.

Please get in touch if you would like to share more tests not currently included in the repository.

## RC Column Calculator
### Usage

1. Clone or download this repository to your local machine.

2. Ensure you have Python and the required libraries (NumPy, LightGBM) installed.

3. Modify the `user_inputs.txt` file to specify the input parameters for your RC column. Ensure the file format is as follows:

- `units`: 0 for metric units (mm, MPa), 1 for imperial units (inches, psi).
- `a`: Shear span.
- `d`: Column section depth.
- `s`: Transverse reinforcement spacing.
- `fc`: Concrete compressive strength.
- `fyl`: Longitudinal reinforcement strength.
- `fyt`: Transverse reinforcement strength.
- `ρl`: Longitudinal reinforcement ratio.
- `ρt`: Transverse reinforcement ratio.
- `v`: Axial load ratio.

4. Run the Python script `Drift_capacity_calculator.py` to calculate the drift capacity:

The result will be displayed in the terminal.

Feel free to contribute or report issues.
Happy calculating!
