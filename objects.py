# class Object():
#     def __init__(self):
#
#
# class Floor():
#     def __init__(self):
#         self.


class Character:
    def __init__(self, name, type='balanced', gender='M'):
        self.name = name
        self.type = type
        self.hp = int
        self.hitpoint = int
        self.gender = gender
        self.inventory = {}

        try:
            if type == 'balanced':
                self.hp = 100
                self.hitpoint = 5
            elif type == 'ADC':
                self.hp = 50
                self.hitpoint = 10
            elif type == 'tank':
                self.hp = 150
                self.hitpoint = 2
            else:
                raise ValueError('invalid type')

        except Exception as e:
            print(e)

thomas = Character("thomas",'ADC')
print(thomas.hp)