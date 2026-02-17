from ursina import *

class PauseMenu(Text):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            text = 'Paused',
            origin = (0, 0),
            scale = 3,
            background = True,
            ignore_pause = True,
            color = color.white,
            enabled = False
        )

        self.resume_button = Button(
            parent = self,
            text = 'Resume',
            color = color.gray,
            scale_y = 0.1,
            scale_x = 0.2,
            y = 0,
            enabled = False,
            ignore_pause = True
        )

        self.exit_button = Button(
            parent = self,
            text = 'Exit',
            color = color.gray,
            scale_y = 0.1,
            scale_x = 0.2,
            y = -0.2,
            enabled = False,
            ignore_pause = True
        )

        self.resume_button.on_click = self.resume_game
        self.exit_button.on_click = self.exit_game

    def input(self, key):
        if key == 'escape':
            application.paused = not application.paused
            self.enabled = application.paused
            self.resume_button.enabled = application.paused
            self.exit_button.enabled = application.paused
            mouse.locked = not application.paused

    def resume_game(self):
        application.paused = False
        self.enabled = False
        self.resume_button.enabled = False
        self.exit_button.enabled = False
        mouse.locked = True

    def exit_game(self):
        application.quit()