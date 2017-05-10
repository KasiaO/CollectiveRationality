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
def Case2ext(t = 5000, n = 10, m = 4, l = 1, k = 4, kneg = 0, 
           prob = [0.5, 0.8], props = [[1,0], [0.7, 0.3], [0.5, 0.5], 
                   [0.3, 0.7], [0, 1]], qnum = 11):
    res = {}
    for prop in props:
        exp = base.runExperimentProbEpi(t, n, m, l, k, kneg, prob, prop, qnum)
        res[str(prop[0])] = exp
    return(res)

if __name__ == "__main__":   
    # Case 2a, no negated literals in the constraint
    # direct replication of the previous study, Case 2a
    case2a = Case2ext()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case2a['0'], quotas, case2a['0.3'],
             quotas, case2a['0.5'], quotas, case2a['0.7'], 
             quotas, case2a['1'])
    plt.legend([r'$prop = ' + str(k) + '$' for k in sorted([float(x) for x in case2a.keys()])], 
                loc = 'upper center', 
                bbox_to_anchor = (0.5, 1.15), ncol = 3, 
                fancybox = True)
    plt.ylim(ymin = 0, ymax = 1.2)
    plt.ylabel('TR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2a epistemic var prob.png')
    plt.show()
    
