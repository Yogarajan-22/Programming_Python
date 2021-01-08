def maxSubArraySum(a,size): 
      
    max_so_far =a[0]
    curr_max = a[0]
    start = beg = 0
    end = 1
    for i in range(1,size):
        if a[i] > curr_max + a[i]:
            curr_max = a[i]
            beg = i
        else:
            curr_max = curr_max + a[i]

        if curr_max > max_so_far:
            max_so_far = curr_max
            start = beg
            end = i + 1

    print("Given array : " + str(a))
    print("The maximum subarray is: " + str(a[start:end]))
    return max_so_far 
  
# Driver function to check the above function  
a = list(map(int, input().split()))
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))