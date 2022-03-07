import requests

BASE_URL = "https://dictionaryapi.com/api/v3/references/collegiate/json/"

API_KEY = "7e22ae82-64bb-43dc-9faf-6d105f77bf79"
PARAMS = {"key": API_KEY}

words = "volatile, levy, convulsed, speculative"

for word in words.split(", "):
    url = BASE_URL + word
    response = requests.get(url, params = PARAMS)
    definition = response.json()[0]["def"][0]["sseq"][0][0][1]["dt"][0][1]
    print(word + ": " + definition)
