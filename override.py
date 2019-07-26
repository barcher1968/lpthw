class Parent(object):

    def override(self):
        print("PARENT Override()")

class Child(Parent):

    def override(self):
        print ("Child Override()")

dad = Parent()
son = Child()

dad.override()
son.override()

