# 🐍 Python Bootcamp Exercises

A collection of Python programming exercises and homework assignments from a Python bootcamp course, featuring practical coding challenges and fundamental programming concepts.

## Project Overview

This repository contains my solutions to various Python programming exercises designed to build foundational programming skills. The exercises progress from basic input/output operations to more complex string manipulation and algorithmic thinking.

## Contents

### 📓 Jupyter Notebooks
- **homework1.ipynb**: Main homework notebook with 8 different programming exercises
- **homework1-291c0126-e4d9-4abe-bfd3-1a6caf4ed3e1.ipynb**: Additional practice notebook

### 🐍 Python Scripts
- **test.py**: Standalone Python script for string indexing exercises

## Exercise Topics

### 1. String Comparison and Sorting
- Compare two words alphabetically
- Return the word that comes first in alphabetical order
- Implement basic sorting logic

### 2. Vowel Detection
- Check if a given letter is a vowel
- Work with tuples and conditional statements
- User input validation

### 3. Age Calculator
- Calculate age based on birth year
- Use datetime module for current year
- String formatting and type conversion

### 4. Age Classification
- Categorize users by age groups
- Multiple conditional statements (if/elif/else)
- Logical comparison operations

### 5. Speed Calculator
- Calculate running/walking speed in m/h
- Distance and time input processing
- Mathematical operations and unit conversion

### 6. String Indexing
- Access characters by index position
- Boundary checking and error handling
- Index validation and user feedback

### 7. Pig Latin Translator
- Transform words according to Pig Latin rules
- String slicing and concatenation
- Vowel detection and word transformation

### 8. Letter Search and Context
- Find letter position in a string
- Return surrounding characters (previous and next)
- Advanced string manipulation and indexing

### 9. String Slicing
- Extract substrings using user-provided indices
- Input validation for numeric values
- Range checking and error handling

## Technical Skills Demonstrated

- **Data Types**: Strings, integers, tuples, lists
- **Control Flow**: if/elif/else statements, conditional logic
- **Functions**: Built-in functions (input, print, sorted, len, range)
- **Modules**: datetime module usage
- **String Operations**: Indexing, slicing, concatenation, formatting
- **Error Handling**: Input validation and boundary checking
- **User Interaction**: Interactive console applications

## Key Learning Outcomes

- Understanding Python syntax and basic programming concepts
- Working with user input and output formatting
- String manipulation and character processing
- Conditional logic and decision-making algorithms
- Index-based operations and boundary checking
- Problem decomposition and solution design

## Development Environment

- **Language**: Python 3.8.2
- **IDE**: Jupyter Notebook, VS Code
- **Platform**: Interactive Python environment

## Usage

### Running Jupyter Notebooks
```bash
jupyter notebook homework1.ipynb
```

### Running Python Scripts
```bash
python test.py
```

## Exercise Examples

### Vowel Detection
```python
vowel = ('a', 'e', 'i', 'o', 'u')
letter = input('Enter a single letter: ')
if letter in vowel:
    print('Yes')
else:
    print('no')
```

### Pig Latin Translation
```python
word = input('Enter a word: ')
vowel = ('a','e','i','o','u')
if word[0] in vowel:
    print(word + 'way')
else:
    new_word = word[1:] + word[0] + 'ay'
    print(new_word)
```

## Educational Value

This project serves as a comprehensive introduction to Python programming, covering:
- Basic syntax and language fundamentals
- Problem-solving through code
- Interactive program development
- String processing algorithms
- Input validation techniques

Perfect for beginners learning Python or anyone wanting to review fundamental programming concepts.

## Contributing

Feel free to fork this repository and add your own solutions or improvements to the existing exercises.

## License

Educational project - free to use for learning purposes.
