def split_and_join(line):
    return line.split(" ")

if __name__ == '__main__':
    line = input()
    result = "-".join(split_and_join(line))
    print(result)