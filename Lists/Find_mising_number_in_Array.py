
from typing import List

class solution():

    def find_missing_bruteforce(self,n: List[int])->int:

        for i in range(0,len(n))+1:
            if i not in n:
                return i

        return -1


    def find_missing_better(self,n: List[int])->int:

        freq_dict={}

        for i in range(0,len(n)+1):
            freq_dict[i] = 0

        for i in n:
            freq_dict[i] = 1

        for k in freq_dict:
            if freq_dict[k] == 0:
                return k


    def find_missing_optimal(self,n: List[int])->int:

        sum = 0
        m=len(n)
        for i in n:
            sum=sum+i

        

        return ((m*(m+1))//2) - sum

print(solution().find_missing_optimal([0,1,2,3,4]))