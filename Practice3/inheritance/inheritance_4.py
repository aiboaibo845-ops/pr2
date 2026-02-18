class a:
    def b(self):
        print("Animal")

class c(a):
    def b(self):
        print("Woof!")

x = c()
x.b()
