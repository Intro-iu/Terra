from life import *

class World:
    def __init__(self):
        self.time = 0
        self.species = {}
        self.speciesNumTotal = {}
        
    def spawn(self, object):
        # 判断世界中原先是否存在同类物种，如果不存在则新建
        objectName = object.__class__.__name__
        if objectName not in self.species:
            self.species[objectName] = []
            self.speciesNumTotal[objectName] = 0
        
        self.species[objectName].append(object) # 添加物种
        self.speciesNumTotal[objectName] += 1 # 物种总数+1

    # 人类繁衍
    def reproduce(self, Father, Mother):
        self.spawn(Human(self.speciesNumTotal['Human'], time=self.time, Father=Father, Mother=Mother))

    def timePass(self):
        self.time += 1
        for human in self.species['Human']:
            human.grow()
            human.target()  # AI决策人类行动
            human.hunger_Cur -= 0.1

            if (self.time - human.birthday) % (30 * 25) == 0:
                human.age += 1

            if human.hunger_Cur <= 0:
                human.health_Cur -= 0.5

            # 死亡判断
            if human.health_Cur <= 0 or human.age >= human.life:
                self.species['Human'].remove(human)
                print('Human', human.id, 'died.', 'Score:', human.score())
                if len(self.species['Human']) == 0:
                    print('The last human died.')
                    break
            else:
                print('Human', human.id, 'is alive.', 'Score:', human.score())

    def run(self):
        for day in range(10):
            for hour in range(25):
                self.timePass()


    