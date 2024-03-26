

class Solution:
    
    def addTwoNumbers(self, l1, l2):
        lst1 = int("".join(list(map(str,l1))[::-1]))
        lst2 = int("".join(list(map(str,l2))[::-1]))
        Sum = str(lst1+lst2)
        return [int(x) for x in Sum][::-1]

s = Solution()
s1 = s.addTwoNumbers([2,4,3],[5,6,4])
print(s1)