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
        '''
        The top_level_table will be array, containing tuple[Key, Value] inside.
        level and count will be start from 0.
        '''
        self.top_level_table : ArrayR[tuple[K,V|ArrayR [K,V]]] = ArrayR(length = self.TABLE_SIZE)
        self.level = 0
        self.count = 0

    def hash(self, key: K) -> int:
        """
        Making hash value.

        Args:
        - key: the key of value.

        Returns:
        - result: the hash value calculated from the key, self.level and self.TABLE_SIZE.
                  if self.level < len of key, it will return self.TABLE_SIZE-1.

        Complexity:
        - Worst & Best case: O(1)
        - There is no loop.

        """
        if self.level < len(key):
            return ord(key[self.level]) % (self.TABLE_SIZE-1)
        return self.TABLE_SIZE-1

    def __getitem__(self, key: K) -> V:
        """
        Get the value at a certain key.

        Args:
        - key: the key of value.

        Raises:
        - KeyError: when the key doesn't exist.

        Returns:
        - result: it will return (index 1) the value from the exact same key(index 0) location.

        Complexity:
        - Worst & Best case: O(1)
        - it will work in one loop till it reach to find correct Key.
        """

        # For finding item, the function always reset level to 0.
        self.level = 0

        # Outer array will be top_level_table.
        outer_array = self.top_level_table

        # It will loop till it find the exact key location.
        while True:

            # index position is the hash value from the key.
            index_position = self.hash(key = key)

            # raise error if the key is not exists.
            if outer_array[index_position] == None:
                raise KeyError("key ", key ," does not exist")

            # return it found the exact key location.
            elif isinstance(outer_array[index_position][1], int):
                return outer_array[index_position][1]

            # There is more array in the index, (same hash key value)
            # Therefore, it needs to add 1 to level and go back to the loop.
            else:
                outer_array = outer_array[index_position][1]
                self.level += 1
                

    def __setitem__(self, key: K, value: V) -> None:
        """
        Set an (key, value) pair in our hash table.

        Args:
        - key:   the key of value.
        - value: the value of key.  

        Returns:
        - result: it will set (key,value)set based on the value of the hash from key.

        Complexity:
        - Best case:  O(1), when it find the hash value with the first level and directly can set to that index.
        - Worst case: O(n), n: the length of key. 
        - it will work in one loop till it reach to find correct Key.
        """

        # For setting (key, value) pair, it needs to set the level to 0,
        # so that since first level we can get the correct hash value from correct level.
        self.level = 0

        # The first outer_array will be top_level_table.
        outer_array = self.top_level_table
        
        # It will keep the loop till it find the correct location for set (key, value) pair.
        while True:

            # The index value will be depends on hash value from key, level and table.
            index_position = self.hash(key = key)

            # If the index in outer_array is None, it means we can set the (key, value) pair in this index.
            if outer_array[index_position] == None:
                outer_array[index_position] = (key,value)

                # The count will be added 1.
                self.count += 1
                return

            # If there is an index, but the key is exact same with the key that we want to set.
            # It means we need to replace the old value to the new value that we want to set currently.
            elif outer_array[index_position][0] == key:
                outer_array[index_position] = (key,value)
                return

            # If there is a value which type is integer,
            # Need to be in loop again in case array example:(lin,lint..)
            elif isinstance(outer_array[index_position][1] , int):
                outer_key , outer_value = outer_array[index_position]
                
                # Make new array and put in the index that there was outer key and outer value set.
                inner_array : ArrayR[tuple[K,V|ArrayR [K,V]]] = ArrayR(length = self.TABLE_SIZE)
                outer_array[index_position] = (key[0 : self.level + 1], inner_array)

                self.level += 1
                outer_array = inner_array
                
                # After we add the old set to new array, add current key and value to new array too.
                index_position = self.hash(key = outer_key)                   
                outer_array[index_position] = (outer_key , outer_value)

            # There is an array, therefore it need to see the next hash with next level (+1)
            else: 
                outer_key , outer_value = outer_array[index_position]
                inner_array = outer_value
                self.level += 1
                outer_array = inner_array



    def __delitem__(self, key: K) -> None:
        """
        Deletes a (key, value) pair in our hash table.

        Args:
        - key: the key of value from the set (Key, Value).

        Raises:
        - KeyError: when the key doesn't exist.

        Returns:
        - result: it will set item based on the value of the hash from key.

        Complexity:
        - Best case: 
        - Worst case: 
        -
        """

        self.level = 0
        index_list : list[int] = self.get_location(key = key)
        list_array : list[ArrayR] = []
        list_array.insert(0 , self.top_level_table)

        for key_index in range(len(index_list)):
            if key_index < (len(index_list) - 1):        
                list_array.insert(key_index + 1, list_array[key_index][index_list[key_index]][1])
                

        current_array = list_array[-1]
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
                        return

                    list_of_items.append(current_array[i])

            if len(list_of_items) == 1:
                if array_index == 0:
                    outer_array[index_list[0]] = list_of_items[0]
                else:
                    outer_array[index_list[array_index - 1]] = list_of_items[0]

    
    def __len__(self) -> int:
        """
        Return the count.
        """
        return self.count


    def __str__(self) -> str:
        """
        String representation.

        Not required but may be a good testing tool.
        """
 
        raise NotImplementedError



    def get_location(self, key) -> list[int]:
        """
        Get the sequence of positions required to access this key.

        Args:
        - key: the key of value from the set (Key, Value).

        Raises:
        - KeyError: when the key doesn't exist.

        Returns:
        - result: a list containing the indices required to retrieve a key.

        Complexity:
        - Best case: O(1), when there is an key and value in the first outer_array.
        - Worst case: O(n), n: the length of the key.
        -
        """
        self.level = 0
        outer_array = self.top_level_table
        index_list : list[int] = []

        while True:
            index_position = self.hash(key = key)
            
            if outer_array[index_position] == None or (outer_array[index_position][0] != key and not isinstance(outer_array[index_position][1], ArrayR)):
                raise KeyError("key ", key ," does not exist")
            

            elif isinstance(outer_array[index_position][1], int):
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

    