import re

targets = ["something <<171>> is here",
           "<<23>> test ",
           "there is nothing"]

pattern = re.compile("<<([\d+])*>>")

for text in targets:
    match_object = pattern.search(text)
    if match_object:
        print(match_object.group(1))
    else:
        print("no match")

