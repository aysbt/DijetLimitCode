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

xs_stat = array('d', [12.292, 11.1613, 4.66571, 1.84314, 1.04291, 0.777015, 1.05077, 1.65442, 1.89949, 1.64311, 1.93199, 2.09924, 1.87003, 1.25188, 0.807536, 0.755385, 0.947204, 1.0134, 0.916394, 0.752066, 0.551647, 0.480825, 0.430062, 0.339736, 0.259111, 0.219167, 0.181339, 0.168709, 0.170135, 0.168461, 0.161905, 0.15092, 0.143298, 0.149543, 0.156085, 0.158695, 0.16199, 0.162997, 0.160913, 0.15699, 0.152083, 0.146292, 0.139368, 0.132384, 0.126673, 0.122171, 0.122027, 0.120568, 0.119602, 0.119931, 0.128213, 0.130565, 0.133476, 0.136966, 0.141213, 0.146015])
xs_stat_exp = array('d', [5.47802, 4.36122, 4.19892, 3.37816, 2.97497, 2.7817, 2.13559, 1.95129, 1.76424, 1.53202, 1.31067, 1.16192, 0.974604, 0.91502, 0.848704, 0.742918, 0.658287, 0.554933, 0.494442, 0.466983, 0.432907, 0.399693, 0.350458, 0.343739, 0.320855, 0.295009, 0.282642, 0.257422, 0.231262, 0.225847, 0.209487, 0.198307, 0.188087, 0.171077, 0.159239, 0.155893, 0.14491, 0.138011, 0.129519, 0.124969, 0.123212, 0.122361, 0.120889, 0.119612, 0.115196, 0.113749, 0.118831, 0.119123, 0.119866, 0.121635, 0.121348, 0.123078, 0.12475, 0.127124, 0.130585, 0.134835])

xs_sys_all = array('d', [18.0287, 15.6733, 8.6325, 3.91811, 2.1875, 1.69301, 2.13894, 2.80253, 2.79607, 2.63993, 2.65454, 2.58143, 2.36525, 1.83277, 1.27788, 1.03022, 1.11398, 1.13528, 1.05868, 0.910854, 0.720537, 0.592423, 0.492657, 0.397243, 0.311835, 0.251862, 0.207095, 0.18806, 0.184561, 0.177655, 0.169964, 0.166488, 0.155208, 0.159438, 0.162678, 0.164746, 0.166951, 0.167498, 0.164833, 0.162225, 0.156879, 0.153625, 0.146906, 0.139942, 0.13422, 0.128718, 0.125957, 0.125876, 0.124731, 0.125308, 0.132913, 0.135618, 0.13851, 0.142256, 0.145583, 0.149747])
xs_sys_all_exp = array('d', [10.4422, 8.9131, 7.47655, 6.2181, 5.2968, 4.500395, 3.855925, 3.167, 2.69755, 2.292435, 1.940255, 1.683285, 1.418775, 1.24041, 1.11487, 0.9766635, 0.844834, 0.7089375, 0.625544, 0.5524985, 0.5503275, 0.4784735, 0.4144995, 0.402687, 0.3619335, 0.3407565, 0.3199655, 0.2868715, 0.260819, 0.241752, 0.219856, 0.2151445, 0.202777, 0.1877995, 0.1729915, 0.1606085, 0.1550125, 0.144495, 0.141409, 0.137229, 0.1342635, 0.131153, 0.127747, 0.12197, 0.1202775, 0.1174895, 0.116965, 0.122172, 0.121244, 0.1215555, 0.1223685, 0.1248045, 0.1276105, 0.130358, 0.1346525, 0.139314])


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
g_all_exp.GetXaxis().SetTitle("gg resonance mass [GeV]")
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

c.SaveAs('xs_limit_ratio_DijetLimitCode_gg_Run2_13TeV_DATA_65_invpb.eps')
