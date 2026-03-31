class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l=0
        r=len(numbers)-1
        answer=[]
        while(l<r):
            
            if numbers[l]+numbers[r]==target:
                answer.append(l+1)
                answer.append(r+1)
                break
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1
        
        return answer
        