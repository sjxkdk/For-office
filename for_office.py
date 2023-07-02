lis_all = list(input().split()) #输入所有人的名单
lis_1 = list(input().split()) #输入签到了的人的名单
for i in range(0,len(lis_1)): #把每个在 lis_1 中出现的人从 lis_all 中删除。
 if lis_1[i] in lis_all: #判断在不在 lis_1 里
 lis_all.remove(lis_1[i]) #在就从 lis_all 中删了
 else:
 continue
print(*lis_all)
