# 正在施工中！！

# About Terra

## 世界观

- 时间刻度：30天为一年
- 地形难度（耐力流失速度加成）

## 人类

### 基因

- 寿命：`life`
- 性别：`gender`
- 基础身高：`height`
- 基础体重：`weight`
- 基础行动点：`movement`

### 属性

- 年龄：`age` 年龄到达寿命的20%时为成年
- 身高：`height`
- 体重：`weight`
- 耐力上限：`maxStrength`
- 血条上限：`maxHealth`
- 饥饿值上限：`maxHunger`
- 耐力：`strength`
- 血条：`health`
- 饥饿值：`hunger`

### 行为

对于每个行为，必须定义消耗的耐力，并对phy进行更改

- 休息：`rest()` 即什么也不做，可恢复耐力值
- 投喂：`feed()` 实际效果为将饥饿值分给他人
- 觅食：`getFood()` 指主动采摘食物并直接食用
- 影响：`influ()` 指属性值被周围人属性值影响（未成年的被影响范围增加100%）

## 植物

- 血量回复值：`healthRecoveryAmount`
- 饥饿回复值：`hungerRecoveryAmount`
- 刷新周期：`refTime`
- 采摘难度：`diff` 即采摘所需消耗的耐力