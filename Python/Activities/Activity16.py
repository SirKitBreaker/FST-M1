class Car:

    def __init__(self, manufacturer, model, make, transmission, color):
        self.manufacturer = manufacturer
        self.model = model
        self.make = make
        self.transmission = transmission
        self.color = color

    def accelerate(self):
        print(self.manufacturer, self.model, "is moving")

    def stop(self):
        print(self.manufacturer, self.model, "has stopped")


Audi = Car("Audi", "E-tron", "2021", "Automatic", "Black")
Hundai = Car("Hundai", "Creta", "2022", "Manual", "White")
Tata = Car("Tata", "Nexon", "2021", "Automatic", "Red")

Audi.accelerate()
Audi.stop()
Hundai.accelerate()
Hundai.stop()
Tata.accelerate()
Tata.stop()

print("All Done")
