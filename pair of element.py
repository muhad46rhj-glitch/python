class pair_elements:

    def twosum(self,nums, target):
        loopup = {}

        for i, num in enumerate(nums):
            if target - num in loopup:
                return (loopup[target - num], i)
            loopup[num] = i
value = int(input("Enter sum for which you want to make this serch : "))
print("index1=%d, index2=%d" % pair_elements().twosum((10,20,30,40,50,60,70),value))