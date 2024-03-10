import random as rd

class Human:
    def __init__(self, id, x = None, y = None, Father = None, Mother = None):
        if x != None and y != None:
            self.x = x
            self.y = y
        # 初始属性
        self.id = id
        self.age = 0

        self.height = 0
        self.weight = 0
        self.health = 5
        self.hunger = 3
        self.strength = 0

        self.maxHeight = 1.6
        self.maxWeight = 50
        self.maxHealth = 5
        self.maxHunger = 3
        self.maxStrength = 0

        self.sonNum = 0

        
        if Father != None and Mother != None:
            self.id = id
            self.gender = rd.randint(0, 1)
            self.Father = Father
            self.Mother = Mother
            self.x = Mother.x + rd.uniform(-0.1, 0.1)
            self.y = Mother.y + rd.uniform(-0.1, 0.1)

            # 基因遗传
            self.maxHeight = (0.4 * Father.maxHeight + 0.6 * Mother.maxHeight) + rd.uniform(-0.2, 0.05)*(Father.maxHeight + Mother.maxHeight)
            self.maxWeight = (0.6 * Father.maxWeight + 0.4 * Mother.maxWeight) + rd.uniform(-0.2, 0.05)*(Father.maxWeight + Mother.maxWeight)

            # 祖先递归sonNum++
            # ToDO

    # 人类成长
    def grow(self):
        self.age += 1/25
        if self.age <= 22:
            self.height += self.maxHeight / 22 / 30 + self.maxHunger / (self.maxHunger+1) * rd.uniform(0.005, 0.010) * self.maxHeight
        self.weight += self.maxWeight / 22 / 30 + self.maxHunger / (self.maxHunger+1) * rd.uniform(0.1, 0.125)
        self.maxHunger = 0.1 * self.weight

    def rest(self):
        if (self.strength < self.maxStrength):
            self.strength += 0.5

    # 采摘并进食
    def getFood(self, target):
        if target.isPickable and self.maxStrength > target.diff:
            self.health += (self.health < self.maxHealth) * target.healthRecoveryAmount
            self.hunger += (self.hunger < self.maxHunger) * target.hungerRecoveryAmount
            self.strength -= target.diff
            target.isPickable = False

    # 投喂他人
    # ToDO

    # 人类行为决策
    def target(self): 
        # actions = [self.getFood, self.feedOther]
        # objects = self.getObject(r=1)
        return

    # 人生得分
    def score(self):
        return self.age + self.sonNum


class Berry:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.isPickable = True
        self.healthRecoveryAmount = 0.3
        self.hungerRecoveryAmount = 0.5
        self.height = rd.uniform(1.0, 1.3)
        self.refTime = 0
        self.diff = 0.5

    def refresh(self):
        self.isPickable = True
        self.refTime = 7