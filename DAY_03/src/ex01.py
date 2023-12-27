from collections import Counter


class Player:
    def __init__(self) -> None:
        self.name = "player"

    def make_step(self, other_last_step: str) -> str:
        return "Cooperate"


class Cheater(Player):
    def __init__(self) -> None:
        self.name = "cheater"

    def make_step(self, other_last_step: str) -> str:
        return "Cheat"


class Cooperator(Player):
    def __init__(self) -> None:
        self.name = "cooperator"

    def make_step(self, other_last_step: str) -> str:
        return super().make_step(other_last_step)


class Copycat(Player):
    def __init__(self) -> None:
        self.name = "copycat"

    def make_step(self, other_last_step: str) -> str:
        return other_last_step if other_last_step != "No steps" else "Cooperate"


class Grudger(Player):
    def __init__(self) -> None:
        self.name = "grudger"
        self.flag_cheat = False

    def make_step(self, other_last_step: str) -> str:
        if other_last_step == "Cheat":
            self.flag_cheat = True
        return "Cheat" if self.flag_cheat else "Cooperate"


class Detective(Player):
    def __init__(self) -> None:
        self.name = "detective"
        self.flag_cheat = False
        self.step_num = -1
        self.strategy = ["Cooperate", "Cheat", "Cooperate", "Cooperate"]

    def make_step(self, other_last_step: str) -> str:
        if self.step_num < 3:
            if other_last_step == "Cheat":
                self.flag_cheat = True
            self.step_num += 1
            return self.strategy[self.step_num]
        elif self.flag_cheat == True:
            return other_last_step
        else:
            return "Cheat"


class Smart(Player):
    def __init__(self) -> None:
        self.name = "smart"

    def make_step(self, other_last_step: str) -> str:
        return "Cooperate" if (other_last_step == "No steps" or other_last_step == "Cooperate") else "Cheat"


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: Player, player2: Player) -> None:
        last_step_p1 = "No steps"
        last_step_p2 = "No steps"
        for i in range(self.matches):
            last_step_p1 = player1.make_step(last_step_p2)
            last_step_p2 = player2.make_step(last_step_p1)
            if last_step_p1 == "Cooperate" and last_step_p2 == "Cooperate":
                self.registry += Counter({player1.name: 2, player2.name: 2})
            elif last_step_p1 == "Cooperate" and last_step_p2 == "Cheat":
                self.registry += Counter({player1.name: -1, player2.name: 3})
            elif last_step_p1 == "Cheat" and last_step_p2 == "Cooperate":
                self.registry += Counter({player1.name: 3, player2.name: -1})

    def top3(self):
        print(*self.registry.most_common(3), sep="\n")


def test_5_behaviors():
    print("TEST 5 behaviors")
    cheater = Cheater()
    cooperator = Cooperator()
    copycat = Copycat()
    grudger = Grudger()
    detective = Detective()
    g = Game()
    g.play(cheater, cooperator)
    g.play(cheater, copycat)
    g.play(cheater, grudger)
    g.play(cheater, detective)
    g.play(cooperator, copycat)
    g.play(cooperator, grudger)
    g.play(cooperator, detective)
    g.play(copycat, grudger)
    g.play(copycat, detective)
    g.play(grudger, detective)
    g.top3()


def test_6_behaviors():
    print("TEST 6 behaviors")
    smart = Smart()
    cheater = Cheater()
    cooperator = Cooperator()
    copycat = Copycat()
    grudger = Grudger()
    detective = Detective()
    g = Game()
    g.play(smart, cheater)
    g.play(smart, cooperator)
    g.play(smart, copycat)
    g.play(smart, grudger)
    g.play(smart, detective)
    g.play(cheater, cooperator)
    g.play(cheater, copycat)
    g.play(cheater, grudger)
    g.play(cheater, detective)
    g.play(cooperator, copycat)
    g.play(cooperator, grudger)
    g.play(cooperator, detective)
    g.play(copycat, grudger)
    g.play(copycat, detective)
    g.play(grudger, detective)
    g.top3()


if __name__ == "__main__":
    test_5_behaviors()
    test_6_behaviors()
