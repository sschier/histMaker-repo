#!/usr/bin/env python
#Author: Sheena C Schier
#Created 01April2017 Created to make trigger efficiency plots
#Intended to run on signal only


import sys, os, subprocess, getopt
import re, time, copy, math, array
import argparse, commands
import ROOT
from ROOT import TString
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?

#local imports
from Effhistograms import *
from CMSobservables import *
from renormalize import *


#======================================================================
def baseLeptonEE(event, hc, CutsDict):
    if( CutsDict["2BaseLep"] == True and CutsDict["eeEvent"] == True ):
        hc.fill(event, "skim")
        return True
    else: return False
#======================================================================
def baseLeptonMM(event, hc, CutsDict):
    if( CutsDict["2BaseLep"] == True and CutsDict["mumuEvent"] == True ):
        hc.fill(event, "skim")
        return True
    else: return False
#======================================================================
def baseLeptonEM(event, hc, CutsDict):
    if( CutsDict["2BaseLep"] == True and CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False ):
        hc.fill(event, "skim")
        return True
    else: return False
#======================================================================
def signalLeptonEE(event, hc, CutsDict):
    if( CutsDict["2SigLep"] == True and CutsDict["eeEvent"] == True ):
        hc.fill(event, "skim")
        return True
    else: return False
#======================================================================
def signalLeptonMM(event, hc, CutsDict):
    if( CutsDict["2SigLep"] == True and CutsDict["mumuEvent"] == True ):
        hc.fill(event, "skim")
        return True
    else: return False
#======================================================================
def signalLeptonEM(event, hc, CutsDict):
    if( CutsDict["2SigLep"] == True and CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False ):
        hc.fill(event, "skim")
        return True
    else: return False
#======================================================================



#======================================================================

def CMSEWsignalEE(event, hc, CutsDict):

    #if( CutsDict["eeEvent"] == True and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["eeEvent"] == True ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        if CutsDict["Jet105"] == False:
            return False
        hc.fill(event, "jet105")

        if CutsDict["Jet145"] == False:
            return False
        hc.fill(event, "jet145")

        return True

    
    else: return False
#======================================================================

def CMSEWsignalMM(event, hc, CutsDict):

    #if( CutsDict["mumuEvent"] == True and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["mumuEvent"] == True ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        if CutsDict["Jet105"] == False:
            return False
        hc.fill(event, "jet105")

        if CutsDict["Jet145"] == False:
            return False
        hc.fill(event, "jet145")

        return True


    else: return False
#======================================================================

def CMSEWsignalEM(event, hc, CutsDict):

    #if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        if CutsDict["Jet105"] == False:
            return False
        hc.fill(event, "jet105")

        if CutsDict["Jet145"] == False:
            return False
        hc.fill(event, "jet145")

        return True

    
    else: return False
#======================================================================

def CMSEWsignalDimuTriggerEE(event, hc, CutsDict):

    if( CutsDict["dimuTrigger"] == False ):
        return False
    #if( CutsDict["eeEvent"] == True and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["eeEvent"] == True ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True
    
    else: return False

#======================================================================

def CMSEWsignalDimuTriggerMM(event, hc, CutsDict):

    if CutsDict["dimuTrigger"] == False:
        return False
    #if( CutsDict["mumuEvent"] == True and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["mumuEvent"] == True ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    
    else: return False

#======================================================================

def CMSEWsignalDimuTriggerEM(event, hc, CutsDict):

    if CutsDict["dimuTrigger"] == False:
        return False
    #if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False

#======================================================================

def CMSEWsignalSingleMuTriggerEE(event, hc, CutsDict):

    if CutsDict["muTrigger"] == False:
        return False
    #if( CutsDict["eeEvent"] == True and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["eeEvent"] == True ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False
#======================================================================

def CMSEWsignalSingleMuTriggerMM(event, hc, CutsDict):

    if CutsDict["muTrigger"] == False:
        return False
    #if( CutsDict["mumuEvent"] == True and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["mumuEvent"] == True ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False
#======================================================================

def CMSEWsignalSingleMuTriggerEM(event, hc, CutsDict):

    if CutsDict["muTrigger"] == False:
        return False
    #if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False
#======================================================================

def CMSEWsignalMetTriggerEE(event, hc, CutsDict):

    if CutsDict["metTrigger"] == False:
        return False
    #if( CutsDict["eeEvent"] == True and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["eeEvent"] == True ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False
#======================================================================

def CMSEWsignalMetTriggerMM(event, hc, CutsDict):

    if CutsDict["metTrigger"] == False:
        return False
    #if( CutsDict["mumuEvent"] == True and CutsDict["RunNewTriggers"] == False ): 
    if( CutsDict["mumuEvent"] == True ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True
    
    else: return False
#======================================================================

def CMSEWsignalMetTriggerEM(event, hc, CutsDict):

    if CutsDict["metTrigger"] == False:
        return False
    if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False ): 
    #if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False and CutsDict["RunNewTriggers"] == False ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False
#======================================================================
#======================================================================

def CMSEWsignalORTriggerEE(event, hc, CutsDict):

    if CutsDict["ORTrigger"] == False:
        return False
    if( CutsDict["eeEvent"] == True ): 
    #if( CutsDict["eeEvent"] == True and CutsDict["RunNewTriggers"] == False ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False
#======================================================================

def CMSEWsignalORTriggerMM(event, hc, CutsDict):

    if CutsDict["ORTrigger"] == False:
        return False
    if( CutsDict["mumuEvent"] == True ): 
    #if( CutsDict["mumuEvent"] == True and CutsDict["RunNewTriggers"] == False ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False
#======================================================================

def CMSEWsignalORTriggerEM(event, hc, CutsDict):

    if CutsDict["ORTrigger"] == False:
        return False
    if( CutsDict["mumuEvent"] == False  and CutsDict["eeEvent"] == False ): 
    #if( CutsDict["mumuEvent"] == False and CutsDict["eeEvent"] == False and CutsDict["RunNewTriggers"] == False ): 

        hc.fill(event, "skim")
        if CutsDict["2SigLep"] == False:
            return False
        if CutsDict["1Jet25"] == False:
            return False
        hc.fill(event,"signal")
        if CutsDict["opSign"] == False:
            return False
        hc.fill(event, "opSign")
        if CutsDict["METoverHt"] == False:
            return False
        if CutsDict["HT100"] == False:
            return False
        if CutsDict["ptll3"] == False:
            return False
        if CutsDict["4mll60"] == False:
            return False
        if CutsDict["lepPt30"] == False:
            return False
        if CutsDict["bVeto"] == False:
            return False
        if CutsDict["70MtLepMET"] == False:
            return False
        if CutsDict["Mtautau"] == False:
            return False
        hc.fill(event, "mtautau")

        return True

    else: return False
#======================================================================
#======================================================================
#
def analyze(infile, weightfile, tree, DSID, data, signal, outfile, debug, region):

    if debug: print "opening input file"

    f=ROOT.TFile(infile, "RO")
    fw=ROOT.TFile(weightfile, "RO")

    if debug: print f.GetName()

    #get sum of weights hist
    #if data: sumWhist = f.Get("weighted__AOD")
    #elif signal: sumWhist = f.Get("weighted__AOD")
    #else: sumWhist = fw.Get("weighted__AOD")
    #print sumWhist.GetName()

    if data:
        t=f.Get("%s" %tree)
        sumWhist = fw.Get("weighted__AOD")
    else:
        t=f.Get("%s_NoSys" % tree) 
        sumWhist = f.Get("weighted__AOD") 


    if debug: print t.GetName()

    t.SetBranchStatus("trigWeight_metTrig", 0)
    t.SetBranchStatus("trigMatch_metTrig", 1)
    t.SetBranchStatus("trigWeight_singleMuonTrig", 0)
    t.SetBranchStatus("trigMatch_singleMuonTrig", 1)
    t.SetBranchStatus("trigWeight_singleElectronTrig", 0)
    t.SetBranchStatus("trigMatch_singleElectronTrig", 1)
    t.SetBranchStatus("HLT_2mu4_j85_xe50_mht_emul", 1)
    t.SetBranchStatus("HLT_mu4_j125_xe90_mht_emul", 1)
    t.SetBranchStatus("mu",1) 
    t.SetBranchStatus("nVtx",1) 
    t.SetBranchStatus("nLep_base",1)
    t.SetBranchStatus("nLep_signal",1) 
    t.SetBranchStatus("lep1Flavor",1) 
    t.SetBranchStatus("lep1Charge",1) 
    t.SetBranchStatus("lep1Pt",1) 
    t.SetBranchStatus("lep1Eta",1) 
    t.SetBranchStatus("lep1Phi",1) 
    t.SetBranchStatus("lep1M",1) 
    t.SetBranchStatus("lep1D0",1) 
    t.SetBranchStatus("lep1D0Sig",1) 
    t.SetBranchStatus("lep1Z0",1) 
    t.SetBranchStatus("lep1Z0SinTheta",1) 
    t.SetBranchStatus("lep1PassOR",1) 
    t.SetBranchStatus("lep1Type",1) 
    t.SetBranchStatus("lep1Origin",1) 
    t.SetBranchStatus("lep1NPix",0) 
    t.SetBranchStatus("lep1PassBL",0) 
    t.SetBranchStatus("lep1VeryLoose",0) 
    t.SetBranchStatus("lep1Loose",0) 
    t.SetBranchStatus("lep1Medium",0) 
    t.SetBranchStatus("lep1Tight",0) 
    t.SetBranchStatus("lep1IsoLoose",0) 
    t.SetBranchStatus("lep1IsoTight",0) 
    t.SetBranchStatus("lep1IsoGradient",0) 
    t.SetBranchStatus("lep1IsoGradientLoose",0) 
    t.SetBranchStatus("lep1IsoLooseTrackOnly",0) 
    t.SetBranchStatus("lep1IsoFixedCutLoose",0) 
    t.SetBranchStatus("lep1IsoFixedCutTight",0) 
    t.SetBranchStatus("lep1IsoFixedCutTightTrackOnly",0) 
    t.SetBranchStatus("lep1Ptcone20",0) 
    t.SetBranchStatus("lep1Ptcone30",0) 
    t.SetBranchStatus("lep1Ptcone40",0) 
    t.SetBranchStatus("lep1Signal",1) 
    t.SetBranchStatus("lep1MatchesTrigger",1) 
    t.SetBranchStatus("lep2Flavor",1) 
    t.SetBranchStatus("lep2Charge",1) 
    t.SetBranchStatus("lep2Pt",1) 
    t.SetBranchStatus("lep2Eta",1) 
    t.SetBranchStatus("lep2Phi",1) 
    t.SetBranchStatus("lep2M",1) 
    t.SetBranchStatus("lep2D0",1) 
    t.SetBranchStatus("lep2D0Sig",1) 
    t.SetBranchStatus("lep2Z0",1) 
    t.SetBranchStatus("lep2Z0SinTheta",1) 
    t.SetBranchStatus("lep2PassOR",1) 
    t.SetBranchStatus("lep2Type",1) 
    t.SetBranchStatus("lep2Origin",1) 
    t.SetBranchStatus("lep2NPix",0) 
    t.SetBranchStatus("lep2PassBL",0) 
    t.SetBranchStatus("lep2VeryLoose",0) 
    t.SetBranchStatus("lep2Loose",0) 
    t.SetBranchStatus("lep2Medium",0) 
    t.SetBranchStatus("lep2Tight",0) 
    t.SetBranchStatus("lep2IsoLoose",0) 
    t.SetBranchStatus("lep2IsoTight",0) 
    t.SetBranchStatus("lep2IsoGradient",0) 
    t.SetBranchStatus("lep2IsoGradientLoose",0) 
    t.SetBranchStatus("lep2IsoLooseTrackOnly",0) 
    t.SetBranchStatus("lep2IsoFixedCutLoose",0) 
    t.SetBranchStatus("lep2IsoFixedCutTight",0) 
    t.SetBranchStatus("lep2IsoFixedCutTightTrackOnly",0) 
    t.SetBranchStatus("lep2Signal",1) 
    t.SetBranchStatus("lep2MatchesTrigger",1) 
    t.SetBranchStatus("lep3Flavor",1) 
    t.SetBranchStatus("lep3Charge",1) 
    t.SetBranchStatus("lep3Pt",1) 
    t.SetBranchStatus("lep3Eta",1) 
    t.SetBranchStatus("lep3Phi",1) 
    t.SetBranchStatus("lep3M",1) 
    t.SetBranchStatus("lep3D0",1) 
    t.SetBranchStatus("lep3D0Sig",1) 
    t.SetBranchStatus("lep3Z0",1) 
    t.SetBranchStatus("lep3Z0SinTheta",1) 
    t.SetBranchStatus("lep3PassOR",1) 
    t.SetBranchStatus("lep3Type",1) 
    t.SetBranchStatus("lep3Origin",1) 
    t.SetBranchStatus("lep3NPix",0) 
    t.SetBranchStatus("lep3PassBL",0) 
    t.SetBranchStatus("lep3VeryLoose",0) 
    t.SetBranchStatus("lep3Loose",0) 
    t.SetBranchStatus("lep3Medium",0) 
    t.SetBranchStatus("lep3Tight",0) 
    t.SetBranchStatus("lep3IsoLoose",0) 
    t.SetBranchStatus("lep3IsoTight",0) 
    t.SetBranchStatus("lep3IsoGradient",0) 
    t.SetBranchStatus("lep3IsoGradientLoose",0) 
    t.SetBranchStatus("lep3IsoLooseTrackOnly",0) 
    t.SetBranchStatus("lep3IsoFixedCutLoose",0) 
    t.SetBranchStatus("lep3IsoFixedCutTight",0) 
    t.SetBranchStatus("lep3IsoFixedCutTightTrackOnly",0) 
    t.SetBranchStatus("lep3Signal",1) 
    t.SetBranchStatus("lep3MatchesTrigger",1) 
    t.SetBranchStatus("lep4Flavor",1) 
    t.SetBranchStatus("lep4Charge",1) 
    t.SetBranchStatus("lep4Pt",1) 
    t.SetBranchStatus("lep4Eta",1) 
    t.SetBranchStatus("lep4Phi",1) 
    t.SetBranchStatus("lep4M",1) 
    t.SetBranchStatus("lep4D0",1) 
    t.SetBranchStatus("lep4D0Sig",1) 
    t.SetBranchStatus("lep4Z0",1) 
    t.SetBranchStatus("lep4Z0SinTheta",1) 
    t.SetBranchStatus("lep4PassOR",1) 
    t.SetBranchStatus("lep4Type",1) 
    t.SetBranchStatus("lep4Origin",1) 
    t.SetBranchStatus("lep4NPix",0) 
    t.SetBranchStatus("lep4PassBL",0) 
    t.SetBranchStatus("lep4VeryLoose",0) 
    t.SetBranchStatus("lep4Loose",0) 
    t.SetBranchStatus("lep4Medium",0) 
    t.SetBranchStatus("lep4Tight",0) 
    t.SetBranchStatus("lep4IsoLoose",0) 
    t.SetBranchStatus("lep4IsoTight",0) 
    t.SetBranchStatus("lep4IsoGradient",0) 
    t.SetBranchStatus("lep4IsoGradientLoose",0) 
    t.SetBranchStatus("lep4IsoLooseTrackOnly",0) 
    t.SetBranchStatus("lep4IsoFixedCutLoose",0) 
    t.SetBranchStatus("lep4IsoFixedCutTight",0) 
    t.SetBranchStatus("lep4IsoFixedCutTightTrackOnly",0) 
    t.SetBranchStatus("lep4Signal",1) 
    t.SetBranchStatus("lep4MatchesTrigger",1) 
    t.SetBranchStatus("nJet30",1) 
    t.SetBranchStatus("nJet25",1) 
    t.SetBranchStatus("nTotalJet",0) 
    t.SetBranchStatus("nBJet30_MV2c10",1) 
    t.SetBranchStatus("nBJet30_MV2c10_FixedCutBEff_60",0) 
    t.SetBranchStatus("nBJet30_MV2c10_FixedCutBEff_70",0) 
    t.SetBranchStatus("nBJet30_MV2c10_FixedCutBEff_85",0) 
    t.SetBranchStatus("DecayModeTTbar",0) 
    t.SetBranchStatus("jetPt",1)
    t.SetBranchStatus("jetEta",1)
    t.SetBranchStatus("jetPhi",1)
    t.SetBranchStatus("jetM",1)
    t.SetBranchStatus("met_Et",1) 
    t.SetBranchStatus("met_Phi",1) 
    t.SetBranchStatus("TST_Et",0) 
    t.SetBranchStatus("TST_Phi",0) 
    t.SetBranchStatus("deltaPhi_MET_TST_Phi",0) 
    t.SetBranchStatus("mt",1) 
    t.SetBranchStatus("meffInc30",1) 
    t.SetBranchStatus("Ht30",1) 
    t.SetBranchStatus("hadronicWMass",0) 
    t.SetBranchStatus("hadronicWPt",0) 
    t.SetBranchStatus("LepAplanarity",0) 
    t.SetBranchStatus("JetAplanarity",0) 
    t.SetBranchStatus("amt2",0) 
    t.SetBranchStatus("amt2b",0) 
    t.SetBranchStatus("amt2bWeight",0) 
    t.SetBranchStatus("mt2tau",0) 
    t.SetBranchStatus("mt2lj",0) 
    t.SetBranchStatus("mbb", 0)
    t.SetBranchStatus("mt_lep1",0)
    t.SetBranchStatus("mt_lep2",0)
    t.SetBranchStatus("mt_lep3",0)
    t.SetBranchStatus("mt_lep4",0)
    t.SetBranchStatus("METOverHT",1)
    t.SetBranchStatus("METOverJ1pT",1)
    t.SetBranchStatus("DPhiJ1Met",1)
    t.SetBranchStatus("mll",1)
    t.SetBranchStatus("Rll",1)
    t.SetBranchStatus("MSqTauTau_1",1)
    t.SetBranchStatus("MSqTauTau_2",1)
    t.SetBranchStatus("RjlOverEl",1)
    t.SetBranchStatus("LepCosThetaLab",0)
    t.SetBranchStatus("LepCosThetaCoM",0)
    t.SetBranchStatus("mt2leplsp_0",0)
    t.SetBranchStatus("mt2leplsp_25",0)
    t.SetBranchStatus("mt2leplsp_50",0)
    t.SetBranchStatus("mt2leplsp_75",0)
    t.SetBranchStatus("mt2leplsp_90",0)
    t.SetBranchStatus("mt2leplsp_95",0)
    t.SetBranchStatus("mt2leplsp_100",0)
    t.SetBranchStatus("mt2leplsp_105",0)
    t.SetBranchStatus("mt2leplsp_110",0)
    t.SetBranchStatus("mt2leplsp_115",0)
    t.SetBranchStatus("mt2leplsp_120",0)
    t.SetBranchStatus("mt2leplsp_150",0)
    t.SetBranchStatus("pileupWeight",1) 
    t.SetBranchStatus("leptonWeight",1) 
    t.SetBranchStatus("eventWeight",1) 
    t.SetBranchStatus("jvtWeight",1) 
    t.SetBranchStatus("bTagWeight",1) 
    t.SetBranchStatus("genWeight",1) 
    t.SetBranchStatus("genWeightUp",0) 
    t.SetBranchStatus("genWeightDown",0) 
    t.SetBranchStatus("SherpaVjetsNjetsWeight",1)
    t.SetBranchStatus("HLT_mu4",1)
    t.SetBranchStatus("HLT_2mu4",1)
    t.SetBranchStatus("HLT_2mu10",0)
    t.SetBranchStatus("HLT_2mu4_j85_xe50_mht",1)
    t.SetBranchStatus("HLT_mu4_j125_xe90_mht",1)
    t.SetBranchStatus("HLT_xe70",0) 
    t.SetBranchStatus("HLT_xe70_mht",0) 
    t.SetBranchStatus("HLT_xe70_mht_wEFMu",0) 
    t.SetBranchStatus("HLT_xe70_tc_lcw",0) 
    t.SetBranchStatus("HLT_xe70_tc_lcw_wEFMu",0) 
    t.SetBranchStatus("HLT_xe80_tc_lcw_L1XE50",0) 
    t.SetBranchStatus("HLT_xe90_tc_lcw_L1XE50",0) 
    t.SetBranchStatus("HLT_xe90_mht_L1XE50",0) 
    t.SetBranchStatus("HLT_xe90_mht_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe90_tc_lcw_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_tc_lcw_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_mht_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_tc_lcw_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe100_mht_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_tc_em_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_tc_em_wEFMu_L1XE50",0) 
    t.SetBranchStatus("HLT_xe110_mht_L1XE50",1)
    t.SetBranchStatus("HLT_xe90_mht_L1XE50",0)
    t.SetBranchStatus("HLT_j85_L1J40",1)
    t.SetBranchStatus("HLT_j125_L1J50",1)
    t.SetBranchStatus("HLT_e26_lhtight_nod0_ivarloose",0)
    t.SetBranchStatus("HLT_e60_lhmedium_nod0",0)
    t.SetBranchStatus("HLT_e60_medium",0)
    t.SetBranchStatus("HLT_e140_lhloose_nod0",0)
    t.SetBranchStatus("HLT_mu26_ivarmedium",0)
    t.SetBranchStatus("ttbarNNLOWeight", 1)
    t.SetBranchStatus("ttbarNNLOWeightUp", 0)
    t.SetBranchStatus("ttbarNNLOWeightDown", 0)
    t.SetBranchStatus("truthTopPt",0)
    t.SetBranchStatus("truthAntiTopPt",0)
    t.SetBranchStatus("truthTtbarPt",0)
    t.SetBranchStatus("truthTtbarM",0)
    t.SetBranchStatus("x1",0)
    t.SetBranchStatus("x2",0)
    t.SetBranchStatus("pdf1",0)
    t.SetBranchStatus("pdf2",0)
    t.SetBranchStatus("scalePDF",0)
    t.SetBranchStatus("id1",0) 
    t.SetBranchStatus("id2",0) 
    t.SetBranchStatus("PRWHash",0) 
    t.SetBranchStatus("EventNumber",1) 
    t.SetBranchStatus("xsec",1) 
    t.SetBranchStatus("TrueHt",0) 
    t.SetBranchStatus("DatasetNumber",1) 
    t.SetBranchStatus("RunNumber",0) 
    t.SetBranchStatus("RandomRunNumber",1) 
    t.SetBranchStatus("FS",0) 

    #-------------------------
    #create output file
    #-------------------------


    if debug: print "opening output file"

    o=ROOT.TFile(outfile, "RECREATE")

    if debug: print "..making histograms collections"

    if region == "dilepton":
        baseLeptonsEE=histcollection("baseLeptonsEE", o, debug, data, tree, DSID, sumWhist, 0)
        baseLeptonsEE.addleptoncollection("skim")

        baseLeptonsMM=histcollection("baseLeptonsMM", o, debug, data, tree, DSID, sumWhist, 0)
        baseLeptonsMM.addleptoncollection("skim")

        baseLeptonsEM=histcollection("baseLeptonsEM", o, debug, data, tree, DSID, sumWhist, 0)
        baseLeptonsEM.addleptoncollection("skim")

        signalLeptonsEE=histcollection("signalLeptonsEE", o, debug, data, tree, DSID, sumWhist, 0)
        signalLeptonsEE.addleptoncollection("skim")

        signalLeptonsMM=histcollection("signalLeptonsMM", o, debug, data, tree, DSID, sumWhist, 0)
        signalLeptonsMM.addleptoncollection("skim")

        signalLeptonsEM=histcollection("signalLeptonsEM", o, debug, data, tree, DSID, sumWhist, 0)
        signalLeptonsEM.addleptoncollection("skim")

    if region == "trigger":
        EWsignalEE=histcollection("EWsignalEE", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalEE.addtriggercollection("skim")
        EWsignalEE.addtriggercollection("signal")
        EWsignalEE.addtriggercollection("opSign")
        EWsignalEE.addtriggercollection("mtautau")
        EWsignalEE.addtriggercollection("jet105")
        EWsignalEE.addtriggercollection("jet145")
        EWsignalMM=histcollection("EWsignalMM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalMM.addtriggercollection("skim")
        EWsignalMM.addtriggercollection("signal")
        EWsignalMM.addtriggercollection("opSign")
        EWsignalMM.addtriggercollection("mtautau")
        EWsignalMM.addtriggercollection("jet105")
        EWsignalMM.addtriggercollection("jet145")
        EWsignalEM=histcollection("EWsignalEM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalEM.addtriggercollection("skim")
        EWsignalEM.addtriggercollection("signal")
        EWsignalEM.addtriggercollection("opSign")
        EWsignalEM.addtriggercollection("mtautau")
        EWsignalEM.addtriggercollection("jet105")
        EWsignalEM.addtriggercollection("jet145")

        EWsignal2muTrigEE=histcollection("EWsignal2muTrigEE", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignal2muTrigEE.addtriggercollection("skim")
        EWsignal2muTrigEE.addtriggercollection("signal")
        EWsignal2muTrigEE.addtriggercollection("opSign")
        EWsignal2muTrigEE.addtriggercollection("mtautau")
        EWsignal2muTrigMM=histcollection("EWsignal2muTrigMM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignal2muTrigMM.addtriggercollection("skim")
        EWsignal2muTrigMM.addtriggercollection("signal")
        EWsignal2muTrigMM.addtriggercollection("opSign")
        EWsignal2muTrigMM.addtriggercollection("mtautau")
        EWsignal2muTrigEM=histcollection("EWsignal2muTrigEM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignal2muTrigEM.addtriggercollection("skim")
        EWsignal2muTrigEM.addtriggercollection("signal")
        EWsignal2muTrigEM.addtriggercollection("opSign")
        EWsignal2muTrigEM.addtriggercollection("mtautau")
        
        EWsignal1muTrigEE=histcollection("EWsignal1muTrigEE", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignal1muTrigEE.addtriggercollection("skim")
        EWsignal1muTrigEE.addtriggercollection("signal")
        EWsignal1muTrigEE.addtriggercollection("opSign")
        EWsignal1muTrigEE.addtriggercollection("mtautau")
        EWsignal1muTrigMM=histcollection("EWsignal1muTrigMM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignal1muTrigMM.addtriggercollection("skim")
        EWsignal1muTrigMM.addtriggercollection("signal")
        EWsignal1muTrigMM.addtriggercollection("opSign")
        EWsignal1muTrigMM.addtriggercollection("mtautau")
        EWsignal1muTrigEM=histcollection("EWsignal1muTrigEM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignal1muTrigEM.addtriggercollection("skim")
        EWsignal1muTrigEM.addtriggercollection("signal")
        EWsignal1muTrigEM.addtriggercollection("opSign")
        EWsignal1muTrigEM.addtriggercollection("mtautau")

        EWsignalMetTrigEE=histcollection("EWsignalMetTrigEE", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalMetTrigEE.addtriggercollection("skim")
        EWsignalMetTrigEE.addtriggercollection("signal")
        EWsignalMetTrigEE.addtriggercollection("opSign")
        EWsignalMetTrigEE.addtriggercollection("mtautau")
        EWsignalMetTrigMM=histcollection("EWsignalMetTrigMM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalMetTrigMM.addtriggercollection("skim")
        EWsignalMetTrigMM.addtriggercollection("signal")
        EWsignalMetTrigMM.addtriggercollection("opSign")
        EWsignalMetTrigMM.addtriggercollection("mtautau")
        EWsignalMetTrigEM=histcollection("EWsignalMetTrigEM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalMetTrigEM.addtriggercollection("skim")
        EWsignalMetTrigEM.addtriggercollection("signal")
        EWsignalMetTrigEM.addtriggercollection("opSign")
        EWsignalMetTrigEM.addtriggercollection("mtautau")

        EWsignalORTrigEE=histcollection("EWsignalORTrigEE", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalORTrigEE.addtriggercollection("skim")
        EWsignalORTrigEE.addtriggercollection("signal")
        EWsignalORTrigEE.addtriggercollection("opSign")
        EWsignalORTrigEE.addtriggercollection("mtautau")
        EWsignalORTrigMM=histcollection("EWsignalORTrigMM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalORTrigMM.addtriggercollection("skim")
        EWsignalORTrigMM.addtriggercollection("signal")
        EWsignalORTrigMM.addtriggercollection("opSign")
        EWsignalORTrigMM.addtriggercollection("mtautau")
        EWsignalORTrigEM=histcollection("EWsignalORTrigEM", o, debug, data, tree, DSID, sumWhist, 0)
        EWsignalORTrigEM.addtriggercollection("skim")
        EWsignalORTrigEM.addtriggercollection("signal")
        EWsignalORTrigEM.addtriggercollection("opSign")
        EWsignalORTrigEM.addtriggercollection("mtautau")

    eventcount = 0

    #-------------------------
    #loop over events
    #-------------------------

    if debug: print "looping over events"

    for event in t:
        #----------------------
        #bookkeep and monitor
        #______________________

        eventcount +=1

        #----------------------------
        #define preliminary variables
        #----------------------------

        #Initialize TLorentz vectors
        lep1Vec = ROOT.TLorentzVector()
        lep2Vec = ROOT.TLorentzVector()

        MET = event.met_Et
        MET_Phi = event.met_Phi
        Meff = event.meffInc30
        Ht30 = event.Ht30
        #metTrigger = event.trigMatch_metTrig
        metTrigger = event.HLT_xe110_mht_L1XE50
        dimuonTrigger = event.HLT_2mu4_j85_xe50_mht_emul
        muonTrigger = event.HLT_mu4_j125_xe90_mht_emul
        nBaseLep = event.nLep_base
        nSigLep  = event.nLep_signal
        nJet25 = event.nJet25
        if event.jetPt.size() > 0: jet1Pt = event.jetPt[0]
        if event.jetPt.size() > 1: jet2Pt = event.jetPt[1]
        lep1Pt = event.lep1Pt
        lep2Pt = event.lep2Pt
        nBTag = event.nBJet30_MV2c10
        RunNumer = event.RandomRunNumber

        if( region == "trigger" or region == "dilepton" ):
            obs = observable()
            index1, index2 = obs.findSignalPairs(event) #Decide leading and subeading lepton based on opposite sign match
            if (index1 == 0 or index2 == 0):
                continue
            mtautau = -999
            if (nSigLep > 1):
                mtautau = obs.calcMtautau(event) #Calculate mtautau

            lep1Vec, lep1Charge, lep1Flavor = obs.getLep1TLVChargeFlavor(event)
            lep2Vec, lep2Charge, lep2Flavor = obs.getLep2TLVChargeFlavor(event)
            #print "lep1 info: pt = %f, eta = %f, charge = %i, type = %i" % (lep1Vec.Pt(), lep1Vec.Eta(), lep1Charge, lep1Flavor)
            #print "lep2 info: pt = %f, eta = %f, charge = %i, type = %i" % (lep2Vec.Pt(), lep2Vec.Eta(), lep2Charge, lep2Flavor)

            #Calculate dilepton variables
            lepPairVec = lep1Vec + lep2Vec
            mll = lepPairVec.M()
            ptll = lepPairVec.Pt()
            dimuFlag = 0
            if(lep1Flavor == 2 and lep2Flavor == 2):
                dimuFlag = 1
            qlql = lep1Charge*lep2Charge
            dphi_l1met = TVector2.Phi_mpi_pi(lep1Vec.Phi() - MET_Phi)
            dphi_l2met = TVector2.Phi_mpi_pi(lep2Vec.Phi() - MET_Phi)
            MT_l1met = TMath.Sqrt(2*lep1Vec.Pt()*MET*(1-TMath.Cos(dphi_l1met)))
            MT_l2met = TMath.Sqrt(2*lep2Vec.Pt()*MET*(1-TMath.Cos(dphi_l2met)))

        #Make dictionary of cuts
        Cuts = {}

        if( nBaseLep > 1):
            Cuts["2BaseLep"] = True
        else: Cuts["2BaseLep"] = False

        if( nSigLep > 1 ):
            Cuts["2SigLep"] = True
        else: Cuts["2SigLep"] = False

        if( nJet25 > 0 ):
            Cuts["1Jet25"] = True
        else: Cuts["1Jet25"] = False

        if( jet1Pt > 105. ):
            Cuts["Jet105"] = True
        else: Cuts["Jet105"] = False

        if( jet1Pt > 145. ):
            Cuts["Jet145"] = True
        else: Cuts["Jet145"] = False
            
        if( qlql == -1 ): 
            Cuts["opSign"] = True
        else: 
            Cuts["opSign"] = False

        if( MET > 125. ): 
            Cuts["MET125"] = True
        else: 
            Cuts["MET125"] = False

        if( Ht30 <= 0.0 ): 
            Cuts["METoverHt"] = False
        elif( MET/Ht30 >= 0.6 and MET/Ht30 <= 1.4 ): 
            Cuts["METoverHt"] = True
        else: 
            Cuts["METoverHt"] = False

        if( Ht30 > 100. ): 
            Cuts["HT100"] = True
        else: 
            Cuts["HT100"] = False

        if( ptll > 3.0 ): 
            Cuts["ptll3"] = True
        else: 
            Cuts["ptll3"] = False

        if( mll >= 4. and mll <=60. ):
            Cuts["4mll60"] = True
        else:
            Cuts["4mll60"] = False

        if( lep1Pt < 30. and lep2Pt < 30. ):
            Cuts["lepPt30"] = True
        else: 
            Cuts["lepPt30"] = False

        if( nBTag == 0 ):
            Cuts["bVeto"] = True
        else: 
            Cuts["bVeto"] = False

        if( MT_l1met < 70. and MT_l2met < 70 ):
            Cuts["70MtLepMET"] = True
        else: 
            Cuts["70MtLepMET"] = False

        if( mtautau <= 0. or mtautau >= 160.):
            Cuts["Mtautau"] = True
        else: 
            Cuts["Mtautau"] = False

        if(MET > 125. and MET <= 200.):
            Cuts["125MET200"] = True
        else: 
            Cuts["125MET200"] = False

        if(MET > 200. and MET <= 250.):
            Cuts["200MET250"] = True
        else: 
            Cuts["200MET250"] = False

        if( MET > 250. ):
            Cuts["MET250"] = True
        else: 
            Cuts["MET250"] = False

        if( metTrigger ):
            Cuts["metTrigger"] = True
        else: 
            Cuts["metTrigger"] = False

        if( dimuonTrigger and jet1Pt > 105. ):
            Cuts["dimuTrigger"] = True
        else: 
            Cuts["dimuTrigger"] = False

        if( muonTrigger and jet1Pt > 145.):
            Cuts["muTrigger"] = True
        else: 
            Cuts["muTrigger"] = False

        if ( (muonTrigger and jet1Pt > 145.) or (dimuonTrigger and jet1Pt > 105.) or metTrigger ):
            Cuts["ORTrigger"] = True
        else:
            Cuts["ORTrigger"] = False

        if( lep1Flavor == 2 and lep2Flavor == 2):
            Cuts["mumuEvent"] = True
        else: 
            Cuts["mumuEvent"] = False

        if( lep1Flavor == 1 and lep2Flavor == 1):
            Cuts["eeEvent"] = True
        else: 
            Cuts["eeEvent"] = False
        if( RunNumer >= 308084 ):
            Cuts["RunNewTriggers"] = True
        else: Cuts["RunNewTriggers"] = False



        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        if debug:
            if eventcount == 1: 
                if region == 'dilepton':
                    print 'Recalculating generator Weight!!'

        #------------------------------
        #trigger efficiency regions
        #------------------------------
        if region == "dilepton":
            baseLeptonEE(   event,  baseLeptonsEE,    Cuts) 
            baseLeptonMM(   event,  baseLeptonsMM,    Cuts) 
            baseLeptonEM(   event,  baseLeptonsEM,    Cuts) 
            signalLeptonEE( event,  signalLeptonsEE,  Cuts) 
            signalLeptonMM( event,  signalLeptonsMM,  Cuts) 
            signalLeptonEM( event,  signalLeptonsEM,  Cuts) 
            

        if region == "trigger":
            CMSEWsignalEE(                event, EWsignalEE,        Cuts)
            CMSEWsignalMM(                event, EWsignalMM,        Cuts)
            CMSEWsignalEM(                event, EWsignalEM,        Cuts)
            CMSEWsignalDimuTriggerEE(     event, EWsignal2muTrigEE, Cuts)
            CMSEWsignalDimuTriggerMM(     event, EWsignal2muTrigMM, Cuts)
            CMSEWsignalDimuTriggerEM(     event, EWsignal2muTrigEM, Cuts)
            CMSEWsignalSingleMuTriggerEE( event, EWsignal1muTrigEE, Cuts)
            CMSEWsignalSingleMuTriggerMM( event, EWsignal1muTrigMM, Cuts)
            CMSEWsignalSingleMuTriggerEM( event, EWsignal1muTrigEM, Cuts)
            CMSEWsignalMetTriggerEE(      event, EWsignalMetTrigEE, Cuts)
            CMSEWsignalMetTriggerMM(      event, EWsignalMetTrigMM, Cuts)
            CMSEWsignalMetTriggerEM(      event, EWsignalMetTrigEM, Cuts)
            CMSEWsignalORTriggerEE(       event, EWsignalORTrigEE,  Cuts)
            CMSEWsignalORTriggerMM(       event, EWsignalORTrigMM,  Cuts)
            CMSEWsignalORTriggerEM(       event, EWsignalORTrigEM,  Cuts)


    if debug: print eventcount
    print "writing histograms for %s efficiency" % region

    if region == "dilepton":
        baseLeptonsEE.write()
        baseLeptonsMM.write()
        baseLeptonsEM.write()
        signalLeptonsEE.write()
        signalLeptonsMM.write()
        signalLeptonsEM.write()

    if region == "trigger":
        EWsignalEE.write()
        EWsignalMM.write()
        EWsignalEM.write()
        EWsignal2muTrigEE.write()
        EWsignal2muTrigMM.write()
        EWsignal2muTrigEM.write()
        EWsignal1muTrigEE.write()
        EWsignal1muTrigMM.write()
        EWsignal1muTrigEM.write()
        EWsignalMetTrigEE.write()
        EWsignalMetTrigMM.write()
        EWsignalMetTrigEM.write()
        EWsignalORTrigEE.write()
        EWsignalORTrigMM.write()
        EWsignalORTrigEM.write()

    if debug: print "...done"

#======================================================================

#======================================================================
def main(argv):

    parser = argparse.ArgumentParser(description="Command line arguments")
    parser.add_argument("--input"      , action='store', default='', help='input root file containing tree to loop over')
    parser.add_argument("--weight"      , action='store', default='', help='root file containing sum of weights hist')
    parser.add_argument("--tree"        , action='store', default='')
    parser.add_argument("--DSID"        , action='store', default='')
    parser.add_argument("--isData"      , action='store_true')
    parser.add_argument("--isSignal"    , action='store_true')
    parser.add_argument("--outfile"     , action='store', default='')
    parser.add_argument("--test"        , action='store_true')
    parser.add_argument("--region"      , action='store', default='', help='current avaiable regions are trigger and dilepton')
    args=parser.parse_args()


    print "Starting Analysis"

    if args.test:
        print args.DSID

    analyze(args.input, args.weight, args.tree, args.DSID, args.isData, args.isSignal, args.outfile, args.test, args.region)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
