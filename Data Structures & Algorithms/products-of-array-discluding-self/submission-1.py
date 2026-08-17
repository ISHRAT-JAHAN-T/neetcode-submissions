class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # left part
        left_result = []
        product = 1

        for i in range(len(nums)):
            if i == 0:
                left_result.append(product)
            else:
                product = product * nums[i - 1]
                left_result.append(product)
     
        right_result = []
        product_2 = 1

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_result.append(product_2)
            else:
                product_2 = product_2 * nums[i + 1]
                right_result.append(product_2)
        right_result.reverse()
        
        #final result

        final_result=[] 
        for i in range(len(nums)): 
            ans= left_result[i]*right_result[i]
            final_result.append(ans)
           

        return final_result