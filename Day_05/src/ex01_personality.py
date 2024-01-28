import random


def turrets_generator():
    def shoot(self):
        print("shoot")

    def search(self):
        print("search")

    def talk(self):
        print("talk")

    while True:
        traits = [random.randint(0, 100) for _ in range(5)]
        if sum(traits) == 100:
            turret = type("Turret", (), {
                "neuroticism": traits[0],
                "openness": traits[1],
                "conscientiousness": traits[2],
                "extraversion": traits[3],
                "agreeableness": traits[4],
                "shoot": shoot,
                "search": search,
                "talk": talk
            })
            yield turret()


def test():
    T = turrets_generator()
    turret = next(T)
    print("instance:", turret)
    print(turret.neuroticism, turret.openness, turret.conscientiousness,
          turret.extraversion, turret.agreeableness)
    turret.talk()
    turret.search()
    turret.talk()

    turret = next(T)
    print("instance:", turret)
    print(turret.neuroticism, turret.openness, turret.conscientiousness,
          turret.extraversion, turret.agreeableness)
    turret.talk()
    turret.search()
    turret.talk()


if __name__ == "__main__":
    test()
