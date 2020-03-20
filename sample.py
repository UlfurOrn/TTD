

def add(numbers):
    if numbers == "":
        return 0

    else:
        return sum([int(num) for num in numbers.split(",")])