class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        new_nums=sorted(nums)

        for i in range(len(new_nums)-1):
            l=i+1
            r=len(new_nums)-1
            while l<r:
                if 0==new_nums[l]+new_nums[r]+new_nums[i]:
                    res.add(tuple(sorted([new_nums[i],new_nums[l],new_nums[r]])))
                    l+=1
                    r-=1
                elif 0>new_nums[l]+new_nums[r]+new_nums[i]:
                    l+=1
                else:
                    r-=1

        return [list(tri) for tri in res]