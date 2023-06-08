class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.age = player_dict['age']
        self.position = player_dict['position']
        self.team = player_dict['team']

    @classmethod
    def add_players(cls, player_dict):
        player_objects = []
        for dict in player_dict:
            player_objects.append(cls(dict))
        return player_objects

kevin = {
    "name": "Kevin Durant",
    "age":34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum",
    "age":24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age":32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)

players = [
    {
    "name": "Kevin Durant",
    "age":34,
    "position": "small forward",
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum",
    "age":24,
    "position": "small forward",
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving",
    "age":32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard",
    "age":33,
    "position": "Point Guard",
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid",
    "age":32,
    "position": "Power Foward",
    "team": "Philidelphia 76ers"
    },
    {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
    }
]


new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)
