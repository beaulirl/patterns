class Singeltn:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(Singeltn)
        return cls.instance


a = Singeltn()

b = Singeltn()

print(a is b)
