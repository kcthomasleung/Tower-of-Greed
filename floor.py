from characters import FloorGuardian


class Tower:
    def __init__(self) -> None:
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

    def check_room_type(self):
        if self.room_type != "lobby" and self.room_type != "battle":
            print("Error: Room type invalid")
        else:
            pass

    def set_location_id(self):
        room_type = str

        if self.room_type == "lobby":
            room_type = "a"
        elif self.room_type == "battle":
            room_type = "b"
        else:
            print("Error: Invalid room type")

        self.location_id = f"{self.level}{room_type}"


tower = Tower()
print(tower.floors[50].battle_room.location_id)
