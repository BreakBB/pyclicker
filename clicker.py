from time import sleep
from pynput.mouse import Controller, Button
from pynput import keyboard
from pynput.keyboard._win32 import KeyCode
from argparse import ArgumentParser


class Clicker:
    mouse = None
    should_run = True
    stop_key = None
    mouse_button = Button.left
    interval: float = 0.5

    def __init__(self, mouse_button: int, stop_key: str, interval: float):

        self.mouse = Controller()

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        self.stop_key = stop_key
        self.mouse_button = self.get_button(mouse_button)
        if interval:
            self.interval = interval

    def run(self) -> None:
        print("Running...")
        while self.should_run:
            self.mouse.press(self.mouse_button)
            sleep(0.5)
            self.mouse.release(self.mouse_button)
            sleep(self.interval)

    def on_press(self, key: KeyCode) -> None:
        if self.stop_key is None:
            print("Any key pressed")
            self.should_run = False
            print("Exiting")
            return

        if hasattr(key, "char"):
            print('Alphanumeric key {} pressed'.format(
                key.char))
            if key.char == self.stop_key:
                self.should_run = False
                print("Exiting")
        else:
            print('Special key {} pressed'.format(
                key))
            if key == self.stop_key:
                self.should_run = False
                print("Exiting")

    @staticmethod
    def get_button(number: int) -> Button:
        if number == 1:
            return Button.left
        elif number == 2:
            return Button.right
        elif number == 3:
            return Button.middle
        elif number is None:
            return Button.left
        else:
            print("Unrecognized mouse button number: " + str(number))
            print("Using left mouse button (1) instead.")
            return Button.left


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-m", "--mouse_button", help="Mouse button to click. 1=left, 2=right, 3=middle. Default: 1",
                        type=int)
    parser.add_argument("-s", "--stop_key", help="Key to stop the clicker. Default: all keys", type=str)
    parser.add_argument("-i", "--interval", help="Click interval in seconds. Default: 0.5", type=float)
    args = parser.parse_args()
    Clicker(mouse_button=args.mouse_button, stop_key=args.stop_key, interval=args.interval).run()
