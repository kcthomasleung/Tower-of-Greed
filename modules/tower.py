from modules.characters import FloorGuardian
from rich import print


class Tower:
    def __init__(self):
        self.name = "Tower of Greed"
        self.floors = []
        self.create_floors()

    def create_floors(self):
        for i in range(1, 101):
            floor = Floor(i)
            self.floors.append(floor)


class Floor:
    def __init__(self, level):
        self.level = level
        self.lobby_room = Room(level, "lobby")
        self.battle_room = Room(level, "battle")


class Room:
    def __init__(self, level, room_type):
        self.level = level
        self.players = []
        self.location_id = ""
        self.room_type = room_type
        self.floor_guardian = {}
        self.check_room_type()
        self.set_location_id()
        self.assign_floor_guardian()

    def check_room_type(self):
        # this method ensures the passed room_type parameter is either "lobby" or "battle" and prints an error otherwise
        if self.room_type != "lobby" and self.room_type != "battle":
            print("Error: Room type invalid")

    def set_location_id(self):
        # method to set the location_id attribute of each room
        room_type = str

        if self.room_type == "lobby":
            room_type = "a"
        elif self.room_type == "battle":
            room_type = "b"
        else:
            print("Error: Invalid room type")

        self.location_id = f"{self.level}{room_type}"

    def assign_floor_guardian(self):
        # method to assign a floor guardian to every battle room
        if self.room_type == "battle":
            self.floor_guardian = FloorGuardian(level=self.level)

