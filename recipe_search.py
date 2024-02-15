import requests

# import responses library to give information about status code errors if authorisation
# or request url is not correct and returns an error
from http.client import responses


def get_authorisation():
    # This function reads the authorisation key from the local host and returns them for use in the next function
    # Reads the Edamam App ID and stores in a variable for use later
    with open('app_id.txt', 'r') as app_id_file:
        app_id = app_id_file.read()
    # Reads the Edamam App Key and stores in a variable for use later
    with open('app_key.txt', 'r') as app_key_file:
        app_key = app_key_file.read()
    return app_id, app_key


def get_input(app_id, app_key):
    # This function prompts the user for an input and validates it against acceptable characters
    while True:
        invalid_characters = ""
        acceptable = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
        ingredient = input('Enter an ingredient (letters and spaces only): ')
        for character in ingredient:
            # If character is a number set a variable to indicate this is true, otherwise false
            if not character in acceptable:
                invalid_characters = True
        if invalid_characters:
            print("Invalid input: Please re-enter a search query using only letters and/or spaces")
        else:
            return ingredient


def confirm_input(ingredient):
    # This function prints a message confirming the user input
    print(f'Searching for recipes containing {ingredient}...\n')


def get_recipes(query):
    # This function sends a GET request to the Edamam API with the specified ingredient,
    # converts the JSON data to a python dictionary and returns the dictionary

    # Define the url which will used to make the API call
    url = f'https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}'

    # Send a GET request to the specified URL and store the response
    response = requests.get(url)

    # Check the response status code. If it is 200 convert the response data from
    # JSON to a python dictionary and store as a variable 'data'
    # A try-except block might be better here for error handling
    if response.status_code == 200:
        data = response.json()
    # If the response status code is not 200 set the variable 'data' to 'Error' and
    # print an error message
    else:
        data = 'Error'
        print(f'An error occurred - Status code {response.status_code}: {responses[response.status_code]}')
        print(f'Please check the URL contains the correct Application ID and Key')
    # Return the dictionary containing the data to pass to the next function
    return data


def print_output(recipes):
    # This function lists the name of each recipe found containing the specified ingredient
    # from the data dictionary
    count = 0
    for hit in recipes['hits']:  # 'hits' contains the recipes
        recipe = hit['recipe']
        count += 1
        # prints the list number, recipe title (label) and the recipe source (website title)
        print(f'{count}) {recipe['label']} ({recipe['source']})')
    # if no recipes are found print a message
    if recipes['count'] == 0:
        print('No recipes found - please try searching for a different ingredient')
    else:
        # if recipes are found, prints the total count of recipes found for the specified query
        print(f"Recipes found: {recipes['count']}")


def print_chosen_recipe(recipes):
    # If any results are returned this function prompts the user to enter the number of the recipe
    # they would like to view and prints out the name, url, number of servings and ingredients
    if recipes['count'] > 0:
        # initialise choice to zero
        choice = 0
        # Check the chosen recipe number is within the range displayed. These come from 'from'
        # and 'to' in the API
        valid_choices = [str(i) for i in range(recipes['from']+1, recipes['to']+1)]
        # creates a list of numbers within the range in string format
        while choice not in valid_choices:
            choice = input('Select a recipe number: ')
            if choice not in valid_choices:
                print(f"Invalid choice. Please select a recipe number between {recipes['from']+1} and {recipes['to']}")
        # converts choice to an integer to use as an index on hits
        choice = int(choice)
        # Stores the data for the chosen recipe ('hits' start from 0, so 1 is deducted from the choice number)
        chosen_recipe = recipes['hits'][choice-1]['recipe']
        print(f"\n{chosen_recipe['label']}")
        print("=" * len(chosen_recipe['label']))  # Underlines the recipe heading
        print(f"\nWebsite: {chosen_recipe['url']}")
        print(f"Servings: {int(chosen_recipe['yield'])}\n")  # converts 'yield' to an integer from a float
        print('Ingredients:')
        # Loops through the ingredient lines and prints them one by one
        for item in chosen_recipe['ingredientLines']:
            print(item)


app_id, app_key = get_authorisation()

ingredient = get_input(app_id, app_key)

confirm_input(ingredient)

recipes = get_recipes(ingredient)

# If the status code returned is not an error, run the function to output the recipes
if recipes != 'Error':
    print_output(recipes)
    print_chosen_recipe(recipes)
