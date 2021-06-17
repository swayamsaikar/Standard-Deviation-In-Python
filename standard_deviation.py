import csv
import math

with open('data.csv', newline="") as f:
    rawData = csv.reader(f)
    # Then In order To Perform operations we have to convert this csv data into an array
    listData = list(rawData)
    listData = listData[0]
    # print(listData)

numAdd = 0

for num in listData:
    # print(num)
    # Now we have to get the sum of all the numbers in this array
    # currently in this array all the elements are strings so i have to convert it into integers
    numAdd = numAdd+int(num)

# print(numAdd)

# total numbers of items in the listData array
totalItems = len(listData)

# Mean -> totalSum / numberOfItems
mean = numAdd/totalItems
print(f"The mean value is :{mean}")

# Now we have to find the standard Deviation

# First We have to square all the numbers in this listData Array
squares = []

for n in listData:
    # print(n)
    # first we have to divide each of the numbers to our mean value
    nm = int(n)-mean

    # then i have to square each of the numbers
    nm = nm**2

    # Then we have to store it in an array
    squares.append(nm)

# Then we have to find the sum of all the numbers in the squares array and divide it by length of listData -1

sum = 0

for i in squares:
    # print(i)
    sum = sum+i

# print(sum)

result = sum/(len(listData)-1)

# And Then we have to find the sqrt of the result variable using math module

deviation = math.sqrt(result)

print(f"Deviation Is {deviation}")

# ** NOT COPIED ANYTHING MAM **
