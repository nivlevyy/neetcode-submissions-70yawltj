class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        fixed=""
        for ch in s:
            if "a"<=ch<="z" or "A"<=ch<="Z" or "0"<=ch<="9":
                fixed=fixed+ch
        fixed=fixed.lower()
        reverse=fixed[::-1]
        
        return fixed==reverse 



        