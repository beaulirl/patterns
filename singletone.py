class MetaSingletone(type):

    def __call__(cls, *args, **kwargs):
        print('Metaclass returns class')
        class_instance = cls.__new__(cls, args)
        cls.__init__(class_instance, args[0])
        return class_instance


class Singletone(metaclass=MetaSingletone):
    instance = None
    value = None

    def __init__(self, value):
        print('Initialization of the class')
        if not self.value:
            self.__class__.value = value
        # else:
        #     self.value = self.__class__.value

    def __new__(cls, args):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            print(cls.__class__)
            print('Create instance for the first time')
        return cls.instance


a = Singletone(5)
b = Singletone(6)
c = Singletone(7)
print(a, a.value, 'a')
print(b, b.value, 'b')
print(c, c.value, 'c')

if a is b:
    print('Singletone success')
