class MyDataDescriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('data descriptor get')
        return self.value

    def __set__(self, instance, value):
        self.value = value


class MyNotDataDescriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('non-data descriptor get')
        return self.value


class MyMetaClass(type):

    # x = MyDataDescriptor(7)

    y = MyNotDataDescriptor(8)


class MyClass(metaclass=MyMetaClass):

    x = MyDataDescriptor(8)


print(MyClass.x)

