import os
import openai
from dotenv import load_dotenv


load_dotenv()
openai.api_key = "cf2a8a541f2b4644847fc48c2ae2e9aa"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2024-02-01' # this might change in the future

deployment_name='django3' #This will correspond to the custom name you chose for your deployment when you deployed a model. 
messages = [
    {
        "role": "user",
        "content": "donnes moi une recette, L'utilisateur a sélectionné les ingrédients suivants: "
                   "Légume: aubergine, Viande: boeuf, "
                   "Féculent: mais, Poisson: thon, "
                   "il veut une recette de repas à partir de ces ingrédients de base ici pour un repas de type : "
                   "et avec un temps de préparation de : 30min "
                   "et 30min max de preparation."
    },
    {
        "role": "assistant",
        "content": "Je peux vous proposer une recette avec ces ingrédients. Veuillez patienter un moment pendant que je génère la recette..."
    }
]

# Send a chat completion call to generate an answer
print('Sending a test completion job')

response = openai.ChatCompletion.create(
    engine=deployment_name,
    messages=messages,
    max_tokens=120,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0
)

# Extract and print the response
text = response['choices'][0]['message']['content'].replace('\n', '').replace(' .', '.').strip()
print(text)