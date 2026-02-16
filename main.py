from ursina import *
from Player import Player
from Terrain import Terrain


app = Ursina()

player = Player(position = (0, 0, 0))

for z in range(20):
    for x in range(20):
        Terrain(
            position = (x, 0, z),
            model = 'cube',
            color = color.green,
            collider = 'box'
        )


if __name__ == "__main__":
    app.run()