from random import choice



def add_setting(usr:dict[str,str] , usr_ensure:tuple[str,str]) ->str:

    key = usr_ensure[0].lower()
    value = usr_ensure[1].lower()
    if key in usr:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        usr[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(info:dict[str,str] , sure_info:tuple[str,str]) ->str:
    key = sure_info[0].lower()
    value = sure_info[1].lower()

    if key in info:
        info[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."



def delete_setting(set_dict:dict[str,str], valid_key:str) ->str:
    key = valid_key.lower()
    if set_dict.get(key):
        set_dict.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"


def view_settings(flow:dict[str,str]) ->str:
    storage_object = ""
    head_info = "Current User Settings:\n"
    if not flow:
        return "No settings available."

    else:
        for item in flow.items():
            infos = f"{item[0].capitalize()}: {item[1]}\n"

            storage_object += infos

        return head_info + storage_object


if __name__ == "__main__":
    test_settings = ({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})
    test_tuple =  ('THEME', 'dark'),("Hello","Bob")
    print(delete_setting(test_settings, choice(test_tuple[0])))
    print(add_setting(test_settings, choice(test_tuple)))
    print(add_setting(test_settings, choice(test_tuple)))
    print(update_setting(test_settings, choice(test_tuple)))
    print(update_setting(test_settings ,choice(test_tuple)))
    print(view_settings(test_settings))
