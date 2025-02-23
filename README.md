# Pong Game

This is a simple Pong game implemented using Pygame.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install Pygame using pip:
    ```sh
    pip install pygame
    ```

## How to Run

1. Clone this repository or download the [pyg.py](http://_vscodecontentref_/0) file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing [pyg.py](http://_vscodecontentref_/1).
4. Run the game using the following command:
    ```sh
    python pyg.py
    ```

## Game Controls

- Use the left arrow key (`←`) to move the paddle left.
- Use the right arrow key (`→`) to move the paddle right.

## Game Rules

- The ball will bounce off the walls and the paddle.
- The score increases by 1 each time the ball hits the paddle.
- The game resets if the ball hits the bottom of the screen.

## Code Overview

- [WIDTH](http://_vscodecontentref_/2), [HEIGHT](http://_vscodecontentref_/3): Screen dimensions.
- [WHITE](http://_vscodecontentref_/4), [BLACK](http://_vscodecontentref_/5): Color definitions.
- [ball_radius](http://_vscodecontentref_/6), [ball_pos](http://_vscodecontentref_/7), [ball_vel](http://_vscodecontentref_/8): Ball properties.
- [paddle_width](http://_vscodecontentref_/9), [paddle_height](http://_vscodecontentref_/10), [paddle_pos](http://_vscodecontentref_/11), [paddle_speed](http://_vscodecontentref_/12): Paddle properties.
- [score](http://_vscodecontentref_/13), [font](http://_vscodecontentref_/14): Score properties.
- [clock](http://_vscodecontentref_/15), [FPS](http://_vscodecontentref_/16): Frame rate control.

