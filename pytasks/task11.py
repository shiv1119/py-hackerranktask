if __name__ == '__main__':
    n = int(input(""))
    if n <= 0 or n >= 10: 
        print("try again")
    student_marks = {}   
    for i in range (n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    count = 0
    for i in student_marks:
        if i == query_name:
            for i in student_marks[i]:
                count += i
    a = count/3
    print("{:.2f}".format(a))

    
    

        