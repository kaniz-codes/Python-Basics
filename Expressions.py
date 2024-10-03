import re
pattern= r"colour"
if re.search(pattern,"Paint it white colour.I libe brown."):
    print("Match")

else:
    print("Not Matched")
