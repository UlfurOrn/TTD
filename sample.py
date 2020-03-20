

def add(numbers):
    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")

    num_list = []
    neg_list = []
    for num in number_list:
        num = int(num)

        if num > 1000:
            num = 0
        elif num < 0:
            neg_list.append(str(num))
        
        num_list.append(num)
    
    if neg_list:
        raise Exception("Negatives not allowed: " + ",".join(neg_list))
    else:
        return sum(num_list)