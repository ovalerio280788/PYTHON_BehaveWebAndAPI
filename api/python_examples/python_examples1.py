print("\n\n**************************************************************************************************")
print("*\t\tIF STATEMENT EXAMPLES")
print("**************************************************************************************************")
print("\tEXAMPLE #1")
a = 200
b = 33
if b > a:
    print("\t\t|- b is greater than a")
elif a == b:
    print("\t\t|- a and b are equal")
else:
    print("\t\t|- a is greater than b")

print("\tEXAMPLE #2")
print("\t\t|- A") if a > b else print("\t\t|- B")

print("\tEXAMPLE #3")
a = 330
b = 330
print("\t\t|- A") if a > b else print("\t\t|- =") if a == b else print("\t\t|- B")

print("\tEXAMPLE #4")
a = 200
b = 33
c = 500
if a > b and c > a:
    print("\t\t|- Both conditions are True")

print("\tEXAMPLE #5")
if a > b or a > c:
    print("\t\t|- At least one of the conditions is True")

print("\tEXAMPLE #6")
x = 41
if x > 10:
    print("\t\t|- Above ten,")
    if x > 20:
        print("\t\t|- and also above 20!")
    else:
        print("\t\t|- but not above 20.")

print("\n\n**************************************************************************************************")
print("*\t\tDICTIONARIES STATEMENT EXAMPLES")
print("**************************************************************************************************")
print("\tEXAMPLE #1")
dict01 = dict(name="oscar", lastname="valerio", gender="M")
print("\t\t|- {}".format(dict01))

print("\tEXAMPLE #2")
print(f"\t\t|- {dict01.keys()}")
print(f"\t\t|- {dict01.items()}")
print(f"\t\t|- {dict01.values()}")
print(f"\t\t|- {dict01['name']}")
print(f"\t\t|- {dict01['lastname']}")

print("\n\n**************************************************************************************************")
print("*\t\tFOR STATEMENT EXAMPLES")
print("**************************************************************************************************")
print("\tEXAMPLE #1")
arr = ["a", "b", "c", "d"]
for a in arr:
    print("\t\t|- %s" % a)
print("\t\t|- " + ",".join(arr))

print("\tEXAMPLE #2")
print("\t\t|- {0}".format([a for a in dict01.keys()]))
