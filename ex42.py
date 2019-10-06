class Animal(object):
    pass

##Dog is-a Animal
    class Dog(Animal):
        def __init__(self,name):
            ##类dog has-a init函数，他接受self，name
            self.name=name
##cat is-a Animal
    class Cat(Animal):
        def __init__(self,name)
