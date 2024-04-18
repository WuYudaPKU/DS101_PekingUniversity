def reverse(s:str):
    return s[::-1]

def f(s):
    stack = []
    for char in s:
        if char == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()  # pop the '('
            stack.extend(temp)
        else:
            stack.append(char)
    return ''.join(stack)

print(f(input()))