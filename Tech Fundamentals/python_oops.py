   
class Cars() :   
     def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
class Supercar(Cars):
        pass

honda=Cars("city",2010,100000)
print(honda.__dict__)