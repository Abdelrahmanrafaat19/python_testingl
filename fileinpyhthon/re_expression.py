import re

file = open("hello238649.txt", "r")
syring = file.read()
print(syring)
first_search = re.findall("[A-z\_| -| .]+@[A-z0-9]+\.com", syring)
print(len(first_search))
result_list = []
if first_search:
    result_list.extend(first_search)
    print(f"the list is Added")
else:
    print("not Found Any Email Match This Pattern")

for couner, email in enumerate(result_list, 1):
    print(f"The Counter =>{couner} the value=>{email}")
# ------------------------------------------- SPLIT IN RE-----------------------
filell = re.sub("Email", "OMML", syring)
print(filell)
