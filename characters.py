# class Object:
#     def __init__(self):
#
#
# class Floor:
#     def __init__(self):
#         self.


class Character:
    # This class is to create game characters (e.g. player and monsters)

    def __init__(self, name, type="balanced", gender="M"):
        self.name = name
        self.type = type
        self.hp = int
        self.hitpoint = int
        self.gender = gender
        self.inventory = {}

    # health regeneration function here
    # def hp_regen():


class Player(Character):
    # This class creates a character for the player

    def __init__(self, name, type="balanced", gender="M"):
        super().__init__(name, type, gender)
        self.initial_hp()

    def initial_hp(self):
        try:
            if self.type == "balanced":
                self.hp = 100
                self.hitpoint = 5
            elif self.type == "ADC":
                self.hp = 50
                self.hitpoint = 10
            elif self.type == "Tank":
                self.hp = 150
                self.hitpoint = 2
            else:
                raise ValueError("invalid type")

        except Exception as e:
            print(e)


class FloorGuardian(Character):
    # This class creates Floor Guardians

    def __init__(self, name, type, description="", level=1):
        super().__init__(name, type)
        self.description = description
        self.level = level
        self.hp = 2 ** level
        self.hitpoint = 1 ** level


thomas = Player("thomas", "ADC")
print(thomas.hp)

# rabbit = FloorGuardian("rabbit", "animal", level=50)
# print(rabbit.hp, rabbit.name)
