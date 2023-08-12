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
