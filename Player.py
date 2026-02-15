from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.NORMAL_HEIGHT: int = 2
        self.CROUCH_HEIGHT: float = 1.5
        self.NORMAL_SPEED: int = 4
        self.SPRINT_SPEED: int = 7
        self.CROUCH_SPEED: float = 0.5
    

    def update(self):
        super().update()
        
        if held_keys['left control']:
            self.speed = self.CROUCH_SPEED
            self.camera_pivot.y = self.CROUCH_HEIGHT

        else:
            self.speed = self.NORMAL_SPEED
            self.camera_pivot.y = self.NORMAL_HEIGHT

        if held_keys['left shift']:
            self.speed = self.SPRINT_SPEED
        
        else:
            self.speed = self.NORMAL_SPEED