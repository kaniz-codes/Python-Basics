class Triangle:
    base=""
    height=""
   def __init__ (self,base,height):
      self.base = base
      self.height = height

  def calculate_area(self):
      area = .5 * self.base *self.height
      print("Area = ",area)


tri1 = Triangle (4,4)
tri1.calculate_area()
