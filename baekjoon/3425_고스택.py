def execute(cmds, num):
    stk = [num]
    for cmd in cmds:
        try:
            if cmd[0] == 'N':
                stk.append(int(cmd.split()[1]))
            elif cmd == "POP":
                stk.pop()
            elif cmd == "INV":
                stk[-1] = -stk[-1]
            elif cmd == "DUP":
                stk.append(stk[-1])
            elif cmd == "SWP":
                temp = stk[-1]
                stk[-1] = stk[-2]
                stk[-2] = temp
            elif cmd == "ADD":
                a = stk.pop()
                b = stk.pop()
                res = a + b
                if abs(res) > 10**9:
                    raise Exception
                stk.append(res)
            elif cmd == "SUB":
                a = stk.pop()
                b = stk.pop()
                res = b - a
                if abs(res) > 10**9:
                    raise Exception
                stk.append(res)
            elif cmd == "MUL":
                a = stk.pop()
                b = stk.pop()
                res = a * b
                if abs(res) > 10**9:
                    raise Exception
                stk.append(res)
            elif cmd == "DIV":
                a = stk.pop()
                b = stk.pop()
                if (a > 0 and b < 0) or (a < 0 and b > 0):
                    res = -(abs(b) // abs(a))
                else:
                    res = b // a
                if abs(res) > 10**9:
                    raise Exception
                stk.append(res)
            elif cmd == "MOD":
                a = stk.pop()
                b = stk.pop()
                if b < 0:
                    res = -(abs(b) % abs(a))
                else:
                    res = abs(b) % abs(a)
                if abs(res) > 10**9:
                    raise Exception
                stk.append(res)
        except:
            return "ERROR"

    if len(stk) != 1:
        return "ERROR"

    return stk[0]

answer = []
done = False

while True:
    # 명령어 입력
    cmds = []
    while True:
        cmd = input()
        if cmd == "QUIT":
            done = True
            break
        if cmd == "END":
            break
        cmds.append(cmd)
    if done:
        break

    # 숫자 입력
    n = int(input())
    for _ in range(n):
        num = int(input())
        answer.append(execute(cmds, num))
    
    # 공백
    input()
    answer.append("")

answer.pop()
for i in answer:
    print(i)
