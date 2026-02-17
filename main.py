from ursina import *
from Player import Player
from Terrain import Terrain


app = Ursina()

player = Player(position = (0, 0, 0))

pause_menu = Text(
    text = 'Paused',
    origin = (0, 0),
    scale = 3,
    background = True,
    visible = False,
    ignore_pause = True,
    color = color.white
)

for z in range(20):
    for x in range(20):
        Terrain(
            position = (x, 0, z),
            model = 'cube',
            color = color.green,
            collider = 'box'
        )

def input(key):
    
    if key == 'escape':
        application.paused = not application.paused
        pause_menu.visible = application.paused
        mouse.locked = not application.paused


if __name__ == "__main__":
    app.run()