# 3D Block Game

## IMPORTANT DISCLAIMER:

"NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT."

## Brief Resume:

I am attempting to build not only a game, but a 3-dimensional game with basic functionalities.
For this incredible project, I will mention what modules that I will be using, how to use this project on your machine and also what I have learned.

> [!NOTE]
> This is still not the complete project and overtime, I will still be adding features into it!

### Modules & External Files:

* `Ursina`: A basic 3D game modelling dependency, allowing for the functionality, mapping and easy game development such as terrain generation, inventory system, hotbar, game controls and much more features.
* `Main.py`: This is where the main program will be executed.
* `Terrain.py`: Focuses on defining single blocks and how it behaves.
* `Player.py`: Maintains player functionality and manipulates how the user can interact with other entities.

### How to Use It:

1. Clone the Repository (I have put a license, meaning that it is free to use!):

```bash
git clone "URL-Of-REP"
```

2. Install the `ursina` framework/engine:

```pwsh
# With pip
pip install ursina

# With UV (recommended, since I have used it for this project)
uv add ursina
```

3. Run all files (OPTIONAL):

If there any any weird bugs saying that it does not recognize any `.py` files from the `Main.py` file imports, make sure to hit the run button in all other files such as `Player.py`, `Terrain.py`, ... before executing `Main.py`, that way, the game will work perfectly fine.

4. Run `Main.py`:

Simply run the `Main.py` file and enjoy the game!