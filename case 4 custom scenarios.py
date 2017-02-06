# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:45:11 2017

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

# Case4, more realistic scenarios

# accept one and only one issue
def Case4a(t = 50, n = 10, m = 3, 
           constraint = [['!0', '!1'], ['!1', '!2'], 
                         ['!0', '!2'], ['0', '1', '2']], 
           p = np.linspace(0.5, 1, 6), qnum = 11):
    res = {}
    for prob in p:
        exp = base.runExperimentCustom(t, n, m, constraint, prob, qnum)
        res[str(prob)] = exp
    return(res)

def Case4sens(t = 5, n = 10, m = 3, 
           constraint = [['!0', '!1'], ['!1', '!2'], 
                         ['!0', '!2'], ['0', '1', '2']], 
           p = 0.5, qnum = 11):
    partRes = []
    for _ in range(10):
        exp = base.runExperimentCustom(t, n, m, constraint, p, qnum)
        partRes.append(exp)    
    return(base.aggRes(partRes))

if __name__ == "__main__":   
    # Case 4a, no negated literals in the constraint
    # direct replication of the previous study, Case 1a
    case4a = Case4a()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case4a['0.5'], quotas, case4a['0.6'],
             quotas, case4a['0.7'], quotas, case4a['0.8'],
             quotas, case4a['0.9'], quotas, case4a['1.0'])
    plt.legend([r'$p = ' + k + '$' for k in sorted(case4a.keys())], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 4a.png')
    plt.show()
    
    # Case 4a, sensitivity analysis
    case4sens = Case4sens()
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case4sens[0], yerr = case4sens[1])
    plt.legend(["p = 0.5"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 4a sensitivity.png')
    plt.show()
    
    # Case 1a, no negated literals in the constraint
    # direct replication of the previous study, Case 1a
    case4sens2 = Case4sens(p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case4sens2[0], yerr = case4sens2[1])
    plt.legend(["p = 0.8"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 4a sensitivity 2.png')
    plt.show()