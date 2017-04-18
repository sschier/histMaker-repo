
import ROOT
from ROOT import TString
ROOT.gROOT.SetBatch(True)
 #------------------------------------------------------------------
class renorm:
    def __init__(self, weights, event):

        self.variables={}
        self.weights = weights
        self.event = event

    def getSumOfWeights(self):
        dsn = str (self.event.DatasetNumber)
        iBin = self.weights.GetXaxis().FindBin(dsn)
        sumOfWeights = self.weights.GetBinContent(iBin)
        return sumOfWeights


    def getDics(self):
        xdict = {}
        brdict = {}
        efdict = {}
        f = open('/export/share/dirac/sschier/HistMaker/Higgsino_analysis/MGPy8EG_A14N23LO_Higgsino_MERGE.txt', 'r')
        for line in f:
            if line.startswith('#'): 
                continue
            else:
                xdict[line.split()[0]] = line.split()[2]
                brdict[line.split()[0]] = line.split()[3]
                efdict[line.split()[0]] = line.split()[4]
        return xdict, brdict, efdict


    def getSignalXS(self):
        signalXS = 0.0
        XSdict, BRdict, EFdict = self.getDics()
        dsn = str (self.event.DatasetNumber)
        if dsn not in XSdict:
            print "Missing signal sample information"
        else:
            xsec = float (XSdict[dsn])
            bratio = float (BRdict[dsn])
            eff = float (EFdict[dsn])
            signalXS = xsec*bratio*eff
            #print "old_xsec = %f" % xsec
            #print "BR = %f" % bratio
            #print "merge*filter eff = %f" % eff
        return signalXS


    def getGenWeight(self, lumi):
        genWeight = 0.0
        intLumi = float (lumi)
        dataset = self.event.DatasetNumber
        sumOfWeights = float (self.getSumOfWeights())
        if self.event.xsec == -1:
            xsec = self.getSignalXS() 
        else: xsec = self.event.xsec
        #print "dataset = %i" % dataset 
        #print "lumi = %f" % intLumi
        #print "new_xsec = %f" % xsec
        #print "sumW = %f" % sumOfWeights

        genWeight = float (lumi*xsec)/sumOfWeights

        return genWeight





