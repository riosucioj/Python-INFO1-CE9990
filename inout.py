"""
Program to determine how many days dog food will last

"""

dogs = input("How many dogs do you have human? ")
try:
    d = float(dogs)
except ValueError:
    print("Sorry,", dogs, "is not a number")
    d = 0
    print("I'll assume you wanted to type ", d, ".", sep = "")

times = input("How many times do you feed your dog(s) per day? ")
try:
    t = float(times)

except ValueError:
    print("Sorry,", times, "is not a number")
    t = 0
    print("I'll assume you wanted to type ", t, ".", sep = "")

cups = input("How many cups of food do you give each dog(s) at each meal? ")
try:
    c = float(cups)
except ValueError:
    print("Sorry,", cups, "is not a number")
    c = 0
    print("I'll assume you wanted to type ", c, ".", sep = "")

"""
large dog food bag is 25 lbs and 4 cups of dog food equal 1 lb
"""

total = d * t * c
days = (25 * 4)/total

print("Your dog(s) will consume ", total, " cups on a daily basis", sep = "")
print("Assuming you purchase a 25 lb bag of dog food that bag will last you ", round(days,), " days.", sep = "")

