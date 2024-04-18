while True:
    try:
        num, stack, res = list(input()), [], ""
        for i in num:
            stack.append(i)
        for _ in range(len(num)):
            res+=stack.pop()
        print("YES" if res=="".join(num) else "NO")
    except:break