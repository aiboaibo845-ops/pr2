class a:
    def __init__(self, b):
        self.b = b

class c(a):
    def __init__(self, b, d):
        super().__init__(b)
        self.d = d

x = c("Buddy","Dog")
print(x.b, x.d)
