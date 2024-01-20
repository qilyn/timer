class Segment:
    """
    How does our hexagon look?
    """

    TIMES = (
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        0.05,
        # .10,
        # .15,
        # .30,
        # .45,
        # .60
    )

    @classmethod
    def seconds(cls, segment):
        print(segment)
        return Segment.TIMES[int(segment)] * 60

    @staticmethod
    def range():
        # roll_range = tuple(i * 60 for i in range(int(180)))
        return tuple((i * 60) - 90 for i in range(6))
