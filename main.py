from utils.utils import *
import json

def main(input):
    french_words = [number_to_french(num) for num in input]  
    return french_words

if __name__ == "__main__":
    with open('./dataset.json', 'r') as file:
            data = json.load(file)
            input = data['numbers']
            main(input)

# Test input
#test_numbers = [1, 2, 3, 17, 21, 30, 77, 81, 95, 100, 130, 200, 252, 1000, 1110, 2045, 180000]
#test_output = [number_to_french(num) for num in test_numbers]
#print(test_output)
