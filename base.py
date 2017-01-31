# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:23:19 2016

@author: Kasia
"""

import itertools
import numpy as np
import math

# Basic module: common classes, methods, functions
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
         
         conj = 0
         for clause in const:
             value = max([self.convertToBool(x, ballot) for x in clause])
             conj += value
             
         if conj < len(const):
             return False
         return True

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
            if decision[issue] >= math.ceil(q * noAgents):
                decision[issue] = True
            else:
                decision[issue] = False
        return(Ballot(self.scenario, decision))
        
    def validateDecision(self, decision):
        return(self.constraint.checkRationality(decision))
        
    def printBallots(self, ballots):
        for b in ballots:
            b.printBallot()

        
def model(n, m, l, k, kneg, p, qnum):
    # generate constraint
    constraint = Constraint(m, l, k, kneg)
    scenario = Scenario(m)
    model = Model(scenario, m, constraint)
    ref = model.drawBallotRef()
    ballots = model.drawBallots(ref, n, p)
    rationality = []
    for q in np.linspace(0, 1, qnum):
        decision = model.groupDecision(ballots, q)
        isRational = model.validateDecision(decision)
        rationality.append(isRational)
    return(rationality)


def runExperiment(t, n, m, l, k, kneg, p, qnum):
    results = [[] for _ in range(qnum)]
    for _ in range(t):
        run = model(n, m, l, k, kneg, p, qnum)
        for i in range(qnum):
            results[i].append(run[i])
    RR = [np.mean(q) for q in results]
    return(RR)
    
#RR = []
#
#for _ in range(40000):
#    RR.append(model(10, 4, 1, 4, 0, 0.6, 0.9))
#print(sum(RR)/len(RR))

#c = Constraint(2, 1, 2, 0)
#s = Scenario(2)
#m = Model(s, 10, c)
#ref = m.drawBallotRef()
##print(ref.getNoIssues())
##print(ref.getVote('3'))
#bs = m.drawBallots(ref, 10, 1)
#m.printBallots(bs)
#dec = m.groupDecision(bs, 0)
#dec.printBallot()
#print(c.checkRationality(dec))
#dec1 = m.groupDecision(bs, 0.7)
#dec1.printBallot()
#print(c.checkRationality(dec1))
#dec2 = m.groupDecision(bs, 0.8)
#dec2.printBallot()
#print(c.checkRationality(dec2))
#rat = m.validateDecision(dec, c)
#print(len(bs))
#print('####ref')
#print([x.getChoice() for x in ref.votes])
#print('####alll')
#for x in m.mod:
#    print([v.getChoice() for v in x.votes])
#    print(x.calcHammDist(ref))
#    print(m.calculateProb(x.calcHammDist(ref), 0.7, ref))
# 
#print("####chosen")    
#for x in bs:
#    print([v.getChoice() for v in x.votes])
#    print(x.calcHammDist(ref))
#    print(m.calculateProb(x.calcHammDist(ref), 0.7, ref))
#    
#print('####distribution')
#print([m.calculateProb(b.calcHammDist(ref), 0.7, ref)\
#                                      for b in m.mod])
#distribution = [m.calculateProb(b.calcHammDist(ref), 0.7, ref)\
#                                      for b in m.mod]
#chosen = list(np.random.choice(m.mod, size = 2, p = distribution))
#for x in chosen:
#    print([v.getChoice() for v in x.votes])                                     
#print(len([m.calculateProb(b.calcHammDist(ref), 0.7, ref)\
#                                      for b in m.mod]))
#print(len(m.mod))

#results = [[] for _ in range(11)]
#for _ in range(5):
#    run = model(6, 4, 1, 4, 0, 0.7)
#    print("###run")
#    print(run)
#    for i in range(11):
#        results[i].append(run[i])
#        print("aggregation")
#        print(i)
#        print(results)
#RR = [np.mean(q) for q in results]