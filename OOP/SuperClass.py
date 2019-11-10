class Base:
    def method(self):
        print('Base method invoked on ' + type(self).__name__, 'instance')

class Child(Base):
    def method(self):
        super(Child, self).method() # python 3 without anything in super function
        print('Child method invoked on ', type(self).__name__, 'instance ')

child = Child()
child.method()