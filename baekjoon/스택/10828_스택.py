import sys

n = int(sys.stdin.readline())  # int 씌우면 개행문자 제거됨
stk = []

for _ in range(n):
    cmd = sys.stdin.readline().strip()  # 끝에 개행문자 제거
    a = cmd.split()
    if len(a) > 1:
        stk.append(a[1])
    else:
        if cmd == 'pop':
            if stk:
                print(stk.pop())
            else:
                print(-1)
        elif cmd == 'size':
            print(len(stk))
        elif cmd == 'empty':
            if stk:
                print(0)
            else:
                print(1)
        elif cmd == 'top':
            if stk:
                print(stk[-1])
            else:
                print(-1)
