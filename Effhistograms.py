#Author:Sheena C Schier
#Last change 01Dec16: Added TTbarNNLOWeight factor to total weight, added plots of nvtx, and electron/muon pts separately, changed hisograms bins
#Feb 2017, created version for CMS signal and control regions
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?
from CMSobservables import *
from renormalize import *


#------------------------------------------------------------------
class lephists:
    def __init__(self, tag, topdir, isdata, treetype, DSID, sumWHist, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.sumWHist = sumWHist
        self.hists={}
        self.detaillevel=detaillevel

        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        self.hists["Rll"]=ROOT.TH1F("h_"+tag+"_Rll",tag+"_Rll; #DeltaR_{lep_{1}-lep_{2}} [mm];Events/(0.1 mm)",40, 0., 4.0)
        self.hists["Ptll"]=ROOT.TH1F("h_"+tag+"_Ptll",tag+"_Ptll; dilepton p_{T} [GeV]; Events/(2 GeV)",30, 0, 60)
        self.hists["Mll"]=ROOT.TH1F("h_"+tag+"_Mll",tag+"_Mll; dilepton invariant mass [GeV]; Events/(2 GeV) ",30, 0, 60)

        topdir.cd()
        self.collections={}

    def write(self):
        self.newdir.cd()
        for i,k in self.hists.iteritems():
            k.SetOption("HIST")
            k.Write()
        for i,k in self.collections.iteritems():
            k.write()
        self.topdir.cd()

    def add(self, coll):
        for i,k in self.hists.iteritems():
            if i in coll.hists: k.Add(coll.hists[i])
        for i,k in self.collections.iteritems():
            if i in coll.collections: k.add(coll.collections[i])

    def fill(self, event):
        #print 'this is the DSID: %s' % self.DSID
        weight=float(1.0)
        totalWeight=float(1.0)
        #intLumi = 36300.0 #Same as used by Lorenzo Rossini
        intLumi = 1.0

        nLep_base = event.nLep_base
        #Initialize TLorentz vectors
        lep1Vec = ROOT.TLorentzVector()
        lep2Vec = ROOT.TLorentzVector()

        #Prefer opposite sign lepton pairs over same sign pairs
        obs = observable()
        lep1Vec, lep1Charge, lep1Flavor = obs.getLep1TLVChargeFlavor(event)
        lep2Vec, lep2Charge, lep2Flavor = obs.getLep2TLVChargeFlavor(event)


        #Calculate dilepton variables
        lepPairVec = lep1Vec + lep2Vec
        mll = lepPairVec.M()
        ptll = lepPairVec.Pt()
        drll = -999.
        if nLep_base > 1:
            drll  = lep2Vec.DeltaR(lep1Vec)

        #Recalculate generator weight
        newNorm = renorm(self.sumWHist, event)
        if self.isdata:
            genWeight = 1.0
        else:
            genWeight = newNorm.getGenWeight(intLumi)
        #genWeight = event.genWeight

        #Calculating weight
        if self.isdata:
            totalWeight = 1.0
        else:
            totalWeight = float(event.SherpaVjetsNjetsWeight*event.ttbarNNLOWeight*event.pileupWeight*event.eventWeight*event.leptonWeight*event.jvtWeight*event.bTagWeight*genWeight) #TODO: NO TRIGGER WEIGHT!!

        self.hists["Rll"].Fill(float(drll), totalWeight)
        self.hists["Ptll"].Fill(float(ptll), totalWeight)
        self.hists["Mll"].Fill(float(mll), totalWeight)


#------------------------------------------------------------------
class triggerhists:
    def __init__(self, tag, topdir, isdata, treetype, DSID, sumWHist, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.sumWHist = sumWHist
        self.hists={}
        self.detaillevel=detaillevel

        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        self.hists["MET"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/25 GeV)",24 ,0,600)

        topdir.cd()
        self.collections={}

    def write(self):
        self.newdir.cd()
        for i,k in self.hists.iteritems():
            k.SetOption("HIST")
            k.Write()
        for i,k in self.collections.iteritems():
            k.write()
        self.topdir.cd()

    def add(self, coll):
        for i,k in self.hists.iteritems():
            if i in coll.hists: k.Add(coll.hists[i])
        for i,k in self.collections.iteritems():
            if i in coll.collections: k.add(coll.collections[i])

    def fill(self, event):
        #print 'this is the DSID: %s' % self.DSID
        weight=float(1.0)
        totalWeight=float(1.0)
        #intLumi = 36300.0 #Same as used by Lorenzo Rossini
        intLumi = 1.0

        #Get variables from tree for filling histogram
        MET=event.met_Et

        genWeight = event.genWeight

        #Calculating weight
        if self.isdata:
            totalWeight = 1.0
        else:
            totalWeight = float(event.SherpaVjetsNjetsWeight*event.ttbarNNLOWeight*event.pileupWeight*event.eventWeight*event.leptonWeight*event.jvtWeight*event.bTagWeight*genWeight) #TODO: NO TRIGGER WEIGHT!!

        self.hists["MET"].Fill(float(MET), totalWeight)


    #TODO:Finish




#------------------------------------------------------------------
class histcollection:
    def __init__(self, tag, topdir, debug, isdata, treetype, DSID, sumWHist, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        if debug: 
            print "topdir"
            print topdir.GetName()
        self.isdata = isdata
        self.tree = treetype
        self.DSID = DSID
        self.sumWHist = sumWHist
        self.detaillevel=detaillevel

        newdir = self.newdir=topdir.mkdir(tag)
        if debug:
            print "newdir"
            print newdir.GetName()
        self.newdir.cd()
        self.collections={}
        self.topdir.cd()

    def write(self):
        self.newdir.cd()
        for i,k in self.collections.iteritems():
            k.write()
        self.topdir.cd()

    def addtriggercollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=triggerhists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.DSID, self.sumWHist, self.detaillevel)
        self.topdir.cd()

    def addleptoncollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=lephists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.DSID, self.sumWHist, self.detaillevel)
        self.topdir.cd()

    def add(self, coll):
        for i,k in self.collections.iteritems():
            if i in coll: k.add(coll[i])

    def fill(self, event):
        for i,k in self.collections.iteritems():
            k.fill(event)

    def fill(self, event, tag):
        for i,k in self.collections.iteritems():
            if i==tag:
                k.fill(event)
                break
