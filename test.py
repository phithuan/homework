nums_list = [2,7,11,15]
target = 9
for i in range(len(nums_list)):
    for j in range(i+1,len(nums_list)):
      if nums_list[i] + nums_list[j]==target:
        print(i,j)