
loo = "aa34"
lee = "bree"
c = ","
loo += lee
loo += c
loo = loo.split()
print(loo)
beeboo = [["Bee,34"]]
broro = ["Bro,45"]
beeboo.append(loo)

lala = []

print(beeboo)
lost = list(map(tuple, beeboo))

print(lala[list(map(tuple, beeboo))])