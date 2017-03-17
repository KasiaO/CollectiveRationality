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

# Case2, variation analysis
def Case2ext(t = 50, n = 89, m = 4, l = 1, k = 4, kneg = 0, 
           p = 0.5, qnum = 11):
    partRes = []
    for _ in range(100):
        exp = base.runExperiment(t, n, m, l, k, kneg, p, qnum)
        partRes.append(exp)    
    return(base.aggRes(partRes))

if __name__ == "__main__":   
    # Case 2a, only positive literals in the constraint    
    # error bars for n = 89
    case1ext = Case2ext()
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case1ext[0], yerr = case1ext[1])
    plt.legend(["n = 89"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2a ext 89.png')
    plt.show()
    
    # error bars for n = 29
    case2ext = Case2ext(n = 29)
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case1ext[0], yerr = case1ext[1])
    plt.legend(["n = 89"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2a ext 29.png')
    plt.show()
    
    # 5-95 confidence intervals
    plt.plot(quotas, case1ext[0], '-', quotas, case1ext[2], '--', quotas, case1ext[3], '--')
    plt.legend(["Mean", "Lower bound", "Upper bound"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2a ext cint 89.png')
    plt.show()
    
    plt.plot(quotas, case2ext[0], '-', quotas, case2ext[2], '--', quotas, case2ext[3], '--')
    plt.legend(["Mean", "Lower bound", "Upper bound"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 2a ext cint 29.png')
    plt.show()