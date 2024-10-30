def read_and_sort_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines() 

    # remove blankspaces and order
    numbers = [number.strip() for number in numbers]
    numbers.sort()
    
    # print the ordered numbers
    for number in numbers:
        print(number)
    

path = 'extra.txt'
content = read_and_sort_file(path)