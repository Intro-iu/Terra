from life import *

class World:
    def __init__(self):
        self.time = 0
        self.species = {}
        
    def spawn(self, object):
        # 判断世界中原先是否存在同类物种，如果不存在则新建
        objectName = object.__class__.__name__
        if objectName not in self.species:
            self.species[objectName] = []
        
        self.species[objectName].append(object) # 添加物种

    # 人类繁衍
    def reproduce(self, Father, Mother):
        self.spawn(Human(len(self.species['Human']), time = self.time, Father=Father, Mother=Mother))

    def timePass(self):
        self.time += 1
        for human in self.species['Human']:
            human.grow()
            human.target()  # AI决策人类行动
            human.hug -= 0.1

            if (self.time - human.birthday) % 30 == 0:
                human.age += 1

            # 死亡判断
            if human.hug <= 0 or human.age >= human.life:
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


    