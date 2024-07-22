def total_salary(path):
    list = []
    salary = []
    total = 0
    count = 0
    try:
        with open(path, "r", encoding = "utf-8") as file:
            while True:
                text = file.readline().strip()
                if text == "":
                    break
                text_list = text.split(',')
                list.append(text_list)
            for i in list:
                salary.append(i[1])      
            for i in salary:
                total = total + int(i)
                count = count+1
            average_salary = int(total/count)
            global_list = []
            global_list.append(total)
            global_list.append(average_salary)
            print(f"Sum is: {global_list[0]}, Average salary is: {global_list[1]}")
    except FileNotFoundError:
        print("File doesn't exist")
    except ZeroDivisionError:
        print("The file is empty")
    


total_salary("/Users/lilitkravchenko/my_repo/homework_2/goit-pycore-hw-04/task1/salary.txt")