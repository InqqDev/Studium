__author__ = "Chris"

class Plants:

    class AppleTree:

        def __init__(self) -> None:
            self.max_age = 100
            self.min_size = 10
            self.max_size = 100
            self.size_modifier = 1
            self.min_breed_age = 50
            self.position = (0, 0)
            self.identifier = "a"

        def get_max_age(self) -> int:
            '''Returns the maximum age of the plant
            input:
                - None
            output:
                - int
                    the maximum age of the plant'''
            return self.max_age

        def get_min_size(self) -> int:
            '''Returns the minimum size of the plant
            input:
                - None
            output:
                - int
                    the minimum size of the plant'''
            return self.min_size

        def get_max_size(self) -> int:
            '''Returns the maximum size of the plant
            input:
                - None
            output:
                - int
                    the maximum size of the plant'''
            return self.max_size
        
        def get_size_modifier(self) -> int:
            '''Returns the size modifier of the plant
            input:
                - None
            output:
                - int
                    the size modifier of the plant'''
            return self.size_modifier

        def get_min_breed_age(self) -> int:
            '''Returns the minimum breeding age of the plant
            input:
                - None
            output:
                - int
                    the minimum breeding age of the plant'''
            return self.min_breed_age
        
        def get_position(self) -> tuple:
            '''Returns the position of the plant
            input:
                - None
            output:
                - tuple
                    the position of the plant'''
            return self.position

        def set_position(self, position: tuple) -> None:
            '''Sets the position of the plant
            input:
                - position: tuple
                    the position of the plant
            output:
                - None'''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the plant
            input:
                - None
            output:
                - str
                    the identifier of the plant'''
            return self.identifier


    class Eucalyptus:

        def __init__(self) -> None:
            self.max_age = 75
            self.min_size = 5
            self.max_size = 50
            self.size_modifier = 2
            self.min_breed_age = 50
            self.position = (0, 0)
            self.identifier = "e"

        def get_max_age(self) -> int:
            '''Returns the maximum age of the plant
            input:
                - None
            output:
                - int
                    the maximum age of the plant'''
            return self.max_age

        def get_min_size(self) -> int:
            '''Returns the minimum size of the plant
            input:
                - None
            output:
                - int
                    the minimum size of the plant'''
            return self.min_size

        def get_max_size(self) -> int:
            '''Returns the maximum size of the plant
            input:
                - None
            output:
                - int
                    the maximum size of the plant'''
            return self.max_size
        
        def get_size_modifier(self) -> int:
            '''Returns the size modifier of the plant
            input:
                - None
            output:
                - int
                    the size modifier of the plant'''
            return self.size_modifier

        def get_min_breed_age(self) -> int:
            '''Returns the minimum breeding age of the plant
            input:
                - None
            output:
                - int
                    the minimum breeding age of the plant'''
            return self.min_breed_age
        
        def get_position(self) -> tuple:
            '''Returns the position of the plant
            input:
                - None
            output:
                - tuple
                    the position of the plant'''
            return self.position

        def set_position(self, position: tuple) -> None:
            '''Sets the position of the plant
            input:
                - position: tuple
                    the position of the plant
            output:
                - None'''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the plant
            input:
                - None
            output:
                - str
                    the identifier of the plant'''
            return self.identifier


    class Bamboo:

        def __init__(self) -> None:
            self.max_age = 50
            self.min_size = 1
            self.max_size = 25
            self.size_modifier = 4
            self.min_breed_age = 25
            self.position = (0, 0)
            self.identifier = "b"
        
        def get_max_age(self) -> int:
            '''Returns the maximum age of the plant
            input:
                - None
            output:
                - int
                    the maximum age of the plant'''
            return self.max_age

        def get_min_size(self) -> int:
            '''Returns the minimum size of the plant
            input:
                - None
            output:
                - int
                    the minimum size of the plant'''
            return self.min_size

        def get_max_size(self) -> int:
            '''Returns the maximum size of the plant
            input:
                - None
            output:
                - int
                    the maximum size of the plant'''
            return self.max_size
        
        def get_size_modifier(self) -> int:
            '''Returns the size modifier of the plant
            input:
                - None
            output:
                - int
                    the size modifier of the plant'''
            return self.size_modifier

        def get_min_breed_age(self) -> int:
            '''Returns the minimum breeding age of the plant
            input:
                - None
            output:
                - int
                    the minimum breeding age of the plant'''
            return self.min_breed_age
        
        def get_position(self) -> tuple:
            '''Returns the position of the plant
            input:
                - None
            output:
                - tuple
                    the position of the plant'''
            return self.position

        def set_position(self, position: tuple) -> None:
            '''Sets the position of the plant
            input:
                - position: tuple
                    the position of the plant
            output:
                - None'''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the plant
            input:
                - None
            output:
                - str
                    the identifier of the plant'''
            return self.identifier


    class Mushroom:

        def __init__(self) -> None:
            self.max_age = 25
            self.min_size = 1
            self.max_size = 10
            self.size_modifier = 1
            self.min_breed_age = 25
            self.position = (0, 0)
            self.identifier = "m"
            
        def get_max_age(self) -> int:
            '''Returns the maximum age of the plant
            input:
                - None
            output:
                - int
                    the maximum age of the plant'''
            return self.max_age

        def get_min_size(self) -> int:
            '''Returns the minimum size of the plant
            input:
                - None
            output:
                - int
                    the minimum size of the plant'''
            return self.min_size

        def get_max_size(self) -> int:
            '''Returns the maximum size of the plant
            input:
                - None
            output:
                - int
                    the maximum size of the plant'''
            return self.max_size
        
        def get_size_modifier(self) -> int:
            '''Returns the size modifier of the plant
            input:
                - None
            output:
                - int
                    the size modifier of the plant'''
            return self.size_modifier

        def get_min_breed_age(self) -> int:
            '''Returns the minimum breeding age of the plant
            input:
                - None
            output:
                - int
                    the minimum breeding age of the plant'''
            return self.min_breed_age
        
        def get_position(self) -> tuple:
            '''Returns the position of the plant
            input:
                - None
            output:
                - tuple
                    the position of the plant'''
            return self.position

        def set_position(self, position: tuple) -> None:
            '''Sets the position of the plant
            input:
                - position: tuple
                    the position of the plant
            output:
                - None'''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the plant
            input:
                - None
            output:
                - str
                    the identifier of the plant'''
            return self.identifier


    class Cactus:

        def __init__(self) -> None:
            self.max_age = 25
            self.min_size = 1
            self.max_size = 10
            self.size_modifier = 2
            self.min_breed_age = 25
            self.position = (0, 0)
            self.identifier = "c"
                
        def get_max_age(self) -> int:
            '''Returns the maximum age of the plant
            input:
                - None
            output:
                - int
                    the maximum age of the plant'''
            return self.max_age

        def get_min_size(self) -> int:
            '''Returns the minimum size of the plant
            input:
                - None
            output:
                - int
                    the minimum size of the plant'''
            return self.min_size

        def get_max_size(self) -> int:
            '''Returns the maximum size of the plant
            input:
                - None
            output:
                - int
                    the maximum size of the plant'''
            return self.max_size
        
        def get_size_modifier(self) -> int:
            '''Returns the size modifier of the plant
            input:
                - None
            output:
                - int
                    the size modifier of the plant'''
            return self.size_modifier

        def get_min_breed_age(self) -> int:
            '''Returns the minimum breeding age of the plant
            input:
                - None
            output:
                - int
                    the minimum breeding age of the plant'''
            return self.min_breed_age
        
        def get_position(self) -> tuple:
            '''Returns the position of the plant
            input:
                - None
            output:
                - tuple
                    the position of the plant'''
            return self.position

        def set_position(self, position: tuple) -> None:
            '''Sets the position of the plant
            input:
                - position: tuple
                    the position of the plant
            output:
                - None'''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the plant
            input:
                - None
            output:
                - str
                    the identifier of the plant'''
            return self.identifier


    class Berrybush:

        def __init__(self) -> None:
            self.max_age = 25
            self.min_size = 1
            self.max_size = 10
            self.size_modifier = 4
            self.min_breed_age = 25
            self.position = (0, 0)
            self.identifier = "e"
                        
        def get_max_age(self) -> int:
            '''Returns the maximum age of the plant
            input:
                - None
            output:
                - int
                    the maximum age of the plant'''
            return self.max_age

        def get_min_size(self) -> int:
            '''Returns the minimum size of the plant
            input:
                - None
            output:
                - int
                    the minimum size of the plant'''
            return self.min_size

        def get_max_size(self) -> int:
            '''Returns the maximum size of the plant
            input:
                - None
            output:
                - int
                    the maximum size of the plant'''
            return self.max_size
        
        def get_size_modifier(self) -> int:
            '''Returns the size modifier of the plant
            input:
                - None
            output:
                - int
                    the size modifier of the plant'''
            return self.size_modifier

        def get_min_breed_age(self) -> int:
            '''Returns the minimum breeding age of the plant
            input:
                - None
            output:
                - int
                    the minimum breeding age of the plant'''
            return self.min_breed_age
        
        def get_position(self) -> tuple:
            '''Returns the position of the plant
            input:
                - None
            output:
                - tuple
                    the position of the plant'''
            return self.position

        def set_position(self, position: tuple) -> None:
            '''Sets the position of the plant
            input:
                - position: tuple
                    the position of the plant
            output:
                - None'''
            self.position = position
        
        def get_identifier(self) -> str:
            '''Returns the identifier of the plant
            input:
                - None
            output:
                - str
                    the identifier of the plant'''
            return self.identifier


    def __init__(self, type: any) -> None:
        self.type = type
        self.age = 1
        self.size = self.type.get_max_size()

    def get_type(self) -> any:
        '''Returns the type of the plant
        input:
            - None
        output:
            - any
                the type of the plant'''
        return self.type
    
    def get_age(self) -> int:
        '''Returns the age of the plant
        input:
            - None
        output:
            - int
                the age of the plant'''
        return self.age
    
    def get_size(self) -> int:
        '''Returns the size of the plant
        input:
            - None
        output:
            - int
                the size of the plant'''
        return self.size
    
    def add_age(self, age) -> None:
        '''Adds age to the plant
        input:
            - age: int
                the age to add
        output: 
            - None'''
        self.age += age

    def add_size(self, size) -> None:
        '''Adds size to the plant
        input:
            - size: int
                the size to add
        output:
            - None'''
        self.size += size

    def get_score(self) -> int:
        '''Returns the score of the plant
        input:
            - None
        output:
            - int
                the score of the plant'''
        return self.size * (1 / self.age)

    
