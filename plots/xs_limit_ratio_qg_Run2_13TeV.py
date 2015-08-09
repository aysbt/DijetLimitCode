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

xs_stat = array('d', [13.4831, 8.69886, 12.7585, 7.44248, 2.87499, 1.93393, 1.39893, 0.99834, 0.969378, 1.1099, 1.11847, 0.984892, 1.09796, 1.42846, 1.6665, 1.4295, 0.980145, 0.871941, 0.965759, 1.01556, 0.929258, 0.748125, 0.57023, 0.445021, 0.348936, 0.262179, 0.231307, 0.224717, 0.213801, 0.204395, 0.197431, 0.188848, 0.180258, 0.169973, 0.159263, 0.152571, 0.154489, 0.158341, 0.160313, 0.161363, 0.161058, 0.15922, 0.156569, 0.153429, 0.149793, 0.145711, 0.141712, 0.137999, 0.13643, 0.135355, 0.13433, 0.133518, 0.132979, 0.132584, 0.132055, 0.131682, 0.13196, 0.132387])
xs_stat_exp = array('d', [7.55374, 5.85882, 4.39145, 4.13483, 3.60138, 3.14953, 2.57061, 2.3519, 1.98301, 1.69799, 1.52347, 1.38177, 1.12345, 0.977257, 0.88675, 0.802435, 0.707324, 0.641945, 0.571419, 0.481199, 0.454, 0.425648, 0.397049, 0.375953, 0.326899, 0.338552, 0.30487, 0.283821, 0.254419, 0.241231, 0.218951, 0.211112, 0.1966, 0.182259, 0.182692, 0.17824, 0.16239, 0.151944, 0.141037, 0.135887, 0.129752, 0.126111, 0.124963, 0.121779, 0.122325, 0.120018, 0.120407, 0.118186, 0.118825, 0.119811, 0.118975, 0.119866, 0.120555, 0.120537, 0.12143, 0.122247, 0.123113, 0.123825])

xs_sys_all = array('d', [30.0837, 17.3312, 16.2013, 12.6827, 6.63927, 4.09172, 2.81754, 2.0801, 1.81432, 1.73606, 1.65535, 1.57397, 1.61795, 1.7229, 1.83735, 1.72639, 1.47083, 1.25776, 1.14978, 1.1122, 1.04584, 0.958034, 0.848282, 0.734786, 0.598486, 0.452036, 0.364983, 0.296993, 0.254484, 0.227288, 0.211742, 0.199772, 0.187461, 0.179778, 0.169754, 0.164864, 0.162421, 0.161903, 0.163566, 0.164676, 0.160845, 0.160713, 0.160136, 0.158488, 0.15671, 0.154409, 0.150531, 0.147364, 0.146792, 0.144107, 0.141662, 0.140163, 0.139234, 0.140407, 0.138848, 0.138441, 0.1369, 0.138308])
xs_sys_all_exp = array('d', [19.3328, 12.7885, 9.65113, 7.59381, 6.93144, 5.626215, 4.84418, 3.901455, 3.362215, 2.95194, 2.484255, 2.08993, 1.76917, 1.57646, 1.26701, 1.149675, 1.02275, 0.925868, 0.776254, 0.674289, 0.6048925, 0.544958, 0.4958745, 0.4595, 0.413392, 0.403484, 0.366213, 0.3271745, 0.298883, 0.2756685, 0.268623, 0.244686, 0.228441, 0.222952, 0.204546, 0.1895015, 0.187344, 0.1689065, 0.160993, 0.149828, 0.147528, 0.1405295, 0.1386355, 0.133901, 0.123478, 0.1207285, 0.124024, 0.116179, 0.1169, 0.1196765, 0.119367, 0.118351, 0.1205315, 0.121376, 0.1220835, 0.120602, 0.1211315, 0.122813])


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
CMS_lumi.lumi_sqrtS = "41.8 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_DijetLimitCode_qg_Run2_13TeV_DATA_41p8_invpb.eps')
