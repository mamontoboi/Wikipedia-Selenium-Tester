"""The class Dino is included in the module, allowing automation of the dino's behavior.
The original code for this class was sourced from the website www.geeksforgeeks.org.
While it may not be flawless, creating a dino bot was not the primary objective of this
project."""

import sys
import time
import math
import pyautogui as gui
import keyboard


class Dino:
    """Automation algorithm of the dinosaur game."""

    def get_pixels_data(self, image, init_x, init_y):
        """Provides a way to retrieve the color value of a specific pixel in an image."""

        pxl = image.load()
        return pxl[init_x, init_y]

    def img_process(self, area: tuple):
        scr_img = gui.screenshot(region=area)
        scr_img.save("dino.jpg")
        return scr_img

    def start_game(self, param_width, param_height):
        # Set size of the image to be taken
        x_init, y_init, width, height = 0, 102, param_width, param_height

        # Area in which bot will be looking obstacles
        y_search1, y_search2, x_start, x_end = 557, 486, 400, 420
        y_search_for_bird = 450

        jumping_time = 0
        last_jumping_time = 0
        current_jumping_time = 0
        last_interval_time = 0

        # Press 'space' to start the game
        keyboard.press('space')

        while True:
            try:
                screen_img = self.img_process((x_init, y_init, width, height))

                # Obtain the background color of the screenshot image
                bg_color = self.get_pixels_data(screen_img, 100, 100)

                for i in reversed(range(x_start, x_end)):
                    # color of the pixel does not match the
                    # color of the background color
                    if self.get_pixels_data(screen_img, i, y_search1) != bg_color \
                            or self.get_pixels_data(screen_img, i, y_search2) != bg_color:
                        keyboard.press('up')
                        jumping_time = time.time()
                        current_jumping_time = jumping_time
                        break
                    if self.get_pixels_data(screen_img, i, y_search_for_bird) != bg_color:
                        keyboard.press("down")
                        time.sleep(0.28)
                        # press keyboard arrow down to duck
                        keyboard.release("down")
                        break

                # Time between this jump and the last one
                interval_time = current_jumping_time - last_jumping_time

                # The game is accelerating if the intervals not same
                if last_interval_time != 0 and math.floor(interval_time) != math.floor(last_interval_time):
                    x_end += 6
                x_end = min(x_end, width)

                # To get the last jump time
                last_jumping_time = jumping_time

                # To get the time between the last jump and the previous one
                last_interval_time = interval_time

                # press q to take the con over the bot
                if keyboard.is_pressed('q'):
                    raise KeyboardInterrupt

            except KeyboardInterrupt:
                print("The dino was suspended.")
                sys.exit(0)
