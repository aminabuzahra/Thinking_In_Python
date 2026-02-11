# built in decorators @prporty and @xxxxxxx.setter
# ============================

class Student:
    def __init__(self, name, mark):
        self._name = name
        self._secret = mark
    
    @property # getter
    def mark(self):
        return self._secret
    
    @mark.setter
    def mark(self, new_mark):
        self._secret = new_mark
    
subhi = Student("Subhi", 50)

subhi.mark = 98.7

print(subhi.mark)

