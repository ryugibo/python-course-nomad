class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start(self):
    print(self, self.color)
    print("I started")

  def hello():
    print("Hi!")

porche = Car()
porche.color = "Red"
print(porche)
porche.start()

Car.hello()
