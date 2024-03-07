# About Terra

## 世界观

- 时间刻度：30天为一年
- 地形难度（生命流失速度加成）

## 人类

### 基因

- 寿命：`life`
- 性别：`gender`
- 基础身高：`height`
- 基础体重：`weight`
- 基础行动点：`movement`

### 属性

- 年龄：`age`
- 身高：`height`
- 体重：`weight`
- 是否饥饿：`isHug`         用于判断能否增长耐力值
- 耐力：`phy`               用于判断是否增长行动点
- 每日行动点：`movement`    为0时原地不动，次日取整恢复
- 速度：`speed`
- 血条：`HP`
- 饥饿值：`hug`

### 行为

- 投喂：`feed()`    实际效果为将饥饿值分给他人
- 觅食：`getFood()` 指主动采摘食物并直接食用
- 影响：`influ()`   指属性值被周围人属性值影响（未成年的被影响范围增加100%）

## 植物

- 饥饿回复值：`hugVal`
- 刷新周期：`refTime`