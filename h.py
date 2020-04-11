class hello:
    def __init__(self, x=0, y=0):
        x += y
        print(x)
s = hello()
s.__init__(1 , 4)