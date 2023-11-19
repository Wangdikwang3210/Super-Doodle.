# Super-Doodle.
Description of SUPER NINJA DOODLE

1.	Game Initialization:
•	The game window is created with a width of 400 pixels and a height of 500 pixels.
•	The player character (Ninja Doodle) is loaded onto the screen with an initial position and size.
•	Various game parameters are set, such as the frame rate (fps), font, colors, and initial scores.
2.	Game Variables:
•	Player and platform positions are defined using player_x, player_y, and platforms.
•	Jumping-related variables like jump, y_change, and Ninja_Spring are used to control the player's movement.
3.	Game Loop:
•	The game runs in a loop (while running:) where events are continuously checked and the game state is updated.
•	The game loop handles user input (key presses) to control the player character's movement and actions.
4.	Collision Detection:
•	The function check_collisions detects if the player collides with platforms, allowing the player to jump off them.
•	If a collision is detected, the player is given a vertical boost (y_change = -10) to simulate a jump.
5.	Score and High Score:
•	The game keeps track of the player's score, and there's a mechanism for increasing the score when the player successfully jumps between platforms.
•	The high score is also tracked and displayed on the screen.
6.	Game Over:
•	If the player falls to the bottom of the screen, the game enters a "Game Over" state, and the player's movement is halted.
•	The user can restart the game by pressing the spacebar after a Game Over.
7.	Platform Movement:
•	Platforms move down the screen, and when they go below a certain threshold, they are repositioned randomly above the visible area.
8.	Color Changing:
•	The background color changes when the player's score increases by 15 points.
•	The Ninja Spring (Ninja_Spring) is incremented when the player's score increases by 50 points.
9.	Music:
•	Background music is played using the Pygame mixer library.
10.	Window Update:
•	The game window is updated each iteration of the loop, displaying the player character, platforms, scores, and other relevant information.
11.	Game Termination:
•	The game terminates when the user closes the window.


WHY I CHOOSE UNIT TEST?
1.	Early Bug Detection: Unit tests allow you to catch and fix bugs early in the development process. By testing individual components of your code in isolation, you can identify and address issues before they propagate to other parts of the system.
2.	Improved Code Quality: Writing unit tests often leads to better code design and modularity. When you design code with testing in mind, you tend to create smaller, more focused functions and classes, making your codebase more maintainable and understandable.
3.	Code Confidence: Unit tests provide a safety net for refactoring and code changes. When you make modifications to your code, running the associated unit tests helps ensure that existing functionality is not broken. This confidence is crucial when working on large and complex projects.
4.	Documentation: Unit tests serve as a form of documentation. They provide examples of how to use the code, and by reading the tests, developers can gain insights into the expected behavior of different components.
5.	Regression Testing: Unit tests act as a form of regression testing, ensuring that new changes don't introduce unexpected side effects or break existing functionality. This becomes especially important as a project evolves and more features are added.


