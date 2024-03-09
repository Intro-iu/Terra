from life import *

class World:
    def __init__(self):
        self.time = 0
        self.human = [Adam, Eva]
        self.plant = []
        

    def spawn(self, object):
        if object.__class__.__name__ == 'Human':
            self.human.append(object)
        if object.__class__.__name__ == 'berry':
            self.plant.append(object)

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

            if human.hug <= 0:
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


    