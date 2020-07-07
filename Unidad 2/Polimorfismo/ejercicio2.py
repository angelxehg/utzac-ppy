class Game:

    def __init__(self, name, players=2):
        self.name = name
        self.players = players

    def __str__(self, show_type=True):
        return self.name + " | " + str(self.players) + " players | " + str(len(self.traits)) + " traits"

    @property
    def traits(self):
        return []


class Football(Game):

    def __init__(self):
        super(Football, self).__init__("Football", 18)

    @property
    def traits(self):
        return [
            'Uses football balloon'
        ]


class Basketball(Game):

    def __init__(self):
        super(Basketball, self).__init__("Basketball", 12)

    @property
    def traits(self):
        return [
            'Uses basketball balloon'
        ]


class Baseball(Game):

    def __init__(self):
        super(Baseball, self).__init__("Baseball", 15)

    @property
    def traits(self):
        return [
            'Uses baseball balloon'
        ]


games = [
    Game("Generic game", 2),
    Football(),
    Basketball(),
    Baseball()
]

for game in games:
    print(game)
    print(game.traits)
