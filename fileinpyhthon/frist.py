# =============================ZIP() and DECORATOR++++++++++++++++
from datetime import datetime


def zipDecoretion(func):
    def innterFunc(*params):
        print("the is the First Before Decoration")
        func(*params)
        print("this is the first After Decoration")

    return innterFunc


@zipDecoretion
def funcWrppwr(*parames):
    for ls, tp, st, key in zip(*parames):
        print(
            f"From List->{ls},FromSet->{st},FromTuplr->{tp}\n =>the key is ->{key} and the value is->{dicfir[key]}"
        )


listFirst = [1, 23, 5568.5, 58]
tuplefirst = (235, 523, 564, "AbelRahmandkldjjdlkdShoainb")
setFirst = {1253, 5465, 2254, 4744, 4}
dicfir = {
    "name": "AbdelrahmanShoaib",
    "lastName": "RaafatShoaib",
    "age": "Twinty Two",
    "birthDate": datetime(
        2001,
        9,
        21,
    ),
}
# for ls, tp, st, key in zip(listFirst, tuplefirst, setFirst, dicfir):
#     print(
#         f"From List->{ls},FromSet->{st},FromTuplr->{tp}\n =>the key is ->{key} and the value is->{dicfir[key]}"
#     )
funcWrppwr(listFirst, tuplefirst, setFirst, dicfir)

# ---------------------------------------------R/Expression-----------------------------------------------------------------
# import re

# file = open("hello238649.txt", "r")
# syring = file.read()
# print(syring)
# first_search = re.findall("[A-z\_| -| .]+@[A-z0-9]+\.net|com", syring)
# print(len(first_search))
# result_list = []
# if first_search:
#     result_list.append(first_search)
#     print(f"the list is Added")
# else:
#     print("not Found Any Email Match This Pattern")

# for couner, email in enumerate(result_list, 1):
#     print(f"The Counter =>{couner} the value=>{email}")
#  -----------------------------------------------------------------------------------------------------------------
# from time import time


# def firstDecorator(func):
#     def wrapperFunc():
#         start = time()
#         func()
#         end = time()
#         print(f"The Execution Time is :", {end - start})

#     return wrapperFunc()


# # @firstDecorator
# def mm():
#     """this fun pint Df'fknslkn"""
#     for number in range(1, 10):
#         print(number)


# print(mm.__doc__)

# lisr = [1, 2, 3, 5]
# # mrit = iter(lisr)
# # print(next(mrit))
# # print(next(mrit))
# # print(next(mrit))
# # print(next(mrit))


# def myYeild():
#     yield 1
#     yield 12
#     yield 1
#     yield 13
#     yield 14
#     yield 15
#     yield 154
#     yield 189


# mf = myYeild()

# print(next(mf))
# print(next(mf))
# print(next(mf))
# print(next(mf))
# print(next(mf))
# print(next(mf))
# print(next(mf))
# print(next(mf))
# print(next(mf))
# import map_file
# import functools

# listTest = ["Amdel", "Fileration", "Reducee", "VeryProfional"]
# listTestFiler = [20, 1, 90, 5, 9, 8, 45126, 49, 40, 0.5]

# for text in map(lambda text1: f"MySkills is -> {text1}", listTest):
#     print(text)
# print("#" * 50)
# for number in filter(map_file.filterMethodTest, listTestFiler):
#     print(number, end=" ")

# print("\n", "#" * 50)
# print(
#     "This is Using reduce function -> ",
#     functools.reduce(map_file.reduceMethodTest, listTestFiler),
#     end=" ",
# )
# # listTestFiler = [20, 1, 90, 5, 9, 8, 45126, 49, 40, 0.5]
# print("\n")
# for counter, number in enumerate(reversed(listTestFiler), 1):
#     print(counter, " -> ", number)

# # sumOfList = [210, 3, 20, -50]

# # lsiWithRande = range(100, 201, 10)
# # for number in lsiWithRande:
# #     print(number, end="\\")
# # print("\n")
# # print(
# #     50 * "#",
# # )
# # print("Hello", "Abdelrahman", "shoaib", "in", "Egypt", sep="@", end="\\")
# # print("Hello", "Abdelrahman", "shoaib", "in", "Egypt", sep="@")
# # print(50 * "#")
# # print(abs(-250.23))
# # print("this using POW method", pow(2, 5))
# # print("this using POW method with mod", pow(2, 5, 10))
# # # sumOfList = [210, 3, 20, -50]
# # print("this using MIN method", min(sumOfList))
# # print("this using MAx method", max(sumOfList))
