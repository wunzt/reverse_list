# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/9/22
# Description: Reverses the order of a list.

def reverse_list(val):
    """Reverses the order of a list."""
    i = 0
    while i < len(list)/2:
        temp = val[i]
        val[i] = val[len(list)-i-1]
        val[len(list) - i - 1] = temp
        i += 1