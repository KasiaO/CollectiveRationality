import numpy as np
import base
import matplotlib.pyplot as plt

if __name__ == "__main__":
    probs = [0.67, 0.69, 0.63, 0.88, 0.83, 0.82, 0.8, 0.78, 0.76]
    qnum = 11
    t = 5000
    # case 1 for custom probabilities
    m1 = 4
    l1 = 1
    k1 = 4
    kneg1 = 0
    n1 = 9
#    res1 = base.runExperimentProb(t, n1, m1, l1, k1, kneg1, probs, qnum)
#    resEpi1 = base.runExperimentProbEpi(t, n1, m1, l1, k1, kneg1, probs, 
#                                        [1/9 for _ in range(9)], qnum)
    resEpiWorst1 = base.runExperimentEpi(t, 1, m1, l1, k1, kneg1, min(probs), qnum)
    resEpiBest1 = base.runExperimentEpi(t, 1, m1, l1, k1, kneg1, max(probs), qnum)
#    quotas = np.linspace(0, 1, 11)
#    plt.plot(quotas, res1, quotas, resEpi1)
#    plt.legend(['RR', 'TR'], 
#                loc = 'upper center', 
#                bbox_to_anchor = (0.5, 1.15), 
#                ncol = 2,
#                fancybox = True)
#    plt.ylim(ymax = 1.2)
#    plt.ylabel('RR/TR', horizontalalignment = 'right',
#               rotation = 'horizontal', verticalalignment = 'top')
#    plt.xlabel('q', horizontalalignment = 'right',
#               rotation = 'horizontal', verticalalignment = 'top')
#    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
#    plt.savefig('custom case 1.png')
#    plt.show()
#    
#    # custom scenario
    m2 = 4
    constraint2 = [['!0', '!1', '!2', '3'], ['!0', '!1', '2', '!3'],
                  ['!0', '1', '!2', '!3'], ['0', '!1', '!2', '!3']]
#    res2 = base.runExperimentDNF(t, m2, constraint2, probs, qnum)
#    
#    # epistemic analysis
#    resEpi2 = base.runExperimentProbEpiDNF(t, m2, constraint2, probs, qnum)
    resEpiWorst2 = base.runExperimentProbEpiDNF(t, m2, constraint2, 
                                                [min(probs)], qnum)
    resEpiBest2 = base.runExperimentProbEpiDNF(t, m2, constraint2, 
                                               [max(probs)], qnum)
#    quotas = np.linspace(0, 1, 11)
#    plt.plot(quotas, res2, quotas, resEpi2)
#    plt.legend(['RR', 'TR'], loc = 'upper center', 
#                bbox_to_anchor = (0.5, 1.15), 
#                ncol = 2,
#                fancybox = True)
#    plt.ylim(ymax = 1.2)
#    plt.ylabel('RR/TR', horizontalalignment = 'right',
#               rotation = 'horizontal', verticalalignment = 'top')
#    plt.xlabel('q', horizontalalignment = 'right',
#               rotation = 'horizontal', verticalalignment = 'top')
#    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
#    plt.savefig('custom case 2.png')
#    plt.show()
#
#    # different constraint
#    constraint3 = [['!0'], ['1'], ['2']]
#    m3 = 3
#    
#    # custom scenario
#    res3 = base.runExperimentDNF(t, m3, constraint3, probs, qnum)
#    
#    # epistemic analysis
#    resEpi3 = base.runExperimentProbEpiDNF(t, m3, constraint3, probs, qnum)
#    
#    plt.plot(quotas, res3, quotas, resEpi3)
#    plt.legend(['RR', 'TR'], loc = 'upper center', 
#                bbox_to_anchor = (0.5, 1.15), 
#                ncol = 2,
#                fancybox = True)
#    plt.ylim(ymax = 1.2)
#    plt.ylabel('RR/TR', horizontalalignment = 'right',
#               rotation = 'horizontal', verticalalignment = 'top')
#    plt.xlabel('q', horizontalalignment = 'right',
#               rotation = 'horizontal', verticalalignment = 'top')
#    plt.grid(b = True, which = 'both', color = '0.65', linestyle = '-')
#    plt.savefig('custom case 3.png')
#    plt.show()