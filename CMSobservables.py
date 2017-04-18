import re, time, copy, math, array
import ROOT
from ROOT import TVector2, TLorentzVector, TMath
ROOT.gROOT.SetBatch(True)
 #------------------------------------------------------------------
class observable:
    def __init__(self):

        self.varibales={}

    def getJetSum(self, event):
        j1_t3 = ROOT.TLorentzVector() 
        j2_t3 = ROOT.TLorentzVector() 
        j3_t3 = ROOT.TLorentzVector() 
        j4_t3 = ROOT.TLorentzVector() 
        j5_t3 = ROOT.TLorentzVector() 
        j6_t3 = ROOT.TLorentzVector() 
        j7_t3 = ROOT.TLorentzVector() 
        j8_t3 = ROOT.TLorentzVector() 
        jetSum = ROOT.TLorentzVector() 

        if event.jetPt.size() > 0: j1_t3.SetPtEtaPhiM(event.jetPt[0], event.jetEta[0], event.jetPhi[0], event.jetM[0]) 
        if event.jetPt.size() > 1: j2_t3.SetPtEtaPhiM(event.jetPt[1], event.jetEta[1], event.jetPhi[1], event.jetM[1]) 
        if event.jetPt.size() > 2: j3_t3.SetPtEtaPhiM(event.jetPt[2], event.jetEta[2], event.jetPhi[2], event.jetM[2])
        if event.jetPt.size() > 3: j4_t3.SetPtEtaPhiM(event.jetPt[3], event.jetEta[3], event.jetPhi[3], event.jetM[3])
        if event.jetPt.size() > 4: j5_t3.SetPtEtaPhiM(event.jetPt[4], event.jetEta[4], event.jetPhi[4], event.jetM[4])
        if event.jetPt.size() > 5: j6_t3.SetPtEtaPhiM(event.jetPt[5], event.jetEta[5], event.jetPhi[5], event.jetM[5])
        if event.jetPt.size() > 6: j7_t3.SetPtEtaPhiM(event.jetPt[6], event.jetEta[6], event.jetPhi[6], event.jetM[6])
        if event.jetPt.size() > 7: j8_t3.SetPtEtaPhiM(event.jetPt[7], event.jetEta[7], event.jetPhi[7], event.jetM[7])

        if event.jetPt.size() == 0:
            jetSum.SetPtEtaPhiM(0.0, 0.0, 0.0, 0.0)
            #print('No jets in event')
        elif event.jetPt.size() == 1:
            jetSum = j1_t3
        elif event.jetPt.size() == 2:
            jetSum = j1_t3 + j2_t3
        elif event.jetPt.size() == 3:
            jetSum = j1_t3 + j2_t3 + j3_t3
        elif event.jetPt.size() == 4:
            jetSum = j1_t3 + j2_t3 + j3_t3 + j4_t3
        elif event.jetPt.size() == 5:
            jetSum = j1_t3 + j2_t3 + j3_t3 + j4_t3 + j5_t3
        elif event.jetPt.size() == 6:
            jetSum = j1_t3 + j2_t3 + j3_t3 + j4_t3 + j5_t3 + j6_t3 
        elif event.jetPt.size() == 7:
            jetSum = j1_t3 + j2_t3 + j3_t3 + j4_t3 + j5_t3 + j6_t3 + j7_t3 
        elif event.jetPt.size() >= 8:
            jetSum = j1_t3 + j2_t3 + j3_t3 + j4_t3 + j5_t3 + j6_t3 + j7_t3 + j8_t3
        else: print "ERROR: can't calculate jet sum"

        return jetSum

    def getLep1TLVChargeFlavor(self, event):
        l1_tlv = ROOT.TLorentzVector()
        l1Charge = 0
        l1Flavor = 0
        index1, index2 = self.findSignalPairs(event)
        #print "index1 = %i, index2 = %i" % (index1, index2)
        #print "l1 charge = %i, l2 charge = %i, l3 charge = %i" % (event.lep1Charge, event.lep2Charge, event.lep3Charge)
        if (index1 == 1):
            l1_tlv.SetPtEtaPhiM(event.lep1Pt, event.lep1Eta, event.lep1Phi, event.lep1M)
            l1Charge = event.lep1Charge
            l1Flavor = event.lep1Flavor
        elif (index1 == 2):
            l1_tlv.SetPtEtaPhiM(event.lep2Pt, event.lep2Eta, event.lep2Phi, event.lep2M)
            l1Charge = event.lep2Charge
            l1Flavor = event.lep2Flavor
        elif (index1 == 3):
            l1_tlv.SetPtEtaPhiM(event.lep3Pt, event.lep3Eta, event.lep3Phi, event.lep3M)
            l1Charge = event.lep3Charge
            l1Flavor = event.lep3Flavor
        #print "returning l1 charge and type: charge = %i, type = %i" % (l1Charge, l1Flavor)
        return l1_tlv, l1Charge, l1Flavor

    def getLep2TLVChargeFlavor(self, event):
        l2_tlv = ROOT.TLorentzVector()
        index1, index2 = self.findSignalPairs(event)
        if (index2 == 2):
            l2_tlv.SetPtEtaPhiM(event.lep2Pt, event.lep2Eta, event.lep2Phi, event.lep2M)
            l2Charge = event.lep2Charge
            l2Flavor = event.lep2Flavor
        elif (index2 == 3):
            l2_tlv.SetPtEtaPhiM(event.lep3Pt, event.lep3Eta, event.lep3Phi, event.lep3M)
            l2Charge = event.lep3Charge
            l2Flavor = event.lep3Flavor
        elif (index2 == 4):
            l2_tlv.SetPtEtaPhiM(event.lep4Pt, event.lep4Eta, event.lep4Phi, event.lep4M)
            l2Charge = event.lep4Charge
            l2Flavor = event.lep4Flavor
        return l2_tlv, l2Charge, l2Flavor

    def getLep1TLV(self, event):
        l1_tlv = ROOT.TLorentzVector()
        index1, index2 = self.findSignalPairs(event)
        if (index1 == 1):
            l1_tlv.SetPtEtaPhiM(event.lep1Pt, event.lep1Eta, event.lep1Phi, event.lep1M)
        elif (index1 == 2):
            l1_tlv.SetPtEtaPhiM(event.lep2Pt, event.lep2Eta, event.lep2Phi, event.lep2M)
        elif (index1 == 3):
            l1_tlv.SetPtEtaPhiM(event.lep3Pt, event.lep3Eta, event.lep3Phi, event.lep3M)
        return l1_tlv

    def getLep2TLV(self, event):
        l2_tlv = ROOT.TLorentzVector()
        index1, index2 = self.findSignalPairs(event)
        if (index2 == 2):
            l2_tlv.SetPtEtaPhiM(event.lep2Pt, event.lep2Eta, event.lep2Phi, event.lep2M)
        elif (index2 == 3):
            l2_tlv.SetPtEtaPhiM(event.lep3Pt, event.lep3Eta, event.lep3Phi, event.lep3M)
        elif (index2 == 4):
            l2_tlv.SetPtEtaPhiM(event.lep4Pt, event.lep4Eta, event.lep4Phi, event.lep4M)
        return l2_tlv

    def findC1(self, event):
        const_1 = 0.
        l1 = self.getLep1TLV(event)
        l2 = self.getLep2TLV(event)
        j  = self.getJetSum(event)
        numerator = (j.Py()*l2.Px()/l2.Py()) - j.Px()
        if(l2.Py()): denominator = l1.Px() - (l1.Py()*l2.Px()/l2.Py())
        if (denominator): const_1 = numerator/denominator
        return const_1

    def findC2(self, event, f1):
        const_2 = 0.
        l1 = self.getLep1TLV(event)
        l2 = self.getLep2TLV(event)
        j  = self.getJetSum(event)
        if(l2.Py()): 
            const_2 = -(j.Py()/l2.Py()) - f1*(l1.Py()/l2.Py())
        return const_2


    def calcMtautau(self, event):
        new_tlv1 = self.getLep1TLV(event)
        new_tlv2 = self.getLep2TLV(event)
        old_tlv1 = self.getLep1TLV(event)
        old_tlv2 = self.getLep2TLV(event)
        old_spacial1 = old_tlv1.Vect() 
        old_spacial2 = old_tlv2.Vect() 
        new_spacial1 = old_tlv1.Vect() 
        new_spacial2 = old_tlv2.Vect() 
        f1 = self.findC1(event)
        f2 = self.findC2(event, f1)
        new_spacial1.SetMag(old_spacial1.Mag()*f1)
        new_spacial2.SetMag(old_spacial2.Mag()*f2)
        if (f1 < 0.): new_tlv1.SetVectM(new_spacial1, old_tlv1.M()) 
        else: new_tlv1.SetVectM(new_spacial1, (-1)*old_tlv1.M())
        if (f2 < 0.): new_tlv2.SetVectM(new_spacial2, old_tlv2.M())
        else: new_tlv2.SetVectM(new_spacial2, (-1)*old_tlv2.M())
        lepSum_old = old_tlv1+old_tlv2
        lepSum_new = new_tlv1+new_tlv2
        new_mass = lepSum_new.M()
        return new_mass

    def findBasePairs(self, event):
        Qlep1 = event.lep1Charge
        Qlep2 = event.lep2Charge
        Qlep3 = event.lep3Charge
        Qlep4 = event.lep4Charge
        Tlep1 = event.lep1Flavor
        Tlep2 = event.lep2Flavor
        Tlep3 = event.lep3Flavor
        Tlep4 = event.lep4Flavor
        index1 = 0
        index2 = 0
        if ( Qlep1*Qlep2 == -1):
            index1 = 1
            index2 = 2
        elif (Qlep1*Qlep3 == -1):
            index1 = 1
            index2 = 3
        elif (Qlep2*Qlep3 == -1):
            index1 = 2
            index2 = 3
        elif (Qlep1*Qlep4 == -1):
            index1 = 1
            index2 = 4
        elif (Qlep2*Qlep4 == -1):
            index1 = 2
            index2 = 4
        elif (Qlep3*Qlep4 == -1):
            index1 = 3
            index2 = 4
        else: 
            index1 = 1
            index2 = 2
        return index1, index2
    def findSignalPairs(self, event):
        if event.lep1Signal:
            Qlep1 = event.lep1Charge
        else: Qlep1 = 0
        if event.lep2Signal:
            Qlep2 = event.lep2Charge
        else: Qlep2 = 0
        if event.lep3Signal:
            Qlep3 = event.lep3Charge
        else: Qlep3 = 0
        if event.lep4Signal:
            Qlep4 = event.lep4Charge
        else: Qlep4 = 0
        Tlep1 = event.lep1Flavor
        Tlep2 = event.lep2Flavor
        Tlep3 = event.lep3Flavor
        Tlep4 = event.lep4Flavor
        index1 = 0
        index2 = 0
        if ( Qlep1*Qlep2 == -1):
            index1 = 1
            index2 = 2
        elif (Qlep1*Qlep3 == -1):
            index1 = 1
            index2 = 3
        elif (Qlep2*Qlep3 == -1):
            index1 = 2
            index2 = 3
        elif (Qlep1*Qlep4 == -1):
            index1 = 1
            index2 = 4
        elif (Qlep2*Qlep4 == -1):
            index1 = 2
            index2 = 4
        elif (Qlep3*Qlep4 == -1):
            index1 = 3
            index2 = 4
        else: 
            index1 = 1
            index2 = 2
        return index1, index2

        
