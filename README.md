# Wind_Speed_Cal_Sentinel_Level2_GPU

This project calculates wind speed from Sentinel-1 Level-2 data using GPU acceleration.

## Setup

1.  **Create the Conda Environment**

    Use the `environment.yml` file to create a Conda environment with all the necessary dependencies.

    ```bash
    conda env create -f environment.yml
    ```

2.  **Activate the Conda Environment**

    ```bash
    conda activate Wind_Speed_Cal_Sentinel_Level2_GPU
    ```

3.  **Set the PYTHONPATH**

    Before running the script, you need to set the `PYTHONPATH` to include the `nansat` and `openwind` directories.

    ```bash
    export PYTHONPATH=`pwd`/nansat:`pwd`/openwind:$PYTHONPATH
    ```

## Usage

To run the wind speed calculation, execute the `sar_wind_GPU.py` script with the following arguments:

```bash
python openwind/openwind/sar_wind_GPU.py -s <path_to_sentinel_data> -w <wind_direction> -n <output_netcdf_path> -f <output_png_path>
```

**Example:**

```bash
python openwind/openwind/sar_wind_GPU.py -s /path/to/your/S1A_IW_GRDH_1SDV_20250904T204345_20250904T204410_060843_07935B_02E7.SAFE -w 270 -n /path/to/your/RESULTS/GPU/tokyo_bay_s1a_wind.nc -f /path/to/your/RESULTS/GPU/tokyo_bay_s1a_wind.png
```

Replace the placeholder paths with the actual paths to your data and desired output locations.
