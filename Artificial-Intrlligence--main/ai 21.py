class Monkey:
    def __init__(self):
        self.has_box = False

    def get_box(self):
        self.has_box = True

    def reach_bananas(self):
        if self.has_box:
            print("Monkey reaches the bananas!")
        else:
            print("Monkey needs a box to reach the bananas.")

class Box:
    def __init__(self):
        self.position = "on_floor"

    def move(self, new_position):
        self.position = new_position

# Initialize objects
monkey = Monkey()
box = Box()

# Monkey moves the box
box.move("under_bananas")
monkey.get_box()
box.move("on_top_of_box")
monkey.reach_bananas()
