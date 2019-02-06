import os
import sys
from sympy import *
from itertools import combinations
# N = 100,000; M = 50,000,000; S = 5,000,000,000
# N = 40,000; M = 60,000,000; S = 3,200,000,000
# N = 50,000; M = 80,000,000; S = 1,500,000,000
# N = 100,000; M = 100,000,000; S = 1,200,000,000
soln = [[100000, 50000000, 5000000000],
        [40000, 60000000, 3200000000],
        [50000, 80000000, 1500000000],
        [100000, 100000000, 1200000000]]
print('------------TASK1---------------')
for n, m, s in soln:
    result = s/(12*(1000000+m))
    print(result)
print('last set of numbers make difference of less than 1% from given one. So it is an answer\n\n')
print('------------TASK2---------------')


baskets = range(1,101)
items = range(1,101)

# Create transactions
transactions = []

for i in baskets:
    basket = set()
    for item in items:
        if i % item == 0:
            basket.add(item)
    transactions.append(basket)


def subsets(S, k):
    return [set(s)for s in combinations(S, k)]

T = [
 {'Bread', 'Milk'},
 {'Beer', 'Bread', 'Diaper', 'Eggs'},
 {'Beer', 'Coke', 'Diaper', 'Milk'},
 {'Beer', 'Bread', 'Diaper', 'Milk'},
 {'Bread', 'Coke', 'Diaper', 'Milk'},
]

def count(X, T):
    return S(sum(1 for x in T if X <= x))

# print(support_count({'Milk', 'Bread', 'Diaper'}, T))

def support(X, T):
    return count(X, T) / len(T)

# print(support({'Milk', 'Bread', 'Diaper'}, T))

def rule_support(xy, T):
    x, y = xy
    return support(x | y, T)

rule = ({'Milk', 'Diaper'}, {'Beer'})


def rule_confidence(xy, T):
    x, y = xy
    return count(x | y , T) / count(x, T)



T = [
 {'A', 'B', 'E'},
 {'B', 'D'},
 {'B', 'C'},
 {'A', 'B', 'D'},
 {'A', 'C'},
 {'B', 'C'},
 {'A', 'C'},
 {'A', 'B', 'C', 'E'},
 {'A', 'B', 'C'},
]

cmin = 1


def find_rules(itemset, T):
    rules = []
    for i in range(len(itemset)):
        for s in subsets(itemset, i):
            if len(s) > 0:
                rule = (set(s), itemset - set(s))
                if rule_confidence(rule, T) >= cmin:
                    rules.append(rule)

    return rules


T = [
  {'A', 'C', 'D'},
  {'B', 'C', 'E'},
  {'A', 'B', 'C', 'E'},
  {'B', 'E'},
  {'A', 'B', 'C', 'E'}
]

smin = 0.4

def union_all(sets):
    result = set()
    for c in sets:
        result = result | c
    return result


def frequent_k(T , k):
    final_freq_set = []
    current_set = T
    for set_len in range(k):
        result = []
        items = subsets(union_all(current_set), set_len+1)
        # print(items)
        for item in items:
            if support(item, T) >= smin:
                final_freq_set.append(item)
                result.append(item)
        current_set = result
    return final_freq_set



def confidence(num, denom):
    rule = [set(denom), set.difference(set(num),set(denom))]
    # print(rule)
    confidence = rule_confidence(rule, transactions)*100
    return confidence

print("{1,2}-> 4,Condidence = %d"%(confidence([1,2,4],[1,2]))   )
print("{1}-> 2,Condidence = %d"%(confidence([1,2],[1]))   )
print("{1,4,7}-> 14,Condidence = %d"%(confidence([1,4,7,14],[1,4,7]))   )
print("{1,3,6}-> 12,Condidence = %d"%(confidence([1,3,6,12],[1,3,6]))   )
print("{4,6}-> 12,Condidence = %d"%(confidence([4,6,12],[4,6]))   )
print("{8,12}-> 96,Condidence = %d"%(confidence([8,12,96],[8,12]))   )
print("{4,6}-> 24,Condidence = %d"%(confidence([4,6,24],[4,6]))   )
print("{1,3,6}-> 12,Condidence = %d"%(confidence([1,3,6,12],[1,3,6])) )
print('The resulting number of rules with confidence of 100 is really big. Hard to represent it in proper for your eye way)')
