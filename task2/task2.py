def get_cats_info(path): 
    list_of_cats = []
    try:
        with open(path, "r", encoding = "utf-8") as file:
            while True:
                cat = file.readline().strip()
                if cat == "":
                    break
                splitted_cat = cat.split(",")
                cat_data = {
                    "id": splitted_cat[0],
                    "name": splitted_cat[1],
                    "age": splitted_cat[2]
                }
                list_of_cats.append(cat_data)
    except FileNotFoundError:
            print("File doesn't exist")
    print(list_of_cats)
    return list_of_cats

get_cats_info("/Users/lilitkravchenko/my_repo/homework_2/goit-pycore-hw-04/task2/cats.txt")