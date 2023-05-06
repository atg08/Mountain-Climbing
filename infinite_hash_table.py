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

        self.top_level_table : ArrayR[tuple[K,V|ArrayR [K,V]]] = ArrayR(length = self.TABLE_SIZE)
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

        self.level = 0
        outer_array = self.top_level_table

        while True:
            index_position = self.hash(key = key)

            if outer_array[index_position] == None:
                raise KeyError("key ", key ," does not exist")

            elif not isinstance(outer_array[index_position][1], ArrayR):
                return outer_array[index_position][1]

            else:
                outer_array = outer_array[index_position][1]
                self.level += 1
                

    def __setitem__(self, key: K, value: V) -> None:
        """
        Set an (key, value) pair in our hash table.
        """
        self.level = 0
        outer_array = self.top_level_table
        
        while True:
            index_position = self.hash(key = key)
            
            if outer_array[index_position] == None:
                outer_array[index_position] = (key,value)
                self.count += 1
                return

            elif outer_array[index_position][0] == key:
                outer_array[index_position] = (key,value)
                return

            elif not isinstance(outer_array[index_position][1] , ArrayR):
                outer_key , outer_value = outer_array[index_position]

                inner_array : ArrayR[tuple[K,V|ArrayR [K,V]]] = ArrayR(length = self.TABLE_SIZE)
                outer_array[index_position] = (key[0 : self.level + 1], inner_array)
                
                self.level += 1

                outer_array = inner_array
                
                index_position = self.hash(key = outer_key)                   
                outer_array[index_position] = (outer_key , outer_value)

            else: 
                outer_key , outer_value = outer_array[index_position]
                
                self.level += 1

                outer_array = outer_value



    def __delitem__(self, key: K) -> None:
        """
        Deletes a (key, value) pair in our hash table.

        :raises KeyError: when the key doesn't exist.
        """

        self.level = 0
        index_list : list[int] = self.get_location(key = key)
        list_array : list[ArrayR] = []
        list_array.insert(0 , self.top_level_table)

        # print("delete function ", key)
        # print("index list is " , index_list , "length is ", len(index_list))
        
        for key_index in range(len(index_list)):
            if key_index < (len(index_list) - 1):        
                list_array.insert(key_index + 1, list_array[key_index][index_list[key_index]][1])
                

        current_array = list_array[-1]
        #print("tuple to delete is " , current_array[index_list[-1]])
        current_array[index_list[-1]] = None
        self.count -= 1

        for array_index in range(len(list_array)-1, 0 , -1):
            current_array = list_array[array_index]
            if array_index != 0:
                outer_array = list_array[array_index - 1]
            else:
                outer_array = current_array

            list_of_items : list[tuple[K, V]] = []


            for i in range (len(current_array)):
                if current_array[i] != None:
                    if isinstance(current_array[i][1] , ArrayR):
                        #print("ArrayR found, more confusion")
                        return

                    list_of_items.append(current_array[i])

            #print("list of items " , list_of_items)


            if len(list_of_items) == 1:
                if array_index == 0:
                    outer_array[index_list[0]] = list_of_items[0]
                else:
                    outer_array[index_list[array_index - 1]] = list_of_items[0]

            # for i in range (len(outer_array)):
            #     if outer_array[i] != None:
            #         print("index " , i , " outer array is " , outer_array[i])

        

    def __len__(self) -> int:
        return self.count


    def __str__(self) -> str:
        """
        String representation.

        Not required but may be a good testing tool.
        """
        # result = ""
        # current_array = self.top_level_table
        # self.level = 0

        # for array_index in range (len(current_array)):
        #     if current_array[array_index] != None:
        #         current_key, current_value = current_array[array_index]

        #         """ for item_inner in inner_table.array:
        #             if item_inner is not None:
        #                 (key_inner , value) = item_inner
        #                 result += "(" + str(key_inner) + "," + str(value) + ")\n" """
                
        #         result += str(key_outer) + ":\n" + str(inner_table)
        #         result += "\n"

        # return result
        raise NotImplementedError



    def get_location(self, key) -> list[int]:
        """
        Get the sequence of positions required to access this key.

        :raises KeyError: when the key doesn't exist.
        """

        self.level = 0
        outer_array = self.top_level_table
        index_list : list[int] = []

        while True:
            index_position = self.hash(key = key)
            
            if outer_array[index_position] == None or (outer_array[index_position][0] != key and not isinstance(outer_array[index_position][1], ArrayR)):
                raise KeyError("key ", key ," does not exist")
            
            elif not isinstance(outer_array[index_position][1], ArrayR):
                index_list.append(index_position)
                return index_list

            else:
                index_list.append(index_position)
                outer_array = outer_array[index_position][1]
                self.level += 1


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

    