from sense_emu import SenseHat

from segment import Segment


class Spatial:
        
    def __init__(self, start_pitch):
        self.set_resting_pitch(start_pitch)

    def set_resting_pitch(self, pitch):
        self.resting_pitch = pitch
        self.segment = self.get_segment(pitch)

    def get_segment(self, pitch):
        for i, r in enumerate(Segment.range()):
            if (pitch < r):
                return i
        return len(Segment.range()) - 1
