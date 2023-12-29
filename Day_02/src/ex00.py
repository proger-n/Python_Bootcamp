def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    result_purse = purse.copy()
    if "gold_ingots" in result_purse:
        result_purse["gold_ingots"] += 1
    else:
        result_purse["gold_ingots"] = 1
    return result_purse


def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    result_purse = purse.copy()
    if "gold_ingots" in result_purse:
        if result_purse["gold_ingots"] > 0:
            result_purse["gold_ingots"] -= 1
        if result_purse["gold_ingots"] == 0:
            del result_purse["gold_ingots"]
    return result_purse


def empty(purse: dict[str, int]) -> dict[str, int]:
    result_purse = {}
    return result_purse


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
