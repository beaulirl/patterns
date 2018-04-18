class C:
    def getx(self):
        print('getting this value')
        return self.__x

    def setx(self, value):
        print('setting this value')
        self.__x = value

    def delx(self):
        print('deleting this value')
        del self.__x

    x = property(getx, setx, delx)


c = C()
c.x = 7
print(c.x)
del c.x


class StaticMethod:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value


class E:

    x = StaticMethod(5)


print(E.x)
print(E().x)


class ClassMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner=None):
        if owner is None:
            owner = type(instance)

        def newfunc(*args):
            return self.f(owner, *args)
        return newfunc


class E:

    def f(klass, x):
        return klass.__name__, x

    f = ClassMethod(f)


print(E().f(3))
print(E.f(3))



