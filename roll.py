import random
num = [1,2,3,4,6,7,8,9,11,13,15,17,22,52]
key = ['玫瑰','表','唇膏','皮带','窗帘','火车','挂历','萝莉','裙子','发卡','头饰','广场','面包','宝剑']
random.shuffle(key)#打乱关键词顺序
test = list(zip(key,num))
random.shuffle(test)
print(test)#最终组合结果
print(len(num))#编码总数
print(len(key))#关键词总数