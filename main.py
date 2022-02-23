class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def __init__(self, **kwargs):
    self.color = kwargs.get("color", "Black")

class Convertible(Car):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.time = kwargs.get("time", 10)

  def take_off(self):
    print("taking off")

  def __str__(self):
    return f"Car with no roof!"

porche = Convertible(color = "Green", price = "$50")
porche.take_off()
print(porche)
print(porche.color, porche.price)
