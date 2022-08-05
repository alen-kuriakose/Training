class Cars(object):
    def __init__(self, modelname, yearm, price,__avgcarprice):
        self.modelname = modelname
        self.yearm = yearm
        self.price = price
        self.__avgcarprice = 700000

    def price_inc(self):
        self.price = int(self.price*1.5)


class Supercar(Cars):
    def __init__(self, modelname, yearm, price,__avgcarprice,carcc):
        self.carcc = carcc
        Cars.__init__(self,modelname,yearm,price,__avgcarprice)


honda = Supercar("city", 2010, 200000,300000,1200)
print(honda.__dict__)
honda.price_inc()
print(honda.price)
