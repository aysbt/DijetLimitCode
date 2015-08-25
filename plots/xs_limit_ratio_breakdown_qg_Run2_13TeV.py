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

xs_stat = array('d', [13.4831, 8.69886, 12.7585, 7.44248, 2.87499, 1.93393, 1.39893, 0.99834, 0.969378, 1.1099, 1.11847, 0.984892, 1.09796, 1.42846, 1.6665, 1.4295, 0.980145, 0.871941, 0.965759, 1.01556, 0.929258, 0.748125, 0.57023, 0.445021, 0.348936, 0.262179, 0.231307, 0.224717, 0.213801, 0.204395, 0.197431, 0.188848, 0.180258, 0.169973, 0.159263, 0.152571, 0.154489, 0.158341, 0.160313, 0.161363, 0.161058, 0.15922, 0.156569, 0.153429, 0.149793, 0.145711, 0.141712, 0.137999, 0.13643, 0.135355, 0.13433, 0.133518, 0.132979, 0.132584, 0.132055, 0.131682, 0.13196, 0.132387])

xs_sys_all = array('d', [30.0837, 17.3312, 16.2013, 12.6827, 6.63927, 4.09172, 2.81754, 2.0801, 1.81432, 1.73606, 1.65535, 1.57397, 1.61795, 1.7229, 1.83735, 1.72639, 1.47083, 1.25776, 1.14978, 1.1122, 1.04584, 0.958034, 0.848282, 0.734786, 0.598486, 0.452036, 0.364983, 0.296993, 0.254484, 0.227288, 0.211742, 0.199772, 0.187461, 0.179778, 0.169754, 0.164864, 0.162421, 0.161903, 0.163566, 0.164676, 0.160845, 0.160713, 0.160136, 0.158488, 0.15671, 0.154409, 0.150531, 0.147364, 0.146792, 0.144107, 0.141662, 0.140163, 0.139234, 0.140407, 0.138848, 0.138441, 0.1369, 0.138308])
xs_sys_lumi = array('d', [14.0639, 8.97051, 13.44, 7.71161, 2.88048, 1.96401, 1.38477, 1.0041, 0.975414, 1.11501, 1.13257, 1.0049, 1.11669, 1.47518, 1.7414, 1.48686, 1.00324, 0.881072, 0.988231, 1.05044, 0.964641, 0.776401, 0.590412, 0.45822, 0.349841, 0.264374, 0.233662, 0.218988, 0.208958, 0.200229, 0.194555, 0.186006, 0.177523, 0.170094, 0.159147, 0.153284, 0.155619, 0.158094, 0.162637, 0.161787, 0.163267, 0.161037, 0.159774, 0.155138, 0.151805, 0.146917, 0.143728, 0.139712, 0.137772, 0.136562, 0.135332, 0.135588, 0.135615, 0.133537, 0.133634, 0.132654, 0.130941, 0.133539])
xs_sys_jes = array('d', [14.0291, 9.26117, 12.7152, 8.68287, 3.57029, 2.2129, 1.50426, 1.09989, 1.02645, 1.08109, 1.09263, 1.04314, 1.15322, 1.41286, 1.60014, 1.49416, 1.16095, 0.998041, 1.00197, 1.00963, 0.955651, 0.857624, 0.739026, 0.628841, 0.49775, 0.37238, 0.308086, 0.260326, 0.227412, 0.204991, 0.194727, 0.186219, 0.177973, 0.170815, 0.16226, 0.154627, 0.154013, 0.157313, 0.156636, 0.155479, 0.15638, 0.157308, 0.153357, 0.153298, 0.151239, 0.147036, 0.144996, 0.141967, 0.139993, 0.138601, 0.136398, 0.136132, 0.133382, 0.133014, 0.132818, 0.1321, 0.132642, 0.132207])
xs_sys_jer = array('d', [13.6039, 8.71687, 12.8258, 7.43905, 2.79441, 1.94282, 1.34902, 0.98769, 0.957079, 1.1034, 1.09828, 0.994208, 1.08972, 1.43869, 1.67383, 1.44931, 1.01176, 0.871979, 0.975537, 1.01269, 0.927833, 0.750296, 0.578977, 0.445144, 0.341219, 0.25988, 0.228088, 0.215499, 0.204148, 0.193489, 0.187669, 0.182537, 0.176012, 0.166258, 0.158166, 0.151617, 0.151593, 0.155298, 0.15791, 0.157786, 0.158802, 0.156632, 0.155041, 0.150751, 0.147847, 0.144231, 0.139568, 0.136507, 0.134857, 0.13481, 0.132084, 0.132205, 0.131213, 0.129301, 0.129543, 0.130453, 0.130217, 0.130097])
xs_sys_allexceptbkg = array('d', [14.7157, 9.62199, 13.4751, 9.02504, 3.64581, 2.27882, 1.54921, 1.12757, 1.05625, 1.11918, 1.13411, 1.08471, 1.1949, 1.4683, 1.67099, 1.54276, 1.20929, 1.05157, 1.04385, 1.05352, 1.0069, 0.890538, 0.765018, 0.655554, 0.516317, 0.389585, 0.318236, 0.26646, 0.238948, 0.214982, 0.205198, 0.193141, 0.186197, 0.178598, 0.165743, 0.1591, 0.160365, 0.161601, 0.162632, 0.16119, 0.162054, 0.159578, 0.159446, 0.158871, 0.155066, 0.152492, 0.149681, 0.145066, 0.144883, 0.143978, 0.141572, 0.139619, 0.138958, 0.138384, 0.135941, 0.136495, 0.137339, 0.137665])
xs_sys_bkg = array('d', [22.2285, 13.0284, 15.2109, 9.39258, 4.56208, 3.26823, 2.38372, 1.73221, 1.58493, 1.66907, 1.60737, 1.37892, 1.42931, 1.6609, 1.83824, 1.56682, 1.1092, 0.961921, 1.0351, 1.06501, 0.968265, 0.782189, 0.5996, 0.46735, 0.363516, 0.275455, 0.243992, 0.224634, 0.210511, 0.20149, 0.196369, 0.186295, 0.177162, 0.168002, 0.159112, 0.152573, 0.153692, 0.157462, 0.158384, 0.160299, 0.159539, 0.158622, 0.155626, 0.151814, 0.147215, 0.145484, 0.141288, 0.136546, 0.135092, 0.134053, 0.133145, 0.133324, 0.133402, 0.132069, 0.129919, 0.130406, 0.131628, 0.131262])


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
g_all.GetYaxis().SetRangeUser(0.5,3.5)
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
CMS_lumi.lumi_sqrtS = "42 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_breakdown_DijetLimitCode_qg_Run2_13TeV_DATA_42_invpb.eps')
