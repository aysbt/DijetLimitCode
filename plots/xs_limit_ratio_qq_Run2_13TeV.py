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

xs_stat = array('d', [8.0158, 10.5788, 4.65056, 2.57241, 2.05967, 1.01622, 0.860767, 1.06139, 1.17236, 0.954049, 0.965226, 1.24654, 1.24543, 0.918677, 0.713323, 0.7754, 0.821743, 0.737862, 0.578853, 0.434062, 0.316459, 0.239236, 0.197947, 0.183178, 0.175149, 0.164938, 0.160147, 0.155912, 0.148799, 0.137963, 0.133585, 0.13138, 0.122696, 0.133014, 0.138529, 0.139831, 0.138922, 0.136889, 0.133604, 0.129398, 0.124811, 0.120285, 0.116131, 0.112947, 0.11268, 0.108712, 0.105079, 0.107114, 0.10674, 0.106475, 0.106144, 0.105845, 0.105907, 0.106192, 0.106281, 0.106309, 0.106659, 0.107262])
xs_stat_exp = array('d', [5.8439, 4.25425, 3.541905, 3.055155, 2.43113, 2.147895, 1.69162, 1.523355, 1.27855, 1.08498, 0.9995345, 0.8714715, 0.8010535, 0.6782465, 0.621159, 0.504092, 0.456937, 0.4138525, 0.3886775, 0.334908, 0.3263765, 0.301576, 0.283081, 0.2485595, 0.224051, 0.2131535, 0.2014945, 0.1885095, 0.1770235, 0.165914, 0.151235, 0.1412885, 0.1417165, 0.12926, 0.1227305, 0.118487, 0.1174055, 0.112705, 0.1076525, 0.104329, 0.1008575, 0.0989312, 0.09689655, 0.0952929, 0.09483955, 0.0937182, 0.0922566, 0.08963275, 0.0901068, 0.09053075, 0.09100155, 0.0911948, 0.0919141, 0.0924769, 0.0929633, 0.0934716, 0.09398665, 0.0945078])

xs_sys_all = array('d', [14.1649, 13.5941, 10.2922, 5.4879, 3.40148, 2.05455, 1.55915, 1.50971, 1.46022, 1.39205, 1.37247, 1.39601, 1.37696, 1.25389, 1.04808, 0.932584, 0.883213, 0.829673, 0.761487, 0.66881, 0.556168, 0.425744, 0.313808, 0.252651, 0.206045, 0.180583, 0.168285, 0.161365, 0.153008, 0.145284, 0.144482, 0.140282, 0.13222, 0.13774, 0.139349, 0.139841, 0.137624, 0.13747, 0.135045, 0.132615, 0.129781, 0.1264, 0.123183, 0.119357, 0.114977, 0.110612, 0.106199, 0.108093, 0.106641, 0.105808, 0.10463, 0.10614, 0.104164, 0.105481, 0.104485, 0.10493, 0.104527, 0.105371])
xs_sys_all_exp = array('d', [12.4376, 8.10187, 6.17594, 4.989095, 4.124785, 3.474835, 2.83222, 2.46139, 1.97498, 1.69714, 1.45996, 1.270205, 1.06064, 0.958562, 0.815537, 0.717602, 0.5980415, 0.5393405, 0.493984, 0.430662, 0.401618, 0.384404, 0.346204, 0.308989, 0.2616815, 0.242763, 0.229183, 0.211736, 0.198466, 0.192951, 0.173, 0.161683, 0.160477, 0.140646, 0.131741, 0.124681, 0.121853, 0.115948, 0.10885, 0.1047445, 0.1024465, 0.09947145, 0.0963119, 0.0946025, 0.0944811, 0.09343545, 0.0919992, 0.0887057, 0.0887729, 0.08935905, 0.0896251, 0.0902391, 0.09053035, 0.0910734, 0.09147545, 0.09199665, 0.09243545, 0.0927634])


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

c.SaveAs('xs_limit_ratio_DijetLimitCode_qq_Run2_13TeV_DATA_40p2_invpb.eps')
