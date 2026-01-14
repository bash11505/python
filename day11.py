#stack
stack = []

def push(x):
    stack.append(x)
    print(x, "pushed")

def pop():
    if not stack:
        print("Stack is empty")
    else:
        print(stack.pop(), "popped")

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

push(10)
push(20)
push(30)
peek()
pop()
peek()

#2nd programme
s = input("Enter a string: ")
stack = []

for ch in s:
    stack.append(ch)

rev = ""
while stack:
    rev += stack.pop()

print("Reversed string:", rev)
