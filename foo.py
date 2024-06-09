'''Updated code'''

'''1.) Assert needs changed for return since assert is used for debugging 
whereas we're looking function logic in this instance''' 
def is_divisible_by_k(x, k):
   return x % k == 0

'''2.) x initialized as tuple needs changed for a list to append elements'''
multiples = []

'''3.) i range needs updated from 1000 to 1,1001 in order to satisfy "lower or
equal to 1000"'''
for i in range(1, 1001):
    if (is_divisible_by_k(i, 2) or is_divisible_by_k(i, 5) or is_divisible_by_k(i, 7)):
        multiples.append(i)

'''4.) The sum stored in a variable and printed'''
result = sum(multiples)
print(result)

