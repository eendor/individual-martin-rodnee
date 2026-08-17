name = "Rodnee Glen A. Martin"
age = 21
occupation = "Student"
movie = "Interstellar"
rating = 9.3

intro = f"I am {name}, and I am {age} years old, I work as a {occupation}, and my rating for {movie} is {rating}%"
print(intro)

yearToCheck = int(input("Please input a year\n"))

if (yearToCheck % 4 == 0 and yearToCheck % 100 != 0) or yearToCheck % 400 == 0:
    print(f"{yearToCheck} is a leap year!")
else:
    print(f"{yearToCheck} is not a leap year!")
