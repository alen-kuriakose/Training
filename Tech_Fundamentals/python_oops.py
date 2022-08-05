
class Cars():
    def __init__(self, modelname, yearm, price):
        self.modelname = modelname
        self.yearm = yearm
        self.price = price

    def price_inc(self):
        self.price = int(self.price*1.5)


class Supercar(Cars):
    def __init__(self, modelname, yearm, price):
        super.__init__(modelname, yearm, price)
        # self.cc = cc


honda = Supercar("city", 2010, 200000)
honda.cc=1200
print(honda.__dict__)
honda.price_inc()
print(honda.price)
