class A:
    def pr(self):
        print("A")
        
class B:
    def pr(self):
        print("B")
        
class C(A,B):
    def pr(self):
        print("C")
        super().pr()

print(C.mro())
c = C()
c.pr()