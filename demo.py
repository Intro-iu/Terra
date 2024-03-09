from life import *
from world import *

world = World()
world.spawn(Berry(1, 1))

world.reproduce(world.human[0], world.human[1])
print(world.plant)
print(world.human)

world.run()