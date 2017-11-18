import json

# Delete config.json if new keys are added
DEFAULT_CONFIG = {
    "token": "Enter token here"
}


try:
    with open('config.json', 'r') as file:
        config = json.load(file)
# Generate config file if config doesnt already exist
except FileNotFoundError:
    with open('config.json', 'w+') as file:
        json.dump(DEFAULT_CONFIG, file)
        config = DEFAULT_CONFIG

