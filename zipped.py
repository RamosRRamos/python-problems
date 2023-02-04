# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':


    x = input()
    lines, column = int(x.split(' ')[0]), int(x.split(' ')[1])

    students = []

    for t in range(column):
        students.append(input())

    for t in range(len(students)):
        students[t] = students[t].split()
        for x in range(len(students[t])):
            students[t][x] = float(students[t][x])


    student_zip = list(zip(*students))

    for student in student_zip:
        value = sum(student) / column
        print(value)


