x =[1, 0, 1, 2, 0, 1, 3]
y = []
zero_num = 0
for c in x:
    if c != 0:
        y.append(c)
    else:
        zero_num += 1

print(y, zero_num)

current_num = 0

while current_num <= zero_num:
    y.append(0)
    current_num += 1

print(y, current_num)

#after running, Execution Timed Out (12000 ms), i.e, my code is inefficient and needs further optimization
#the time complexity for this program would be O(n^2) since there is a nested loop.

#RECHECKED, I AS WRONG, the time complexity is still O(n)
#but this brings the question...why did this fail?

#UPON, further re checking, even though the first ver is technically more efficient it can create bugs on edge cases
#after some tinkering, I got this

def move_zeros(lst):
    final_list = []
    
    for c in lst:
        if c!= 0:
            final_list.append(c)

    for c in lst:
        if c == 0:
            final_list.append(0)
            
    return final_list

#it surprisingly worked, and I don't quite know why it passed the time requirement of being less than 12 seconds.
#WELL, found out why, the time complexity for the second ver, is O(n), since each for loop concludes to n and 2n is simplified as n. 
#for loops make it essentially impossible to go to an infinite loop

#best rated, on code wars, i.e both best practice and clever
def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array

#problems:
#modified original list in place but have a return value
#o(n^2) or more 
#In Python, searching a list to find an element and shifting all the remaining items over takes $O(n)$ time. Because .remove() is sitting inside a for loop that runs $n$ times:

