# Wind_Speed_Cal_Sentinel_Level2_GPU

## Setup

First, set the python path:

```bash
export PYTHONPATH=/home/user/AB/GC/GPU_lev2_wind_speed/nansat:/home/user/AB/GC/GPU_lev2_wind_speed/openwind:$PYTHONPATH
```

## Usage

To run the script, use the following command:

```bash
python openwind/openwind/sar_wind_GPU.py -s /home/user/AB/GC/GPU_lev2_wind_speed/DATA/Tokyo_bay/S1A_IW_GRDH_1SDV_20250904T204345_20250904T204410_060843_07935B_02E7.SAFE -w 270 -n /home/user/AB/GC/GPU_lev2_wind_speed/RESULTS/GPU/tokyo_bay_s1a_wind.nc -f /home/user/AB/GC/GPU_lev2_wind_speed/RESULTS/GPU/tokyo_bay_s1a_wind.png
```