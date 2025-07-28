def funct(nums) -> bool:
    left = 0
    right = 1
    last = len(nums)-1
    while left < right and right <= last:
        if nums[left] == nums[right]:
            return True
        elif right == last and left < last:
            left = left +1
            right = left +1
        else:
            right = right + 1
    return False


def main():
    nums= []
    nums.append([1,2,3,-1])
    nums.append([1,2,-3,4])
    nums.append([1,1,1,3,3,4,3,2,4,2])
    nums.append([0,0,0,1])
    for i in range(len(nums)):
        ans = funct(nums[i])
        print(f"{nums[i]} --> {ans}\n")
    return 0

if __name__=="__main__":
    main()