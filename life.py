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
        self.hug = 0
        self.height = 0
        self.weight = 0
        self.strength = 0
        self.sonNum = 0

        self.id = id
        self.hug = 1.5
        self.gender = rd.randint(0, 1)
        self.Father = Father
        self.Mother = Mother
        
        if Father != None and Mother != None:
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
        self.age += 1/30
        if self.age <= 22:
            self.height += self.height_B / 22 / 30 + self.hug / (self.hug+1) * rd.uniform(0.005, 0.010) * self.height_B
        self.weight += self.weight_B / self.life + self.hug / (self.hug+1) * rd.uniform(0.1, 0.125)
        self.strength += self.strength_B / self.life + self.hug / (self.hug+1) * rd.uniform(-0.05, 0.1)

    # 采摘并进食
    def getFood(self, target):
        if target.isPickable:
            self.hug += target.hugVal
            self.strength -= target.diff
            target.isPickable = False

    # 投喂他人
    def feed(self, person, value):
        self.strength -= value * 0.1
        self.hug -= value * 1.05
        person.hug += value

    def target(self):
        return

    # 人生得分
    def score(self):
        return self.age + self.sonNum


Adam = Human(id = 1, time = 0, x = 0, y = 0)
Eva = Human(id = 0, time = 0, x = 0, y = 0)

Adam.gender = 1
Adam.life = 100
Adam.height_B = 1.8
Adam.weight_B = 70
Adam.strength_B = 0.8
Adam.age = 22
Adam.height = 1.8
Adam.weight = 70
Adam.strength = 0.8

Eva.gender = 0
Eva.life = 100
Eva.height_B = 1.6
Eva.weight_B = 50
Eva.strength_B = 0.6
Eva.age = 22
Eva.height = 1.6
Eva.weight = 50
Eva.strength = 0.6

class berry:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isPickable = True
        self.hugVal = 1
        self.height = rd.uniform(1.0, 1.3)
        self.refTime = 0
        self.diff = 0.5

    def refresh(self):
        self.isPickable = True
        self.refTime = 7