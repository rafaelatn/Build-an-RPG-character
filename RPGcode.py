#defining full/empty dot output
full_dot = '●'
empty_dot = '○'

#creating function to create character + conditions 
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

#creating library 
    stats = {'STR': strength, 'INT': intelligence, 'CHA': charisma}

#conditions for values in stats (library created beforehand)
    for stat in stats.values():
        if not isinstance(stat, int):
            return 'All stats should be integers'
        if stat < 1:
            return 'All stats should be no less than 1'
        if stat > 4:
            return 'All stats should be no more than 4'

#condition for sum of values
    if sum(stats.values()) != 7:
        return 'The character should start with 7 points'

#putting together library's values (user input) with full_dot/empty_dot 
    character_string = name
    for key in ['STR', 'INT', 'CHA']:
        stat = stats[key]
        character_string += f'\n{key} {full_dot*stat}{empty_dot*(10-stat)}'

#output of the combination (user input + full_dot/empty_dot)
    return character_string

#EXAMPLE
create_character('ren', 4, 2, 1) 
#ren
#STR ●●●●○○○○○○
#INT ●●○○○○○○○○
#CHA ●○○○○○○○○○
