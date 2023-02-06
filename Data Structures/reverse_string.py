import stack

string = "iaS si eman yM"
reversed_string = ""
s = stack.Stack()

for i in string:
    s.push(i)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)