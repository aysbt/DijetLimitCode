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

xs_stat = array('d', [0.774406, 0.986218, 1.75866, 1.14641, 0.919007, 0.737969, 0.392757, 0.279419, 0.189352, 0.168139, 0.168823, 0.139586, 0.112821, 0.0966805, 0.0797317, 0.0730251, 0.0777934, 0.0925955, 0.0952212, 0.0900524, 0.0882402, 0.0900611, 0.0943155, 0.0976048, 0.100283, 0.0990596, 0.0922381, 0.0766865, 0.0552401, 0.0354419, 0.0256382, 0.0186629, 0.0145845, 0.0123074, 0.0112314, 0.0114168, 0.012173, 0.0127663, 0.0128261, 0.01233, 0.0118628, 0.0118075, 0.0121371, 0.01201, 0.0119846, 0.0117518, 0.0116898, 0.0114021, 0.0109518, 0.0103538, 0.00979565, 0.00930067, 0.00910024, 0.00945993, 0.00994439, 0.0105076])
xs_stat_exp = array('d', [1.135775, 0.8386765, 0.7627025, 0.6236365, 0.51727, 0.419236, 0.3993075, 0.3559885, 0.284311, 0.24024, 0.2280625, 0.1981365, 0.188856, 0.1642985, 0.152, 0.1254045, 0.1073285, 0.0990953, 0.0897164, 0.0791696, 0.0707024, 0.0635862, 0.0573578, 0.05032625, 0.04748195, 0.0424117, 0.03836, 0.0344605, 0.03161445, 0.02992775, 0.0272681, 0.0264569, 0.02613395, 0.024436, 0.0216682, 0.0210522, 0.0186031, 0.0181665, 0.0161242, 0.01440485, 0.01365405, 0.013109, 0.012854, 0.01212855, 0.010987, 0.009940435, 0.00973575, 0.00959334, 0.00972272, 0.009528715, 0.0094567, 0.00973143, 0.00959768, 0.009403555, 0.009493375, 0.009247495])

xs_sys_all = array('d', [1.96856, 2.43822, 2.76583, 2.04621, 1.46395, 1.12298, 0.726003, 0.487341, 0.338475, 0.292971, 0.269578, 0.239681, 0.202668, 0.169284, 0.139073, 0.128541, 0.121525, 0.132959, 0.130894, 0.124102, 0.120602, 0.11783, 0.116425, 0.116592, 0.115549, 0.110867, 0.10454, 0.0942745, 0.0782696, 0.0566834, 0.0380103, 0.0260337, 0.0189558, 0.0150787, 0.0133684, 0.0128971, 0.0130313, 0.0131463, 0.0130563, 0.012868, 0.0125073, 0.0124197, 0.0125219, 0.012125, 0.0121815, 0.0119257, 0.0119576, 0.0117623, 0.0114172, 0.0108835, 0.0104712, 0.00997223, 0.00965398, 0.00993409, 0.0101813, 0.0105714])
xs_sys_all_exp = array('d', [2.67522, 2.19755, 1.82921, 1.39324, 1.052685, 0.825972, 0.67222, 0.5580595, 0.485295, 0.414629, 0.3724995, 0.320681, 0.2813525, 0.2604625, 0.223714, 0.1877485, 0.1655965, 0.1459175, 0.1230215, 0.114149, 0.1020235, 0.09069065, 0.082192, 0.0730009, 0.06256325, 0.0540863, 0.04947105, 0.0445009, 0.0404743, 0.0381551, 0.0349583, 0.0320151, 0.0287547, 0.02631, 0.02377695, 0.0221527, 0.0209546, 0.0186064, 0.01734865, 0.01645255, 0.0146564, 0.0141953, 0.01339455, 0.0122686, 0.01170885, 0.0109162, 0.0104373, 0.0103499, 0.01008445, 0.01021665, 0.0102788, 0.00998176, 0.009929745, 0.00994015, 0.0100449, 0.009597815])


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
CMS_lumi.lumi_sqrtS = "1769 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_DijetLimitCode_gg_Run2_13TeV_DATA_1769_invpb.eps')
