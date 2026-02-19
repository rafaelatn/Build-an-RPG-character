# Build an RPG Character
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)

This project is a Python lab that practices core programming concepts by building a function capable of creating and validating an RPG character.

The application validates a character's name and attributes (stats), ensuring they follow specific rules. If all validations pass, it returns a formatted string representing the character and their stats visually.


## Objective

Create a function named `create_character` that:
- Validates user input
- Handles multiple error cases
- Returns a formatted, multi-line string representing an RPG character

(All validations must follow the user stories provided in the lab).

---

## Function Signature

```python
create_character(name, strength, intelligence, charisma)
```

## Parameters
| Name           | Type  | Description       |
| -------------- | ----- | ----------------- |
| `name`         | `str` | Character name    |
| `strength`     | `int` | Strength stat     |
| `intelligence` | `int` | Intelligence stat |
| `charisma`     | `int` | Charisma stat     |


### Name Validation
- name is not of type str
- name is an empty string
- name length exceeds 10 characters
- name contains spaces

### Stats Validation
- The function returns an error message if:
- Any stat is not an integer
- Any stat is less than 1
- Any stat is greater than 4
- The sum of all stats is not equal to 7

## Return Value
### On Validation Failure (name)
Returns a `str` describing the first validation error encountered:
- "The character name should be a string"
- "The character should have a name"
- "The character name is too long
- "The character name should not contain spaces)

### On Validation Failure (stats)
- "All stats should be integers"
- "All stats should be no less than 1"
- "All stats should be no more than 4"
- "The character should start with 7 points"

## On Success

### Returns a multi-line string in the following format:

<character_name>\
STR <strength_visual>\
INT <intelligence_visual>\
CHA <charisma_visual>

### Each stat visual consists of:
- A number of full dots (●) equal to the stat value
- A number of empty dots (○) to complete a total of 10 dots

### Example
#### Input
create_character('ren', 4, 2, 1)

#### Output
ren\
STR ●●●●○○○○○○\
INT ●●○○○○○○○○\
CHA ●○○○○○○○○○
