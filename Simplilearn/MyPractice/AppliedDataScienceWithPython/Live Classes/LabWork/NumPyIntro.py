import numpy as np
num_array_1=[10,20,30,40,50,60]
num_array_2=[70,80,90,100,110,120]
num_array=np.array([num_array_1,[70,80,90,100,110,120]])
num_array_2d=np.reshape(num_array, (2,6))
array_transpose=num_array_2d.transpose()  #it changes 2*6 matrix to 6*2 matrix, it can also be written as num_array_2d.T
print("Array Elements:", num_array)
print("2D Array Elements:\n", num_array_2d)
print("Array Shape:", num_array.shape)
print("Transposed Array:\n", array_transpose)
print("Array Data Type:", num_array.dtype)
print("Array Size:", num_array.size)
print("Array Addition:\n", np.add(num_array_1, num_array_2))
print("Array Subtraction:\n", np.subtract(num_array_2, num_array_1))
print("Array Multiplication:\n", np.multiply(num_array_1, num_array_2))
print("Array Division:\n", np.divide(num_array_2, num_array_1))
print("Array Median:", np.median(num_array_1)) #Middle Element in a Sorted Array , if even no of elements then average of two middle elements (30+40)/2 = 35
print("Array Mean:", np.mean(num_array_1))  #Average of All Elements (10+20+30+40+50+60)/6 = 35
print("Array Variance:", np.var(num_array_1)) #Each Element - Mean ,take mod value for -ve values and then square it, then average of all squared values 10-35 = -25 => 25^2=625 + 20-35=-15 => 15^2=225 + 30-35=-5 => 5^2=25 + 40-35=5 => 5^2=25 + 50-35=15 => 15^2=225 + 60-35=25 => 25^2=625 => (625+225+25+25+225+625)/6 = 291.66
print("Array Standard Deviation:", np.std(num_array_1)) #Each Element - Mean and then square it, then average of all squared values and then square root of it => sqrt(291.66) = 17.08
print("Array Minimum:", np.min(num_array_1))
print("Array Maximum:", np.max(num_array_1))
print("Percentile 50 of Array:", np.percentile(num_array_1, 20)) # calculates the 40th percentile value in the array , each element pecentage is calculated as (element index/total elements)*100 => 10=(1/6)*100=16.66 , 20=(2/6)*100==33.33 , 30=(3/6)*100=50 , 40=(4/6)*100=66.66 , 50=(5/6)*100=83.33 , 60=(6/6)*100=100 , so 40th percentile lies between 10 and 30 , so it will be 26
print("Index of Minimum Element in Array:", np.argmin(num_array_1)) #Index of Minimum Element
print("Index of Maximum Element in Array:", np.argmax(num_array_1))

char_array_1= ['Hello','World']
char_array_2= ['Welcome','Learners']
char_array=np.array([char_array_1,char_array_2])
char_concat=np.char.add(char_array_1, char_array_2)
char_upper=np.char.upper(char_array_1)
char_lower=np.char.lower(char_array_2)
char_split=np.char.split(char_array_1[0]) #splitting first element of char_array_1
char_replace = np.char.replace(char_array_1, 'Hello', 'Hi') #replacing 'o' with 'a' in char_array_1
print("Character Array Elements:", char_array)
print("Concatenated Character Array:", char_concat)
print("Uppercase Character Array:", char_upper)
print("Lowercase Character Array:", char_lower)
print("Split Character Array:", char_split)
print("Replaced Character Array:", char_replace)