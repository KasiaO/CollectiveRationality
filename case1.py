# import
import numpy as np
import base
import matplotlib.pyplot as plt
import time

# parameters to be set
# t - int - number of runs of the simulation
# n - int - number of agents
# m - int - number of issues
# l - int - number of clauses in the constraint
# k - int - number of literals in each clause
# kneg - int - number of negative literals in each clause
# p - int - probability of a correct vote
# qnum - int - how many quotas on the interval 0 to 1 to consider

# Case1, effect of observability
def Case1(t = 5000, n = 10, m = 4, l = 1, k = 4, kneg = 0, 
           p = np.linspace(0.5, 1, 6), qnum = 11):
    res = {}
    for prob in p:
        exp = base.runExperiment(t, n, m, l, k, kneg, prob, qnum)
        res[str(prob)] = exp
    return(res)

if __name__ == "__main__":   
    # Case 1a, only positive literals in the constraint
    start = time.time()
    case1a = Case1()
    end = time.time()
    print("The simulation took " + str(end - start) + " s to finish.")
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case1a['0.5'], quotas, case1a['0.6'],
             quotas, case1a['0.7'], quotas, case1a['0.8'],
             quotas, case1a['0.9'], quotas, case1a['1.0'])
    plt.legend(["$\pi$ = " + k for k in sorted(case1a.keys())], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1a.png')
    plt.show()
     
    # Case 1b: only negative literals in the constraint
    start2 = time.time()
    case1b = Case1(kneg = 4)
    end2 = time.time()
    print("The simulation took " + str(end2 - start2) + " s to finish.")
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case1b['0.5'], quotas, case1b['0.6'],
             quotas, case1b['0.7'], quotas, case1b['0.8'],
             quotas, case1b['0.9'], quotas, case1b['1.0'])
    plt.legend(["$\pi$ = " + k for k in sorted(case1b.keys())], loc = 'lower right')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1b.png')
    plt.show()

    