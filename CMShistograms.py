#Author:Sheena C Schier
#Last change 01Dec16: Added TTbarNNLOWeight factor to total weight, added plots of nvtx, and electron/muon pts separately, changed hisograms bins
#Feb 2017, created version for CMS signal and control regions
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True) #Do I want to run in batch mode?
from CMSobservables import *
from renormalize import *
#------------------------------------------------------------------
class minhists:
    def __init__(self, tag, topdir, isdata, treetype, DSID, sumWHist, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.DSID = DSID
        self.sumWHist = sumWHist
        self.hists={}
        self.detaillevel=detaillevel

        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        self.hists["MET"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(25 GeV)",22,50,600)
        self.hists['Lep1Pt']=ROOT.TH1F("h_"+tag+"_Lep1Pt",tag+"_Lep1Pt; leading lepton p_{T} [GeV]; Events/(2 GeV)",35, 0, 70)
        self.hists['Jet1Pt']=ROOT.TH1F("h_"+tag+"_Jet1Pt",tag+"_Jet1Pt; leading jet p_{T} [GeV]; Events/(25 GeV)",20, 0, 500)
        self.hists['mll']=ROOT.TH1F("h_"+tag+"_mll2",tag+"_mll2; dilepton invariant mass [GeV]; Events/(2 GeV) ",50, 0, 100)
        self.hists['ptll']=ROOT.TH1F("h_"+tag+"_ptll",tag+"_ptll; dilepton p_{T} [GeV]; Events/(5 GeV)",20, 0, 100)

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
        intLumi = 36100.0 #Full 2015+2016 dataset
        #intLumi = 1.0

        #Initialize TLorentz vectors
        lep1Vec = ROOT.TLorentzVector()
        lep2Vec = ROOT.TLorentzVector()
        jet1Vec = ROOT.TLorentzVector()
        jet2Vec = ROOT.TLorentzVector()

        #Get variables from tree for filling histogram
        #datasetNum = event.DatasetNumber
        MET=event.met_Et
        if event.jetPt.size() > 0: jet1Vec.SetPtEtaPhiM(event.jetPt[0], event.jetEta[0], event.jetPhi[0], event.jetM[0])

        obs = observable()
        lep1Vec, lep1Charge, lep1Flavor = obs.getLep1TLVChargeFlavor(event)
        lep2Vec, lep2Charge, lep2Flavor = obs.getLep2TLVChargeFlavor(event)

        #Calculate dilepton variables
        lepPairVec = lep1Vec + lep2Vec
        mll = lepPairVec.M()
        ptll = lepPairVec.Pt()

        genWeight = event.genWeight

        #Calculating weight
        if self.isdata:
            totalWeight = 1.0
        else:
            totalWeight = float(event.SherpaVjetsNjetsWeight*event.ttbarNNLOWeight*event.pileupWeight*event.eventWeight*event.leptonWeight*event.jvtWeight*event.bTagWeight*genWeight) #TODO: NO TRIGGER WEIGHT!!

        self.hists["MET"].Fill(float(MET), totalWeight)
        self.hists["Lep1Pt"].Fill(float(lep1Vec.Pt()), totalWeight)
        self.hists["Jet1Pt"].Fill(float(jet1Vec.Pt()), totalWeight)
        self.hists["mll"].Fill(float(mll), totalWeight)
        self.hists["ptll"].Fill(float(ptll), totalWeight)
#------------------------------------------------------------------
#------------------------------------------------------------------
class basehists:
    def __init__(self, tag, topdir, isdata, treetype, DSID, sumWHist, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.DSID = DSID
        self.sumWHist = sumWHist
        self.hists={}
        self.detaillevel=detaillevel

        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        self.hists["MET"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(25 GeV)",22,50,600)
        self.hists['Lep1Pt']=ROOT.TH1F("h_"+tag+"_Lep1Pt",tag+"_Lep1Pt; leading lepton p_{T} [GeV]; Events/(2 GeV)",35, 0, 70)
        self.hists['Lep2Pt']=ROOT.TH1F("h_"+tag+"_Lep2Pt",tag+"_Lep2Pt; subleading lepton p_{T} [GeV]; Events/(2 GeV)",35, 0, 70)
        self.hists['Jet1Pt']=ROOT.TH1F("h_"+tag+"_Jet1Pt",tag+"_Jet1Pt; leading jet p_{T} [GeV]; Events/(25 GeV)",20, 0, 500)
        self.hists['Jet2Pt']=ROOT.TH1F("h_"+tag+"_Jet2Pt",tag+"_Jet2Pt; subleading jet p_{T} [GeV]; Events/(25 GeV)",20, 0, 500)
        self.hists['nLepSignal']=ROOT.TH1F("h_"+tag+"_nLep_signal",tag+"_nLep_signal; lepton count; Events/count",4, 1, 5)
        self.hists['nJet25']=ROOT.TH1F("h_"+tag+"_nJet25",tag+"_nJet25; jet count; Events/count",7, 1, 8)
        self.hists['mll']=ROOT.TH1F("h_"+tag+"_mll2",tag+"_mll2; dilepton invariant mass [GeV]; Events/(2 GeV) ",50, 0, 100)
        self.hists['ptll']=ROOT.TH1F("h_"+tag+"_ptll",tag+"_ptll; dilepton p_{T} [GeV]; Events/(5 GeV)",20, 0, 100)
        self.hists['dphiJ1met']=ROOT.TH1F("h_"+tag+"_dphi_j1met",tag+"_dphi_j1met; #Delta#phi_{jet_{1}-met} [rad];Events/(0.25 rad)",14, -3.5, 0. )
        self.hists['dphiJ2met']=ROOT.TH1F("h_"+tag+"_dphi_j2met",tag+"_dphi_j2met; #Delta#phi_{jet_{2}-met} [rad];Events/(0.25 rad)",14, -3.5, 0. )
        self.hists['dphiL1met']=ROOT.TH1F("h_"+tag+"_dphi_l1met",tag+"_dphi_l1met;#Delta#phi_{lep_{1}-met}  [rad];Events/(0.25 rad)",14, 0., 3.5)
        self.hists['dphiL2met']=ROOT.TH1F("h_"+tag+"_dphi_l2met",tag+"_dphi_l2met; #Delta#phi_{lep_{2}-met} [rad];Events/(0.25 rad)",14, 0., 3.5)
        self.hists['dphiL1L2']=ROOT.TH1F("h_"+tag+"_dphi_l1l2",tag+"_dphi_l1l2;#Delta#phi_{lep_{1}-lep_{2}} [rad];Events/(0.25 rad)",14, 0., 3.5)
        self.hists['dRL1L2']=ROOT.TH1F("h_"+tag+"_dR_l1l2",tag+"_dR_l1l2;#DeltaR_{lep_{1}-lep_{2}} [mm];Events/(0.25 mm)",16, 0., 4.0)
        self.hists['METoverHt']=ROOT.TH1F("h_"+tag+"_METoverHt",tag+"_METoverHt; MET/H_{T}; Events/0.1",30, 0.0, 3.0)
        self.hists['qlql']=ROOT.TH1F("h_"+tag+"_qlql",tag+"_qlql; Q_{l}Q_{l} [e^{2}]; Events/e^{2}",4, -1, 3)
        self.hists['Ht30']=ROOT.TH1F("h_"+tag+"_Ht30",tag+"_Ht30; H_{T} [GeV]; Events/(25 GeV)",21, 0, 525)
        self.hists['MtL1met']=ROOT.TH1F("h_"+tag+"_Mt_l1met",tag+"_Mt_l1met; m_{T} {l1-met} [GeV]; Events/(10 GeV) ",15, 0, 150)
        self.hists['MtL2met']=ROOT.TH1F("h_"+tag+"_Mt_l2met",tag+"_Mt_l2met;  m_{T} {l2-met} [GeV]; Events/(10 GeV)",10, 0, 100)
        self.hists['MTauTau']=ROOT.TH1F("h_"+tag+"_MTauTau",tag+"_MTauTau; M_{#Tau#Tau}; Events/(20 GeV) ",52, -40., 1000)

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
        intLumi = 36100.0 #Full 2015+2016 dataset
        #intLumi = 1.0

        #Initialize TLorentz vectors
        lep1Vec = ROOT.TLorentzVector()
        lep2Vec = ROOT.TLorentzVector()
        jet1Vec = ROOT.TLorentzVector()
        jet2Vec = ROOT.TLorentzVector()

        #Get variables from tree for filling histogram
        #datasetNum = event.DatasetNumber
        MET=event.met_Et
        MET_Phi = event.met_Phi
        ht30 = event.Ht30
        if event.jetPt.size() > 0: jet1Vec.SetPtEtaPhiM(event.jetPt[0], event.jetEta[0], event.jetPhi[0], event.jetM[0])
        if event.jetPt.size() > 1: jet2Vec.SetPtEtaPhiM(event.jetPt[1], event.jetEta[1], event.jetPhi[1], event.jetM[1])
        dphi_j1met = TVector2.Phi_mpi_pi(jet1Vec.Phi() - MET_Phi) 
        dphi_j2met = TVector2.Phi_mpi_pi(jet2Vec.Phi() - MET_Phi) 
        nJet25 = event.nJet25
        nLep_signal = event.nLep_signal

        obs = observable()
        lep1Vec, lep1Charge, lep1Flavor = obs.getLep1TLVChargeFlavor(event)
        lep2Vec, lep2Charge, lep2Flavor = obs.getLep2TLVChargeFlavor(event)

        #Calculate dilepton variables
        lepPairVec = lep1Vec + lep2Vec
        mll = lepPairVec.M()
        ptll = lepPairVec.Pt()
        qlql = lep1Charge*lep2Charge
        dphi_l1met = TVector2.Phi_mpi_pi(lep1Vec.Phi() - MET_Phi) 
        dphi_l2met = TVector2.Phi_mpi_pi(lep2Vec.Phi() - MET_Phi) 
        dphi_l1l2  = lep2Vec.DeltaPhi(lep1Vec)
        mt_l1met = TMath.Sqrt(2*lep1Vec.Pt()*MET*(1-TMath.Cos(dphi_l1met)))
        mt_l2met = TMath.Sqrt(2*lep2Vec.Pt()*MET*(1-TMath.Cos(dphi_l2met)))
        mtautau = -999.
        dR_l1l2 = -999.
        if nLep_signal >= 2:
            dR_l1l2  = lep2Vec.DeltaR(lep1Vec)
            mtautau = obs.calcMtautau(event)

        genWeight = event.genWeight

        #Calculating weight
        if self.isdata:
            totalWeight = 1.0
        else:
            totalWeight = float(event.SherpaVjetsNjetsWeight*event.ttbarNNLOWeight*event.pileupWeight*event.eventWeight*event.leptonWeight*event.jvtWeight*event.bTagWeight*genWeight) #TODO: NO TRIGGER WEIGHT!!

        self.hists["MET"].Fill(float(MET), totalWeight)
        self.hists["Lep1Pt"].Fill(float(lep1Vec.Pt()), totalWeight)
        self.hists["Lep2Pt"].Fill(float(lep2Vec.Pt()), totalWeight)
        self.hists["Jet1Pt"].Fill(float(jet1Vec.Pt()), totalWeight)
        self.hists["Jet2Pt"].Fill(float(jet2Vec.Pt()), totalWeight)
        self.hists["nLepSignal"].Fill(float(nLep_signal), totalWeight)
        self.hists["nJet25"].Fill(float(nJet25), totalWeight)
        self.hists["mll"].Fill(float(mll), totalWeight)
        self.hists["ptll"].Fill(float(ptll), totalWeight)
        self.hists["dphiJ1met"].Fill(float((-1)*math.fabs(dphi_j1met)), totalWeight)
        self.hists["dphiJ2met"].Fill(float((-1)*math.fabs(dphi_j2met)), totalWeight)
        self.hists["dphiL1met"].Fill(float(math.fabs(dphi_l1met)), totalWeight)
        self.hists["dphiL2met"].Fill(float(math.fabs(dphi_l2met)), totalWeight)
        self.hists["dphiL1L2"].Fill(float( math.fabs(dphi_l1l2)), totalWeight)
        self.hists["dRL1L2"].Fill(float(dR_l1l2), totalWeight)
        self.hists["qlql"].Fill(int(qlql), totalWeight)
        if (ht30): self.hists["METoverHt"].Fill(float(MET/ht30), totalWeight)
        self.hists["Ht30"].Fill(float(ht30), totalWeight)
        self.hists["MtL1met"].Fill(float(mt_l1met), totalWeight)
        self.hists["MtL2met"].Fill(float(mt_l2met), totalWeight)
        self.hists["MTauTau"].Fill(float(mtautau), totalWeight)
#------------------------------------------------------------------
class allhists:
    def __init__(self, tag, topdir, isdata, treetype, DSID, sumWHist, detaillevel=99):
        self.tag=tag
        self.topdir=topdir
        self.isdata = isdata
        self.tree = treetype
        self.DSID = DSID
        self.sumWHist = sumWHist
        self.hists={}
        self.detaillevel=detaillevel

        self.newdir=topdir.mkdir(tag)
        self.newdir.cd()

        self.hists["mu"]=ROOT.TH1F("h_"+tag+"_mu",tag+"_mu; mu; Events",50,0,50)
        self.hists["MET"]=ROOT.TH1F("h_"+tag+"_MET",tag+"_MET; MET [GeV]; Events/(25 GeV)",22,50,600)
        self.hists['Lep1Pt']=ROOT.TH1F("h_"+tag+"_Lep1Pt",tag+"_Lep1Pt; leading lepton p_{T} [GeV]; Events/(2 GeV)",35, 0, 70)
        self.hists['Lep1Eta']=ROOT.TH1F("h_"+tag+"_Lep1Eta",tag+"_Lep1Eta; leading lepton #eta; Events/0.1",25, 0, 2.5)
        self.hists['Lep2Eta']=ROOT.TH1F("h_"+tag+"_Lep2Eta",tag+"_Lep2Eta; subleading lepton #eta; Events/0.1",25, 0, 2.5)
        self.hists['Lep2Pt']=ROOT.TH1F("h_"+tag+"_Lep2Pt",tag+"_Lep2Pt; subleading lepton p_{T} [GeV]; Events/(2 GeV)",35, 0, 70)
        self.hists['ElPt']=ROOT.TH1F("h_"+tag+"_elPt",tag+"_elPt; electron p_{T} [GeV]; Events/(10 GeV)",20, 0, 200)
        self.hists['MuPt']=ROOT.TH1F("h_"+tag+"_muPt",tag+"_muPt; muon p_{T} [GeV]; Events/(10 GeV)",20, 0, 200)
        #self.hists['ElPt']=ROOT.TH1F("h_"+tag+"_elPt",tag+"_elPt; electron p_{T} [GeV]; Events/(1 GeV)",50, 0, 50)
        #self.hists['MuPt']=ROOT.TH1F("h_"+tag+"_muPt",tag+"_muPt; muon p_{T} [GeV]; Events/(1 GeV)",50, 0, 50)
        self.hists['Jet1Pt']=ROOT.TH1F("h_"+tag+"_Jet1Pt",tag+"_Jet1Pt; leading jet p_{T} [GeV]; Events/(25 GeV)",20, 0, 500)
        self.hists['Jet2Pt']=ROOT.TH1F("h_"+tag+"_Jet2Pt",tag+"_Jet2Pt; subleading jet p_{T} [GeV]; Events/(25 GeV)",20, 0, 500)
        self.hists['nLepSignal']=ROOT.TH1F("h_"+tag+"_nLep_signal",tag+"_nLep_signal; lepton count; Events/count",4, 1, 5)
        self.hists['nJet25']=ROOT.TH1F("h_"+tag+"_nJet25",tag+"_nJet25; jet count; Events/count",7, 1, 8)
        self.hists['nVtx']=ROOT.TH1F("h_"+tag+"_nVtx",tag+"_nVtx; nvertices; Events/count",50, 0, 50)
        self.hists['mll']=ROOT.TH1F("h_"+tag+"_mll",tag+"_mll; dilepton invariant mass [GeV]; Events/(2 GeV) ",30, 0, 60)
        self.hists['mll2']=ROOT.TH1F("h_"+tag+"_mll2",tag+"_mll2; dilepton invariant mass [GeV]; Events/(2 GeV) ",50, 0, 100)
        self.hists['ptll']=ROOT.TH1F("h_"+tag+"_ptll",tag+"_ptll; dilepton p_{T} [GeV]; Events/(5 GeV)",20, 0, 100)
        self.hists['dphiJ1met']=ROOT.TH1F("h_"+tag+"_dphi_j1met",tag+"_dphi_j1met; #Delta#phi_{jet_{1}-met} [rad];Events/(0.25 rad)",14, -3.5, 0. )
        self.hists['dphiJ2met']=ROOT.TH1F("h_"+tag+"_dphi_j2met",tag+"_dphi_j2met; #Delta#phi_{jet_{2}-met} [rad];Events/(0.25 rad)",14, -3.5, 0. )
        self.hists['dphiL1met']=ROOT.TH1F("h_"+tag+"_dphi_l1met",tag+"_dphi_l1met;#Delta#phi_{lep_{1}-met}  [rad];Events/(0.25 rad)",14, 0., 3.5)
        self.hists['dphiL2met']=ROOT.TH1F("h_"+tag+"_dphi_l2met",tag+"_dphi_l2met; #Delta#phi_{lep_{2}-met} [rad];Events/(0.25 rad)",14, 0., 3.5)
        self.hists['dphiL1L2']=ROOT.TH1F("h_"+tag+"_dphi_l1l2",tag+"_dphi_l1l2;#Delta#phi_{lep_{1}-lep_{2}} [rad];Events/(0.25 rad)",14, 0., 3.5)
        self.hists['dRL1L2']=ROOT.TH1F("h_"+tag+"_dR_l1l2",tag+"_dR_l1l2;#DeltaR_{lep_{1}-lep_{2}} [mm];Events/(0.25 mm)",16, 0., 4.0)
        self.hists['lepCharge']=ROOT.TH1F("h_"+tag+"_lep_charge",tag+"_lep_charge; Q_{l} [e], Events/e",4, -1, 3)
        self.hists['qlql']=ROOT.TH1F("h_"+tag+"_qlql",tag+"_qlql; Q_{l}Q_{l} [e^{2}]; Events/e^{2}",4, -1, 3)
        self.hists['lepFlavor']=ROOT.TH1F("h_"+tag+"_lep_flavor",tag+"_lep_flavor; lepton flavor; Events/lepton flavor",3, 1, 4)
        self.hists['lepFlavor'].GetXaxis().SetBinLabel(1,"el")
        self.hists['lepFlavor'].GetXaxis().SetBinLabel(2,"mu")
        self.hists['METoverHt']=ROOT.TH1F("h_"+tag+"_METoverHt",tag+"_METoverHt; MET/H_{T}; Events/0.1",30, 0.0, 3.0)
        self.hists['Ht30']=ROOT.TH1F("h_"+tag+"_Ht30",tag+"_Ht30; H_{T} [GeV]; Events/(25 GeV)",21, 0, 525)
        self.hists['Mt']=ROOT.TH1F("h_"+tag+"_Mt",tag+"_Mt; M_{T} [GeV]; Events/(25 GeV)",10, 0, 250)
        self.hists['MtL1met']=ROOT.TH1F("h_"+tag+"_Mt_l1met",tag+"_Mt_l1met; m_{T} {l1-met} [GeV]; Events/(10 GeV) ",15, 0, 150)
        self.hists['MtL2met']=ROOT.TH1F("h_"+tag+"_Mt_l2met",tag+"_Mt_l2met;  m_{T} {l2-met} [GeV]; Events/(10 GeV)",10, 0, 100)
        self.hists['MTauTau']=ROOT.TH1F("h_"+tag+"_MTauTau",tag+"_MTauTau; M_{#Tau#Tau}; Events/(20 GeV) ",52, -40., 1000)
        #self.hists['TotalWeight'] = ROOT.TH1F("h_"+tag+"_TotalWeight", tag+"_TotalWeight", 100, -20, 20)
        #self.hists['PileupWeight'] = ROOT.TH1F("h_"+tag+"_PileupWeight", tag+"_PileupWeight", 100, -5, 5)
        #self.hists['EventWeight'] = ROOT.TH1F("h_"+tag+"_EventWeight", tag+"_EventWeight", 100, -5, 5)
        #self.hists['LeptonWeight'] = ROOT.TH1F("h_"+tag+"_LeptonWeight", tag+"_LeptonWeight", 100, -5, 5)
        #self.hists['JVTWeight'] = ROOT.TH1F("h_"+tag+"_JVTWeight", tag+"_JVTWeight", 100, -5, 5)
        #self.hists['BTagWeight'] = ROOT.TH1F("h_"+tag+"_BTagWeight", tag+"_BTagWeight", 100, -5, 5)
        #self.hists['GenWeight'] = ROOT.TH1F("h_"+tag+"_GenWeight", tag+"_GenWeight", 100, -20, 20)
        #self.hists['TTbarNNLOWeight'] = ROOT.TH1F("h_"+tag+"_ttbarNNLOWeight", tag+"_ttbarNNLOWeight", 100, -5, 5)
        #self.hists['SherpaVjetsNjetsWeight'] = ROOT.TH1F("h_"+tag+"_SherpaVjetsNjetsWeight", tag+"_SherpaVjetsNjetsWeight", 100, -5, 5)

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
        intLumi = 36300.0 #Same as used by Lorenzo Rossini
        #intLumi = 3230.0 #data16PeriodC (in pb^-1)
        #intLumi = 2582.0 #date16PeriodK (in pb^-1)
        #intLumi = 2222.0 #(in pb^-1)
        #intLumi = 2147.0 #(in pb^-1)
        #intLumi = 1948.44 #(in pb^-1)
        #intLumi = 5812.0 #(in pb^-1)
        #intLumi = 1.0

        #Initialize TLorentz vectors
        lep1Vec = ROOT.TLorentzVector()
        lep2Vec = ROOT.TLorentzVector()
        jet1Vec = ROOT.TLorentzVector()
        jet2Vec = ROOT.TLorentzVector()

        #Get variables from tree for filling histogram
        mu = event.mu
        nVtx = event.nVtx
        datasetNum = event.DatasetNumber
        MET=event.met_Et
        MET_Phi = event.met_Phi
        ht30 = event.Ht30
        if event.jetPt.size() > 0: jet1Vec.SetPtEtaPhiM(event.jetPt[0], event.jetEta[0], event.jetPhi[0], event.jetM[0])
        if event.jetPt.size() > 1: jet2Vec.SetPtEtaPhiM(event.jetPt[1], event.jetEta[1], event.jetPhi[1], event.jetM[1])
        dphi_j1met = TVector2.Phi_mpi_pi(jet1Vec.Phi() - MET_Phi) 
        dphi_j2met = TVector2.Phi_mpi_pi(jet2Vec.Phi() - MET_Phi) 
        nJet25 = event.nJet25
        mt = event.mt
        nLep_base = event.nLep_base
        nLep_signal = event.nLep_signal

        obs = observable()
        lep1Vec, lep1Charge, lep1Flavor = obs.getLep1TLVChargeFlavor(event)
        lep2Vec, lep2Charge, lep2Flavor = obs.getLep2TLVChargeFlavor(event)

        #Calculate dilepton variables
        lepPairVec = lep1Vec + lep2Vec
        mll = lepPairVec.M()
        ptll = lepPairVec.Pt()
        qlql = lep1Charge*lep2Charge
        dphi_l1met = TVector2.Phi_mpi_pi(lep1Vec.Phi() - MET_Phi) 
        dphi_l2met = TVector2.Phi_mpi_pi(lep2Vec.Phi() - MET_Phi) 
        dphi_l1l2  = lep2Vec.DeltaPhi(lep1Vec)
        mt_l1met = TMath.Sqrt(2*lep1Vec.Pt()*MET*(1-TMath.Cos(dphi_l1met)))
        mt_l2met = TMath.Sqrt(2*lep2Vec.Pt()*MET*(1-TMath.Cos(dphi_l2met)))
        mtautau = -999.
        dR_l1l2 = -999.
        if nLep_signal >= 2:
            dR_l1l2  = lep2Vec.DeltaR(lep1Vec)
            mtautau = obs.calcMtautau(event)

        genWeight = event.genWeight

        #Calculating weight
        if self.isdata:
            totalWeight = 1.0
        else:
            totalWeight = float(event.SherpaVjetsNjetsWeight*event.ttbarNNLOWeight*event.pileupWeight*event.eventWeight*event.leptonWeight*event.jvtWeight*event.bTagWeight*genWeight) #TODO: NO TRIGGER WEIGHT!!

        self.hists["mu"].Fill(float(mu), totalWeight)
        self.hists["MET"].Fill(float(MET), totalWeight)
        self.hists["Lep1Pt"].Fill(float(lep1Vec.Pt()), totalWeight)
        self.hists["Lep2Pt"].Fill(float(lep2Vec.Pt()), totalWeight)
        self.hists["Lep1Eta"].Fill(float(lep1Vec.Eta()), totalWeight)
        if lep1Flavor == 1: self.hists["ElPt"].Fill(int(lep1Vec.Pt()), totalWeight) 
        elif lep1Flavor == 2: self.hists["MuPt"].Fill(int(lep1Vec.Pt()), totalWeight) 
        if lep2Flavor == 1: self.hists["ElPt"].Fill(int(lep2Vec.Pt()), totalWeight) 
        elif lep2Flavor == 2: self.hists["MuPt"].Fill(int(lep2Vec.Pt()), totalWeight) 
        self.hists["Lep2Eta"].Fill(float(lep2Vec.Eta()), totalWeight)
        self.hists["Jet1Pt"].Fill(float(jet1Vec.Pt()), totalWeight)
        self.hists["Jet2Pt"].Fill(float(jet2Vec.Pt()), totalWeight)
        self.hists["nLepSignal"].Fill(float(nLep_signal), totalWeight)
        self.hists["nJet25"].Fill(float(nJet25), totalWeight)
        self.hists["nVtx"].Fill(float(nVtx), totalWeight)
        self.hists["mll"].Fill(float(mll), totalWeight)
        self.hists["mll2"].Fill(float(mll), totalWeight)
        self.hists["ptll"].Fill(float(ptll), totalWeight)
        self.hists["dphiJ1met"].Fill(float((-1)*math.fabs(dphi_j1met)), totalWeight)
        self.hists["dphiJ2met"].Fill(float((-1)*math.fabs(dphi_j2met)), totalWeight)
        self.hists["dphiL1met"].Fill(float(math.fabs(dphi_l1met)), totalWeight)
        self.hists["dphiL2met"].Fill(float(math.fabs(dphi_l2met)), totalWeight)
        self.hists["dphiL1L2"].Fill(float( math.fabs(dphi_l1l2)), totalWeight)
        self.hists["dRL1L2"].Fill(float(dR_l1l2), totalWeight)
        self.hists["lepCharge"].Fill(int(lep1Charge), totalWeight)
        self.hists["lepCharge"].Fill(int(lep2Charge), totalWeight)
        self.hists["qlql"].Fill(int(qlql), totalWeight)
        self.hists["lepFlavor"].Fill(int(lep1Flavor), totalWeight)
        self.hists["lepFlavor"].Fill(int(lep2Flavor), totalWeight)
        if (ht30): self.hists["METoverHt"].Fill(float(MET/ht30), totalWeight)
        self.hists["Ht30"].Fill(float(ht30), totalWeight)
        self.hists["Mt"].Fill(float(mt), totalWeight)
        self.hists["MtL1met"].Fill(float(mt_l1met), totalWeight)
        self.hists["MtL2met"].Fill(float(mt_l2met), totalWeight)
        self.hists["MTauTau"].Fill(float(mtautau), totalWeight)
        #self.hists["TotalWeight"].Fill(float(totalWeight))
        #self.hists["PileupWeight"].Fill(float(event.pileupWeight))
        #self.hists["EventWeight"].Fill(float(event.eventWeight))
        #self.hists["LeptonWeight"].Fill(float(event.leptonWeight))
        #self.hists["JVTWeight"].Fill(float(event.jvtWeight))
        #self.hists["BTagWeight"].Fill(float(event.bTagWeight))
        #self.hists["GenWeight"].Fill(float(genWeight))
        #self.hists["TTbarNNLOWeight"].Fill(float(event.ttbarNNLOWeight))
        #self.hists["SherpaVjetsNjetsWeight"].Fill(float(event.SherpaVjetsNjetsWeight))


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

    def addcollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=allhists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.DSID, self.sumWHist, self.detaillevel)
        self.topdir.cd()

    def addbasecollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=basehists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.DSID, self.sumWHist, self.detaillevel)
        self.topdir.cd()

    def addmincollection(self, tag):
        self.newdir.cd()
        self.collections[tag]=minhists(self.tag+"_"+tag, self.newdir, self.isdata, self.tree, self.DSID, self.sumWHist, self.detaillevel)
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
