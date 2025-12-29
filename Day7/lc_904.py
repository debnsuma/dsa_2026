# https://leetcode.com/problems/fruit-into-baskets/description/
def totalFruit(fruits):

    low = 0
    high = 0
    basket = {}
    max_fruits = float('-inf')

    while high < len(fruits):
        if basket.get(fruits[high]):
            basket[fruits[high]] += 1
        else:
            basket[fruits[high]] = 1
        
        while len(basket.keys()) > 2:
            if basket[fruits[low]] == 1:
                basket.pop(fruits[low])
            else:
                basket[fruits[low]] -= 1
            low += 1   
        
        if len(basket.keys()) <= 2:
            max_fruits = max(max_fruits, high-low+1)
        high += 1


    return max_fruits

fruits = [1,2,1, 2, 2, 2, 10, 1]
print(totalFruit(fruits))          


    



