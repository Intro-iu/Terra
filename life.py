import random as rd

class Human:
    def __init__(self, id, time, x = None, y = None, Father = None, Mother = None):
        if x != None and y != None:
            self.x = x
            self.y = y
        # 初始属性
        self.id = id
        self.age = 0
        self.birthday = time
        self.maxHealth = 5
        self.maxHunger = 3
        self.height = 0
        self.weight = 0
        self.maxStrength = 0

        self.health = 5
        self.hunger = 3
        self.strength = 0
        self.sonNum = 0

        
        if Father != None and Mother != None:
            self.id = id
            self.gender = rd.randint(0, 1)
            self.Father = Father
            self.Mother = Mother
            self.x = Mother.x + rd.uniform(-0.1, 0.1)
            self.y = Mother.y + rd.uniform(-0.1, 0.1)

            # 基因遗传
            self.life = (Father.life + Mother.life) / 2
            self.height_B = (0.4 * Father.height_B + 0.6 * Mother.height_B) + rd.uniform(-0.2, 0.05)*(Father.height_B + Mother.height_B)
            self.weight_B = (0.6 * Father.weight_B + 0.4 * Mother.weight_B) + rd.uniform(-0.2, 0.05)*(Father.weight_B + Mother.weight_B)
            self.strength_B = (0.4 * Father.strength_B + 0.6 * Mother.strength_B) + rd.uniform(-0.15, 0.15)*(Father.strength_B + Mother.strength_B)

            # 祖先递归sonNum++
            # ToDO

    # 人类成长
    def grow(self):
        self.age += 1/25
        if self.age <= 22:
            self.height += self.height_B / 22 / 30 + self.maxHunger / (self.maxHunger+1) * rd.uniform(0.005, 0.010) * self.height_B
        self.weight += self.weight_B / 22 / 30 + self.maxHunger / (self.maxHunger+1) * rd.uniform(0.1, 0.125)
        self.maxHunger = 0.1 * self.weight
        self.maxStrength += self.strength_B / 22 / 30

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


Eva = Human(id = 0, time = 0, x = 0, y = 0)
Adam = Human(id = 1, time = 0, x = 0, y = 0)

Eva.gender = 0
Eva.life = 100
Eva.height_B = 1.6
Eva.weight_B = 50
Eva.strength_B = 0.6
Eva.age = 22
Eva.height = 1.6
Eva.weight = 50
Eva.maxStrength = 0.8
Eva.strength = 0.8

Adam.gender = 1
Adam.life = 100
Adam.height_B = 1.8
Adam.weight_B = 70
Adam.strength_B = 0.8
Adam.age = 22
Adam.height = 1.8
Adam.weight = 70
Adam.maxStrength = 1
Adam.strength = 1

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