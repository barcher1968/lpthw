class Parent(object):

    def altered(self):
        print("PARENT Altered()")

class Child(Parent):

    def altered(self):
        print("CHild before parent altered()")
        super(Child, self).altered()
        print("CHild, after Parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()