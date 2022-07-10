class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #s range = [1 , 3999] 
        #s length = [1, 15]
        
        total_value = 0
        value = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        #Check if they are in descending order
        #We check until the second last letter
        if len(s) > 1:
            index = 0
            for _ in (range(len(s)-1)) :
                if value[s[index+1]] <= value[s[index]]:
                    letter = s[index]
                    total_value += value[letter]
                    index += 1
                    if index >= (len(s)-1):
                        break
                else:
                    bigger = s[index+1]
                    smaller = s[index]
                    small_value = value[bigger] - value[smaller]
                    total_value += small_value
                    index += 2
                    if index >= (len(s)-1):
                        break
            #We check for the last letter
            if value[s[-1]] <= value[s[-2]]:
                letter = s[-1]
                total_value += value[letter]
        else:
            total_value = value[s[0]]
        
        return total_value

#Runtime: 57 ms
#Memory usage: 13.1 MB