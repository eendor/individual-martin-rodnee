students = ["Mary", "Matthew", "Tom", "Anna", "Thomas"]
grades = [100, 85, 88, 90, 75]

for i in range(len(students)):
    print(f"The grade of {students[i]} is {grades[i]}")

car = {
    "brand": "Toyota",
    "model": "Vios",
    "year of make": 2015,
    "color": "Black"
}

print(f"I own a {car['brand']} {car['model']}, and it was made in {car['year of make']}")

def get_square(num):
    return num ** 2

print(get_square(5))
