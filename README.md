# OaklandTask

REQUIREMENTS: The requests module must be installed to run this code. The code was written and tested using requests version 2.34.2

There are two python scripts in this repository. The first script is "tasks.py", which contains code for each individual step in the exercise. It can be run in VS Code or by entering "python tasks.py" in the command line, and you can search for different Pokemon by manually changing the name in the "get_pokemon_info() function call - however it does not accept arguments from the command line. This script is unpolished and contains some leftover debugging statements - it is not the finished product but I have included it to show some of my thought process as I worked through the exercise.

The second script is "poke.py", which is my full working code. It can be run in an IDE or from the command line and is able to accept arguments. To run the code from the command line, enter "python poke.py name", where "name" is the name of the Pokemon you want to search for. If no name is entered, the user will be prompted to enter the name of a Pokemon. The code initially searches the database for the Pokemon, and if it doesn't find it, it will then call the API and enter the details into the database.
