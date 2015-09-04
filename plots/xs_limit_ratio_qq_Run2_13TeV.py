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

xs_stat = array('d', [7.30764, 5.00611, 2.32696, 0.995303, 0.587761, 0.615919, 0.921013, 1.11112, 0.999755, 1.00267, 1.19137, 1.13509, 0.833969, 0.508956, 0.403621, 0.495131, 0.599257, 0.586043, 0.470618, 0.356755, 0.291045, 0.25543, 0.212963, 0.1677, 0.132475, 0.115412, 0.115684, 0.105511, 0.104025, 0.100555, 0.0949939, 0.0900126, 0.0934679, 0.0989992, 0.102743, 0.105357, 0.106082, 0.104405, 0.101387, 0.0974134, 0.0930417, 0.0880087, 0.0832118, 0.0782449, 0.0739699, 0.0703537, 0.0709839, 0.0698242, 0.0692104, 0.0684988, 0.0681934, 0.0681317, 0.0680208, 0.0677637, 0.0675847, 0.0677319])
xs_stat_exp = array('d', [3.20889, 2.50854, 2.1707, 1.878, 1.64899, 1.48647, 1.29293, 1.07436, 0.93558, 0.835563, 0.728884, 0.660386, 0.570712, 0.527421, 0.460958, 0.401138, 0.383403, 0.322843, 0.308836, 0.269037, 0.25341, 0.220644, 0.20602, 0.196193, 0.184772, 0.170872, 0.153756, 0.143638, 0.13316, 0.126622, 0.119118, 0.112768, 0.108474, 0.099903, 0.100716, 0.0901738, 0.0870849, 0.0805312, 0.0789201, 0.0766568, 0.0744938, 0.071728, 0.0688413, 0.0687949, 0.0667975, 0.0661106, 0.063588, 0.0635747, 0.0635615, 0.0635593, 0.0636437, 0.0637606, 0.0638667, 0.0640505, 0.0641105, 0.0642055])

xs_sys_all = array('d', [9.2145, 6.91205, 3.59898, 1.66443, 0.994762, 1.01517, 1.32504, 1.41151, 1.35899, 1.35954, 1.38068, 1.31123, 1.08647, 0.752455, 0.560417, 0.601718, 0.648559, 0.634623, 0.547292, 0.446601, 0.349089, 0.290888, 0.241313, 0.192199, 0.154875, 0.125193, 0.118726, 0.108347, 0.104953, 0.102496, 0.0978532, 0.0943767, 0.0973504, 0.0998841, 0.105425, 0.105793, 0.105978, 0.104013, 0.103198, 0.0990549, 0.0956666, 0.0911268, 0.0855285, 0.0817995, 0.0765413, 0.0733673, 0.0727553, 0.0714237, 0.0703047, 0.0696831, 0.0688, 0.0689254, 0.0682202, 0.0680882, 0.068512, 0.0686543])
xs_sys_all_exp = array('d', [5.19075, 3.96418, 3.34343, 2.863645, 2.491375, 2.10389, 1.68206, 1.462285, 1.24104, 1.08231, 0.9402235, 0.8049225, 0.725906, 0.6264525, 0.5672445, 0.503862, 0.4276885, 0.3768365, 0.355516, 0.313671, 0.291721, 0.2633065, 0.2419025, 0.2219035, 0.2002785, 0.1895905, 0.175589, 0.1683045, 0.1502285, 0.139875, 0.129911, 0.1233565, 0.116778, 0.107678, 0.1000142, 0.09584945, 0.0896301, 0.08582945, 0.08361435, 0.0813843, 0.0774643, 0.07480645, 0.07320105, 0.06968735, 0.0664212, 0.06759095, 0.06312345, 0.06250005, 0.06255715, 0.06249495, 0.062588, 0.06272145, 0.0627535, 0.06293805, 0.0631202, 0.06309305])


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

c.SaveAs('xs_limit_ratio_DijetLimitCode_qq_Run2_13TeV_DATA_65_invpb.eps')
