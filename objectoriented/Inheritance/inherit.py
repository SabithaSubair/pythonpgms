class parent:
    def phone(self):
        print("nokia")

    def lap(self):
            print("hp")


class child(parent):
    def bike(self):
        print("duke")
ch=child()
ch.phone()
ch.lap()
ch.bike()
