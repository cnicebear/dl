with open("../src/covid19_day_wise.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

covid = {
    "date": [],
    "data": [],
    "header": [h for h in data[0].strip().split(",")[1:]]
}
for row in data[1:]:
    split_row = row.strip().split(",")
    covid["date"].append(split_row[0])
    covid["data"].append([float(n) for n in split_row[1:]])
# print(data[1].strip())
# print(type(data[1].strip()))
# print(data[1].strip().split(","))
# 获取 2020 年 2 月 3 日的所有数据
print(covid["data"][covid["date"].index('2020-02-03')])
# 2020 年 1 月 24 日之前的累积确诊病例有多少个？
total = 0
index = covid["date"].index('2020-01-24')
total = covid["data"][index][0]
print(total)
# 2020 年 7 月 23 日的新增死亡数是多少？
# 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
# 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
# 画图展示新增确诊的变化曲线
# 画图展示死亡率的变化曲线
