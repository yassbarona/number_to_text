from utils.utils import *
import json

def main(input):
    french_words = [number_to_french(num) for num in input]  
    return french_words

if __name__ == "__main__":
    with open('./dataset.json', 'r') as file:
            data = json.load(file)
            input = data['numbers']
            result = main(input)
            print(result)


