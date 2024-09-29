months={"Jan":31,"Feb":28,"Mar":31,"Apr":30,"May":31,"Jun":30,"Jul":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}
print(f"Months dictionary is {months}")
print(f"Month names are {months.keys()}")
print(f"No. of days are{months.values()}")
print("Months with number of days as 31 are :")
for x,y in months.items():
    if y==31:
        print(x)
       
print()       
print("Months with number of days as 30 are :")
for x,y in months.items():
    if y==30:
        print(x)

        