class NewType(object):
    def __init__(self, datainput1, datainput2, datainput3):
        self.data1 = datainput1
        self.data2 = datainput2
        self.data3 = datainput3

NewType.data1 = 1
NewType.data2 = 'Visali'
NewType.data3 = 2026

print(NewType.data1)
print(NewType.data2)
print(NewType.data3)
