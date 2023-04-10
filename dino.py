import pyautogui as gui
import keyboard
import time
import math


class Dino:
    """Automation algorithm of the dinosaur game."""

    def get_pixels_data(self, image, init_x, init_y):
        px = image.load()
        return px[init_x, init_y]

    def start_game(self, param_width, param_height):
        # Set size of the image to be taken
        x, y, width, height = 0, 102, param_width, param_height

        # Area in which bot will be looking obstacles
        y_search1, y_search2, x_start, x_end = 557, 486, 400, 435
        y_search_for_bird = 460

        jumping_time = 0
        last_jumping_time = 0
        current_jumping_time = 0
        last_interval_time = 0

        # Press 'space' to start the game
        keyboard.press('space')

        while True:
            try:
                screen_img = gui.screenshot(region=(x, y, width, height))
                screen_img.save("dino.jpg")

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
                    x_end += 8
                if x_end >= width:
                    x_end = width

                # To get the last jump time
                last_jumping_time = jumping_time

                # To get the time between the last jump and the previous one
                last_interval_time = interval_time

                # press q to take the con over the bot
                if keyboard.is_pressed('q'):
                    raise KeyboardInterrupt

            except KeyboardInterrupt as e:
                print("The dino was suspended.")
                exit(0)
