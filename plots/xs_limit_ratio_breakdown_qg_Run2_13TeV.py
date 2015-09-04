#!/usr/bin/env python

import string, re
from ROOT import *
from array import array
import CMS_lumi


gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.06)
gStyle.SetPadBottomMargin(0.14)
gROOT.ForceStyle()


masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])

xs_stat = array('d', [9.27197, 6.59059, 2.77974, 1.1509, 0.71554, 0.631862, 0.923053, 1.30437, 1.37069, 1.2449, 1.50024, 1.48777, 1.26241, 0.823442, 0.573455, 0.595751, 0.69501, 0.721993, 0.626517, 0.506572, 0.390985, 0.334182, 0.282897, 0.222017, 0.182441, 0.14795, 0.129763, 0.126603, 0.124769, 0.121115, 0.116706, 0.111087, 0.11451, 0.114971, 0.117893, 0.120354, 0.120758, 0.121099, 0.119221, 0.115905, 0.111707, 0.11008, 0.10561, 0.101259, 0.0969261, 0.0924037, 0.0895898, 0.0873745, 0.0854951, 0.0890997, 0.0887404, 0.0885351, 0.0884573, 0.088597, 0.0889309, 0.0891478])

xs_sys_all = array('d', [12.5406, 9.37948, 4.78078, 2.24239, 1.38317, 1.25686, 1.68168, 1.94743, 1.92662, 1.87468, 1.87853, 1.77258, 1.55049, 1.16436, 0.832195, 0.755232, 0.795726, 0.796131, 0.715206, 0.602903, 0.479742, 0.395314, 0.325895, 0.25961, 0.211346, 0.171212, 0.145859, 0.136918, 0.131901, 0.127337, 0.123564, 0.119239, 0.11822, 0.119847, 0.123728, 0.125759, 0.126204, 0.123843, 0.123354, 0.11945, 0.115794, 0.112136, 0.108037, 0.104277, 0.0984421, 0.0934844, 0.0910292, 0.0893694, 0.0882712, 0.0901911, 0.0901477, 0.0892953, 0.0896335, 0.0882758, 0.0884687, 0.0886266])
xs_sys_lumi = array('d', [9.81289, 6.87049, 2.77784, 1.15056, 0.700884, 0.630868, 0.929309, 1.31968, 1.40529, 1.28215, 1.56259, 1.54264, 1.28837, 0.834521, 0.582873, 0.606434, 0.721272, 0.752518, 0.653671, 0.513098, 0.39774, 0.340064, 0.287563, 0.22646, 0.179531, 0.147853, 0.130028, 0.126179, 0.125786, 0.12291, 0.117932, 0.112254, 0.111283, 0.115005, 0.119894, 0.122923, 0.123953, 0.123876, 0.121208, 0.117734, 0.114171, 0.109742, 0.104884, 0.0996428, 0.0946832, 0.0914628, 0.0887846, 0.0863996, 0.0848149, 0.087723, 0.0876388, 0.0870421, 0.0866771, 0.0871145, 0.0875739, 0.0874017])
xs_sys_jes = array('d', [9.26231, 6.89437, 2.8486, 1.16868, 0.713769, 0.636801, 0.923281, 1.26845, 1.3489, 1.3034, 1.49817, 1.48806, 1.2965, 0.900706, 0.616326, 0.609406, 0.692435, 0.713093, 0.644068, 0.528493, 0.415448, 0.342106, 0.288032, 0.232045, 0.185519, 0.15092, 0.130713, 0.12645, 0.122867, 0.118693, 0.114812, 0.111368, 0.111088, 0.113301, 0.117811, 0.118344, 0.119212, 0.120011, 0.117406, 0.114593, 0.111314, 0.10816, 0.103277, 0.0986437, 0.0934231, 0.0898432, 0.0876526, 0.0852287, 0.0836959, 0.0859556, 0.0856084, 0.0848474, 0.0850338, 0.0855501, 0.0853157, 0.0861754])
xs_sys_jer = array('d', [9.43975, 6.57582, 2.73085, 1.13021, 0.682826, 0.622687, 0.927036, 1.29153, 1.36387, 1.29054, 1.50266, 1.50306, 1.24655, 0.834942, 0.578162, 0.601306, 0.697827, 0.721708, 0.631654, 0.500743, 0.388795, 0.332444, 0.280911, 0.221413, 0.177409, 0.145473, 0.127131, 0.123411, 0.123139, 0.119048, 0.11552, 0.109801, 0.109608, 0.112802, 0.117056, 0.11911, 0.121503, 0.120358, 0.117867, 0.115286, 0.110763, 0.106814, 0.102707, 0.0985608, 0.0935585, 0.0892285, 0.0860346, 0.0846071, 0.0828486, 0.0865476, 0.0857814, 0.084906, 0.0856398, 0.0862076, 0.0849003, 0.0860822])
xs_sys_allexceptbkg = array('d', [9.83788, 7.24729, 2.94769, 1.20805, 0.725391, 0.656722, 0.956133, 1.32004, 1.40964, 1.35172, 1.56154, 1.5579, 1.346, 0.937789, 0.647005, 0.639328, 0.723707, 0.743606, 0.670664, 0.551267, 0.426892, 0.361375, 0.298098, 0.239937, 0.190147, 0.158076, 0.135694, 0.128843, 0.127316, 0.123437, 0.118957, 0.114539, 0.112659, 0.117741, 0.121053, 0.122881, 0.123131, 0.1236, 0.122071, 0.11763, 0.114921, 0.110499, 0.106678, 0.103001, 0.0965324, 0.0920132, 0.0894288, 0.0887239, 0.0859146, 0.0887736, 0.0887782, 0.0882258, 0.0875664, 0.0882443, 0.0880411, 0.0890215])
xs_sys_bkg = array('d', [11.5217, 8.16118, 4.15314, 2.03934, 1.31111, 1.14035, 1.51365, 1.815, 1.8288, 1.59973, 1.77437, 1.69853, 1.4238, 0.962617, 0.699861, 0.687936, 0.763596, 0.773707, 0.665526, 0.534368, 0.41719, 0.354754, 0.300091, 0.238545, 0.188025, 0.156593, 0.136422, 0.131205, 0.127395, 0.122596, 0.118449, 0.113722, 0.112066, 0.115896, 0.119609, 0.121989, 0.121967, 0.120479, 0.119161, 0.11588, 0.11195, 0.107603, 0.102467, 0.0976463, 0.0938142, 0.0896857, 0.0875314, 0.0861936, 0.0848364, 0.0870018, 0.0856153, 0.0845813, 0.0855947, 0.0855332, 0.0867183, 0.085887])


r_all = array('d')
r_lumi = array('d')
r_jes = array('d')
r_jer = array('d')
r_allexceptbkg = array('d')
r_bkg = array('d')


for i in range(0,len(xs_stat)):
  r_all.append( xs_sys_all[i] / xs_stat[i] )
  r_lumi.append( xs_sys_lumi[i] / xs_stat[i] )
  r_jes.append( xs_sys_jes[i] / xs_stat[i] )
  r_jer.append( xs_sys_jer[i] / xs_stat[i] )
  r_allexceptbkg.append( xs_sys_allexceptbkg[i] / xs_stat[i] )
  r_bkg.append( xs_sys_bkg[i] / xs_stat[i] )

g_all = TGraph(len(masses),masses,r_all)
g_all.SetMarkerStyle(20)
g_all.SetMarkerColor(kBlack)
g_all.SetLineWidth(2)
g_all.SetLineStyle(1)
g_all.SetLineColor(kBlack)
g_all.GetXaxis().SetTitle("qg resonance mass [GeV]")
g_all.GetYaxis().SetTitle("Limit ratio")
g_all.GetYaxis().SetTitleOffset(1.1)
g_all.GetYaxis().SetRangeUser(0.5,3.)
#g_all.GetXaxis().SetNdivisions(1005)

g_lumi = TGraph(len(masses),masses,r_lumi)
g_lumi.SetMarkerStyle(24)
g_lumi.SetMarkerColor(kGreen+2)
g_lumi.SetLineWidth(2)
g_lumi.SetLineStyle(2)
g_lumi.SetLineColor(kGreen+2)

g_jes = TGraph(len(masses),masses,r_jes)
g_jes.SetMarkerStyle(25)
g_jes.SetMarkerColor(kBlue)
g_jes.SetLineWidth(2)
g_jes.SetLineStyle(3)
g_jes.SetLineColor(kBlue)

g_jer = TGraph(len(masses),masses,r_jer)
g_jer.SetMarkerStyle(26)
g_jer.SetMarkerColor(45)
g_jer.SetLineWidth(2)
g_jer.SetLineStyle(4)
g_jer.SetLineColor(45)

g_allexceptbkg = TGraph(len(masses),masses,r_allexceptbkg)
g_allexceptbkg.SetMarkerStyle(27)
g_allexceptbkg.SetMarkerColor(kMagenta)
g_allexceptbkg.SetLineWidth(2)
g_allexceptbkg.SetLineStyle(5)
g_allexceptbkg.SetLineColor(kMagenta)

g_bkg = TGraph(len(masses),masses,r_bkg)
g_bkg.SetMarkerStyle(30)
g_bkg.SetMarkerColor(kRed)
g_bkg.SetLineWidth(2)
g_bkg.SetLineStyle(6)
g_bkg.SetLineColor(kRed)

c = TCanvas("c", "",800,800)
c.cd()

g_all.Draw("ALP")
g_lumi.Draw("LP")
g_jes.Draw("LP")
g_jer.Draw("LP")
g_allexceptbkg.Draw("LP")
g_bkg.Draw("LP")

legend = TLegend(.40,.56,.60,.80)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.AddEntry(g_all, "All / Stat. only","lp")
legend.AddEntry(g_lumi, "Lumi / Stat. only","lp")
legend.AddEntry(g_jes, "JES / Stat. only","lp")
legend.AddEntry(g_jer, "JER / Stat. only","lp")
legend.AddEntry(g_allexceptbkg, "All except bkg / Stat. only","lp")
legend.AddEntry(g_bkg, "Bkg / Stat. only","lp")

legend.Draw()

#draw the lumi text on the canvas
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "65 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_breakdown_DijetLimitCode_qg_Run2_13TeV_DATA_65_invpb.eps')
