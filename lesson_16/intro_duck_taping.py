class Circle:
    def draw(self):
        print ("Drawing circle")

class Square:
    def draw(self):
        print ("Drawing square")

class Renderer:
    def render(self, drawer):
        drawer.draw()

r = Renderer()

r.render(Circle())
r.render(Square())

