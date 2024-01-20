class Printer:
    """
    Print!
    """

    @staticmethod
    def p_sleeping(segment):
        print("[ ] {}".format(segment))

    @staticmethod
    def p_counting(timer):
        m, s = timer.remaining()
        print("[x] {}:{}".format(m, "0" + str(s) if s < 10 else s))
