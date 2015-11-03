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

xs_stat = array('d', [0.373245, 0.729224, 0.749304, 0.51653, 0.485702, 0.31179, 0.204037, 0.145153, 0.118367, 0.12084, 0.104699, 0.0848555, 0.0641548, 0.0543576, 0.047996, 0.0478736, 0.0520838, 0.056903, 0.0542284, 0.0515971, 0.0509319, 0.0531768, 0.0551673, 0.0566582, 0.0565528, 0.0529559, 0.045109, 0.0329733, 0.0218742, 0.014847, 0.0113783, 0.00880015, 0.00724962, 0.00675315, 0.00682426, 0.00692529, 0.0071654, 0.00704883, 0.00684132, 0.00655443, 0.00640048, 0.00642755, 0.00646899, 0.00668889, 0.00649358, 0.00614679, 0.00576717, 0.00529031, 0.00482739, 0.00436217, 0.00421678, 0.00410902, 0.00411572, 0.00418978, 0.00428701, 0.00433157])
xs_stat_exp = array('d', [0.676823, 0.5293625, 0.398825, 0.340792, 0.2879685, 0.2517005, 0.2200845, 0.2007295, 0.1668755, 0.144864, 0.1282025, 0.1098995, 0.09719825, 0.0901967, 0.0833574, 0.0701342, 0.0609684, 0.0541542, 0.0482992, 0.04679215, 0.04156035, 0.03633395, 0.03206895, 0.0280869, 0.02571885, 0.02370295, 0.02172135, 0.0199726, 0.01803245, 0.016692, 0.01641875, 0.01485385, 0.0138403, 0.01265835, 0.0120821, 0.0107712, 0.00979475, 0.00901551, 0.00845537, 0.007665285, 0.007026815, 0.006803575, 0.0064069, 0.005779425, 0.005424805, 0.005038205, 0.004803375, 0.004742145, 0.00451236, 0.004314105, 0.004345175, 0.004166715, 0.00403069, 0.003870555, 0.00363478, 0.003690605])

xs_sys_all = array('d', [0.82147, 1.19683, 1.09947, 0.803474, 0.629664, 0.461803, 0.301626, 0.210189, 0.169315, 0.15975, 0.14034, 0.114906, 0.0928419, 0.0770832, 0.0679586, 0.0665974, 0.069166, 0.0700806, 0.0679091, 0.0641745, 0.0629837, 0.0629184, 0.0639981, 0.0638037, 0.0617575, 0.0586043, 0.0529361, 0.0451882, 0.0343616, 0.0229805, 0.0148121, 0.0108115, 0.00867909, 0.00748847, 0.00726895, 0.00732564, 0.00739262, 0.00732058, 0.00711229, 0.00692194, 0.0067567, 0.00672501, 0.00655951, 0.00653841, 0.00637906, 0.00610068, 0.00584878, 0.00551712, 0.00507471, 0.00466002, 0.00446959, 0.00431538, 0.00420174, 0.00419521, 0.00425214, 0.00424506])
xs_sys_all_exp = array('d', [1.25232, 0.996774, 0.7815935, 0.604155, 0.4599715, 0.3724675, 0.298686, 0.257382, 0.2284925, 0.2014455, 0.1757395, 0.155858, 0.135611, 0.1222025, 0.1065885, 0.0893078, 0.08021135, 0.0695399, 0.0617724, 0.0599736, 0.05101905, 0.0456115, 0.0417081, 0.036968, 0.0313885, 0.0281677, 0.02636, 0.0242915, 0.02153105, 0.01978565, 0.01805905, 0.0161204, 0.0150401, 0.01367445, 0.01268845, 0.011698, 0.0103915, 0.00971092, 0.0090192, 0.008259385, 0.007745975, 0.00715103, 0.006567665, 0.00608866, 0.005588195, 0.00531195, 0.005082815, 0.004825495, 0.00484148, 0.00457326, 0.00440779, 0.004285375, 0.00415029, 0.0040409, 0.003835485, 0.0037301])


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
CMS_lumi.lumi_sqrtS = "1769 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_DijetLimitCode_qq_Run2_13TeV_DATA_1769_invpb.eps')
