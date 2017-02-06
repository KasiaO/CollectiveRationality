# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:32:26 2016

@author: Kasia
"""

# import
import numpy as np
import base
import matplotlib.pyplot as plt

# parameters to be set
# t - int - number of runs of the simulation
# n - int - number of agents
# m - int - number of issues
# l - int - number of clauses in the constraint
# k - int - number of literals in each clause
# kneg - int - number of negative literals in each clause
# p - int - probability of a correct vote
# qnum - int - how many quotas on the interval 0 to 1 to consider

# Case3, replication of previous study
def Case3(t = 5000, n = 10, m = 4, l = 2, k = 2, kneg = [0, 1, 2], 
           p = 0.5, qnum = 11):
    res = {}
    for kNeg in kneg:
        exp = base.runExperiment(t, n, m, l, k, kNeg, p, qnum)
        res[str(2 - kNeg)] = exp
    return(res)

if __name__ == "__main__":   
    # Case 3a, no negated literals in the constraint
    # direct replication of the previous study, Case 2a
    case3a = Case3()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case3a['0'], quotas, case3a['1'],
             quotas, case3a['2'])
    plt.legend(["k+ = " + str(k) for k in sorted([int(x) for x in case3a.keys()])], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.savefig('Case 3a.png')
    plt.show()
    
    case3b = Case3(p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case3b['0'], quotas, case3b['1'],
             quotas, case3b['2'])
    plt.legend(["k+ = " + str(k) for k in sorted([int(x) for x in case3b.keys()])], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.savefig('Case 3b.png')
    plt.show()