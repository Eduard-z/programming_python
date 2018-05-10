bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
people = [bob, sue]                             # ссылки в списке списков
for person in people:
    print(person["name"].split()[-1])                # вывести фамилию
    person["pay"] *= 1.10                           # увеличить оклад на 10%
G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age'])
     for rec in people)
print(G.__next__())

db = {}
db['bob'] = bob                                 # ссылки на словари в словаре
db['sue'] = sue
print([db[key]['name'] for key in db])
print([rec['name'] for rec in db.values()])
db['tom'] = dict(name='Tom', age=50, job=None, pay=0)

print(db)
import pprint
pprint.pprint(db)
