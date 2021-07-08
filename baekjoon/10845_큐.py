from collections import deque
import sys

n = int(sys.stdin.readline())
dq = deque()

for _ in range(n):
    try:
        # sys.stdin.readline() 사용 시 개행 문자 포함됨
        cmd = sys.stdin.readline().strip()
        if cmd[:2] == "pu":
            dq.append(int(cmd.split()[1]))
        elif cmd == "pop":
            print(dq.popleft())
        elif cmd == "size":
            print(len(dq))
        elif cmd == "empty":
            if len(dq) == 0:
                print(1)
            else:
                print(0)
        elif cmd == "front":
            print(dq[0])
        elif cmd == "back":
            print(dq[-1])
    except Exception:
        print(-1)
