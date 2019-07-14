# PyClicker

PyClicker is a simple mouse simulating tool for Windows. It uses the Windows API to stay "below radar" and is therefore not detected by programs which recognize similar tools.

## How to use it

### From command line

`py clicker.py [--mouse_button,  -m] [--stop_key, -s] [--interval, -i]`

| Parameter                 | Type      | Description                                                   | Default |
|---------------------------|-----------|---------------------------------------------------------------|---------|
| `--mouse_button`, `-m`    | int       | Mouse button to click. 1=left, 2=right, 3=middle.             | 1       |
| `--stop_key`, `-s`        | string    | Key to stop the clicker. If `None` any key will interrupt.    | None    |
| `--internval`, `-i`       | float     | Click interval in seconds.                                    | 0.5     |