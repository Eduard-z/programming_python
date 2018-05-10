from chapter_1 import db
import pickle

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()

dbfile = open('people-pickle', 'rb')
pickle.load(dbfile)
for key in db:
    print(key, '=>\n', db[key])

import shelve
dbfile = shelve.open('people-shelve')
dbfile['bob'] = db['bob']
dbfile['sue'] = db['sue']
dbfile.close()

dbfile = shelve.open('people-shelve')
for key in dbfile:
    print(key, '=>\n', dbfile[key])
dbfile.close()

dbfile = shelve.open('people-shelve')
sue = dbfile['sue']                         # извлекает объект sue
sue['pay'] *= 1.50
dbfile['sue'] = sue                         # изменяет объект sue
dbfile['tom'] = db['tom']                   # добавляет новую запись
dbfile.close()
