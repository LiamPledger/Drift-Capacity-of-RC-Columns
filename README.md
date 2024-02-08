# Drift-Capacity-of-RC-Columns
This repository uses existing data of cyclic tests of RC columns to train a Gradient-Boosted Decision Tree (GBDT) machine learning algorithm to estimate drift capacity. 

A total of 341 RC column tests from the ACI-369 database are used to train the algorithm.

**Please get in touch if you would like to share more tests not currently included in the repository.**

## RC Column Drift Capacity Calculator
### Usage in python

1. Clone or download this repository to your local machine.

2. Ensure you have Python and the required libraries (NumPy, Pandas, LightGBM) installed.

3. Modify the `user_inputs.txt` file to specify the input parameters for your RC column. Ensure the file format is as follows:

- `units`: 0 for metric units (mm, MPa), 1 for imperial units (inches, psi).
- `a`: Shear span.
- `d`: Column section depth.
- `s`: Transverse reinforcement spacing.
- `ldb` : longitudinal bar diameter.
- `fc`: Concrete compressive strength.
- `fyl`: Longitudinal reinforcement yield strength.
- `fyt`: Transverse reinforcement yield strength.
- `ρl`: Longitudinal reinforcement area ratio.
- `ρt`: Transverse reinforcement area ratio.
- `v`: Axial load ratio (Considering gross concrete section, Ag).

4. Run the Python script `drift_capacity_calculator.py` to calculate the drift capacity:
The result will be displayed in the terminal.

### Web-user interface:
Alternatively, if a web-user interface is preferred:

1. Install the required Python packages:
   
   **pip install -r requirements.txt**
3. Open a command prompt, locate the directory where the files have been saved and start the Flask web server:

   - cd ~/Desktop/my_project  # On macOS and Linux
   - cd C:\Users\YourUsername\Desktop\my_project  # On Windows
     
   - **python run_web_server.py**
5. Fill in the input form with the required parameters:

- Select units (metric or imperial).
- Enter values for a, d, s, fc, fyl, fyt, ρl, ρt, and v.

4. Click the "Submit" button to calculate the drift capacity.
5. The estimated drift capacity will be displayed on the web page.

**Feel free to contribute or report issues.**
Happy calculating!
