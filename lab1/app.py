# переписать программу так, чтобы добавление нового поля
# не требовало редактирования более 1 места в этой программе

from tkinter import *

class IntEntry:
    def __init__(self, root):
        self.v = IntVar()
        self.e = Entry(root, textvariable=self.v)
        self.e.pack()
    def getVal(self):
        try:
            return self.v.get()
        except:
            return 0

class StrEntry(IntEntry):
    def __init__(self, root):
        self.v = StringVar()
        self.e = Entry(root, textvariable=self.v)
        self.e.pack()

class EntryStore:
    def __init__(self):
        self.entries = []
    def get(self):
        return self.entries
    def addIntEntry(self, root):
        e = IntEntry(root)
        self.entries.append(e)
    def addStrEntry(self, root):
        e = StrEntry(root)
        self.entries.append(e)

root = Tk()
es = EntryStore()

# функция которая печатает содержимое всех полей :P
def f():
    for v in es.get():
        print(v.getVal())

# тут мы можем лишь 1 раз вызвать метод и будет создано поле
es.addIntEntry(root)
es.addIntEntry(root)
es.addStrEntry(root)
es.addStrEntry(root)
es.addStrEntry(root)
es.addStrEntry(root)
es.addStrEntry(root)
es.addStrEntry(root)

l = Label(root, text='Your name, please!!!')
b = Button(root, text='Ok', command=f)

l.pack()
b.pack()

root.mainloop()

