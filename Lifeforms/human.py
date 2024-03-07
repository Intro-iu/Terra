import random as rd

class Human:
    age = 0
    hug = 0
    movement = 0
    sonNum = 0

    def __init__(self, id, Father, Mother):
        self.id = id
        self.gender = rd.randint(0, 1)
        self.Father = Father
        self.Mother = Mother
        
        # 基因遗传
        self.life = (Father.life + Mother.life) / 2
        self.height_B = (0.4 * Father.height_B + 0.6 * Mother.height_B) + rd.uniform(-0.2, 0.05)*(Father.height_B + Mother.height_B)
        self.weight_B = (0.6 * Father.weight_B + 0.4 * Mother.weight_B) + rd.uniform(-0.2, 0.05)*(Father.weight_B + Mother.weight_B)
        self.movement_B = (0.4 * Father.movement_B + 0.6 * Mother.movement_B) + rd.uniform(-0.15, 0.15)*(Father.movement_B + Mother.movement_B)

        # 初始属性
        self.height = 0
        self.weight = 0
        self.movement = 1

    def grow(self):
        self.age += 1/30
        self.height += self.height_B / self.life + self.hug + rd.uniform(-0.05, 0.1)
        self.weight += self.weight_B / self.life + self.hug + rd.uniform(-0.05, 0.1)
        self.movement += self.movement_B / self.life + self.hug + rd.uniform(-0.05, 0.1)

    def feed(self, person, value):
        # 投喂他人
        self.hug -= value * 1.05
        person.hug += value

    def score(self):
        # 人生得分
        return self.age + self.sonNum