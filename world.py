from life import *

class World:
    def __init__(self):
        self.time = 0
        self.daysInYear = 30
        self.hoursInDay = 24
        self.species = {}
        self.speciesNumTotal = {}
        
    def spawn(self, object):
        # 判断世界中原先是否存在同类物种，如果不存在则新建
        objectName = object.__class__.__name__
        if objectName not in self.species:
            self.species[objectName] = {}
            self.speciesNumTotal[objectName] = 0
        
        self.species[objectName][object.id] = object
        self.speciesNumTotal[objectName] += 1 # 物种总数+1

    # 人类繁衍
    def reproduce(self, Father, Mother):
        self.spawn(Human(self.speciesNumTotal['Human'], Father=Father, Mother=Mother))

    def timePass(self):
        self.time += 1
        for i in list(self.species['Human'].keys()):
            human = self.species['Human'][i]
            human.grow()
            human.target()  # AI决策人类行动
            human.hunger -= 0.1

            human.age += 1

            if human.hunger <= 0:
                human.health -= 0.5

            # 死亡判断
            if human.health <= 0:
                print('Human', human.id, 'died.', 'Time:', self.time, 'Score:', human.score())
                if len(self.species['Human']) == 0:
                    print('The last human died.')
                    break
                del self.species['Human'][i]
            elif self.time % 25 == 0:
                print('Human', human.id, 'health:', human.health, 'hunger:', human.hunger, 'strength:', human.strength, 'age:', human.age)

    def run(self):
        for day in range(self.daysInYear):
            print('Day', day)
            for hour in range(self.hoursInDay):
                self.timePass()
            if 0 in self.species['Human'].keys():
                self.species['Human'][0].getFood(self.species['Berry'][0])