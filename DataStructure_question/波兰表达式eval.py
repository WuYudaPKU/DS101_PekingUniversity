def cal(s):
    t=s.pop(0)
    if t in "+-*/":
        return str(eval(cal(s)+t+cal(s)))
    else:return t

s=input().split()
print(f"{float(cal(s)):.6f}")

"""
* + 11.0 12.0 + 24.0 35.0
1357.000000
"""