from __future__ import annotations
from dataclasses import dataclass

from mountain import Mountain

from typing import TYPE_CHECKING, Union

from data_structures.linked_stack import *
# Avoid circular imports for typing.
if TYPE_CHECKING:
    from personality import WalkerPersonality

@dataclass
class TrailSplit:
    """
    A split in the trail.
       ___path_top____
      /               \
    -<                 >-path_follow-
      \__path_bottom__/
    """

    path_top: Trail
    path_bottom: Trail
    path_follow: Trail
    
    def remove_branch(self) -> TrailStore:
        """Removes the branch, should just leave the remaining following trail."""

        self.path_top = None
        self.path_bottom = None
        
        return self.path_follow.store

@dataclass
class TrailSeries:
    """
    A mountain, followed by the rest of the trail
    --mountain--following--
    """

    mountain: Mountain
    following: Trail

    def remove_mountain(self) -> TrailStore:
        """Removes the mountain at the beginning of this series."""

        self.mountain = None
        return self.following.store

    def add_mountain_before(self, mountain: Mountain) -> TrailStore:
        """Adds a mountain in series before the current one."""

        temp_store = TrailSeries(mountain=mountain,following=Trail(self))
        return temp_store

    def add_empty_branch_before(self) -> TrailStore:
        """Adds an empty branch, where the current trailstore is now the following path."""

        temp_store = TrailSplit(path_top = Trail(None), path_bottom = Trail(None), path_follow = Trail(self)) 

        return temp_store

    def add_mountain_after(self, mountain: Mountain) -> TrailStore:
        """Adds a mountain after the current mountain, but before the following trail."""

        temp_store = TrailSeries(mountain = self.mountain, following = Trail(store = TrailSeries(mountain = mountain, following = self.following)))
        return temp_store


    def add_empty_branch_after(self) -> TrailStore:
        """Adds an empty branch after the current mountain, but before the following trail."""

        temp_branch = TrailSeries(mountain = self.mountain,
                                  following = Trail(TrailSplit(
                                                    path_top = Trail(None), 
                                                    path_bottom = Trail(None), 
                                                    path_follow = self.following)))
        return temp_branch


TrailStore = Union[TrailSplit, TrailSeries, None]

@dataclass
class Trail:

    store: TrailStore = None

    def add_mountain_before(self, mountain: Mountain) -> Trail:
        """Adds a mountain before everything currently in the trail."""

        temp_trail = Trail(TrailSeries(mountain, self))
        return temp_trail


    def add_empty_branch_before(self) -> Trail:
        """Adds an empty branch before everything currently in the trail."""

        temp_trail = Trail(TrailSplit(
                                path_top = Trail(None), 
                                path_bottom = Trail(None), 
                                path_follow = self
                                )
                            )
        return temp_trail


    def follow_path(self, personality: WalkerPersonality) -> None:
        """Follow a path and add mountains according to a personality."""

        temp_stack_follow = LinkedStack()
        temp_new_trail = self

        temp_new_trail.traverse_trail(personality = personality, linkstack = temp_stack_follow)
        
        while not temp_stack_follow.is_empty():

            temp_new_trail = temp_stack_follow.pop()

            temp_new_trail.traverse_trail(personality = personality, linkstack = temp_stack_follow)

        return



    def collect_all_mountains(self) -> list[Mountain]:
        """Returns a list of all mountains on the trail."""
        raise NotImplementedError()

    def length_k_paths(self, k) -> list[list[Mountain]]: # Input to this should not exceed k > 50, at most 5 branches.
        """
        Returns a list of all paths of containing exactly k mountains.
        Paths are represented as lists of mountains.
        Paths are unique if they take a different branch, even if this results in the same set of mountains.
        """
        raise NotImplementedError()

    def traverse_trail(self, personality : WalkerPersonality, linkstack : LinkedStack):
        
        temp_new_trail = self

        while temp_new_trail.store != None:

            if isinstance (temp_new_trail.store, TrailSeries) :
                
                personality.add_mountain(mountain = temp_new_trail.store.mountain)

                temp_new_trail = temp_new_trail.store.following

            elif isinstance (temp_new_trail.store, TrailSplit) :

                linkstack.push(temp_new_trail.store.path_follow)

                if personality.select_branch(top_branch = temp_new_trail.store.path_top , bottom_branch = temp_new_trail.store.path_bottom) == True:
                    temp_new_trail = temp_new_trail.store.path_top

                else:
                    temp_new_trail = temp_new_trail.store.path_bottom

        return 
    