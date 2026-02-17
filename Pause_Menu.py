from ursina import *
from ursina.shaders.screenspace_shaders.camera_vertical_blur import camera_vertical_blur_shader

class PauseMenu(Entity): # Inheriting from Entity is generally cleaner for menus
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            ignore_paused = True,
            enabled = True        # Keep the container enabled to listen for input
        )
        
        # The visual text element
        self.title = Text(
            parent = self,
            text = 'Paused',
            origin = (0, 0),
            scale = 3,
            y = 0.3,
            visible = False,
        )

        # Background color to keep the pause menu modular
        # self.background = Entity(
        #     parent = self,
        #     model = 'quad',
        #     scale = (2, 2),
        #     color = color.black66,
        #     z = 1
        # )

        self.resume_button = Button(
            parent = self,
            text = 'Resume',
            color = color.gray,
            scale = (0.2, 0.1),
            y = 0,
            visible = False,      # Use visible for the UI toggle
            ignore_paused = True
        )

        self.exit_button = Button(
            parent = self,
            text = 'Exit',
            color = color.gray,
            scale = (0.2, 0.1),
            y = -0.15,
            visible = False,
            ignore_paused = True
        )

        self.resume_button.on_click = self.resume_game
        self.exit_button.on_click = application.quit

    def input(self, key):
        if key == 'escape':
            # Toggle the pause state
            application.paused = not application.paused
            self.toggle_menu_visibility()

    def toggle_menu_visibility(self):
        is_paused = application.paused
        self.title.visible = is_paused
        self.resume_button.visible = is_paused
        self.exit_button.visible = is_paused
        
        # Handle mouse lock
        mouse.locked = not is_paused
        mouse.visible = is_paused

        if is_paused:
            # Apply shader and set a default intensity
            camera.shader = camera_vertical_blur_shader
            camera.set_shader_input('blur_size', 0.05)
        else:
            # Explicitly kill the shader
            camera.shader = None
            # This line ensures the GPU forgets the blur parameters
            camera.set_shader_input('blur_size', 0)

    def resume_game(self):
        # Force the state to False first
        application.paused = False
        # Manually ensure shader is killed in case the toggle logic missed a frame
        camera.shader = None
        self.toggle_menu_visibility()