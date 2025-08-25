# merge two sorted arrays without duplicates

from typing import List

class solution():

    def merge_without_duplicates(n: List[int],m: List[int])-> List[int]:

        i,j = 0,0
        result = []
        
        while i<len(n) and j<len(m):

            if n[i] <= m[j]:
                if len(result) == 0 or result[-1] != n[i]:
                    result.append(n[i])
                i+=1

            else:
               if len(result) == 0 or result[-1] != m[j]:
                    result.append(m[j])
               j+=1

        
        while i<len(n):
            if len(result) == 0 or result[-1] != n[i]:
                    result.append(n[i])
            i+=1

        while j<len(m):
            if len(result) == 0 or result[-1] != m[j]:
                    result.append(m[j])
            j+=1

        return result
    

print(solution.merge_without_duplicates([1,2,2,3,4],[2,3,5,6]))


