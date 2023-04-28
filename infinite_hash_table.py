from __future__ import annotations
from typing import Generic, TypeVar

from data_structures.referential_array import ArrayR
from data_structures.hash_table import *

K = TypeVar("K")
V = TypeVar("V")

class InfiniteHashTable(Generic[K, V]):
    """
    Infinite Hash Table.

    Type Arguments:
        - K:    Key Type. In most cases should be string.
                Otherwise `hash` should be overwritten.
        - V:    Value Type.

    Unless stated otherwise, all methods have O(1) complexity.
    """

    TABLE_SIZE = 27

    def __init__(self) -> None:
        self.array = ArrayR(self.TABLE_SIZE)
        self.location_list = []
        self.level = 0
        self.count = 0
 
    def hash(self, key: K) -> int:
        if self.level < len(key):
            return ord(key[self.level]) % (self.TABLE_SIZE-1)
        return self.TABLE_SIZE-1

    def __getitem__(self, key: K) -> V:
        """
        Get the value at a certain key

        :raises KeyError: when the key doesn't exist.
        """
        raise NotImplementedError()

    def __setitem__(self, key: K, value: V) -> None:
        """
        Set an (key, value) pair in our hash table.
        """
        self.level = 0
        table = self.array

        while True:
            position = self.hash(key)

            #inside index is not empty
            if isinstance(table[position], tuple) and isinstance(table[position][1], ArrayR):
                table = table[position][1]
                self.level += 1
                # print(key)
                continue

            elif isinstance(table[position], tuple) and isinstance(table[position][1], int):
                crash = table[position] #lin 1
                # print("collision will be :",collision, " in ",position)
                table[position] = (crash[0][:self.level],ArrayR(self.TABLE_SIZE))
                table = table[position][1]
                self.level += 1
                table[self.hash(crash[0])] = crash
                # print(" so now, i will make this ",collision, " into ",self.hash(collision[0]),"and",(key,value)," one will be in",self.hash(key))
                table[self.hash(key)] = (key,value)
                
                
                while self.hash(crash[0]) == self.hash(key): #lin and link are in same location
                    # print("However, now it detected we need to do one more hash table!")
                    
                    # print("going to make new table in",self.hash(collision[0]))
                    table[position] = (crash[0][:self.level],ArrayR(self.TABLE_SIZE))
                    table = table[position][1]
                    self.level += 1

                    table[self.hash(crash[0])] = crash
                    table[self.hash(key)] = (key,value)
                    # print(" so now, i will make this ",collision, " into ",self.hash(collision[0]),"and",(key,value)," one will be in",self.hash(key))
                    # print("Done~")
                
                return

            else:
                table[position] = (key,value)
                self.count += 1
                # print("first, i will put this ",table[position],"into",self.hash(key))
                # print("done")
                return

        


    def __delitem__(self, key: K) -> None:
        """
        Deletes a (key, value) pair in our hash table.

        :raises KeyError: when the key doesn't exist.
        """
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        """
        String representation.

        Not required but may be a good testing tool.
        """
        raise NotImplementedError()

    def get_location(self, key):
        """
        Get the sequence of positions required to access this key.

        :raises KeyError: when the key doesn't exist.
        """
        raise NotImplementedError()
        
    def __contains__(self, key: K) -> bool:
        """
        Checks to see if the given key is in the Hash Table

        :complexity: See linear probe.
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

if __name__ == "__main__":
    ih = InfiniteHashTable()
    ih["lin"] = 1
    ih["leg"] = 2
    ih["mine"] = 3
    ih["linked"] = 4
    ih["limp"] = 5
    ih["mining"] = 6
    ih["jake"] = 7
    ih["linger"] = 8

    # print(ih.get_location("lin"))
    # print(ih.get_location("leg"))
