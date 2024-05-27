# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/description/

class Solution:
    def waysToReachStair(self, k):
        # def recursion(current_step, target, jump, last_op):
        #     cnt = 0
        #     if current_step < 0 :
        #         return 0
            
        #     if current_step > target + 1:
        #         return 0
            
        #     if current_step == target:
        #         cnt = 1

        #     if last_op == "down":
        #         return cnt + recursion(current_step + 2**jump, target, jump+1, "expo")
        #     else:
        #         return cnt + recursion(current_step + 2**jump, target, jump+1, "expo") + recursion(current_step-1, target, jump, "down") 

        # jump = 0
        # target = k
        # current_step = 1
        # cnt = 0
        # if current_step == target:
        #     cnt = 1
        # return cnt + recursion(current_step + 2**jump, target, jump+1, "expo") + recursion(current_step-1, target, jump, "down") 
    
        # def calculate_power(base, pow):
        #     if pow == 0:
        #         return base ** pow
        #     if pow == 1:
        #         return base
        #     if pow%2==0:
        #         return 2 * calculate_power(base, int(pow/2))
        #     else:
        #         return base * calculate_power(base, pow-1)
        # def recursion(current_step, target, jump, last_op):
        #     cnt = 0
        #     if current_step < 0 :
        #         return 0
            
        #     if current_step > target + 1:
        #         return 0
            
        #     if current_step == target:
        #         cnt = 1

        #     get_jump = calculate_power(2, jump)

        #     if last_op == "down":
        #         return cnt + recursion(current_step + get_jump, target, jump+1, "expo")
        #     else:
        #         return cnt + recursion(current_step + get_jump, target, jump+1, "expo") + recursion(current_step-1, target, jump, "down") 

        # jump = 0
        # target = k
        # current_step = 1
        # cnt = 0
        # if current_step == target:
        #     cnt = 1
        # get_jump = calculate_power(2, jump)
        # return cnt + recursion(current_step + get_jump, target, jump+1, "expo") + recursion(current_step-1, target, jump, "down") 
    
        def memo(current_step, target, jump, last_op, down_list, expo_list):
            cnt = 0
            if current_step < 0 :
                return 0
            
            if current_step > target + 1:
                return 0
            
            if current_step == target:
                cnt = 1

            if last_op == "down":
                if expo_list[current_step].get(jump, -1) != -1:
                    return expo_list[current_step].get(jump)
                else:
                    calc = cnt + memo(current_step + 2**jump, target, jump+1, "expo",down_list, expo_list)
                    expo_list[current_step][jump] = calc
                    return calc
            else:
                down1 = 0
                expo1 = 0
                if down_list[current_step].get(jump, -1) != -1:
                    down1 = down_list[current_step].get(jump)
                else:
                    down1 = memo(current_step-1, target, jump, "down",down_list, expo_list) 
                    down_list[current_step][jump] = down1

                if expo_list[current_step].get(jump, -1) != -1:
                    expo1 = expo_list[current_step].get(jump)
                else:
                    expo1 = memo(current_step + 2**jump, target, jump+1, "expo",down_list, expo_list)
                    expo_list[current_step][jump] = expo1
                    
                return cnt + down1 + expo1

        jump = 0
        target = k
        current_step = 1
        cnt = 0
        down_list = [{-1:-1}] * (k+2)
        expo_list = [{-1:-1}] * (k+2) 
        if current_step == target:
            cnt = 1
        down1 = memo(current_step-1, target, jump, "down",down_list, expo_list) 
        down_list[current_step][jump] = down1

        expo1 = memo(current_step + 2**jump, target, jump+1, "expo",down_list, expo_list)
        expo_list[current_step][jump] = expo1
        
        return cnt + down1 + expo1
    
object = Solution()
print(object.waysToReachStair(0))
        