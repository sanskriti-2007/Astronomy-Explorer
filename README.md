# Astronomy Explorer


### Video Demo:

https://youtu.be/B-LsD-FDlsU


### Description:

Astronomy Explorer is a Python-based command-line application that allows users to explore information about the eight planets in our solar system. The program stores planetary data in a JSON file and presents it through an interactive menu-driven interface.
The project was created as my final project for Harvard University's CS50P (Introduction to Programming with Python). It demonstrates the use of functions, dictionaries, JSON files, loops, exception handling and, modular programming structure.


## Features

### View Planet Information:

Users can view a list of all available planets and select one to display detailed information, including:
* Radius
* Gravity
* Number of moons
* Length of a day
* Length of a year
* Average temperature
* An interesting fact

### Compare Planets:

Users can compare any two different planets side by side. The program displays each property for both planets, making it easy to observe their differences.
The program also validates user input by ensuring:
* Both planets exist.
* The same planet cannot be selected twice.

### Random Planet:

This feature randomly selects one of the eight planets and displays its complete information. Since the planet is chosen randomly each time, users are encouraged to discover interesting facts about every planet in the Solar System.

### Astronomy Quiz

The application includes an astronomy quiz that loads questions from a separate JSON file. Five questions are randomly selected for each attempt, making each quiz unique.
Features include:
* Randomized questions
* Input validation for answers
* Final score display
* Personalized result message based on performance
* Option to replay the quiz without returning to the main menu

## Error Handling

The application includes input validation to improve the user experience.
Examples include:
* Rejecting invalid menu choices
* Rejecting non-numeric menu input
* Detecting planets that do not exist
* Preventing comparison of a planet with itself

### File Structure

* project.py contains the main application logic
* planets.json stores all planetary data used by the program
* quiz.json stores all astronomy quiz questions
* test_project.py contains unit tests written using pytest
* README.md documents the project

## Libraries Used

This project uses only Python's built-in standard library modules:

* `json` – for loading planetary and quiz data from JSON files.
* `random` – for selecting a random planet and random quiz questions.

No external Python packages are required to run this project.

### Design Choices:

One of my primary goals was to make the program easy to extend. Instead of hardcoding planetary information directly into Python, I stored all data in a JSON file.
Similarly, quiz questions are stored in a separate JSON file. This allows new planets, additional properties, or new quiz questions to be added without modifying the core logic of the program.
To reduce duplicated code and improve readability, I separated responsibilities into multiple helper functions. Examples include:
* Loading planet and quiz data
* Displaying the list of planets
* Displaying detailed planet information
* Comparing planets
* Selecting a random planet
* Validating planet selections
* Returning quiz result messages
This modular approach makes the project easier to maintain, expand, and test.

### Testing:

The project includes a test_project.py file using pytest to verify the correctness of important helper functions.
The tests cover:
* Loading planet data from JSON
* Loading quiz questions from JSON
* Random planet selection
* Planet validation
* Quiz result messages
This ensures that the core logic of the application works correctly independent of user interaction.

### Future Improvements

Possible future additions include:
* Information about moons, stars, and galaxies
* Search functionality
* Additional astronomical objects beyond the Solar System


Overall this project combines my interest in astronomy with the programming concepts learned throughout CS50P while providing an interactive way to explore our Solar System.

