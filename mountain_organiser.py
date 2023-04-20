from __future__ import annotations

from mountain import Mountain
from algorithms.mergesort import *

class MountainOrganiser:

    def __init__(self) -> None:
        self.merged_list = []

    def cur_position(self, mountain: Mountain) -> int:
            for i in range(len(self.merged_list)):
                if self.merged_list[i].name == mountain.name:
                    return i
            raise KeyError()

    def add_mountains(self, mountains: list[Mountain]) -> None:

        if self.merged_list == []:
            self.merged_list = mountains

        else:
            self.merged_list = merge(self.merged_list,mountains)
