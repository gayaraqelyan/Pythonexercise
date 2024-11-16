# ------------------------------------------Exercise 1 ----------------------------------------------------------------
from builtins import input

# Create a string made of the middle three characters

# def middle_chars(strData):
#     print(strData)
#
#     mi = int(len(strData) / 2)
#
#     output = strData[mi - 1:mi + 2]
#     print(output)
#
#
# middle_chars("ankrfhrgfna")


# ------------------------------------------Exercise  2 --------------------------------------------------------------
# Write a Python program to add "ing" at the end of a given string
# def add_string(str1):
#    length=len(str1)
#    if length>2:
#         if str1[-3:]=='ing':
#            str1+="ly"
#         else:
#             str1+="ing"
#    return str1
# print(add_string("ab"))
# print(add_string("abc"))
# print(add_string("string"))


# --------------------------------------------Exercise 3 ----------------------------------------------------------------
# Write a Python script that thakes input from the user and display that input back in upper and lower cases.
# Word = input("Enter the number  ")
# print(Word.upper())
# print(Word.lower())

# ------------------------------------------------Exercise 4 ----------------------------------------------------------
# Write a Python program to remove the n th index character from a nonempty string
# Version 1
#Word = input("Enter the word   ")
#n =3
# str=Word.replace(Word[n],"")
# print(str)


# Version 2
#str1=list(Word)
# del str1[n]
# print('   '.join(str1))