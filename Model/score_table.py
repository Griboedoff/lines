import json


class ScoreTable:
    def __init__(self, path: str, json: dict, game_mode: int):
        self._game_mode = game_mode
        self._path = path
        self._score_dict = json
        self._score_dict["You score"] = 0

    def update_score(self, d_score: int):
        self._score_dict["You score"] += d_score

    @property
    def game_mode(self):
        return self._game_mode

    @property
    def current_score(self):
        return self._score_dict["You score"]

    @staticmethod
    def load_from(path: str, game_mode):
        with open(path, 'r') as f:
            return ScoreTable(path, json.loads(f.read()), game_mode)

    def save(self):
        with open(self._path, 'w') as f:
            f.write(json.dumps(self._score_dict))

    def save_to(self, path: str):
        with open(path, 'w') as f:
            f.write(json.dumps(self._score_dict))

    def __str__(self):
        return "\n".join([": ".join(map(str, kv))
                          for kv in sorted(self._score_dict.items(),
                                           key=lambda x: x[1],
                                           reverse=True)])
