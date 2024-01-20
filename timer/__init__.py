from sense_emu import SenseHat
from time import sleep

from .printer import Printer
from .screen import Screen
from .spatial import Spatial
from .timer import Timer
from .segment import Segment


hat = SenseHat()
hat.clear()

spatial = Spatial(hat.get_gyroscope()["pitch"])
screen = Screen(hat)
timer = Timer()
timer.start(0)

settlingCounter = 0
print(list(enumerate(Segment.range())))

while True:
    timer.start(spatial.segment)
    while not timer.should_end():
        Printer.p_counting(timer)
        screen.fill_screen_with_segment(
            timer.seconds_remaining() / Segment.seconds(spatial.segment),
            spatial.segment,
        )
        sleep(1)

    spatial.set_resting_pitch(hat.get_gyroscope()["pitch"])

    while hat.get_gyroscope()["pitch"] == spatial.resting_pitch:
        # sleeping until moved
        print("zzzz")
        screen.blue()
        sleep(0.5)

    spatial.set_resting_pitch(hat.get_gyroscope()["pitch"])
    settling_counter = 0

    screen.clear()

    while settling_counter < 2:
        new_pitch = hat.get_gyroscope()["pitch"]
        sleep(0.5)

        if new_pitch == spatial.resting_pitch:  # TODO: fudge this
            print("shuffle:", settling_counter)
            settling_counter += 1
        else:
            print("shuffle: shake shake")
            settling_counter = 0

        spatial.set_resting_pitch(new_pitch)
