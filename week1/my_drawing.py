from shapes import Triangle, Rectangle, Oval

rect1 = Rectangle()
rect2 = Rectangle()
oval1 = Oval()
tri1 = Triangle()

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")

rect1.draw()

rect2.set_x(150)
rect2.set_y(150)
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")

rect2.draw()

oval1.randomize()

oval1.draw()

tri1 = Triangle(5, 5, 100, 5, 100, 200)
tri1.set_color("red")

tri1.draw()