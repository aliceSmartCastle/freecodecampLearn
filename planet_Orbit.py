class Planet:
    def __init__(self,name:str,planet_type:str,star:str):
        resolve_type     = [name, planet_type, star]
        robust_referred = [isinstance(i,str) for i in resolve_type]
        if not all(robust_referred) :
            raise TypeError("name, planet type, and star must be strings") from None
        elif not all(resolve_type):
            raise ValueError("name, planet_type, and star must be non-empty strings") from None
        self.name        = name
        self.planet_type = planet_type
        self.star        = star
    def orbit(self) ->str:
        return f"{self.name} is orbiting around {self.star}..."
    def __str__(self) ->str:
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"





if __name__=="__main__":
 planet_1 = Planet('Mars','rocks','sun')
 planet_2 = Planet ("Venus","rocks","sun")
 planet_3 = Planet ("Neptune","ice","sun")

 print(planet_1)
 print(planet_2)
 print(planet_3)

 print(planet_1.orbit())
 print(planet_2.orbit())
 print(planet_3.orbit())