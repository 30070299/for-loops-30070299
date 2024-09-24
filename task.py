import random

def task_1(): # Lottery ticket generator
    tickets = []

    for _ in range(6):
        tickets.append(random.randint(1, 50))

    return tickets

def task_2(): # Countdown

    output = []

    count = 100
    num = int(input("Please enter a number less than 100: "))

    while count > num:
        output.append(count)
        count -= 1

    else:
        output.append(num)

    return output

def task_3():
    

    people_cars = {
        "Adam": "Volvo",
        "Kate": "BMW",
        "Mark": "BMW",
        "Hannah": "Ford",
        "Max": "Volvo",
        "Celine": "Fiat"
    }

    car_make_lengths = set()

    for i in people_cars.values():
        car_make_lengths.add(len(i))
    
    print(f"There will be {len(car_make_lengths)} different sizes of key rings.")

    return car_make_lengths