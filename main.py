'''

Exercise 9a

Write a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of
the odd-indexed numbers. So calling the function as even_odd_sums([10, 20,
30, 40, 50, 60]) , you’ll get back [90, 120] .

'''

def even_odd_sums(numbers):
    even_sum = sum(numbers[1::2])
    odd_sum = sum(numbers[::2])
    return [odd_sum, even_sum]
    
print(even_odd_sums((1, 2, 3, 4, 5, 6)))
print(even_odd_sums([2, 5, 6, 3]))