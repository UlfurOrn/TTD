

def add(numbers):
    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")

    num_list = []
    for num in number_list:
        num = int(num)

        if num > 1000:
            num = 0
        
        num_list.append(num)
    
    return sum(num_list)