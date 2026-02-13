from typing import Any


class extract_info:
    def __init__(self):
        pass

    def extract_attribute(self) -> tuple[dict[str, list[Any]], dict[str, list[Any]]]:
        method_list = []
        init_list = []

        for attr in dir(self):
            if not attr.startswith("__") and not callable(self):
                if type(getattr(self, attr)).__name__ == 'method':
                    method_list.append(attr)
                else:
                    init_list.append(attr)
        init_dict = {"init": init_list}
        method_dict = {"method": method_list}
        class_tuple = (init_dict, method_dict)
        return class_tuple


