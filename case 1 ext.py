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


# Case1, variation analysis
def Case1ext(t = 50, n = 10, m = 4, l = 1, k = 4, kneg = 0, 
           p = 0.5, qnum = 11):
    partRes = []
    for _ in range(100):
        exp = base.runExperiment(t, n, m, l, k, kneg, p, qnum)
        partRes.append(exp)    
    return(base.aggRes(partRes))

if __name__ == "__main__":   
    # Case 1a, only positive literals in the constraint
    case1ext = Case1ext()
    quotas = np.linspace(0, 1, 11)
    plt.errorbar(x = quotas, y = case1ext[0], yerr = case1ext[1])
    plt.legend(["$\pi$ = 0.5"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1a ext 05.png')
    plt.show()
    
    case2ext = Case1ext(p = 0.8)
    plt.errorbar(x = quotas, y = case2ext[0], yerr = case2ext[1])
    plt.legend(["$\pi$ = 0.8"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1a ext 08.png')
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
    plt.savefig('Case 1a ext cint 05.png')
    plt.show()
    
    plt.plot(quotas, case2ext[0], '-', quotas, case2ext[2], '--', quotas, case2ext[3], '--')
    plt.legend(["Mean", "Lower bound", "Upper bound"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1a ext cint 08.png')
    plt.show()
    
    # Case 1b, negative literals in the constraint
    case3ext = Case1ext(kneg = 4)
    plt.errorbar(x = quotas, y = case3ext[0], yerr = case3ext[1])
    plt.legend(["$\pi$ = 0.5"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1b ext 05.png')
    plt.show()
    
    case4ext = Case1ext(p = 0.8, kneg = 4)
    plt.errorbar(x = quotas, y = case4ext[0], yerr = case4ext[1])
    plt.legend(["$\pi$ = 0.8"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1b ext 08.png')
    plt.show()
    
    # 5-95 confidence intervals
    plt.plot(quotas, case3ext[0], '-', quotas, case3ext[2], '--', quotas, case3ext[3], '--')
    plt.legend(["Mean", "Lower bound", "Upper bound"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1b ext cint 05.png')
    plt.show()
    
    plt.plot(quotas, case4ext[0], '-', quotas, case4ext[2], '--', quotas, case4ext[3], '--')
    plt.legend(["Mean", "Lower bound", "Upper bound"], loc = 'lower left')
    plt.ylim(ymax = 1.2)
    plt.ylabel('RR', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.xlabel('q', horizontalalignment = 'right', 
               rotation = 'horizontal', verticalalignment = 'top')
    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
    plt.savefig('Case 1b ext cint 08.png')
    plt.show()