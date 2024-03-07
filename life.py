import random as rd

class Human:
    # 初始属性
    age = 0
    hug = 0
    height = 0
    weight = 0
    phy = 0
    sonNum = 0


    def __init__(self, id, Father = None, Mother = None):
        self.id = id
        self.hug = 1.5
        self.gender = rd.randint(0, 1)
        self.Father = Father
        self.Mother = Mother
        
        if Father != None and Mother != None:

            # 基因遗传
            self.life = (Father.life + Mother.life) / 2
            self.height_B = (0.4 * Father.height_B + 0.6 * Mother.height_B) + rd.uniform(-0.2, 0.05)*(Father.height_B + Mother.height_B)
            self.weight_B = (0.6 * Father.weight_B + 0.4 * Mother.weight_B) + rd.uniform(-0.2, 0.05)*(Father.weight_B + Mother.weight_B)
            self.phy_B = (0.4 * Father.phy_B + 0.6 * Mother.phy_B) + rd.uniform(-0.15, 0.15)*(Father.phy_B + Mother.phy_B)

            # 祖先递归somNum++
            An0 = Father
            An1 = Mother

            while An0.id != 0:
                An0.sonNum += 1
                An0 = An0.Father

            while An1.id != 0:
                An1.sonNum += 1
                An1 = An1.Mother

    # 人类成长
    def grow(self):
        self.age += 1/30
        if self.age <= 22:
            self.height += self.height_B / self.life + self.hug / (self.hug+1) * rd.uniform(0.1, 0.125)
        self.weight += self.weight_B / self.life + self.hug / (self.hug+1) * rd.uniform(0.1, 0.125)
        self.phy += self.phy_B / self.life + self.hug / (self.hug+1) * rd.uniform(-0.05, 0.1)

    # 采摘并进食
    def getFood(self, target):
        if target.isPickable:
            self.hug += target.hugVal
            self.phy -= target.diff
            target.isPickable = False

    # 投喂他人
    def feed(self, person, value):
        self.phy -= value * 0.1
        self.hug -= value * 1.05
        person.hug += value

    def target(self):
        return

    # 人生得分
    def score(self):
        return self.age + self.sonNum
    
# 人类繁衍
def reproduce(Father, Mother):
    global id
    id += 1
    return Human(id, Father, Mother)

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

class berry:
    def __init__(self):
        self.isPickable = True
        self.hugVal = 1
        self.height = rd.uniform(1.0, 1.3)
        self.refTime = 0
        self.diff = 0.5

    def refresh(self):
        self.isPickable = True
        self.refTime = 7