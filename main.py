class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def __init__(self, *args, **kwargs):
    self.wheels
    self.doors
    self.windows
    self.seats
    self.color = kwargs.get("color", "Black")
    self.price = kwargs.get("price", "$20")
    
  def __str__(self):
    return f"Car with {self.wheels} wheels"
    
print(dir(Car))

porche = Car(color = "Green", price = "$50")
print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)
