import random
import re

# generate list of nsamples random integer in range 0..7 included
nsamples = 10
data = [random.randrange(0, 8) for i in range(nsamples)]
print("data = ", data)

# Create the string with the following pattern: ```n-…-n```
L = [f"{x}{x*'-'}{x}" for x in data]
print("list = ", L)

# Verify that each string in the list follows the pattern
for s in L:
    m = re.match(r"(\d)(-*)(\d)", s)
    n = int(m.group(1))
    assert len(m.group(2)) == n and int(m.group(3)) == n

# convert to a multi-line string and replace all "00" by "*"
inputstr = "\n".join(L)
print(f"inputstr :\n{inputstr}")
str = re.sub(r"00", r"*", inputstr)
print(f"str :\n{str}")

# Verify that str has the correct pattern
m = re.findall(r"^(\d)(-*)(\d)$|^(\*{1})$", str, re.M)
print(m)
assert len(m) == nsamples
