'''EPR 08 Aufgabe'''
__author__ = "Chris"

from plants import Plants

class Animals:

    class Koalabear:

        def __init__(self) -> None:
            self.type = 1
            self.max_health = 50
            self.max_stamina = 40
            self.max_damage = 0
            self.stamina_when_killed = 30
            self.max_age = 35
            self.min_breed_age = 10
            self.move_range = 2
            self.position = []
            self.consumes = [Plants.Eucalyptus]
            self.identifier = "K"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)



    class Pandabear:
        
        def __init__(self) -> None:
            self.type = 1
            self.max_health = 60
            self.max_stamina = 30
            self.max_damage = 0
            self.stamina_when_killed = 20
            self.max_age = 40
            self.min_breed_age = 10
            self.move_range = 2
            self.position = []
            self.consumes = [Plants.Bamboo]
            self.identifier = "P"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class Fly:
            
        def __init__(self) -> None:
            self.type = 1
            self.max_health = 10
            self.max_stamina = 20
            self.max_damage = 0
            self.stamina_when_killed = 5
            self.max_age = 10
            self.min_breed_age = 5
            self.move_range = 5
            self.position = []
            self.consumes = [Plants.Mushroom, Plants.Cactus]
            self.identifier = "F"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class Trex:
                
        def __init__(self) -> None:
            self.type = 0
            self.max_health = 100
            self.max_stamina = 50
            self.max_damage = 35
            self.stamina_when_killed = 50
            self.max_age = 50
            self.min_breed_age = 20
            self.move_range = 3
            self.position = []
            self.consumes = [Animals.Horse, Animals.Human, Animals.Fox]
            self.identifier = "T"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class Eagle:
                        
        def __init__(self) -> None:
            self.type = 0
            self.max_health = 50
            self.max_stamina = 30
            self.max_damage = 10
            self.stamina_when_killed = 20
            self.max_age = 30
            self.min_breed_age = 10
            self.move_range = 5
            self.position = []
            self.consumes = [Animals.Mouse]
            self.identifier = "E"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class Mouse:
                                
        def __init__(self) -> None:
            self.type = 1
            self.max_health = 20
            self.max_stamina = 10
            self.max_damage = 0
            self.stamina_when_killed = 5
            self.max_age = 10
            self.min_breed_age = 5
            self.move_range = 4
            self.position = []
            self.consumes = [Plants.Berrybush, Plants.AppleTree]
            self.identifier = "M"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class Horse:
                                        
        def __init__(self) -> None:
            self.type = 1
            self.max_health = 40
            self.max_stamina = 20
            self.max_damage = 10
            self.stamina_when_killed = 10
            self.max_age = 40
            self.min_breed_age = 10
            self.move_range = 3
            self.position = []
            self.consumes = [Plants.AppleTree, Plants.Berrybush]
            self.identifier = "H"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class Human:
                                            
        def __init__(self) -> None:
            self.type = 2
            self.max_health = 100
            self.max_stamina = 100
            self.max_damage = 20
            self.stamina_when_killed = 50
            self.max_age = 100
            self.min_breed_age = 20
            self.move_range = 1
            self.position = []
            self.consumes = [Animals.Horse, Animals.Rabbit, Plants.Mushroom, Plants.AppleTree, Plants.Berrybush]
            self.identifier = "U"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class Rabbit:

        def __init__(self) -> None:
            self.type = 1
            self.max_health = 20
            self.max_stamina = 10
            self.max_damage = 0
            self.stamina_when_killed = 5
            self.max_age = 10
            self.min_breed_age = 5
            self.move_range = 4
            self.position = []
            self.consumes = [Plants.Berrybush]
            self.identifier = "R"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class VenusFlyTrap:

        def __init__(self) -> None:
            self.type = 1
            self.max_health = 20
            self.max_stamina = 10
            self.max_damage = 20
            self.stamina_when_killed = 5
            self.max_age = 10
            self.min_breed_age = 5
            self.move_range = 0
            self.position = []
            self.consumes = [Animals.Fly]
            self.identifier = "V"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)


    class Fox:

        def __init__(self) -> None:
            self.type = 2
            self.max_health = 30
            self.max_stamina = 15
            self.max_damage = 5
            self.stamina_when_killed = 10
            self.max_age = 15
            self.min_breed_age = 5
            self.position = []
            self.consumes = [Animals.Mouse, Plants.Berrybush]
            self.identifier = "F"
        
        def get_type(self) -> int:
            '''Returns the type of the animal
            input:
                - None
            output:
                - int
            '''
            return self.type

        def get_max_health(self) -> int:
            '''Returns the max health of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_health

        def get_max_stamina(self) -> int:
            '''Returns the max stamina of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_stamina

        def get_max_damage(self) -> int:
            '''Returns the max damage of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_damage

        def get_max_age(self) -> int:
            '''Returns the max age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.max_age

        def get_stamina_when_killed(self) -> int:
            '''Returns the stamina when killed of the animal
            input:
                - None
            output:
                - int
            '''
            return self.stamina_when_killed

        def get_consumes(self) -> list:
            '''Returns the consumes of the animal
            input:
                - None
            output:
                - list
            '''
            return self.consumes
        
        def get_min_breed_age(self) -> int:
            '''Returns the min breed age of the animal
            input:
                - None
            output:
                - int
            '''
            return self.min_breed_age

        def get_move_range(self) -> int:
            '''Returns the move range of the animal
            input:
                - None
            output:
                - int
            '''
            return self.move_range
        
        def get_position(self) -> list:
            '''Returns the position of the animal
            input:
                - None
            output:
                - list
            '''
            return self.position

        def set_position(self, position: list) -> None:
            '''Sets the position of the animal
            input:
                - list
            output:
                - None
            '''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the animal
            input:
                - None
            output:
                - str
            '''
            return self.identifier

        def add_position(self, position: list) -> None:
            '''Adds a position to the position list of the animal
            input:
                - list
            output:
                - None
            '''
            self.position.append(position)
    

    def __init__(self, type: any) -> None:
        self.type = type
        self.health = type.get_max_health()
        self.stamina = type.get_max_stamina()
        self.damage = type.get_max_damage()
        self.stamina_when_killed = type.get_stamina_when_killed()
        self.age = type.get_max_age()
    
    def get_health(self) -> int:
        '''Returns the health of the animal
        input:
            - None
        output:
            - int
        '''
        return self.health

    def get_stamina(self) -> int:
        '''Returns the stamina of the animal
        input:
            - None
        output:
            - int
        '''
        return self.stamina

    def add_damage(self, damage: int) -> None:
        '''Adds damage to the animal
        input:
            - int
        output:
            - None
        '''
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def add_stamina(self, stamina: int) -> None:
        '''Adds stamina to the animal
        input:
            - int
        output:
            - None
        '''
        self.stamina += stamina
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina

    def reduce_stamina(self, stamina: int) -> None:
        '''Reduces stamina from the animal
        input:
            - int
        output:
            - None
        '''
        self.stamina -= stamina
        if self.stamina < 0:
            self.stamina = 0
    
    def get_score(self) -> float:
        '''Returns the score of the animal
        input:
            - None
        output:
            - float
        '''
        return self.health * (1 / self.type.get_health()) + self.stamina *\
            (1 /self.type.get_stamina())

    def get_type(self) -> any:
        '''Returns the type of the animal
        input:
            - None
        output:
            - any
        '''
        return self.type
    
    def get_age(self) -> int:
        '''Returns the age of the animal
        input:
            - None
        output:
            - int
        '''
        return self.age
