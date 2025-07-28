def funct(nums) -> list:
    left = 0
    right = 1
    count = 0
    while left < right and right <= (len(nums)-count-1):
        if nums[left]==0:
            count = count +1 
            for i in range(left,len(nums)-1):
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
            left = 0
            right = 1
        else:
            left = left + 1
            right = right + 1
    return nums


def main():
    nums= []
    nums.append([0,1,0,3,12])
    nums.append([1,2,3,4])
    nums.append([0,0,0,0])

    for i in range(len(nums)):
        print(f"Input: {nums[i]}")
        funct(nums[i])
        print(f"Output: {nums[i]}\n")
    return 0

if __name__=="__main__":
    main()