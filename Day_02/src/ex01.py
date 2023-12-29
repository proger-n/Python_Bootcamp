import ex00


def split_booty(*purses: dict[str, int]) -> dict[str, int]:
    res = [{}, {}, {}]
    count = 0
    for p in purses:
        if "gold_ingots" in p:
            count += p["gold_ingots"]

    while count > 0:
        for i in range(3):
            if count > 0:
                res[i] = ex00.add_ingot(res[i])
                count -= 1

    return res[0], res[1], res[2]


def test_split_booty():
    input_purses = [[{}],
                    [{"gold_ingots": 1}, {"gold_ingots": 2}],
                    [{"ddd": "eee"}, {"gold_ingots": 2}, {"gold_ingots": 2}],
                    [{"gold_ingots": 2}, {"gold_ingots": 1}, {"gold_ingots": 2}]]
    right_purses = [[{}, {}, {}],
                    [{"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 1}],
                    [{"gold_ingots": 2}, {"gold_ingots": 1}, {"gold_ingots": 1}],
                    [{"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1}]]
    for i in range(4):
        print(f"TEST {i}")
        print("INPUT: ", input_purses[i])
        print("OUTPUT:   ", list(split_booty(*input_purses[i])))
        print("EXPECTED: ", right_purses[i])
        print("conclusion: ", right_purses[i] == list(
            split_booty(*input_purses[i])))
        print("---------------------------------------------------")


if __name__ == "__main__":
    test_split_booty()
