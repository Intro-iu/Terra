from life import *

humanNum = 2
Adam = Human(0)
Eva = Human(1)

Adam.gender = 1
Adam.life = 100
Adam.height_B = 1.8
Adam.weight_B = 70
Adam.phy_B = 0.8
Adam.age = 22
Adam.height = 1.8
Adam.weight = 70
Adam.phy = 0.8

Eva.gender = 0
Eva.life = 100
Eva.height_B = 1.6
Eva.weight_B = 50
Eva.phy_B = 0.6
Eva.age = 22
Eva.height = 1.6
Eva.weight = 50
Eva.phy = 0.6

HUMAN = [Adam, Eva]

for day in range(10):
    Adam.getFood(berry())
    for hour in range(24):
        for human in HUMAN:
            print('Human', human.id, 'hunger:', human.hug)
            human.grow()
            human.target()
            human.hug -= 0.1
            if human.hug <= 0:
                HUMAN.remove(human)
                print('Human', human.id, 'died.', 'Score:', human.score())
                humanNum -= 1
                if humanNum == 0:
                    print('The last human died.')
                    break