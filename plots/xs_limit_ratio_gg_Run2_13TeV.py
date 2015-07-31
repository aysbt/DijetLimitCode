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
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
gROOT.ForceStyle()


masses = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])

xs_stat = array('d', [10.5454, 19.7451, 12.3585, 3.12581, 3.3185, 1.91614, 1.16177, 1.37181, 1.84513, 1.81173, 1.59247, 1.8136, 2.24945, 2.03803, 1.38889, 1.29787, 1.38632, 1.33388, 1.14575, 0.866594, 0.635951, 0.500446, 0.37322, 0.310025, 0.291638, 0.277028, 0.25957, 0.255045, 0.249723, 0.23554, 0.218904, 0.206927, 0.19663, 0.203432, 0.212901, 0.215584, 0.21468, 0.212325, 0.209186, 0.204148, 0.198026, 0.191322, 0.1857, 0.181377, 0.177349, 0.172401, 0.16765, 0.165819, 0.167806, 0.170941, 0.172965, 0.174285, 0.176359, 0.179971, 0.184041, 0.188741, 0.19496, 0.201702])
xs_stat_exp = array('d', [9.61372, 6.94123, 5.89102, 5.37004, 4.656325, 3.76967, 3.054805, 2.679795, 2.372195, 1.93964, 1.718555, 1.503075, 1.312415, 1.096825, 1.033265, 0.893457, 0.8038545, 0.728714, 0.673936, 0.5897995, 0.5190235, 0.496699, 0.4789045, 0.434043, 0.412885, 0.371281, 0.3372625, 0.2979355, 0.287519, 0.2716795, 0.247283, 0.2467865, 0.235172, 0.2181435, 0.200803, 0.1926765, 0.1846865, 0.178526, 0.1733965, 0.1671675, 0.1580895, 0.1575615, 0.1544575, 0.156659, 0.151003, 0.1496475, 0.147158, 0.146553, 0.150742, 0.1542635, 0.158712, 0.1605845, 0.1618275, 0.168154, 0.1724795, 0.178412, 0.1830205, 0.18977])

xs_sys_all = array('d', [27.1354, 28.0486, 23.1952, 7.66399, 6.66318, 4.2431, 2.75343, 2.92923, 3.05669, 2.89836, 2.64247, 2.56632, 2.58981, 2.52313, 2.1343, 1.85208, 1.66508, 1.54797, 1.41326, 1.22933, 1.03239, 0.846609, 0.61665, 0.482541, 0.398572, 0.339684, 0.30048, 0.281819, 0.2726, 0.254657, 0.239311, 0.222006, 0.211599, 0.212447, 0.213421, 0.213232, 0.21268, 0.210574, 0.20759, 0.205145, 0.202155, 0.200062, 0.197779, 0.191965, 0.185101, 0.182324, 0.177934, 0.17421, 0.17401, 0.176651, 0.178677, 0.178316, 0.178916, 0.185913, 0.188667, 0.192998, 0.196914, 0.204604])
xs_sys_all_exp = array('d', [22.7976, 15.7063, 12.12805, 10.81735, 8.65517, 7.48523, 5.90863, 5.09098, 4.327825, 3.476615, 3.00473, 2.45701, 2.12225, 1.811485, 1.634625, 1.376665, 1.138415, 0.971314, 0.851095, 0.810085, 0.714648, 0.650442, 0.60375, 0.542154, 0.5037355, 0.4557655, 0.4269255, 0.3581015, 0.338192, 0.311004, 0.288367, 0.286189, 0.2697745, 0.2424045, 0.217351, 0.203468, 0.190655, 0.18663, 0.177175, 0.173205, 0.165206, 0.1623055, 0.1629145, 0.1583225, 0.153909, 0.1536985, 0.150436, 0.148371, 0.1536045, 0.159338, 0.1615235, 0.165185, 0.1659995, 0.171207, 0.175905, 0.1806045, 0.186136, 0.192096])


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
g_all_exp.GetYaxis().SetRangeUser(0.5,3.5)
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
legend.SetTextSize(0.03)
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
CMS_lumi.lumi_sqrtS = "40.2 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_DijetLimitCode_gg_Run2_13TeV_DATA_40p2_invpb.eps')
