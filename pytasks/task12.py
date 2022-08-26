if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(0,N):
        go = input().split()
        if go[0] == "print":
            print(list)
        elif go[0] == "insert":
            list.insert(int(go[1]),int(go[2]))
        elif go[0] == "remove":
            list.remove(int(go[1]))
        elif go[0] == "append":
            list.append(int(go[1]))
        elif go[0] == "pop":
            list.pop()
        elif go[0] == "sort":
            list.sort()
        elif go[0] == "reverse":
            list.reverse()   