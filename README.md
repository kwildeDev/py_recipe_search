# py_recipe_search
## Recipe Search using Edamam API
A python project using the Edamam API to search for recipes based on a specified query

## Description
Edamam is a Nutrition Analysis, Food Database, Recipe Search API provider.
The aim of this project is to introduce the implementation of the Edamam API to search for food recipes based on a specified ingredient

The program begins by fetching authorisation keys from the local host and saving these to variables to use in the search function.
The program then prompts the user to enter an ingredient and validates the input against acceptable characters. The input is then confirmed to the user by displaying the searched ingredient.
A request is made to the API using the authorisation keys and specified ingredient.
The program outputs the list number, recipe title (label) and the recipe source (website title) of recipes found.
The user is prompted to choose a recipe number from the list and the website link, number of servings and ingredient lines are displayed.

## Installation
You will need to have Python installed to run this program.

- You will also need to sign up for a free account on [Edamam](https://www.edamam.com/) to access the Recipe Search API.
- Once logged in, head to **Accounts**, and click on **Go to Dashboard**. From there click on **Applications**, and then view the details for **Recipe Search API**.
This will give you your **Application ID** and **Application Key**. These need to be saved into separate text files in order to use the program.
- Paste the Application ID into a text file, making sure not to include any spaces or newlines, and save it to `app_id.txt`.
- Paste the Application Key into a text file, making sure not to include any spaces or newlines, and save it to `app_key.txt`.
These files need to be located in the same folder as the program.

## Usage

1. Ensure you have Python installed on your machine. You can download Python from the official website.
2. Clone the repository to your local machine or download the Python file.
3. Open a terminal/command prompt and navigate to the directory containing the Python file.
4. Run the program with the command `python recipe_search.py`.
