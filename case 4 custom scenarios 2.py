# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:41:39 2017

@author: Kasia
"""

# import
import numpy as np
import base
import matplotlib.pyplot as plt
import scipy.stats as stats

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

def Case4b(t = 50, n = 10, m = 4, l = 1, k = 4, kneg = 0, 
           p = np.linspace(0.5, 1, 6), qnum = 11, mu = 0.75, sigma = 0.15):
    lower, upper = 0.5, 1
    dist = stats.truncnorm(
        (lower - mu) / sigma, (upper - mu) / sigma, loc = mu, scale = sigma)
    prob = dist.rvs(n)
    exp = base.runExperimentProb(t, n, m, l, k, kneg, prob, qnum)
    return(exp)

def Case4c(t = 50, n = range(9, 109, 20), m = 4, l = 1, k = 4, kneg = 0, 
           p = np.linspace(0.5, 1, 6), qnum = 11, mu = 0.75, sigma = 1):
    lower, upper = 0.5, 1
    dist = stats.truncnorm(
        (lower - mu) / sigma, (upper - mu) / sigma, loc = mu, scale = sigma)
    res = {}
    for noAgents in n:
        prob = dist.rvs(noAgents)
        exp = base.runExperimentProb(t, noAgents, m, l, k, kneg, prob, qnum)
        res[str(noAgents)] = exp
    return(res)

if __name__ == "__main__":  
    # Case 4b, random distribution of observability
    case4b = Case4b()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case4b)
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 4b.png')
    plt.show()
    
    # Case 4c, sensitivity to number of agents
    case4c = Case4c()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case4c['9'], quotas, case4c['29'],
             quotas, case4c['49'], quotas, case4c['69'],
             quotas, case4c['89'])
    plt.legend([r"$n = " + str(k) + "$" for k in sorted([int(x) for x in case4c.keys()])], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 4c.png')
    plt.show()