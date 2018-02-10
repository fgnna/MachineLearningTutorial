class Parent:
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print (self.last_name)
        print (self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print (self.last_name)
        print (self.number_of_toys)
        print (self.number_of_toys)


billy_cyrus = Child("Cyrus", "blue", 3)
billy_cyrus.show_info()
