def common_elements():
    list_3 = [x for x in range(100) if x % 3 == 0]
    list_5 = [x for x in range(100) if x % 5 == 0]

    set_3 = set(list_3)
    set_5 = set(list_5)
    return set_3 & set_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, "Test failed!"
print("ОК")
