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
xs_stat_exp = array('d', [3.78652, 3.14478, 2.72866, 2.27239, 2.25376, 1.7538, 1.52206, 1.4179, 1.2295, 1.09235, 0.942697, 0.788861, 0.744651, 0.696239, 0.571836, 0.488146, 0.451538, 0.41692, 0.377907, 0.345801, 0.319972, 0.2833, 0.265039, 0.257246, 0.230111, 0.20923, 0.206034, 0.192859, 0.175223, 0.167692, 0.155077, 0.147004, 0.139667, 0.125645, 0.118047, 0.113118, 0.107298, 0.104612, 0.0998593, 0.0964493, 0.0924754, 0.095515, 0.0907703, 0.0876647, 0.0827607, 0.0825839, 0.0799452, 0.0852043, 0.0823653, 0.0791724, 0.0792803, 0.0793793, 0.079605, 0.0798477, 0.0802499, 0.0808961])

xs_sys_all = array('d', [12.5406, 9.37948, 4.78078, 2.24239, 1.38317, 1.25686, 1.68168, 1.94743, 1.92662, 1.87468, 1.87853, 1.77258, 1.55049, 1.16436, 0.832195, 0.755232, 0.795726, 0.796131, 0.715206, 0.602903, 0.479742, 0.395314, 0.325895, 0.25961, 0.211346, 0.171212, 0.145859, 0.136918, 0.131901, 0.127337, 0.123564, 0.119239, 0.11822, 0.119847, 0.123728, 0.125759, 0.126204, 0.123843, 0.123354, 0.11945, 0.115794, 0.112136, 0.108037, 0.104277, 0.0984421, 0.0934844, 0.0910292, 0.0893694, 0.0882712, 0.0901911, 0.0901477, 0.0892953, 0.0896335, 0.0882758, 0.0884687, 0.0886266])
xs_sys_all_exp = array('d', [6.963035, 5.234485, 4.78548, 4.11655, 3.46492, 2.882205, 2.543355, 2.031055, 1.757135, 1.48026, 1.322525, 1.10827, 0.954116, 0.872991, 0.7542415, 0.6370555, 0.5723285, 0.5029675, 0.434956, 0.4068035, 0.3650865, 0.3335655, 0.3109965, 0.285384, 0.2527855, 0.24022, 0.222743, 0.2072525, 0.193565, 0.1746095, 0.1628835, 0.152846, 0.147671, 0.1341245, 0.128476, 0.116897, 0.1136705, 0.1087305, 0.104016, 0.1010055, 0.09851205, 0.09298415, 0.0917058, 0.0900467, 0.0882874, 0.08667085, 0.0846071, 0.08561135, 0.08328465, 0.0811388, 0.0809772, 0.0810575, 0.08118935, 0.081406, 0.0820564, 0.08247915])


r_all_exp = array('d')
r_all = array('d')

for i in range(0,len(xs_stat)):
  r_all_exp.append( xs_sys_all_exp[i] / xs_stat_exp[i] )
  r_all.append( xs_sys_all[i] / xs_stat[i] )

g_all_exp = TGraph(len(masses),masses,r_all_exp)
g_all_exp.SetMarkerStyle(24)
g_all_exp.SetMarkerColor(kGreen+2)
g_all_exp.SetLineWidth(2)
g_all_exp.SetLineStyle(2)
g_all_exp.SetLineColor(kGreen+2)
g_all_exp.GetXaxis().SetTitle("qg resonance mass [GeV]")
g_all_exp.GetYaxis().SetTitle("Limit ratio")
g_all_exp.GetYaxis().SetTitleOffset(1.1)
g_all_exp.GetYaxis().SetRangeUser(0.5,3.)
#g_all_exp.GetXaxis().SetNdivisions(1005)

g_all = TGraph(len(masses),masses,r_all)
g_all.SetMarkerStyle(20)
g_all.SetMarkerColor(kBlack)
g_all.SetLineWidth(2)
g_all.SetLineStyle(1)
g_all.SetLineColor(kBlack)

c = TCanvas("c", "",800,800)
c.cd()

g_all_exp.Draw("ALP")
g_all.Draw("LP")

legend = TLegend(.40,.65,.60,.75)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.AddEntry(g_all_exp, "All / Stat. only (expected)","lp")
legend.AddEntry(g_all, "All / Stat. only (observed)","lp")

legend.Draw()

#l1 = TLatex()
#l1.SetTextAlign(12)
#l1.SetTextFont(42)
#l1.SetNDC()
#l1.SetTextSize(0.04)
#l1.DrawLatex(0.18,0.43, "CMS Preliminary")
#l1.DrawLatex(0.18,0.35, "#intLdt = 5 fb^{-1}")
#l1.DrawLatex(0.19,0.30, "#sqrt{s} = 7 TeV")
#l1.DrawLatex(0.18,0.25, "|#eta| < 2.5, |#Delta#eta| < 1.3")
#l1.DrawLatex(0.18,0.20, "Wide Jets")

#draw the lumi text on the canvas
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "65 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_DijetLimitCode_qg_Run2_13TeV_DATA_65_invpb.eps')
