from ursina import *

class Terrain(Entity):
    def __init__(self, is_modifiable: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.is_modifiable = is_modifiable

    def input(self, key):
        if self.hovered and self.is_modifiable:

            if key == 'left mouse down':
                destroy(self)

            if key == 'right mouse down':
                Terrain(
                    position=self.position + mouse.normal,
                    model='cube',
                    color=color.white,
                    collider='box'
                )