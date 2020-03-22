

def add(number_str):
    if number_str == "":
        return 0
    
    delimiter = ","

    if number_str[:2] == "//":
        delimiter = number_str[2]
        number_str = number_str[4:]

    number_str = number_str.replace("\n", delimiter)
    number_str_list = number_str.split(delimiter)

    number_list = []
    negative_list = []
    for num in number_str_list:
        num = int(num)

        if num > 1000:
            num = 0
        elif num < 0:
            negative_list.append(str(num))
        
        number_list.append(num)
    
    if negative_list:
        raise Exception("Negatives not allowed: " + ",".join(negative_list))
    else:
        return sum(number_list)