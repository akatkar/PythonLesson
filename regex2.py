import re

pattern = re.compile("aa(\d+)*bb(\d+)*cc")

line = "aa1234bb4567cc"

match_object = pattern.search(line)
if match_object:
    val1, val2 = match_object.group(1,2)
    print(val1, ",",val2)
else:
    print("no match")
