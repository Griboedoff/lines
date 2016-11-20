import json

CURR_SCORE = 'Your score'


class ScoreBoard:
    def __init__(self, path: str, json: dict, game_mode: int):
        self._hint_mode = game_mode
        self._path = path
        self._score_dict = json
        self._score_dict[CURR_SCORE] = 0
        self.max_score = max(self._score_dict.values())

    def set_hint_mode(self, n):
        if self._hint_mode == 2:
            raise ValueError("You can't change hint mode if it set for 2")
        self._hint_mode = n

    def update_score(self, d_score: int):
        self._score_dict[CURR_SCORE] += d_score

    @property
    def hint_mode(self):
        return self._hint_mode

    @property
    def current_score(self):
        return self._score_dict[CURR_SCORE]

    @staticmethod
    def load_from(path: str, game_mode):
        try:
            with open(path, 'r') as f:
                return ScoreBoard(path, json.loads(f.read()), game_mode)
        except Exception as e:
            return ScoreBoard('./records.json', {}, game_mode)

    def set_name(self, name: str):
        if CURR_SCORE == name:
            raise ValueError("Name must not be {}".format(name))
        score = self._score_dict[CURR_SCORE]
        self._score_dict.pop(CURR_SCORE)
        self._score_dict[name] = score

    def save(self):
        with open(self._path, 'w') as f:
            f.write(json.dumps(self._score_dict))

    def __str__(self):
        return "\n".join(
            list(": ".join(map(str, kv)) for kv in sorted(
                filter(
                    lambda x: x[0] != CURR_SCORE,
                    self._score_dict.items()),
                key=lambda x: x[1],
                reverse=True)) +
            ['\n',
             ': '.join([CURR_SCORE, str(self._score_dict[CURR_SCORE])])])
