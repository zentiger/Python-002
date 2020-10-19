import abc

class Animal(metaclass=abc.ABCMeta):
    def __init__(self, name, category, size, temper ):
        self.name = name 
        self.category = category
        self.size = size
        self.temper = temper 
        self.dangerous = False
        if self.category == "食肉" and self.size in ["中", "大"] and self.temper == "凶猛":
            self.dangerour = True
    
class Cat(Animal):
    bark = f"Miao ~"
    def __init__(self, name, category, size, temper):
        self.pet = True
        super().__init__(name, category, size, temper)

class Dog(Animal):
    
    pass 

class Zoo(object):
    def __init__(self,name):
        self.name = name 
        self.animals = []
        
    def __getattr__(self,attr):
        self.__setattr__(attr,True)
        return self.__dict__[attr]
        
    def add_animal(self, animal):
        if id(animal) in self.animals:
            print(f"{animal.__class__.__name__}:\"{animal.name}\" is alreay in Zoo:\"{self.name}\"")
            return None
        
        self.animals.append(id(animal))
        animal_type = animal.__class__.__name__
        hasattr(self,animal_type)

	
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)

