class parent:
    def m1(self):
        print("inside parent")

class child(parent):
    def m2(self):
        print("inherit parent")

class subchild(child):
    def m3(self):
        print("inherit child")

ch=subchild()
ch.m1()
ch.m2()
ch.m3()
