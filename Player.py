from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.NORMAL_HEIGHT: int = 1.6
        self.CROUCH_HEIGHT: float = 1.3
        self.NORMAL_SPEED: int = 3.5
        self.SPRINT_SPEED: int = 6
        self.CROUCH_SPEED: float = 1

        self.editor_camera = EditorCamera(
            enabled = False,
            ignore_pause = True
        )
    

    def update(self):
        super().update()
        
        if held_keys['left control']:
            self.speed = self.CROUCH_SPEED
            self.camera_pivot.y = self.CROUCH_HEIGHT

        elif held_keys['left shift']:
            self.speed = self.SPRINT_SPEED
            self.camera_pivot.y = self.NORMAL_HEIGHT

        else:
            self.speed = self.NORMAL_SPEED
            self.camera_pivot.y = self.NORMAL_HEIGHT

        # Ceiling collision check
        # Cast a ray upwards from the player's head to detect blocks
        hit_info = raycast(
            self.position + Vec3(0, 1, 0),
            direction=Vec3(0, 1, 0),
            distance=1.5,
            ignore=(self,)
        )

        if hit_info.hit:
            # Snap the player's Y position so the head is just below the ceiling
            self.y = min(self.y, hit_info.world_point.y - self.camera_pivot.y - 0.25)