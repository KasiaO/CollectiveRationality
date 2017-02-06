# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:32:58 2017

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

# auxiliary function for aggregating results for different constraints
def aggRes(RR):
    agg = []
    for i in range(len(RR[0])):
        agg.append(np.mean([r[i] for r in RR]))
    return(agg)

# Case3, replication of previous study
def Case3(t = 100, n = 10, m = 4, l = 2, k = 2, kneg = [0, 1, 2], 
           p = 0.5, qnum = 11):
    res = {}
    for kNeg in kneg:
        partRes = []
        for _ in range(5):
            exp = base.runExperimentEpi(t, n, m, l, k, kNeg, p, qnum)
            partRes.append(exp)    
        res[str(max(kneg) - kNeg)] = aggRes(partRes)
    return(res)

if __name__ == "__main__":   
    # Case 3, mixed clauses
    # direct replication of the previous study
    case3a = Case3()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case3a['0'], quotas, case3a['1'],
             quotas, case3a['2'])
    plt.legend(["k+ = " + str(k) for k in sorted([int(x) for x in case3a.keys()])], loc = 'lower center')
    plt.ylim(ymax = 5)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 3a.png')
    plt.show()
    
    case3b = Case3(p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case3b['0'], quotas, case3b['1'],
             quotas, case3b['2'])
    plt.legend(["k+ = " + str(k) for k in sorted([int(x) for x in case3b.keys()])], loc = 'lower center')
    plt.ylim(ymax = 5)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 3b.png')
    plt.show()
    
    case3c = Case3(m = 6, l = 2, k = 3, kneg = [0, 1, 2, 3])
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case3c['0'], quotas, case3c['1'],
             quotas, case3c['2'], quotas, case3c['3'])
    plt.legend(["k+ = " + str(k) for k in sorted([int(x) for x in case3c.keys()])], loc = 'lower center')
    plt.ylim(ymax = 7)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 3c.png')
    plt.show()
    
    case3d = Case3(m = 6, l = 2, k = 3, kneg = [0, 1, 2, 3], p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case3d['0'], quotas, case3d['1'],
             quotas, case3d['2'], quotas, case3d['3'])
    plt.legend(["k+ = " + str(k) for k in sorted([int(x) for x in case3d.keys()])], loc = 'lower center')
    plt.ylim(ymax = 7)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 3d.png')
    plt.show()
    
    case3e = Case3(l = 2, k = 3, kneg = [0, 1, 2, 3])
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case3e['0'], quotas, case3e['1'],
             quotas, case3e['2'], quotas, case3e['3'])
    plt.legend(["k+ = " + str(k) for k in sorted([int(x) for x in case3e.keys()])], loc = 'lower center')
    plt.ylim(ymax = 5)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 3e.png')
    plt.show()
    
    case3f = Case3(l = 2, k = 3, kneg = [0, 1, 2, 3], p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case3f['0'], quotas, case3f['1'],
             quotas, case3f['2'], quotas, case3f['3'])
    plt.legend(["k+ = " + str(k) for k in sorted([int(x) for x in case3f.keys()])], loc = 'lower center')
    plt.ylim(ymax = 5)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 3f.png')
    plt.show()