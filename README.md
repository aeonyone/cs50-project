# ARCADE SNAKE GAME

#### Video Demo:  https://www.youtube.com/watch?v=cYDztO_dLTQ
#### Description:
Snake is a single player top-down perspective game with a goal to grow the player-controlled snake by consuming food on the map. The game is projected over a grid and gameplay is executed from 2 actions per second (APS) to 10 APS, depending of the selected difficulty.
The game presents two major obstacles - the player must navigate the map without hitting the walls or eating its tail. 

#### Win condition:
Snake game win condition is to cover all available land. This task is no small feat, and for casual player might never be achieved. Hence, the enjoyment of gameplay should be primary goal.

#### Settings:
As the game starts, player has a choice to set two main settings. First is the speed (difficulty) of the gameplay. Second is the choice of the map. Both of the settings are chosen at the start of the game. Speed can be chosen using keys 1 to 5. Map can be chosen using keys 1 to 3.

#### Controls:
Game is controlled by using WASD keys.
W directs snake upwards.
A directs snake to left.
S directs snake downwards.
D directs snake to right.
Player may change the target direction multiple times before game renders the next position, but only the last key stroke will be executed. Player cannot direct snake backwards relative to the current direction.
Additionally, player can hold Space bar to temporarily increase the speed of gameplay. The speed of gameplay is reverted back to selected setting after Space bar is released.

#### Implementation:
##### High level overview:
The game is implemented in Python. The game relies on pygame library to help with collecting user input and rendering the game.
The central components of the game are the state and the game loop.
The state represents the game at any given point of time. Most of the state is immutable, such as display size, visual assets, FPS, map and will be reused for the whole duration of the game. Rest of state represents player and gameplay mechanics - snake position and length, movement direction and food location, and will change as game advances.
The game loop collects user input, executes gameplay mechanics, draws and renders the window. All changes to state of the game is performed using functions. Function specific documentation can be found in the game files.
##### Key design choices:
###### Paradigm:
The game was implemented in a way that is most intuitive for the author, which likely best resembles imperative paradigm. Object oriented programming or other paradigms might be be more appropriate based on the context.
###### Game grid:
Everything that exists in the game, exists on an invisible grid. Game grid consists of 20x20 blocks. Each block is 32x32 pixels. I chose to use grid, because, first, I wanted the game to resemble an arcade game and, secondly, because it simplifies game mechanics by allowing the author to design all game mechanics as rect collisions. 
###### Rects
Rect is a pygame object, which resembles a rectangle of certain height and width placed in specific point on the window. Each piece of wall, snake or food was represented as a rect on the grid. 
Food is defined as a single rect. If the food is eaten, the rect will get assigned random coordinates on the grid. Both walls and the snake was represented as list of rects. Walls were static and defined once at the start of the game, while snake was changing over the course of the game. 
###### Snake
The first rect of the snake represented the head. Rest of the rects represented the body, with last rect representing the tail. At each snake movement, the first list rect coordinates were updated based on the target direction, and rest of the list inherited rects from list [n - 1] position. Each part of snake body was visualised by conditionally checking positions of relative rects. Based on these positions, appropriate icon was uses to create an illusion of realistic snake body movement.
###### Game speed:
The game is fundamentally turn-based, with each turn executing at regular intervals. Hence, my first approach was to execute the game loop at a target speed. However, this created a problem. Foe example, if game was running at moderate speed, e.g. 4 fps, user input was collected only once 250ms. In practice, it meant that user key stroke input could get lost if a keystore was too short.
As such, I decided to run game loop at constant 60 FPS regardless of actual game speed. This allows user input to be responsive. The actual game speed mechanics is controlled using a modulo operation. Each loop increments frame variable, which is divided by the game speed variable. If the remainder is 0, game mechanics are executed. To achieve faster game speed, game speed variable is set to smaller amount.
###### Maps
Maps are defined as hardcoded list of lists with coordinates. These coordinates correspond to the grid blocks, which should behave and render as a wall. Existing maps can be changed and new maps can be changed by adjusting the coordinates.
###### Visual assets:
Game icon, wall icon and food icon were retrieved from https://www.flaticon.com/
Snake body part icons were created by the author.
#### Files:
The game is implemented in several files:
###### main.py
Contains the game loop which collects user input, executes the gameplay and renders the window
###### config.py
Contains global variables and configuration settings
###### assets.py
Contains definition of icons and fonts that are used in the gameplay 
###### fn.py
Contains implementation of gameplay functions
###### menu.py
Contains functions for generating menu windows and collecting user input
###### maps.py
Contains definition of the maps
###### /assets/
Contain visual game assets

#### Game development process:
The game was developed over the course of 4 weeks. To keep the process focused, key features were determined before hand in the order of ascending complexity and descending importance to gameplay. Not all goals were reached, however the main gameplay features was implemented as planned.
[x] Game grid exists
[x] Snake is moving across the grid
[x] Snake can eat food
[x] Wall exists
[x] Snake dies when hits the wall
[x] Snake grows when eats food
[x] Menu exists and collects user input
[x] Snake can exit bounds and re-enter on the other side
[x] Snake body movement appears natural
[x] Holding spacebar fast forwards gameplay
[-] Player sees the current points
[-] Points are displayed at then end of the game
[-] User can generate randomized maps based on seed

#### Bugs:
Of course, where there is software, there will be bugs. Current list of known bugs:
[-] Snake body can render incorrectly when exiting bounds and immediately turning on re-entering on the other side. This does not break the gameplay.