# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:47:48 2017

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
    stdev = []
    for i in range(len(RR[0])):
        agg.append(np.mean([r[i] for r in RR]))
        stdev.append(np.std([r[i] for r in RR]))
    return((agg, stdev))

# Case3, replication of previous study
def Case1ext(t = 500, n = 10, m = 4, l = 1, k = 4, kneg = 0, 
           p = 0.5, qnum = 11):
    partRes = []
    for _ in range(10):
        exp = base.runExperiment(t, n, m, l, k, kneg, p, qnum)
        partRes.append(exp)    
    return(aggRes(partRes))

if __name__ == "__main__":   
    # Case 1a, no negated literals in the constraint
    # direct replication of the previous study, Case 1a
    case1ext = Case1ext()
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case1ext[0], yerr = case1ext[1])
    plt.legend(["p = 0.5"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1 ext.png')
    plt.show()
    
    # Case 1a, no negated literals in the constraint
    # direct replication of the previous study, Case 1a
    case2ext = Case1ext(p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case2ext[0], yerr = case2ext[1])
    plt.legend(["p = 0.8"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2 ext.png')
    plt.show()
    
    # Case 1b, negated literals in the constraint
    # direct replication of the previous study, Case 1a
    case3ext = Case1ext(kneg = 4)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case3ext[0], yerr = case3ext[1])
    plt.legend(["p = 0.5"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 3 ext.png')
    plt.show()
    
    case4ext = Case1ext(p = 0.8, kneg = 4)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case4ext[0], yerr = case4ext[1])
    plt.legend(["p = 0.8"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 4 ext.png')
    plt.show()
    
    # Case3, replication of previous study
    case5ext = Case1ext(l = 2, k = 2, kneg = 2)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case5ext[0], yerr = case5ext[1])
    plt.legend(["p = 0.5"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 5 ext.png')
    plt.show()
    
    case6ext = Case1ext(l = 2, k = 2, kneg = 2, p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case6ext[0], yerr = case6ext[1])
    plt.legend(["p = 0.8"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 6 ext.png')
    plt.show()
    
    # Case3, replication of previous study
    case7ext = Case1ext(l = 2, k = 2, kneg = 0)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case7ext[0], yerr = case7ext[1])
    plt.legend(["p = 0.5"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 7 ext.png')
    plt.show()
    
    case8ext = Case1ext(l = 2, k = 2, kneg = 2, p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case8ext[0], yerr = case8ext[1])
    plt.legend(["p = 0.8"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 7 ext.png')
    plt.show()