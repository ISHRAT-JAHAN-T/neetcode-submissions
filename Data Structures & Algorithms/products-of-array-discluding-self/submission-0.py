class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # left part
        left_result = []
        product = 1

        #print("length", len(nums))

        for i in range(len(nums)):
            if i == 0:
                left_result.append(product)
            else:
                product = product * nums[i - 1]
                left_result.append(product)

        #print("hello world")
        #print(left_result)

        # right result
        right_result = []
        product_2 = 1

        #print("print the reverse array")

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_result.append(product_2)
            else:
                product_2 = product_2 * nums[i + 1]
                right_result.append(product_2)
        right_result.reverse()
        #print(right_result) 

        final_result=[] 
        for i in range(len(nums)): 
            ans= left_result[i]*right_result[i]
            final_result.append(ans)
        #print("here is my final ans list", final_result)    

        return final_result