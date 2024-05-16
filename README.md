# Text to Number

## Description
This Python code takes a list of French characters and returns a list of their equivalent names in French.

## Installation
Clone the repository and navigate to `main.py`.

## Usage
Run the main script: `python -m main.py`

## Use of AI

I used ChatGPT to accelerate the creation of this package. Here are the prompts I used:

### Base code creation:
"""I need to create an algorithm that serves to transform input numbers given in a list into their text equivalent in French. For example: if the input is [1, 2, 3] the output should be ['un', 'deux', 'trois'].

There are some important rules to follow. Here are the rules:

The units
Less than 16 follow no rules but each has a specific name: "zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize" (from 0 to 16).

The tens
As French up to 60, or using Belgium-French (septante, huitante, nonante), up to 90, follow the same pattern:
  - "dix"
  - "vingt"
  - "trente"
  - "quarante"
  - "cinquante"
  - "soixante"
  - "septante"
  - "huitante"
  - "nonante" (from 10 to 90). "huitante" could also be "octante".
  
In French from France, the pattern changes at 70:
  - 70 = 60 + 10 = "soixante-dix"
  - 80 = 4 * 20 = "quatre-vingts"
  - 90 = 4 * 20 + 10 = "quatre-vingt-dix" (because why not!)

Numbers from 22 to 29, then 32 to 39...
The rule is easy:
  - 22 = 20 + 2 = "vingt-deux", with a dash in between.
  
From 17 to 19, it follows this rule:
  - 17 = 10 + 7 = "dix-sept"

Numbers ending with 1:
The rule is the same as above, but with "-et-" which means "and" instead of "-":
  - 21 = "vingt-et-un"
  
Before 1990, the writing was "vingt et un", but since the 1990 simplification reform, all words used for numbers are joined-up with dashes.

Numbers after 70 and 90:
 - 74 = 60 + 14 = "soixante-quatorze"
 - 77 = 60 + 17 = 60 + 10 + 7 = "soixante-dix-sept"
 - 95 = 4 * 20 + 15 = "quatre-vingt-quinze"
 - 99 = 4 * 20 + 10 + 9 = "quatre-vingt-dix-neuf"

Plurals of "quatre-vingt":
  - 80: 4 * 20 = "quatre-vingts" → means 4 times 20 so 20 is plural, thus "vingts" ends with an "s". 
But when it is not the ending of the word, the plural form disappears:
  - 82 = 4 * 20 + 2 = "quatre-vingt-deux", without an "s" at "vingt".

71, 81, 91
For some unknown reasons, 71 uses an "-et-", 81 and 91 use a dash:
  - 71 = 60 + 11 = "soixante-et-onze"
  - 81 = 4 * 20 + 1 = "quatre-vingt-un"
  - 91 = 4 * 20 + 11 = "quatre-vingt-onze"

100 and more
One hundred is "cent". 
One thousand is "mille". 
The rule is joining this and the rest with a dash:
  - 130 = 100 + 30 = "cent-trente"
  - 1110 = 1000 + 100 + 10 = "mille-cent-dix"

Plurals of "cent" and "mille":
Like 80, 100 and 1000 can be plural if it ends a word and then takes an "s": "cents", "milles":
  - 200 = 2 * 100 = "deux-cents"
  - 3000 = 3 * 1000 = "trois-milles"

When "cent" or "mille" is not ending the word, then it is not plural:
  - 252 = 2 * 100 + 52 = "deux-cent-cinquante-deux"
  - 2045 = 2 * 1000 + 45 = "deux-mille-quarante-cinq" 
  - 200000 = 2 * 100 * 1000 = "deux-cent-milles", without "s" at "cents", but with "s" at "milles".
  - 180000 = (100 + 4 * 20) * 1000 = "cent-quatre-vingt-milles", without "s" at "vingt", but with "s" at "milles".

This is what you need to do:

1. Describe the rules that you have been able to identify for the algorithm.
2. Provide me with a Python script that can handle all of the rules and can serve as a base code for me to use in a package.
3. Provide me with a Python list that I can use as a test input."""

### Debugging:
 """I'm getting the following error running the previous script you provided:
 File "c:\Users\ybaronadao\Desktop\TEMP\number_to_text\utils\utils.py", line 57, in 
number_to_french
    return thousands(n)
           ^^^^^^^^^^^^
  File "c:\Users\ybaronadao\Desktop\TEMP\number_to_text\utils\utils.py", line 14, in 
thousands
    return UNITS[thousand] + "-mille-" + number_to_french(remainder)
           ~~~~~^^^^^^^^^^
IndexError: list index out of range

Do the following:
1. Find the possible cause of the error.
2. Share an explanation about it.
3. Give me the best solution.
"""

### Testing set:
 """Give me a dictionary with 20 items, each key should be a random number between 0 and 9999999 and the value should be its name in text in French:
Here is an example: {0: 'zéro', 1: 'un', 2: 'deux'}"""

### Write Docstrings:
 """Write siple Docstrings for the funtions i previously shared"""
