from life import *

humanNum = 2

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