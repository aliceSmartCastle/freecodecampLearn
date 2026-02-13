import typing
from typing import Any
from magicClass import extract_info


class MusicalInstrument(extract_info):
    def __init__(self, name: str, instrument_type: str) -> None:
        super().__init__()
        self.name = name
        self.instrument_type = instrument_type

    def play(self) -> str:
        return f'The {self.name} is funny to play!'

    def get_fact(self) -> str:
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'

    def revel_method(self, method: str) -> str:
        if hasattr(self, method):
            return getattr(self, method)()
        else:
            return getattr(self, method, f"the {method} not found in {MusicalInstrument.__name__}")
    @typing.no_type_check
    def lead_init(self, init_name: str) -> str:

        if init_name in self.extract_attribute()[0].get('init'):
            return getattr(self, init_name)
        else:
            return getattr(self, init_name, f"the {init_name} not found in {MusicalInstrument.__name__}")


    @typing.no_type_check
    def export_update(self, names: str = '', new_value: Any =0, assign_mapping: typing.Optional[dict[str,Any]] = None, using_map:bool=False):
        final_list = ""
        default_init=self.extract_attribute()[0].get('init')
        if assign_mapping is None:
            assign_mapping ={}
        if using_map:
            for key,value in assign_mapping.items():
              setattr(self,key,value)
            for keys,value in self.__dict__.items():
              if keys not in default_init:
                final_list+=(f"update dynamic class {MusicalInstrument.__name__} {names} to init attribute {keys} to {value} "
                                  f"successfully.\n")
            return final_list
        else:
            increment_init = names
            setattr(self, increment_init, new_value)
            return f"update dynamic {MusicalInstrument.__name__} {names} to {self.__dict__.get(names)} successfully."




if __name__ == "__main__":
    instrument_1 = MusicalInstrument(name='Oboe', instrument_type='woodwind')
    instrument_2 = MusicalInstrument(name='Trumpet', instrument_type='brass')
    print(instrument_1.play())
    print(instrument_1.get_fact())
    print(instrument_2.get_fact())
    print(instrument_2.revel_method(method='play'))
    print(instrument_2.lead_init("name"))
    print(instrument_1.export_update( names="colour", new_value="brown"))
    calling_mapping = {"note": "C#", "price": 800, "master": "sv jali"}
    print(instrument_1.export_update(assign_mapping=calling_mapping,using_map=True).strip())
    




