from collections import deque

for t in range(10):
    n = int(input())
    original = list(map(int, input().split()))
    command_cnt = int(input())
    command = [[] for _ in range(command_cnt)]
    tmp = deque(input().split())

    i = -1
    while i != command_cnt:
        if len(tmp) == 0:
            break

        if tmp[0] == "I":
            tmp.popleft()
            i += 1
        else:
            command[i].append(tmp[0])
            tmp.popleft()

    # 명령어 개수만큼 실행
    for i in range(len(command)):
        x = int(command[i][0])
        y = int(command[i][1])
        s = command[i][2:]
        for j in range(y):
            original.insert(x, int(s[j]))
            x += 1

    print(f"#{t+1} ", end="")
    print(*original[:10])
