import ctypes
from time import sleep
from typing import Union
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode, Key
from argparse import ArgumentParser


class Clicker:
    mouse: Controller = None
    should_run: bool = True
    stop_key: KeyCode = None
    mouse_button: Button = Button.left
    interval: float = 0.5

    def __init__(self, mouse_button: int, stop_key: str, interval: float):
        self.mouse = Controller()

        listener = Listener(on_press=self.on_press)
        listener.start()

        if stop_key:
            self.stop_key = KeyCode.from_char(stop_key)
        self.mouse_button = self.get_button(mouse_button)
        if interval:
            self.interval = interval

    def run(self) -> None:
        if self.stop_key:
            key = "{}".format(self.stop_key)
        else:
            key = "any key"
        print("Starting to click. Press {} to stop the clicker.".format(key))
        while self.should_run:
            self.mouse.press(self.mouse_button)
            self.mouse.release(self.mouse_button)
            sleep(self.interval)

    def on_press(self, key: Union[KeyCode, Key]) -> None:
        if self.stop_key is None:
            print("Any key pressed")
            self.should_run = False
            print("Exiting")
            return
        elif not self.should_run:
            return

        if hasattr(key, "char"):
            print("Alphanumeric key '{}' pressed".format(
                key.char))
            if key.char == self.stop_key:
                self.should_run = False
                print("Exiting")
        else:
            print("Special key '{}' pressed".format(
                key.name))
            if key.name == self.stop_key.char:
                self.should_run = False
                print("Exiting")

    @staticmethod
    def get_button(number: int) -> Button:
        if number == 1 or number is None:
            return Button.left
        elif number == 2:
            return Button.right
        elif number == 3:
            return Button.middle
        else:
            print("Unrecognized mouse button number: " + str(number))
            print("Using left mouse button instead.")
            return Button.left


if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("WARNING: You're not an admin. Some programs will prevent mouse clicks if you're not an admin.")

    parser = ArgumentParser()
    parser.add_argument("-m", "--mouse_button", help="Mouse button to click. 1=left, 2=right, 3=middle. Default: 1",
                        type=int)
    parser.add_argument("-s", "--stop_key", help="Key to stop the clicker. Default: all keys", type=str)
    parser.add_argument("-i", "--interval", help="Click interval in seconds. Default: 0.5", type=float)
    args = parser.parse_args()
    Clicker(mouse_button=args.mouse_button, stop_key=args.stop_key, interval=args.interval).run()
