# Angry-birds-
Pygame and OpenGL-Based Game Project inspired from the Angry birds game
# Pygame and OpenGL-Based Game Project

## Overview
This project is a game developed using Pygame and OpenGL. It features a main menu with interactive buttons and a gameplay section where the player controls a bird, aiming to hit enemy birds to increase the score. The game also includes background music and sound effects for various actions.

## Features
- Main menu with a rotating sphere and interactive buttons.
- Gameplay involving dragging and launching a bird to hit enemy birds.
- Background music and sound effects for different actions.
- Dynamic background and textures for various game elements.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2.  **Install dependencies:**
   Ensure you have Python and pip installed, then run:
   ```bash
   pip install pygame PyOpenGL
```
3. **Download Required Assets**

Place the following files in the appropriate directories:

- **Images (.png, .jpg):** For textures and sprites.
- **Sound files (.mp3):** For background music and sound effects.

Update the file paths in the script if necessary.
## Usage

To run the game, execute the following command:

```bash
python main.py
```
## Project Structure

```bash
.
├── main.py               # Main script for the menu
├── game.py               # Game logic script
├── assets/
│   ├── images/
│   │   ├── play1.png
│   │   ├── logo3.png
│   │   ├── pinkbird.png
│   │   ├── sunset.jpg
│   │   ├── sparkles.png
│   │   ├── sparlkesmany.png
│   │   ├── lens_flare.png
│   │   ├── Cherry_Blossom_background.webp
│   │   ├── pird.png
│   │   ├── pig.png
│   │   ├── exit7.png
│   │   ├── refresh.png
│   └── sounds/
│       ├── HeatleyBros_Beginning.mp3
│       ├── Mouse_Click.mp3
│       ├── Angry_Birds_Collision.mp3
│       ├── Cherry_Blossom_Theme.mp3
│       ├── Game_Over.mp3
│       ├── Win_Sound.mp3
│       ├── Slingshot_Sound.mp3
└── README.md             # This file
```
## Controls

- **Mouse Click:** Interact with buttons and drag the bird.
- **Mouse Drag and Release:** Launch the bird towards enemy birds.

## Game Mechanics

- **Score:** Increase by 100 points for each enemy bird hit.
- **Level Cleared:** Achieved when the score reaches 1000 points.
- **Game Over:** Occurs when the player fails to hit any enemies within three tries.

  
## Video


https://github.com/user-attachments/assets/2d4f1ffa-299b-49dc-a771-80c5a28e4597

