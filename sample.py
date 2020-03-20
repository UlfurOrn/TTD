

def add(numbers):
    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")

    return sum([int(num) for num in number_list])