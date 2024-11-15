# Write a program to print the following  number pattern using a loop.
# num=int(input("Enter the number  "))

# for i in range(1,num+1):
#    for j in range(1,i+1):
#        print(j, end=" ")
#    print()

# -----------------------------------------------------------------------------------------------------------------------
# Display numbers from a list using a loop.
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# if the number is greater than 150, then it and move to next number
# if the number greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#    if i > 500:
#       break
#   if i > 150:
#       continue
#   if i %5==0:
#        print(i)
# ----------------------------------------------------------------------------------------------------------------------

# Write a program to count the total number of digits in a number using a while loop.
# num = int(input("Enter the number "))
# count = 0
# while num != 0:
#    num //= 10
#    count += 1
# print(count)

# -----------------------------------------------------------------------------------------------------------------------
# Print the following pattern
# Use two for loops.First for loop to print the upper pattern and second for loop to print lower pattern
# numbers = int(input("Enter the number  "))

# First for loop to print the upper pattern
# for i in range(1, numbers + 1):
# print("*" * i)
# Second for loop to print lower pattern
# for i in range(numbers - 1, 0, -1):
#    print("*" * i)

# -----------------------------------------------------------------------------------------------------------------------
#  Create new dict from another
#  Write Python program to find the length of a given dictionary values.

# def test(dict):
#   result = {}
#   for val in dict.values():
#         result[val] = len(val)
#     return result


# OriginalDict = {1: "red",
#                 2: "green",
#                 3: "black",
#                 4: "white",
#                5: "black"}
# print("Original Dictionary: ", OriginalDict)
# print("Length of dictionary values: ", test(OriginalDict))





