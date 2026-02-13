


def create_character(name:str, strength:int, intelligence:int, charisma:int,style_return:bool = True) ->str:
    full_dot = '●'
    empty_dot = '○'
    spaces = " "
    stats_unique = (strength, intelligence, charisma)
    status_values = 10
    validate_stats = [isinstance(stats, int) for stats in stats_unique]
    if not isinstance(name, str):
        return "The character name should be a string"
    elif not name:
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif spaces in name:
        return "The character name should not contain spaces"
    if not all(validate_stats):
        return "All stats should be integers"
    for status in stats_unique:
        if status < 1:
            return "All stats should be no less than 1"
        elif status > 4:
            return "All stats should be no more than 4"
    if sum(stats_unique) != 7:
        return "The character should start with 7 points"


    character_name = f"{name}\n"
    strength_dot = status_values - strength
    strength_draw = f"STR {full_dot * strength}" + f"{strength_dot * empty_dot}\n"
    intel_dot = status_values- intelligence
    intel_draw = f"INT {full_dot*intelligence}" +f"{intel_dot*empty_dot}\n"
    charisma_dot = status_values - charisma
    charisma_draw=f"CHA {full_dot*charisma}"+f"{charisma_dot*empty_dot}\n"


    #return character_name+strength_draw+intel_draw+charisma_draw
    if style_return:
     return (f"{character_name}{strength_draw}{intel_draw}"
            f"{charisma_draw}")
    else:
        return (f"{name}\nSTR {full_dot * strength}{(status_values - strength) * empty_dot}\n"
                f"INT {full_dot * intelligence}{(status_values - intelligence) * empty_dot}\n"
                f"CHA {full_dot * charisma}{(status_values - charisma) * empty_dot}")



if __name__ == "__main__":
 print(create_character("Ren", 4, 1, 2,style_return=False))
