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
def Case1epi_ext(t = 5000, n = 10, m = 4, l = 1, k = 4, kneg = 0, 
           p = 0.5, qnum = 11):
    exp = base.runExperimentEpiSP(t, n, m, l, k, kneg, p, qnum)
    return(exp)

if __name__ == "__main__":   
    # Case 1a, no negated literals in the constraint
    # direct replication of the previous study, Case 1a
    case1a = Case1epi_ext()
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case1a[1:], quotas, case1a[:1]*11)
    plt.legend([r'voters $\pi = 0.5$', 'SP $\pi = 0.5$'], 
                loc = 'upper center', 
                bbox_to_anchor = (0.5, 1.15), ncol = 3, 
                fancybox = True)
    plt.ylim(ymin = 0, ymax = 1.2)
    plt.ylabel('TR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1a epistemic soc 05.png')
    plt.show()
     
#    # Case 1b: all literals in the constraint are negated
    # direct replication of the previous study, Case 1b
    case1b = Case1epi_ext(p = 0.8)
    quotas = np.linspace(0, 1, 11)
    plt.plot(quotas, case1b[1:], quotas, case1b[:1]*11)
    plt.legend([r'voters $\pi = 0.8$', 'SP $\pi = 0.8$'], 
                loc = 'upper center', 
                bbox_to_anchor = (0.5, 1.15), ncol = 3, 
                fancybox = True)
    plt.ylim(ymin = 0, ymax = 1.2)
    plt.ylabel('TR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1a epistemic soc 08.png')
    plt.show()

