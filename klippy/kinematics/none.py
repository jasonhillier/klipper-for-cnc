# Dummy "none" kinematics support (for developer testing)
#
# Copyright (C) 2018-2021  Kevin O'Connor <kevin@koconnor.net>
#
# This file may be distributed under the terms of the GNU GPLv3 license.

class NoneKinematics:
    def __init__(self, toolhead, config, trapq):
        self.axes_min = self.axes_max = toolhead.Coord(0., 0., 0., e=0.)
        self.axis = [None, None, None]
        self.axis_names = ""
        self.trapq = trapq
    def get_steppers(self):
        return []
    def calc_position(self, stepper_positions):
        return [0, 0, 0]
    def set_position(self, newpos, homing_axes):
        pass
    def home(self, homing_state):
        pass
    def check_move(self, move):
        pass
    def get_status(self, eventtime):
        return {
            'homed_axes': '',
            'axis_minimum': self.axes_min,
            'axis_maximum': self.axes_max,
        }

def load_kinematics(toolhead, config, trapq, **kwargs):
    return NoneKinematics(toolhead, config, trapq)
