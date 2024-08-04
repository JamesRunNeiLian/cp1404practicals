from prac_09.unreliable_car import UnreliableCar

car1 = UnreliableCar("Mostly Good", 100, 90)
car2 = UnreliableCar("Dodgy", 100, 9)
car1.drive(40)
car2.drive(80)
print(car1)
print(car2)