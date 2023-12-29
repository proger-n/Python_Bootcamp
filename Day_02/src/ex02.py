import ex00


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("SQUEAK")
        res = func(*args, **kwargs)
        return res
    return wrapper


add_ingot = my_decorator(ex00.add_ingot)
get_ingot = my_decorator(ex00.get_ingot)
empty = my_decorator(ex00.empty)


def test_add_ingot(purses_input: list[dict[str, int]]):
    print("TESTING ADD INGOT")
    purses_correct_result = [{"gold_ingots": 1},
                             {"gold_ingots": 2},
                             {"ddd": "eee", "gold_ingots": 1},
                             {"gold_ingots": 3, "ddd": "eee"}]
    for i in range(len(purses_input)):
        print(f"{i} INPUT: {purses_input[i]}")
        print(f"{i} OUTPUT: {add_ingot(purses_input[i])}")
        if add_ingot(purses_input[i]) == purses_correct_result[i]:
            print("correct")
        else:
            print("wrong")
    print("-----------------------------------------")


def test_get_ingot(purses_input: list[dict[str, int]]):
    print("TESTING GET INGOT")
    purses_correct_result = [{},
                             {},
                             {"ddd": "eee"},
                             {"gold_ingots": 1, "ddd": "eee"}]
    for i in range(len(purses_input)):
        print(f"{i} INPUT: {purses_input[i]}")
        print(f"{i} OUTPUT: {get_ingot(purses_input[i])}")
        if get_ingot(purses_input[i]) == purses_correct_result[i]:
            print("correct")
        else:
            print("wrong")
    print("-----------------------------------------")


def test_empty(purses_input: list[dict[str, int]]):
    print("TESTING EMPTY INGOT")
    purses_correct_result = [{},
                             {},
                             {},
                             {}]
    for i in range(len(purses_input)):
        print(f"{i} INPUT: {purses_input[i]}")
        print(f"{i} OUTPUT: {empty(purses_input[i])}")
        if empty(purses_input[i]) == purses_correct_result[i]:
            print("correct")
        else:
            print("wrong")
    print("-----------------------------------------")


def tests():
    p = [{},
         {"gold_ingots": 1},
         {"ddd": "eee"},
         {"gold_ingots": 2, "ddd": "eee"}]
    test_add_ingot(p)
    test_get_ingot(p)
    test_empty(p)
    print("add_ingot(get_ingot(add_ingot(empty(purse))))")
    print("result:", add_ingot(get_ingot(add_ingot(empty({})))))


if __name__ == "__main__":
    tests()
