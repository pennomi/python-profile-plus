import cProfile
import enum


class Sort(str, enum.Enum):
    cumulative = 'cumulative'


class ProfilePlus(cProfile.Profile):
    def __enter__(self):
        self.enable()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disable()

    def print_stats(self, sort=-1):
        super().print_stats(sort=sort)
