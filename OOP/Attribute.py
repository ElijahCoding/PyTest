class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == 'secret_field' and self.password == '123abc':
            return 'Secret value'
        else:
            return object.__getattribute__(self, item)

obj = MyObject()
print(obj.password)
obj.password = '123abc'
print(obj.password)
print(obj.secret_field)