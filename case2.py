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

# Case2, replication of previous study
def Case2(t = 5000, n = range(9, 109, 20), m = 4, l = 1, k = 4, kneg = 0, 
           p = 0.5, qnum = 11):
    res = {}
    for noAgents in n:
        exp = base.runExperiment(t, noAgents, m, l, k, kneg, p, qnum)
        res[str(noAgents)] = exp
    return(res)

if __name__ == "__main__":   
    # Case 2a, only positive literals in the constraint
    case2a = Case2()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case2a['9'], quotas, case2a['29'],
             quotas, case2a['49'], quotas, case2a['69'],
             quotas, case2a['89'])
    plt.legend(["n = " + str(k) for k in sorted([int(x) for x in case2a.keys()])], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2a.png')
    plt.show()
    
    case2b = Case2(p = 0.8)
    plt.plot(quotas, case2b['9'], quotas, case2b['29'],
             quotas, case2b['49'], quotas, case2b['69'],
             quotas, case2b['89'])
    plt.legend(["n = " + str(k) for k in sorted([int(x) for x in case2b.keys()])], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2b.png')
    plt.show()
    
    # constraint with negative literals
    # not shown in the study
    case2c = Case2(p = 0.8, kneg = 4)
    plt.plot(quotas, case2c['9'], quotas, case2c['29'],
             quotas, case2c['49'], quotas, case2c['69'],
             quotas, case2c['89'])
    plt.legend(["n = " + str(k) for k in sorted([int(x) for x in case2c.keys()])], loc = 'lower right')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2c.png')
    plt.show()