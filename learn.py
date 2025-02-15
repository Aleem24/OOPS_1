# Blueprint or class of a player
class Player:

# Instance attribute

 def __init__(self,name,number,club):
    self.name = name
    self.number = number
    self.club = club

position = Player("Messi",10,"Argentina")
print(f"Hi I am one of the fan of {position.name} and he is in {position.number} jersey number. In Fifa world cup, he was playing in {position.club}")

# Blueprint or class of a country
class Country:
  
# Instance attribute

 def __init__(self,name,continent,population,area,capital,GDP):
   self.name = name
   self.continent = continent
   self.population = population
   self.area = area
   self.capital = capital
   self.GDP = GDP

place = Country("China","Asia", 1,410,710,000, 9,596,960 SQ.KM,"Beijing", 17.8)
print(f"Hello, I am talking about a country named {place.name}. It is in {place.continent} and it has an population of {place.population}. {place.name}'s land area is {place.area} and it's capital city is {place.capital}. The last thing is it's GDP is {place.GDP}")
   

  