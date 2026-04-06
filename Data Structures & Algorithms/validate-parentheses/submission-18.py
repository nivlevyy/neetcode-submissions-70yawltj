class Solution:
    def isValid(self, s: str) -> bool:

        if not s :
            return True
        
        my_stack=list()

        for ch in s:
            
            if not my_stack :
              if (ch==')' or ch==']' or ch=='}'):
                return False
            else:
              last = my_stack[-1]

            if ch=='(' or ch=='[' or ch=='{':
                my_stack.append(ch)
            else:
                if (ch==')'and last=='(') or  (ch==']'and last=='[') or (ch=='}'and last=='{'):
                    my_stack.pop()
                else:
                    return False


        return not my_stack
                
        