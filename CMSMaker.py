#!/usr/bin/env python
#Author: Sheena C Schier
#Created 22March2017 to validate CMS Signal and Control Regions and make N-1 CR plots


import sys, os, subprocess, getopt
import re, time, copy, math, array
import argparse, commands
import ROOT
from ROOT import TString
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?

#local imports
from CMShistograms import *
from CMSobservables import *
from renormalize import *


#======================================================================
def preselection(event, hc, CutsDict):

    #preselction in the analysis framework is Event Cleaning, two signal leptons with pt defined in SUSYTools_config file, one jet > 25 GeV, MET > 50 (MET > 125 for data)
    hc.fill(event,"skim")

    if CutsDict["2SigLep"] == False:
        return False
    if CutsDict["1Jet25"] == False:
        return False
    hc.fill(event,"signal")

    return True
#======================================================================
#======================================================================

def CMSEWsignal(event, hc, CutsDict):


    if CutsDict["opSign"] == False:
        return False
    hc.fill(event, "opSign")
    if CutsDict["MET125"] == False:
        return False
    hc.fill(event, "MET125")
    if CutsDict["METoverHt"] == False:
        return False
    hc.fill(event, "ratio_MET_Had")
    if CutsDict["HT100"] == False:
        return False
    hc.fill(event, "Ht")
    if CutsDict["ptll3"] == False:
        return False
    hc.fill(event, "ptll")
    if CutsDict["4mll60"] == False:
        return False
    hc.fill(event, "mll")
    if CutsDict["lepPt30"] == False:
        return False
    hc.fill(event, "lepPt")
    if CutsDict["bVeto"] == False:
        return False
    hc.fill(event, "bVeto")
    if CutsDict["70MtLepMET"] == False:
        return False
    hc.fill(event, "mtLepMET")
    if CutsDict["Mtautau"] == False:
        return False
    hc.fill(event, "mtautau")

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True



#======================================================================
#======================================================================

def CMSttCR(event, hc, CutsDict):


    if( CutsDict["bVeto"] == True ):
        return False
    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
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
    if CutsDict["70MtLepMET"] == False:
        return False
    if CutsDict["Mtautau"] == False:
        return False

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")
    return True

   

#Need bjet with pt > 40

#======================================================================
#======================================================================

def CMSDYCR(event, hc, CutsDict):

    if( CutsDict["Mtautau"] == True ):
        return False
    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
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

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True

#======================================================================
#======================================================================

def CMSEWminusbVeto(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
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
    if CutsDict["70MtLepMET"] == False:
        return False
    if CutsDict["Mtautau"] == False:
        return False

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True

#======================================================================
#======================================================================

def CMSEWminusMET(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
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

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True

#======================================================================
#======================================================================

def CMSEWminusMtata(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
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

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True
#======================================================================
#======================================================================

def CMSEWminusMt(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
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
    if CutsDict["Mtautau"] == False:
        return False

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True

#======================================================================
#======================================================================

def CMSEWminusqlql(event, hc, CutsDict):

    if CutsDict["MET125"] == False:
        return False
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

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True

#======================================================================
#======================================================================

def CMSEWminusRatio(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
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

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True

#======================================================================
#======================================================================

def CMSEWminusHt(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
    if CutsDict["METoverHt"] == False:
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

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True

#======================================================================
#======================================================================

def CMSEWminusPtll(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
    if CutsDict["METoverHt"] == False:
        return False
    if CutsDict["HT100"] == False:
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

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True


#======================================================================
#======================================================================

def CMSEWminusMll(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
    if CutsDict["METoverHt"] == False:
        return False
    if CutsDict["HT100"] == False:
        return False
    if CutsDict["ptll3"] == False:
        return False
    if CutsDict["lepPt30"] == False:
        return False
    if CutsDict["bVeto"] == False:
        return False
    if CutsDict["70MtLepMET"] == False:
        return False
    if CutsDict["Mtautau"] == False:
        return False

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True


#======================================================================
#======================================================================

def CMSEWminusLepPt(event, hc, CutsDict):

    if CutsDict["opSign"] == False:
        return False
    if CutsDict["MET125"] == False:
        return False
    if CutsDict["METoverHt"] == False:
        return False
    if CutsDict["HT100"] == False:
        return False
    if CutsDict["ptll3"] == False:
        return False
    if CutsDict["4mll60"] == False:
        return False
    if CutsDict["bVeto"] == False:
        return False
    if CutsDict["70MtLepMET"] == False:
        return False
    if CutsDict["Mtautau"] == False:
        return False

    if CutsDict["125MET200"] and CutsDict["mumuEvent"] and CutsDict["dimuTrigger"]:
        hc.fill(event, "lowmet")

    if CutsDict["200MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "midmet")

    if CutsDict["MET250"] and CutsDict["metTrigger"]:
        hc.fill(event, "highmet")

    return True

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
    t.SetBranchStatus("HLT_xe110_mht_L1XE50",0)
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

    if debug: print "..making histograms for preslection"

    presel=histcollection("presel",o, debug, data, tree, DSID, sumWhist, 0)
    presel.addmincollection("skim")
    presel.addmincollection("signal")

    EWsignal=histcollection("EWsignal", o, debug, data, tree, DSID, sumWhist, 0)
    EWsignal.addmincollection("opSign")
    EWsignal.addmincollection("MET125")
    EWsignal.addmincollection("ratio_MET_Had")
    EWsignal.addmincollection("Ht")
    EWsignal.addmincollection("ptll")
    EWsignal.addmincollection("mll")
    EWsignal.addmincollection("lepPt")
    EWsignal.addmincollection("bVeto")
    EWsignal.addmincollection("mtLepMET")
    EWsignal.addmincollection("mtautau")
    EWsignal.addbasecollection("lowmet")
    EWsignal.addbasecollection("midmet")
    EWsignal.addbasecollection("highmet")

    DYCR=histcollection("DYCR", o, debug, data, tree, DSID, sumWhist, 0)
    DYCR.addbasecollection("lowmet")
    DYCR.addbasecollection("midmet")
    DYCR.addbasecollection("highmet")

    ttCR=histcollection("ttCR", o, debug, data, tree, DSID, sumWhist, 0)
    ttCR.addbasecollection("lowmet")
    ttCR.addbasecollection("midmet")
    ttCR.addbasecollection("highmet")

    EWbVeto=histcollection("EWbVeto", o, debug, data, tree, DSID, sumWhist, 0)
    EWbVeto.addbasecollection("lowmet")
    EWbVeto.addbasecollection("midmet")
    EWbVeto.addbasecollection("highmet")

    EWMET=histcollection("EWMET", o, debug, data, tree, DSID, sumWhist, 0)
    EWMET.addbasecollection("lowmet")
    EWMET.addbasecollection("midmet")
    EWMET.addbasecollection("highmet")

    EWMtata=histcollection("EWMtata", o, debug, data, tree, DSID, sumWhist, 0)
    EWMtata.addbasecollection("lowmet")
    EWMtata.addbasecollection("midmet")
    EWMtata.addbasecollection("highmet")

    EWMt=histcollection("EWMt", o, debug, data, tree, DSID, sumWhist, 0)
    EWMt.addbasecollection("lowmet")
    EWMt.addbasecollection("midmet")
    EWMt.addbasecollection("highmet")

    EWopSign=histcollection("EWopSign", o, debug, data, tree, DSID, sumWhist, 0)
    EWopSign.addbasecollection("lowmet")
    EWopSign.addbasecollection("midmet")
    EWopSign.addbasecollection("highmet")

    EWratio=histcollection("EWratio", o, debug, data, tree, DSID, sumWhist, 0)
    EWratio.addbasecollection("lowmet")
    EWratio.addbasecollection("midmet")
    EWratio.addbasecollection("highmet")

    EWHt=histcollection("EWHt", o, debug, data, tree, DSID, sumWhist, 0)
    EWHt.addbasecollection("lowmet")
    EWHt.addbasecollection("midmet")
    EWHt.addbasecollection("highmet")

    EWPtll=histcollection("EWPtll", o, debug, data, tree, DSID, sumWhist, 0)
    EWPtll.addbasecollection("lowmet")
    EWPtll.addbasecollection("midmet")
    EWPtll.addbasecollection("highmet")

    EWMll=histcollection("EWMll", o, debug, data, tree, DSID, sumWhist, 0)
    EWMll.addbasecollection("lowmet")
    EWMll.addbasecollection("midmet")
    EWMll.addbasecollection("highmet")

    EWLepPt=histcollection("EWLepPt", o, debug, data, tree, DSID, sumWhist, 0)
    EWLepPt.addbasecollection("lowmet")
    EWLepPt.addbasecollection("midmet")
    EWLepPt.addbasecollection("highmet")

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
        metTrigger = event.trigMatch_metTrig
        if data:
            dimuonTrigger = event.HLT_2mu4_j85_xe50_mht
        else: dimuonTrigger = event.HLT_2mu4_j85_xe50_mht_emul
        nBaseLep = event.nLep_base
        nSigLep  = event.nLep_signal
        nJet25 = event.nJet25
        if event.jetPt.size() > 0: jet1Pt = event.jetPt[0]
        if event.jetPt.size() > 1: jet2Pt = event.jetPt[1]
        nBTag = event.nBJet30_MV2c10
        RunNumber = event.RandomRunNumber

        obs = observable()
        index1, index2 = obs.findSignalPairs(event) #Decide leading and subeading lepton based on opposite sign match
        if (index1 == 0 or index2 == 0):
            continue
        mtautau = -999
        if (nSigLep > 1):
            mtautau = obs.calcMtautau(event) #Calculate mtautau

        lep1Vec, lep1Charge, lep1Flavor = obs.getLep1TLVChargeFlavor(event)
        lep2Vec, lep2Charge, lep2Flavor = obs.getLep2TLVChargeFlavor(event)
        lep1Pt = lep1Vec.Pt()
        lep2Pt = lep2Vec.Pt()

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

        if( nSigLep > 1 ):
            Cuts["2SigLep"] = True
        else: Cuts["2SigLep"] = False

        if( nJet25 > 0 ):
            Cuts["1Jet25"] = True
        else: Cuts["1Jet25"] = False

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

        if( RunNumber >= 308084 and dimuonTrigger ):
            Cuts["dimuTrigger"] = True
        else: 
            Cuts["dimuTrigger"] = False

        if(lep1Flavor == 2 and lep2Flavor == 2):
            Cuts["mumuEvent"] = True
        else: 
            Cuts["mumuEvent"] = False

        if(lep1Flavor == 1 and lep2Flavor == 1):
            Cuts["eeEvent"] = True
        else: 
            Cuts["eeEvent"] = False



        #print out event status
        if (eventcount%1000 == 0): print "%i events analyzed" % eventcount
        #print out event status
        if eventcount == 1: 
            print MET
            #print "pileup weight %f" % event.pileupWeight
            #print "trigger weight %f" % event.trigWeight_metTrig
            #print "event weight %f" % event.eventWeight
            #print "gen weight %f" % event.genWeight
            #print "lepton weight %f" % event.leptonWeight
            #print "jvt weight %f" %  event.jvtWeight
            #print "bTag weight %f" % event.bTagWeight

        #------------------------------
        #preselection cuts
        #------------------------------
        if not preselection(event, presel, Cuts):
            continue
        CMSEWsignal(    event, EWsignal, Cuts)
        CMSttCR(        event, ttCR,     Cuts)
        CMSDYCR(        event, DYCR,     Cuts)

        CMSEWminusbVeto(event, EWbVeto,  Cuts)
        CMSEWminusMET(  event, EWMET,    Cuts)
        CMSEWminusMtata(event, EWMtata,  Cuts)
        CMSEWminusMt(   event, EWMt,     Cuts)
        CMSEWminusqlql( event, EWopSign, Cuts)
        CMSEWminusRatio(event, EWratio,  Cuts)
        CMSEWminusHt(   event, EWHt,     Cuts)
        CMSEWminusPtll( event, EWPtll,   Cuts)
        CMSEWminusMll(  event, EWMll,    Cuts)
        CMSEWminusLepPt(event, EWLepPt,  Cuts)

    if debug: print eventcount
    print "writing histograms"
    presel.write()
    EWsignal.write()
    ttCR.write()
    DYCR.write()
    EWbVeto.write()
    EWMET.write()
    EWMtata.write()
    EWMt.write()
    EWopSign.write()
    EWratio.write()
    EWHt.write()
    EWPtll.write()
    EWMll.write()
    EWLepPt.write()

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
    parser.add_argument("--region"      , action='store', default="SR")
    args=parser.parse_args()


    print "Starting Analysis"

    if args.test:
        print args.DSID

    analyze(args.input, args.weight, args.tree, args.DSID, args.isData, args.isSignal, args.outfile, args.test, args.region)   

    print "Done"



if __name__ == '__main__':
    main(sys.argv[1:])
 #======================================================================
