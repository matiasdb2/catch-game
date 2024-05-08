# Catch Game on Pygame
This is a simple Catch game implemented using Pygame, a popular Python library for game development.

## Features
### Player as an Arkanoid-style Bar: The player is represented as a bar that moves along the x-axis. The movement of the bar is controlled using the 'A' and 'D' keys. It possesses acceleration and comes to a halt when it collides with the borders of the game window.

### Red Falling Object: A red object falls along the y-axis, appearing randomly at any x-axis position. As the game progresses, the falling object accelerates its descent after every three successful catches.

### Score Tracking: The game keeps track of the player's score, which increases each time a falling object is successfully caught.

### Lose and Restart System: If the player fails to catch an object, the game ends and displays the final score. The player can restart the game by pressing the 'R' key.

### Built-in Music Player: An 8-bit version of the popular song 'Dura' by Daddy Yankee plays continuously in the background, adding to the immersive epic gaming experience.

## Changelog
### Added a `pip install --upgrade pygame` command at the beginning of the code to ensure compatibility for users who do not have the Pygame library installed.

### Updated the music playback functionality. The `pygame.mixer.music.play()` command now has the loop parameter set to `(-1)`, enabling the music to loop continuously throughout the game.

### Enhanced the player movement for a more enjoyable gaming experience. The `player_acc` value has been adjusted to `0.5`, providing smoother acceleration for the player-controlled bar. The `player_max_vel` value has been increased to `10`, allowing for faster movement and greater responsiveness. These modifications contribute to improved gameplay dynamics and overall user satisfaction.
