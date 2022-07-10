#Converting integer to string
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #Check if odd or even number of digits in x:
        #We need to convert it to a string first
        result = True
        middle_index = int(len(str(x))/2) #Do not +1
        str_x = str(x)
        for i in range(middle_index):
            if str_x[i] != str_x[len(str_x)-(1+i)]:
                result = False
                return result
        return result

#Runtime: 87 ms
#Memory usage: 13.6 MB

#Without converting integer to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Without converting integer to a string
        if x < 0:
            return False
        elif x >= 0 and x <= 9:
            return True
        else:
            num_list = []
            num = x
            while num >= 1:
                y = num%10
                num = int(num/10)
                num_list.append(y)
            rev_num_list = num_list.copy()
            rev_num_list.reverse()
            for i in range(len(num_list)):
                if num_list[i] != rev_num_list[i]:
                    return False
            return True

#Runtime: 152 ms
#Memory usage: 13.9 MB