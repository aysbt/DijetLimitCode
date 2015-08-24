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

xs_stat = array('d', [22.3337, 10.786, 17.3995, 12.9119, 3.97864, 2.74638, 2.07942, 1.38697, 1.22781, 1.45198, 1.59933, 1.36466, 1.33414, 1.73327, 2.28521, 2.13213, 1.41946, 1.08788, 1.2452, 1.3944, 1.34101, 1.12676, 0.862794, 0.677736, 0.511847, 0.393714, 0.322891, 0.302415, 0.285506, 0.268335, 0.260514, 0.255765, 0.244383, 0.232223, 0.222849, 0.207364, 0.204008, 0.207945, 0.216137, 0.219047, 0.219261, 0.21814, 0.215519, 0.21177, 0.205814, 0.199433, 0.19427, 0.190228, 0.191367, 0.192586, 0.193879, 0.19674, 0.200283, 0.203947, 0.20829, 0.213258, 0.219107, 0.22589])
xs_stat_exp = array('d', [9.49284, 7.96023, 6.67129, 5.71589, 4.66765, 4.27515, 3.75304, 3.25249, 2.79173, 2.52338, 2.15927, 1.81585, 1.6515, 1.5108, 1.25607, 1.07202, 0.961419, 0.91267, 0.794071, 0.709098, 0.620592, 0.577106, 0.527946, 0.491945, 0.436141, 0.443247, 0.411217, 0.399545, 0.364645, 0.335363, 0.309874, 0.280883, 0.250506, 0.240625, 0.241478, 0.222516, 0.208779, 0.205653, 0.194101, 0.190014, 0.176588, 0.173191, 0.168672, 0.161794, 0.160532, 0.162141, 0.15666, 0.155047, 0.157784, 0.16172, 0.162313, 0.168112, 0.172665, 0.177607, 0.179842, 0.186106, 0.191509, 0.200528])

xs_sys_all = array('d', [54.1968, 25.7766, 23.8135, 20.1944, 9.76688, 6.15776, 4.42915, 3.0816, 2.60814, 2.56899, 2.46285, 2.29042, 2.22468, 2.35236, 2.55077, 2.532, 2.13867, 1.77697, 1.60557, 1.55888, 1.48962, 1.3785, 1.22234, 1.08345, 0.91135, 0.684575, 0.535158, 0.438331, 0.370818, 0.323687, 0.297412, 0.278558, 0.266534, 0.251505, 0.235409, 0.221672, 0.216499, 0.217276, 0.217524, 0.216956, 0.215982, 0.21772, 0.216478, 0.213417, 0.213675, 0.207917, 0.210197, 0.202443, 0.20232, 0.202019, 0.203688, 0.205038, 0.206911, 0.209445, 0.212497, 0.218607, 0.224202, 0.229246])                                                                                               
xs_sys_all_exp = array('d', [28.1625, 18.166, 15.2484, 11.5414, 10.5614, 8.3932, 7.09015, 5.84451, 5.18569, 4.336505, 3.637985, 3.19093, 2.677445, 2.29711, 1.882415, 1.61154, 1.529295, 1.32494, 1.1069, 0.974663, 0.872959, 0.7570055, 0.717379, 0.6329035, 0.5850115, 0.54332, 0.523087, 0.454718, 0.4139265, 0.3780525, 0.3616705, 0.337585, 0.3143135, 0.292594, 0.273277, 0.2666565, 0.242272, 0.2319665, 0.2084985, 0.203577, 0.20065, 0.190455, 0.185494, 0.1803555, 0.171907, 0.169828, 0.166008, 0.163576, 0.1611855, 0.1659605, 0.1710605, 0.172834, 0.175707, 0.1794665, 0.186162, 0.1930865, 0.201742, 0.205289])                                                                   


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

c.SaveAs('xs_limit_ratio_DijetLimitCode_gg_Run2_13TeV_DATA_42_invpb.eps')
