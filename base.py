import itertools
import numpy as np
import math

# basic module: common classes, methods, functions
# based on the replicated study

class Issue:
    
    def __init__(self, index):
        self.index = index

class Scenario:
    
    def __init__(self, m):
        self.issues = [Issue(str(x)) for x in range(m)]

    def getAllIssues(self):
        return(self.issues)
        
    def getNoIssues(self):
        return(len(self.issues))

class Vote:
    
    def __init__(self, issue, choice):
        self.issue = issue
        self.choice = choice # True/False
        
    def getIssueIndex(self):
        return(self.issue.index)
        
    def getChoice(self):
        return(self.choice)
  
class Ballot:
    
    def __init__(self, scenario, profile):
        votes = []
        issues = scenario.getAllIssues()
        for i in range(len(issues)):
            votes.append(Vote(issues[i], profile[i]))
        self.votes = votes
        
    def getVote(self, index):
        for vote in self.votes:
            if vote.getIssueIndex() == index:
                return(vote.getChoice())
        return(None)
        
    def getNegVote(self, index):
        return(not self.getVote(index))
        
    def calcHammDist(self, ballotRef):
        # calculate Hamming distance
        dist = 0
        for i in range(len(self.votes)):
            if self.getVote(str(i)) != ballotRef.getVote(str(i)):
                dist += 1
        return(dist)
    
    def getNoIssues(self):
        return(len(self.votes))
        
    def printBallot(self):
        print([v.getChoice() for v in self.votes])
        
class Constraint:
    
    def __init__(self, m, l, k, kneg):
        constraint = []
        for _ in range(l):
            clause = np.random.choice(a = range(m), \
                                         size = k, replace = False)
            clause = list(map(str, clause))
            for i in range(kneg):
                clause[i] = "!" + clause[i]
            constraint.append(clause)
        self.constraint = constraint
    
    def convertToBool(self, strIndex, ballot):
        if '!' not in strIndex:
             return ballot.getVote(strIndex)
        return(ballot.getNegVote(strIndex[1:]))
        
    def checkRationality(self, ballot):
        const = self.constraint
        
        try:
             conj = 0
             for clause in const:
                 value = max([self.convertToBool(x, ballot) for x in clause])
                 conj += value
                 
             if conj < len(const):
                 return False
             return True
        except TypeError:
            ballot.printBallot()
            print(clause)
            raise
     
class ConstraintCustom(Constraint):   
    # constraint uses DNF instead of CNF
    def __init__(self, constraint):
        self.constraint = constraint
        
    def checkRationality(self, ballot):
        const = self.constraint
        
        try:
             dis = 0
             for clause in const:
                 value = min([self.convertToBool(x, ballot) for x in clause])
                 dis += value
                 
             if dis:
                 return True
             return False
        except TypeError:
            ballot.printBallot()
            print(clause)
            raise

class Model:
    
    def __init__(self, scenario, m, constraint):
        self.scenario = scenario
        self.m = m
        profiles = itertools.product(range(2), repeat = m)
        allBallots = [Ballot(scenario, x) for x in profiles]
        allBallots = [x for x in allBallots if constraint.checkRationality(x)]
        self.mod = allBallots
        self.constraint = constraint
    
    def drawBallotRef(self):
        ballotRef = np.random.choice(self.mod)
        return(ballotRef)

    def _prob(self, p, k):
        m = self.m
        return(math.pow(p,m-k)*math.pow(1-p,k))
        
    def calculateProbRat(self, p, ballotRef):
        probRat = 0
        for b in self.mod:
            probRat += self._prob(p, b.calcHammDist(ballotRef))
        return(probRat)
        
    def calculateProb(self, k, p, ballotRef):
        prob = self._prob(p, k)/self.calculateProbRat(p, ballotRef)
        return(prob)
        
    def drawBallots(self, ballotRef, n, p):
        distribution = [self.calculateProb(b.calcHammDist(ballotRef), p, ballotRef)\
                                      for b in self.mod]
        ballots = list(np.random.choice(a = self.mod, size = n, \
                                       p = distribution))                             
        return(ballots)
        
    def groupDecision(self, ballots, q):
        decision = []
        noIssues = self.m
        noAgents = len(ballots)
        for issue in range(noIssues):
            decision.append(sum([x.getVote(str(issue)) for x in ballots]))
            if decision[issue] >= math.ceil(round(q, 2) * noAgents):
                decision[issue] = True
            else:
                decision[issue] = False
        return(Ballot(self.scenario, decision))
        
    def validateDecision(self, decision):
        return(self.constraint.checkRationality(decision))
        
    def printBallots(self, ballots):
        for b in ballots:
            b.printBallot()
    
    def validateDecEpistem(self, decision, ref):
        return(ref.getNoIssues()-decision.calcHammDist(ref))

        
def model(m, l, k, kneg):
    # generate constraint
    constraint = Constraint(m, l, k, kneg)
    scenario = Scenario(m)
    model = Model(scenario, m, constraint)
    return(model)

def modelCustom(m, constraint):
    # generate constraint
    constraint = ConstraintCustom(constraint)
    scenario = Scenario(m)
    model = Model(scenario, m, constraint)
    return(model)


def runExperiment(t, n, m, l, k, kneg, p, qnum):
    results = [[] for _ in range(qnum)]
    mod = model(m, l, k, kneg)
    for _ in range(t):
        ref = mod.drawBallotRef()
        ballots = mod.drawBallots(ref, n, p)
        rationality = []
        for q in np.linspace(0, 1, qnum):
            decision = mod.groupDecision(ballots, q)
            isRational = mod.validateDecision(decision)
            rationality.append(isRational)
        for i in range(qnum):
            results[i].append(rationality[i])
    RR = [np.mean(q) for q in results]
    return(RR)


# runExperiment for epistemic analysis
def runExperimentEpi(t, n, m, l, k, kneg, p, qnum):
    results = [[] for _ in range(qnum)]
    mod = model(n, m, l, k, kneg, p, qnum)
    for _ in range(t):
        ref = mod.drawBallotRef()
        ballots = mod.drawBallots(ref, n, p)
        truth = []
        for q in np.linspace(0, 1, qnum):
            decision = mod.groupDecision(ballots, q)
            isTrue = mod.validateDecEpistem(decision, ref)
            truth.append(isTrue)
        for i in range(qnum):
            results[i].append(truth[i])
    TR = [np.mean(q) for q in results]
    return(TR)  

# run experiment with custom constraint
def runExperimentCustom(t, n, m, constraint, p, qnum):
    results = [[] for _ in range(qnum)]
    mod = modelCustom(m, constraint)
    for _ in range(t):
        ref = mod.drawBallotRef()
        ballots = mod.drawBallots(ref, n, p)
        rationality = []
        for q in np.linspace(0, 1, qnum):
            decision = mod.groupDecision(ballots, q)
            isRational = mod.validateDecision(decision)
            rationality.append(isRational)
        for i in range(qnum):
            results[i].append(rationality[i])
    RR = [np.mean(q) for q in results]
    return(RR)

# override runExperiment for varying probability
def runExperimentProb(t, n, m, l, k, kneg, prob, qnum):
    results = [[] for _ in range(qnum)]
    mod = model(m, l, k, kneg)
    for _ in range(t):
        ref = mod.drawBallotRef()
        ballots = []
        for p in prob:
            ballots.append(mod.drawBallots(ref, 1, p)[0])
        rationality = []
        for q in np.linspace(0, 1, qnum):
            decision = mod.groupDecision(ballots, q)
            isRational = mod.validateDecision(decision)
            rationality.append(isRational)
        for i in range(qnum):
            results[i].append(rationality[i])
    RR = [np.mean(q) for q in results]
    return(RR)

# auxiliary function for aggregating results for different constraints
def aggRes(RR):
    agg = []
    stdev = []
    lower = []
    upper = []
    for i in range(len(RR[0])):
        agg.append(np.mean([r[i] for r in RR]))
        stdev.append(np.std([r[i] for r in RR]))
        lower.append(np.percentile([r[i] for r in RR], 5))
        upper.append(np.percentile([r[i] for r in RR], 95))
    return((agg, stdev, lower, upper))
