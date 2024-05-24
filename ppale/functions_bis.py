import openai
import csv
from dotenv import load_dotenv
import os

# chargement des variables d'environnement stockée dans ".env"
load_dotenv()

# données d'identification et d'authentification openAI
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")

def find_recipe(ingredients):
    # le moteur IA utilisé dans ce programme
    engine = "text-davinci-002"

    # à partir de la liste d'ingrédients, génération d'une chaîne de caractères qui s'intègrera naturellement dans la question posée
    formatted_ingredients = "\n- " + "\n- ".join(ingredients)
    print("FORMATTED INGREDIENTS:",formatted_ingredients)

    # la question qui sera posée au modèle openAI
    question_asked_to_openAI_completions = "Provide a cooking recipe based on the following ingredients:\n" + formatted_ingredients + "\n\nThe response must be aligned with the following template:\n- Name of the recipe\n- Ingredients\n- Steps"

    # un dictionnaire contenant les arguments à passer à l'endpoint "completions" via la méthode "openai.Completion.create" (SDK openAI)
    completion_arguments = {
    "engine" : engine,
    "prompt" : question_asked_to_openAI_completions,
    "temperature" : 0.7,
    "top_p" : 1,
    "max_tokens" : 300,
    "frequency_penalty" : 0,
    "presence_penalty" : 0
    }

    response = openai.Completion.create(
        engine = completion_arguments["engine"],
        prompt =  completion_arguments["prompt"],
        temperature = completion_arguments["temperature"],
        top_p = completion_arguments["top_p"],
        max_tokens = completion_arguments["max_tokens"],
        frequency_penalty = completion_arguments["frequency_penalty"],
        presence_penalty = completion_arguments["presence_penalty"])

    complete_recipe = response["choices"][0]["text"][2:]

    complete_recipe = complete_recipe.replace('to prepare the dish\n\n','')
    complete_recipe = complete_recipe.replace('Recipe for','')
    complete_recipe = complete_recipe.replace('Instructions:','Steps:')
    complete_recipe = complete_recipe.replace('Ingredients','Ingredients:')

    recipe_name = complete_recipe[complete_recipe.find("\n") + 1 : complete_recipe.find("\nIngredients:")]

    ingredients_extraction = complete_recipe[complete_recipe.find("Ingredients:") + 14 : complete_recipe.find("Steps:") - 1]
    steps_extraction = complete_recipe[complete_recipe.find("Steps:") + 6:]

    ingredients_list = list(ingredients_extraction.split('\n'))
    ingredients_list = list(i.strip('- ') for i in ingredients_list)
    ingredients_list = list(filter(lambda a: a != '', ingredients_list))

    steps_list = list(steps_extraction.split('\n'))
    steps_list = list(i[:] for i in steps_list)
    steps_list = list(filter(lambda a: a != '', steps_list))

    print("=========================================\n"+str(response)+"\n=========================================\n")

    result = {
        "RecipeName" : recipe_name,
        "Ingredients" : ingredients_list,
        "Steps" : steps_list
    }

    print(result)

    return result

def ingredients_csv_to_dict(csv_file):
    fields = []
    rows = []
    result = dict()
    with open(csv_file, 'r') as infile:
        csvreader = csv.reader(infile,delimiter=',')
        fields = next(csvreader)
        # print(fields)
        for row in csvreader:
            rows.append(row)
    for category in range(len(fields)):
        if category%2 == 1:
            to_insert = []
            for ingredient in range(len(rows)):
                # print(fields[category])
                # print(to_insert)
                if rows[ingredient][category] != "":
                    to_insert.append(rows[ingredient][category])
            result[fields[category].split("|")[1]] = to_insert
    return result

def split_ingredients_dict_by_category(ingredients_list_csv_to_dict,category):
    cat = category.capitalize()
    category_list = ingredients_list_csv_to_dict[category]
    choices = []
    cpt = 1
    for ingredient in category_list:
        choices.append([cpt,ingredient])
        cpt += 1
    return tuple(choices)

def truc():
    pass

# définition des variables importables dans le projet

ingredients_full_list = ingredients_csv_to_dict("api_home/ingredients_list.csv")

PROTEIN_CHOICES = split_ingredients_dict_by_category(ingredients_full_list,'proteins')
VEGETABLES_CHOICES = split_ingredients_dict_by_category(ingredients_full_list,'vegetables')
LEGUMES_CHOICES = split_ingredients_dict_by_category(ingredients_full_list,'legumes')
STARCH_CHOICES = split_ingredients_dict_by_category(ingredients_full_list,'starch')
SPICES_AND_HERBS_CHOICES = split_ingredients_dict_by_category(ingredients_full_list,'spices_and_herbs')

CHOICES = [PROTEIN_CHOICES,VEGETABLES_CHOICES,LEGUMES_CHOICES,STARCH_CHOICES,SPICES_AND_HERBS_CHOICES]