import re

#1
p = r"ab*"
s = input("Enter a string: ")
if re.fullmatch(p, s):
    print("Match")
else:
    print("No match")

#2
p = r"ab{2,3}"
s = input("Enter a string: ")
if re.fullmatch(p, s):
    print("Match")
else:
    print("No match")

#3
s = input("Enter a string: ")
p = r"\b[a-z]+(?:_[a-z]+)+\b"
matches = re.findall(p, s)
print(matches)

#4
s = input()
p = r"\b[A-Z][a-z]+\b"
print(re.findall(p, s))

#5
s = input()
pattern = r"a.*b"
print("Match" if re.fullmatch(pattern, s) else "No match")

#6
s = input()
print(re.sub(r"[ ,\.]", ":", s))

#7
s = input().strip()
parts = re.split(r"_+", s)
camel = parts[0] + "".join(p.capitalize() for p in parts[1:] if p)
print(camel)

#8
s = input().strip()
print(re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])", s))

#9
s = input().strip()
print(re.sub(r"(?<!^)(?=[A-Z])", " ", s))

#10
s = input().strip()
snake = re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()
print(snake)