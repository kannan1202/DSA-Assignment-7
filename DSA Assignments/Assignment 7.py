from collections import Counter
import heapq
def MostFrequentPurchase(purchases):
    count = Counter(purchases) #stores the frequency of the strings in the form of a dictionary.
    result = heapq.nlargest(1,count,key=count.get)
    return result

#driver code
purchases = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
'greenPants', 'greenPants', 'greenPants']
result = MostFrequentPurchase(purchases)
print(f"The most frequent purchase of the day is {result}")