class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        op_set={"+","-","*","/"}
        stack=[]

        for t in tokens:
            
            if t.lstrip('-').isnumeric():
                stack.append(int(t))
            else :
                num2=stack.pop()
                num1=stack.pop()
                res=-1
                match t:
                    case "+":
                        
                       res = num1+num2
                    case "-":
                       res = num1-num2
                    case "*":
                       res = num1*num2
                    case "/":
                       res = int(num1/num2)
                   
                stack.append(res)

        return int (stack[-1])





