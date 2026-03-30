class Solution:
   
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        codestr=""
        for st in strs:
            length=len(st)

            codestr=codestr+str(length)+"*"+st
        return codestr

    def decode(self, s: str) -> List[str]:
        answer_list=[]
        if not s:
            return answer_list
        i=0
        numst=""
        
        while i<len(s):
            while s[i].isnumeric():
                numst=numst+s[i]
                i+=1
            num=int(numst)
            i+=1 # the "*" charachter
            word=""
            for _ in range(num):
                word=word+s[i]
                i+=1
            answer_list.append(word)
            numst=""
        return answer_list
                

                






