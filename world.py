from life import *

class World:
    def __init__(self):
        self.time = 0
        self.human = [Adam, Eva]
        self.plant = []
        self.speDic = { 
            'Human': self.human, 
            'Berry': self.plant,
            'Tree' : self.plant,
        }
        

    def spawn(self, object):
        self.speDic[object.__class__.__name__].append(object)

    # 人类繁衍
    def reproduce(self, Father, Mother):
        self.spawn(Human(self.human.__len__(), time = self.time, Father=Father, Mother=Mother))

    def timePass(self):
        self.time += 1
        for human in self.human:
            human.grow()
            human.target()  # AI决策人类行动
            human.hug -= 0.1

            if (self.time - human.birthday) % 30 == 0:
                human.age += 1

            if human.hug <= 0:
                self.human.remove(human)
                print('Human', human.id, 'died.', 'Score:', human.score())
                if self.human.__len__() == 0:
                    print('The last human died.')
                    break
            else:
                print('Human', human.id, 'is alive.', 'Score:', human.score())

    def run(self):
        for day in range(10):
            for hour in range(25):
                self.timePass()


    