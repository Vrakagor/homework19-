def common_elements():
    numbers = set()

    for x in range(100):
        if x % 3 == 0 and x % 5 == 0:
            numbers.add(x)
    return numbers


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, "Test failed!"
print("ОК")
