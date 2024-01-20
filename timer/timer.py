from time import time as t
from .segment import Segment


class Timer:
    DONE = None
    STARTED_AT = 0
    END_AT = 0

    def __init__(self):
        self.STARTED_AT = 0
        self.END_AT = 0

    def start(self, segment):
        self.STARTED_AT = int(t())
        self.END_AT = self.STARTED_AT + Segment.seconds(segment)

    def should_end(self):
        return t() >= self.END_AT

    def seconds_remaining(self):
        return self.END_AT - int(t())

    def remaining(self):
        seconds = self.seconds_remaining()
        minutes = int(seconds / 60)
        return (minutes, int(seconds - minutes * 60))
