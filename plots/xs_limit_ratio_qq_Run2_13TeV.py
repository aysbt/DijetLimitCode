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


masses = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])

xs_stat = array('d', [9.20414, 6.46756, 9.75353, 5.52489, 2.6515, 1.8268, 1.15166, 0.89812, 0.899687, 0.982368, 0.888957, 0.797769, 0.910204, 1.26509, 1.31159, 0.936666, 0.626957, 0.647552, 0.790112, 0.821323, 0.717788, 0.562002, 0.419864, 0.315301, 0.237014, 0.200394, 0.185005, 0.175093, 0.165276, 0.159748, 0.155628, 0.149022, 0.140277, 0.129785, 0.129573, 0.128112, 0.126267, 0.132322, 0.135556, 0.135839, 0.134694, 0.132778, 0.129958, 0.126311, 0.123086, 0.119043, 0.115495, 0.112104, 0.109159, 0.111718, 0.109867, 0.108461, 0.107637, 0.110966, 0.110893, 0.110689, 0.110496, 0.110653])
xs_stat_exp = array('d', [6.3096, 5.22297, 4.25223, 3.47572, 3.04047, 2.60441, 2.15104, 1.78077, 1.66965, 1.42838, 1.19613, 1.08528, 0.913016, 0.790579, 0.725155, 0.643135, 0.587455, 0.501085, 0.455891, 0.418071, 0.374923, 0.347929, 0.326963, 0.297864, 0.273909, 0.253204, 0.235359, 0.218651, 0.20471, 0.189115, 0.178858, 0.159363, 0.159808, 0.157049, 0.141023, 0.134004, 0.131722, 0.122563, 0.11646, 0.112234, 0.107646, 0.10364, 0.0998586, 0.0990011, 0.096574, 0.0956892, 0.0946548, 0.0924197, 0.0923265, 0.092337, 0.0942341, 0.0956634, 0.0950288, 0.0940434, 0.0944047, 0.0949219, 0.0953054, 0.0958432])

xs_sys_all = array('d', [18.3008, 11.5649, 11.7677, 9.50971, 5.75474, 3.42925, 2.18439, 1.58849, 1.36759, 1.27995, 1.23461, 1.21253, 1.28931, 1.3976, 1.40659, 1.27732, 1.05467, 0.901229, 0.86207, 0.868535, 0.82412, 0.762062, 0.674901, 0.581266, 0.452589, 0.34483, 0.274011, 0.221667, 0.187517, 0.172637, 0.16399, 0.15574, 0.146984, 0.140868, 0.139995, 0.137278, 0.134814, 0.136424, 0.136991, 0.136186, 0.134855, 0.135522, 0.132289, 0.130894, 0.128785, 0.125827, 0.122859, 0.119163, 0.117131, 0.114852, 0.113656, 0.110533, 0.108054, 0.11106, 0.109963, 0.110278, 0.109243, 0.109851])
xs_sys_all_exp = array('d', [14.3962, 9.48121, 7.01623, 5.889505, 4.98805, 4.13835, 3.45536, 2.83787, 2.44881, 2.06521, 1.82667, 1.56513, 1.322575, 1.168415, 1.010515, 0.892765, 0.795551, 0.701526, 0.615877, 0.525111, 0.481777, 0.439153, 0.404622, 0.3637935, 0.332707, 0.316218, 0.277452, 0.2606355, 0.2418035, 0.22732, 0.209817, 0.19432, 0.186331, 0.1732935, 0.162105, 0.153349, 0.145746, 0.1325985, 0.1257205, 0.1224045, 0.1197185, 0.1137055, 0.110121, 0.0989737, 0.0979682, 0.0980667, 0.0929121, 0.09417125, 0.0930828, 0.0962552, 0.0942701, 0.0943524, 0.0933915, 0.0932595, 0.0937428, 0.09398685, 0.09477415, 0.0948558])


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
g_all_exp.GetXaxis().SetTitle("qq resonance mass [GeV]")
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
CMS_lumi.lumi_sqrtS = "42 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_DijetLimitCode_qq_Run2_13TeV_DATA_42_invpb.eps')
