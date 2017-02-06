# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:19:04 2017

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

# Case1a, replication of previous study
def Case1(t = 5000, n = 10, m = 4, l = 1, k = 4, kneg = 0, 
           p = np.linspace(0.5, 1, 6), qnum = 11):
    res = {}
    for prob in p:
        exp = base.runExperimentEpi(t, n, m, l, k, kneg, prob, qnum)
        res[str(prob)] = exp
    return(res)

if __name__ == "__main__":   
    # Case 1a, no negated literals in the constraint
    # direct replication of the previous study, Case 1a
    case1a = Case1()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case1a['0.5'], quotas, case1a['0.6'],
             quotas, case1a['0.7'], quotas, case1a['0.8'],
             quotas, case1a['0.9'], quotas, case1a['1.0'])
    plt.legend([r'$p = ' + k + '$' for k in sorted(case1a.keys())], 
                loc = 'upper center', 
                bbox_to_anchor = (0.5, 1.15), ncol = 3, 
                fancybox = True, shadow = True)
    plt.ylim(ymin = 0, ymax = 5)
    plt.ylabel('TR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1a epistemic.png')
    plt.show()
     
#    # Case 1b: all literals in the constraint are negated
    # direct replication of the previous study, Case 1b
    case1b = Case1(kneg = 4)
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case1b['0.5'], quotas, case1b['0.6'],
             quotas, case1b['0.7'], quotas, case1b['0.8'],
             quotas, case1b['0.9'], quotas, case1b['1.0'])
    plt.legend([r'$p = ' + k + '$' for k in sorted(case1b.keys())], 
                loc = 'upper center', 
                bbox_to_anchor = (0.5, 1.15), ncol = 3, 
                fancybox = True, shadow = True)
    plt.ylim(ymin = 0, ymax = 5)
    plt.ylabel('TR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1b epistemic.png')
    plt.show()