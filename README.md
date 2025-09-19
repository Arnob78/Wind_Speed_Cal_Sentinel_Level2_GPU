# GPU-Accelerated Sentinel-1 Wind Analysis

This project contains a GPU-accelerated workflow to process Sentinel-1 Level-1 GRD (Ground Range Detected) data and generate a Level-2 ocean wind speed product using the CuPy library.

## Project Structure

- `DATA/`: Contains the input Sentinel-1 data.
- `RESULTS/GPU/`: Contains the output GeoTIFF and PNG files from the GPU script.
- `openwind/`: Source code for the wind analysis application.
- `nansat/`: Source code for the underlying satellite data handling toolbox.
- `environment.yml`: A Conda environment file to replicate the analysis environment.

## Setup and Execution

### 1. Create and Activate Conda Environment

This project requires a specific Conda environment with GPU support. Create and activate it using the provided `environment.yml` file:

```bash
# Create the environment from the file
conda env create -f environment.yml

# Activate the environment
conda activate py3nansat
```

### 2. Set Environment Variable

Before running the script, you must set the `PYTHONPATH` to allow Python to find the local `openwind` and `nansat` modules. From the project root directory, run:

**On macOS/Linux:**
```bash
export PYTHONPATH=$(pwd)/openwind:$(pwd)/nansat:$PYTHONPATH
```

**On Windows:**
```bash
set PYTHONPATH=%cd%\\openwind;%cd%\\nansat;%PYTHONPATH%
```

### 3. Run the GPU Analysis

Execute the following command to run the GPU-accelerated script:

```bash
python openwind/openwind/sar_wind_GPU.py -s DATA/Tokyo_bay/S1A_IW_GRDH_1SDV_20250904T204345_20250904T204410_060843_07935B_02E7.SAFE -w 270 -n RESULTS/GPU/tokyo_bay_s1a_wind.nc -f RESULTS/GPU/tokyo_bay_s1a_wind.png
```
