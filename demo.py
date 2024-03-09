from life import *
from world import *

world = World()
world.spawn(Berry(1, 1))
world.spawn(Adam)
world.spawn(Eva)

world.reproduce(world.species['Human'][0], world.species['Human'][1])
print(world.species['Berry'])
print(world.species['Human'])

world.run()