class Key:
    def __init__(self) -> None:
        pass

    def __getitem__(self, key: int) -> int:
        if key == 404:
            return 3

    def __str__(self) -> str:
        return "GeneralTsoKeycard"

    def __len__(self) -> int:
        return 1337

    def __gt__(self, other: int) -> bool:
        return True

    def __getattr__(self, passphrase: str) -> str:
        return "zax2rulez"


def tests():
    key = Key()
    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"
    print("ALL TESTS correct, no error")


if __name__ == "__main__":
    tests()
