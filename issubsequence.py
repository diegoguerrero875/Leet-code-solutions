#from leetcode problem is subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # current index in string t
        for let in s:
            j = t.find(let, i)  # search for let in t starting from index i
            if j == -1:  # let not found in t
                return False
            i = j + 1  # update i to the next position in t
        return True
