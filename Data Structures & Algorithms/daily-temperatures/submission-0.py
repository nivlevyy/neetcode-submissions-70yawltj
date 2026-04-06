class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        if not temperatures:
            return answer
        answer=[0]*len(temperatures)

        stack=list()
        
        for i,t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                    last=stack[-1]
                    answer[last[1]]=i-last[1]
                    stack.pop()
            stack.append((t,i))
        return answer 


        
                

