#!/usr/bin/env python
# coding: utf-8

# In[4]:

if __name__ == "__main__":
class ListDivideException(Exception):
    pass
def list_divide (numbers, divide=2):
    count = 0
    for num in numbers: 
        if num %divide == 0:
            count += 1
    return count
def test_lists_divide():
    try: 
        assert list_divide([1, 2, 3, 4, 5]) == 2 
        assert list_divide([2, 4, 6, 8, 10]) == 5
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2 
        assert list_divide([]) == 0 
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError: 
        raise ListDivideException("Test failed")
 


# In[ ]:




