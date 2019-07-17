# PyClicker

PyClicker is a simple mouse simulating tool for Windows. It uses the Windows API to stay "below radar" if it is run as admin and is therefore not detected by programs which recognize similar tools.

## How to use it

### Parameters

| Parameter                 | Type      | Description                                                   | Default |
|---------------------------|-----------|---------------------------------------------------------------|---------|
| `--mouse_button`, `-m`    | int       | Mouse button to click. 1=left, 2=right, 3=middle.             | 1       |
| `--stop_key`, `-s`        | string    | Key to stop the clicker. If `None` any key will interrupt.    | None    |
| `--internval`, `-i`       | float     | Click interval in seconds.                                    | 0.5     |

### From command line

Install Python and the requirements listed in the `requirements.txt`. After that you can simply run the `clicker.py` file like this:

`py clicker.py [--mouse_button, -m] [--stop_key, -s] [--interval, -i]`


### Using the .exe file

You can find an executable file at the [releases](https://github.com/BreakBB/pyclicker/releases) page. With this executable you don't need to install Python but can simply use it. The application will use the default parameter stated above. To change them you have to start the executable from command line just as you would if you would run the Python file directly.

`clicker.exe [--mouse_button, -m] [--stop_key, -s] [--interval, -i]`

## How to build the executable

You can build the executable by running `pyinstaller`. If you don't want the executable to ask for admin permission you should omit the `--uac-admin` parameter.

`pyinstaller --onefile --uac-admin clicker.py`
