class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []

        def backtracking(index, combination):
            
            if index==len(digits):
                result.append(combination)
                return
            
            curd=digits[index]
            letters=phone_map[curd]
            
            for letter in letters:
                backtracking(index+1,combination+letter)
        backtracking(0, "")
        return result



        