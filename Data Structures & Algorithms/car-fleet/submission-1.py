class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        if not position:
            return 0
        d={}
        #O(N)
        for i in range(len(position)):
            d[position[i]]=i
        sort_pos=sorted(position) #(nlog(n))

        fl_stack=list()
        #iterating on the sorted position
        #if i have bigger time i pop out until i am the lowest time  
        for pos in sort_pos:
            time=(target-pos)/speed[d[pos]]
            if not fl_stack:
                fl_stack.append(time)
            else:
                
                while(fl_stack and time>=fl_stack[-1]):

                    fl_stack.pop()
                fl_stack.append(time)
        return len(fl_stack)




