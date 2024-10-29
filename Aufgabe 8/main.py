__author__ = "Chris"

import random
import time
from cmd_interface import EntityMap, Matrix
from plants import Plants
from animals import Animals


PLANTSTRINGS = ["AppleTree", "Eucalyptus", "Bambus", "Mushroom", "Cactus",\
    "Berrybush"]
PLANTS = [Plants.AppleTree, Plants.Eucalyptus, Plants.Bamboo, Plants.Mushroom,\
    Plants.Cactus, Plants.Berrybush]
ANIMALSTRINGS = ["Koalabear", "Pandabear", "Fly", "T-rex", "Eagle", "Mouse",\
    "Horse", "Human", "Rabbit", "VenusFlyTrap", "Fox"]
ANIMALS = [Animals.Koalabear, Animals.Pandabear, Animals.Fly, Animals.Trex,\
    Animals.Eagle, Animals.Mouse, Animals.Horse, Animals.Human, Animals.Rabbit,\
        Animals.VenusFlyTrap, Animals.Fox]


class Ecosystem:
    '''Ecosystem class'''

    def __init__(self) -> None:
        '''Constructor'''
        self.plants = []
        self.animals = []
        self.height = 20
        self.width = 20
        self.weather = "clear"
        self.round = 0
        self.max_round = 0
        self.tick = 0
        self.ticks_per_round = 5
        self.await_input = False
        self.round_time = 1
        self.map = EntityMap(self.width, self.height)
        self.screen = Matrix(self.width, self.height)

    def add_plant(self, plant) -> None:
        ''''Add plant to ecosystem
        input: plant (any)
        output: None
        '''
        self.plants.append(plant)

    def add_animal(self, animal) -> None:
        '''Add animal to ecosystem
        input: animal (any)
        output: None'''
        self.animals.append(animal)

    def get_plants(self) -> list:
        '''Get plants
        input: None
        output: plants (list)'''
        return self.plants

    def get_animals(self) -> list:
        '''Get animals
        input: None
        output: animals (list)'''
        return self.animals

    def get_weather(self) -> str:
        '''Get weather
        input: None
        output: weather (str)'''
        return self.weather

    def get_round(self) -> int:
        '''Get round
        input: None
        output: round (int)'''
        return self.round

    def get_tick(self) -> int:
        '''Get tick
        input: None
        output: tick (int)'''
        return self.tick

    def set_weather(self, weather) -> None:
        '''Set weather
        input: weather (str)
        output: None'''
        self.weather = weather

    def add_round(self) -> None:
        '''Add round
        input: None
        output: None'''
        self.round += 1

    def set_tick(self, tick) -> None:
        '''Set tick
        input: tick (int)
        output: None'''
        self.tick = tick

    def set_rounds(self, rounds) -> None:
        '''Set rounds
        input: rounds (int)
        output: None'''
        self.max_round = rounds

    def set_await_input(self, await_input) -> None:
        '''Set await input
        input: await_input (bool)
        output: None'''
        self.await_input = await_input

    def do_await_input(self) -> bool:
        '''Do await input
        input: None
        output: await_input (bool)'''
        return self.await_input

    def set_round_time(self, round_time) -> None:
        '''Set round time
        input: round_time (int)
        output: None'''
        self.round_time = round_time

    def get_round_time(self) -> int:
        '''Get round time
        input: None
        output: round_time (int)'''
        return self.round_time

    def get_rounds(self) -> int:
        '''Get rounds
        input: None
        output: rounds (int)'''
        return self.max_round

    def get_ticks_per_round(self) -> int:
        '''Get ticks per round
        input: None
        output: ticks_per_round (int)'''
        return self.ticks_per_round

    def lightning_strike(self) -> None:
        '''Lightning strike
        input: None
        output: None'''
        spot = (random.randint(0, self.width), random.randint(0, self.height))
        for i in self.plants:
            if spot in i.get_type().get_position():
                i.set_health(0)

    def get_map(self) -> EntityMap:
        '''Get map
        input: None
        output: map (EntityMap)'''
        return self.map

    def get_screen(self) -> Matrix:
        '''Get screen
        input: None
        output: screen (Matrix)'''
        return self.screen

    def get_free_positions(self) -> list:
        '''Get free positions
        input: None
        output: free_positions (list)'''
        free_positions = []
        x = 0
        for i in self.map.get_matrix():
            for j in range(len(i)):
                if i[j] == " ":
                    free_positions.append((x, j))
            x += 1
        return free_positions

    def get_random_free_position(self) -> tuple:
        '''Get random free position
        input: None
        output: position (tuple)'''
        if len(self.get_free_positions()) > 0:
            return random.choice(self.get_free_positions())
        else:
            print("No free positions left!")
            return (999, 999)

    def get_random_position(self) -> tuple:
        '''Get random position
        input: None
        output: position (tuple)'''
        return (random.randint(0, self.width), random.randint(0, self.height))


def config_input_handler(question: str, rangetuple: tuple) -> int:
    '''
    Config input handler
    input: question (str), rangetuple (tuple)
    output: user_input (int)
    '''
    user_input = None
    while user_input not in range(rangetuple[0], rangetuple[1], rangetuple[2]):
        user_input = input(question + " " + str(rangetuple[0]) + " - " +\
            str(rangetuple[1]) + ": ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Please enter a number!")
            user_input = None
    return int(user_input)


def config(ecosystem: Ecosystem) -> None:
    '''
    Config function
    input: ecosystem (Ecosystem)
    output: None
    '''
    for i in PLANTSTRINGS:
        for j in range(config_input_handler("How many of the type " + i +\
            " do you want to add?", (1, 10, 1))):
            ecosystem.add_plant(Plants(PLANTS[PLANTSTRINGS.index(i)]()))
            # set position
            ecosystem.get_plants()[-1].get_type().set_position(
                ecosystem.get_random_free_position())

    for i in ANIMALSTRINGS:
        for j in range(config_input_handler("How many of the type " + i +\
            " do you want to add?", (1, 10, 1))):
            ecosystem.add_animal(Animals(ANIMALS[ANIMALSTRINGS.index(i)]()))
            # set position
            ecosystem.get_animals()[-1].get_type().add_position(
                ecosystem.get_random_free_position())

    ecosystem.set_rounds(config_input_handler(
        "How many rounds do you want to simulate?", (1, 1000, 1)))


    if config_input_handler(
        "Do you want to wait for user input after each tick? (0 = no, 1 = yes)"\
            , (0, 2, 1)) == 0:
        ecosystem.set_await_input(False)
    else:
        ecosystem.set_await_input(True)

    if not ecosystem.do_await_input():
        ecosystem.set_round_time(config_input_handler(\
            "How long should be waited between rounds? (in seconds)",\
                (1, 1000, 1)))



def tick(ecosystem: Ecosystem) -> Ecosystem:
    '''
    Tick function
    input: ecosystem (Ecosystem)
    output: ecosystem (Ecosystem)
    '''
    # register entity positions
    for i in ecosystem.get_animals():
        for j in i.get_type().get_position():
            if type(j) != int:
                ecosystem.get_map().set(j[0], j[1],\
                    i.get_type().get_identifier())
    for i in ecosystem.get_plants():
        j = i.get_type().get_position()
        ecosystem.get_map().set(j[0], j[1], i.get_type().get_identifier())
    # rules:
    # entities with age >= min_breed_age breed
    print(len(ecosystem.get_animals()))
    animal_length = len(ecosystem.get_animals())
    for j in range(animal_length):
        i = ecosystem.get_animals()[j]
        if random.randint(0, 3) == 0:
            classtype = i.get_type().__class__
            ecosystem.add_animal(Animals(classtype()))
            ecosystem.get_animals()[-1].get_type().set_position(
                ecosystem.get_random_free_position())
    print(len(ecosystem.get_plants()))
    # plants grow with size_modifier when it is raining or stormy
    print(ecosystem.get_weather())
    if ecosystem.get_weather() == "rainy" or\
        ecosystem.get_weather() == "stormy":
        size_growth = len(ecosystem.get_plants())
        for j in range(size_growth - 1):
            i = ecosystem.get_plants()[j]
            position = ecosystem.get_plants()[j - 1].get_type().get_position()
            try:
                if ecosystem.get_map().get(position[0] + 1,position[1]) == " ":
                    classtype = i.get_type().__class__
                    ecosystem.add_plant(Plants(classtype()))
                    ecosystem.get_plants()[-1].get_type().set_position(
                        (position[0] + 1, position[1]))
            except IndexError:
                try:
                    if ecosystem.get_map().get_matrix()[position[0] - 1]\
                        [position[1]] == " ":
                        classtype = i.get_type().__class__
                        ecosystem.add_plant(Plants(classtype()))
                        ecosystem.get_plants()[-1].get_type().set_position(\
                            (position[0] - 1, position[1]))
                except IndexError:
                    try:
                        if ecosystem.get_map().get_matrix()[position[0]]\
                            [position[1] + 1] == " ":
                            classtype = i.get_type().__class__
                            ecosystem.add_plant(Plants(classtype()))
                            ecosystem.get_plants()[-1].get_type().set_position(
                                (position[0], position[1] + 1))
                    except IndexError:
                        try:
                            if ecosystem.get_map().get_matrix()[position[0]]\
                                [position[1] - 1] == " ":
                                classtype = i.get_type().__class__
                                ecosystem.add_plant(Plants(classtype()))
                                ecosystem.get_plants()[-1].get_type()\
                                    .set_position((position[0], position[1] - 1))
                        except IndexError:
                            pass
    # animals grow by 0 or 1
    length = len(ecosystem.get_animals())
    for j in range(length):
        i = ecosystem.get_animals()[j]
        position = random.choice(i.get_type().get_position())
        if type(position) != int:
            try:
                if ecosystem.get_map().get_matrix()[position[0] + 1]\
                    [position[1]] == " ":
                    classtype = i.get_type().__class__
                    ecosystem.add_animal(Animals(classtype()))
                    ecosystem.get_animals()[-1].get_type().add_position(
                        (position[0] + 1, position[1]))
                    continue
            except IndexError:
                try:
                    if ecosystem.get_map().get_matrix()[position[0] - 1]\
                        [position[1]] == " ":
                        classtype = i.get_type().__class__
                        ecosystem.add_animal(Animals(classtype()))
                        ecosystem.get_animals()[-1].get_type().add_position(
                            (position[0] - 1, position[1]))
                        continue
                except IndexError:
                    try:
                        if ecosystem.get_map().get_matrix()[position[0]]\
                            [position[1] + 1] == " ":
                            classtype = i.get_type().__class__
                            ecosystem.add_animal(Animals(classtype()))
                            ecosystem.get_animals()[-1].get_type()\
                                .add_position((position[0], position[1] + 1))
                            continue
                    except IndexError:
                        try:
                            if ecosystem.get_map().get_matrix()[position[0]]\
                                [position[1] - 1] == " ":
                                classtype = i.get_type().__class__
                                ecosystem.add_animal(Animals(classtype()))
                                ecosystem.get_animals()[-1].get_type()\
                                    .add_position(
                                        (position[0], position[1] - 1))
                                continue
                        except IndexError:
                            pass
    # animals with 0 stamina take 10% damage
    for i in ecosystem.get_animals():
        if i.get_stamina() == 0:
            i.get_type().set_health(i.get_type().get_health() - 99999)
    # carnivores hunt with 1-3 hits per attack, the lower the stamina the
    #   higher the chance of an attack.
    for i in ecosystem.get_animals():
        if i.get_type().get_type() == "carnivore":
            if i.get_type().get_stamina() < 80:
                if random.randint(0, 100) < i.get_type().get_stamina():
                    j = random.sample(ecosystem.get_animals())
                    if j != i:
                        j.get_type().set_health(j.get_type().get_health() -\
                            random.randint(0, 3))
                        if j.get_type().get_health() <= 0:
                            i.get_type().set_stamina(i.get_type()\
                                .get_stamina() + j.get_type()\
                                    .get_stamina_when_killed())
    # if less than 3 plants of the same type are left, all types of that plant
    #   disappear
    for i in ecosystem.get_plants():
        temp_type_list = []
        type_i = i.get_type().__class__
        for j in ecosystem.get_plants():
            type_j = j.get_type().__class__
            if type_i == type_j:
                temp_type_list.append(j)
        if len(temp_type_list) < 3:
            for j in temp_type_list:
                ecosystem.get_plants().remove(j)
    # herbivores eat between 0 and 3 plant size units
    for i in ecosystem.get_animals():
        if i.get_type().get_type() == "herbivore":
            will_eat = random.randint(1, 3)
            if will_eat > 0:
                for roll in range(200):
                    random_spot = ecosystem.get_random_position()
                    for j in ecosystem.get_plants():
                        if random_spot in j.get_type().get_position():
                            ecosystem.get_plants().remove(j)
                            break
    # animals can only hunt specific plants and animals
    for i in ecosystem.get_animals():
        if i.get_type().get_type() == "carnivore":
            for j in range(3):
                attacked = random.sample(ecosystem.get_animals())
                if attacked != i:
                    attacked.get_type().set_health(attacked.get_type()\
                        .get_health() - random.randint(0, 3))
                    if attacked.get_type().get_health() <= 0:
                        i.get_type().set_stamina(i.get_type().get_stamina() +\
                            attacked.get_type().get_stamina_when_killed())
    # clean up
    # kill entities with age => max_age
    for i in ecosystem.get_animals():
        if i.get_age() >= i.get_type().get_max_age():
            ecosystem.get_animals().remove(i)
    # kill plants with size <= min_size
    for i in ecosystem.get_plants():
        if i.get_size() <= i.get_type().get_min_size():
            ecosystem.get_plants().remove(i)
    # kill entities with health <= 0
    for i in ecosystem.get_animals():
        if i.get_health() <= 0:
            ecosystem.get_animals().remove(i)
    for i in ecosystem.get_animals():
        if type(i.get_type().get_position()) == tuple:
            i.get_type().set_position([i.get_type().get_position()])

    uwu = EntityMap(20, 20)
    uwu.refresh()

    # register entity positions
    for i in ecosystem.get_animals():
        for j in i.get_type().get_position():
            if type(j) != int:
                uwu.set(j[0], j[1], i.get_type().get_identifier())
    for i in ecosystem.get_plants():
        j = i.get_type().get_position()
        uwu.set(j[0], j[1], i.get_type().get_identifier())

    # print ecosystem
        ecosystem.get_screen().refresh()
        ecosystem.get_screen().add_matrix(0, 0, uwu.get_matrix())
        ecosystem.get_screen().set(0, 0, "#")
        ecosystem.get_screen().set(19, 0, "#")
        ecosystem.get_screen().set(19, 19, "#")
        ecosystem.get_screen().set(0, 19, "#")
        ecosystem.get_screen().print()

        if ecosystem.do_await_input():
            input("Press enter to continue")
        else:
            time.sleep(ecosystem.get_round_time())

    return ecosystem

def round_cycle(ecosystem: Ecosystem) -> Ecosystem:
    '''
    Round function
    input: ecosystem (Ecosystem)
    output: ecosystem (Ecosystem)
    '''
    # add counter for round
    ecosystem.add_round()
    # rules:
    # weather changes 50% chance. clear, cloudy, rainy, stormy
    # if weather is stormy, 50% chance of lightning strike
    # lightning strike hits random spot on map. kills entities and plants
    # in that spot
    if random.randint(0, 1) == 0:
        ecosystem.set_weather(random.choice(["clear", "cloudy", "rainy",\
            "stormy"]))
        if ecosystem.get_weather() == "stormy":
            if random.randint(0, 1) == 0:
                # lightning strike
                ecosystem.lightning_strike()
    ecosystem.set_weather("stormy")
    print("round uwu")
    # tick
    for i in range(ecosystem.get_ticks_per_round()):
        ecosystem.set_tick(i + 1)
        ecosystem = tick(ecosystem)

    for i in ecosystem.get_animals():
        print(i.get_type())

    return ecosystem


def main() -> None:
    '''
    Main function
    input: None
    output: None
    '''
    print("Welcome to the Ecosystem Simulator!\n")
    # initialize ecosystem
    Habitat = Ecosystem()
    Habitat.get_screen().refresh()
    Habitat.get_map().refresh()
    # config
    config(Habitat)

    # start simulation
    while Habitat.get_round() < Habitat.get_rounds():
        Habitat = round_cycle(Habitat)


if __name__ == "__main__":
    main()
