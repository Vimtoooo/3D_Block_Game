from ursina import *

class Terrain(Entity):
    def __init__(self, is_modifiable: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.is_modifiable = is_modifiable

    def input(self, key):
        if self.hovered and self.is_modifiable and distance(self.position, camera.world_position) < 5:

            if key == 'left mouse down':
                destroy(self)

            if key == 'right mouse down':
                Terrain(
                    position=self.position + mouse.normal,
                    model='cube',
                    color=color.blue,
                    collider='box'
                )

    def update(self):
        if distance(self.position, camera.world_position) > 20:
            self.visible = False
        
        else:
            self.visible = True