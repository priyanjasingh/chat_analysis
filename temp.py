import re

regexp = re.compile(r"(.)\1")
data = ["parrot","follia","carrot","mattia","rettoo","melone"]

for str in data:
    match = re.search(regexp, str)
    if match:
        print str, "<- match for double", match.group(1)
    else:
        print str, "<- doesn't match"
