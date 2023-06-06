# Eye-Tracker

Modular, Extensible Eye-Tracking solution
[Youtube Video Demonstration](https://youtu.be/zDN-wwd5cfo "Eye tracking")

## Overview

A **very** accurate eye-tracking software.
![What it looks like](https://i.imgur.com/DQRmibk.png)

## Features

- Cross-platform
- Works with glasses
- Does not require high-end hardware, works well even with a 640\*480 webcam
- Uses blob detection algorithm, but earlier versions used circle detection too.
- Highly extensible/flexible
- New image sources or capture sources can easily be added

## Requirements

- Python 3.7 +

## Guide

Full installation & run:

WINDOWS:

```shell
pip install poetry
poetry config virtualenvs.in-project true
poetry install
poetry shell

python main.py
```

CONDA WINDOWS

```shell
conda create -p D:\env\eye-tracker-pc

conda activate D:\env\eye-tracker-pc
python main.py -fs=camera  -cam-id=1

conda deactivate
```

To run Qt Designer:

```shell
pyqt6-tools designer
```

Options & Arguments:

- `--frame-source` allows you to specify the source of your frames. Currently available options are: `camera`, `folder`, `file`. Defaults to `camera`

`camera` means images will come from your device's camera

`folder` means images will come one-by-one from your `DEBUG_DUMP_LOCATION` setting folder in `settings.py` with the interval of `REFRESH_PERIOD`

`file` means the image will be static, good for debugging or development. Path can be specified in the `STATIC_FILE_PATH` setting

- There are some Environment variables that can be specified to change the behaviour. Like `DEBUG_DUMP` to set whether a dump should be made when the program crashes

## Developer

Basic Eye-Tracking is provided by:

- Stepan Filonov (@stepacool) stepanfilonov@gmail.com
