from life import *
from world import *

Eva = Human(id = 0, x = 0, y = 0)
Adam = Human(id = 1, x = 0, y = 0)

Eva.gender = 0
Eva.maxHeight = 1.6
Eva.maxWeight = 50
Eva.age = 22
Eva.height = 1.6
Eva.weight = 50
Eva.maxStrength = 0.8
Eva.strength = 0.8

Adam.gender = 1
Adam.maxHeight = 1.8
Adam.maxWeight = 70
Adam.age = 22
Adam.height = 1.8
Adam.weight = 70
Adam.maxStrength = 1
Adam.strength = 1

world = World(daysInYear=5)
world.spawn(Berry(0, 1, 1))
world.spawn(Eva)
world.spawn(Adam)

world.reproduce(world.species['Human'][0], world.species['Human'][1])

world.run()