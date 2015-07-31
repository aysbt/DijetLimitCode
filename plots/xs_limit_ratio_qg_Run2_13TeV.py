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

xs_stat = array('d', [10.3751, 13.8264, 6.55349, 2.44435, 2.22862, 1.24374, 0.947578, 1.12949, 1.41524, 1.28891, 1.25175, 1.45199, 1.61689, 1.35701, 1.0093, 0.995174, 1.01626, 0.943728, 0.76496, 0.567827, 0.418643, 0.338593, 0.251817, 0.231712, 0.219958, 0.207757, 0.198495, 0.192832, 0.183754, 0.17555, 0.163001, 0.151375, 0.151426, 0.157052, 0.16044, 0.161611, 0.160995, 0.15858, 0.155725, 0.152297, 0.148288, 0.143719, 0.139386, 0.135483, 0.131857, 0.128721, 0.126059, 0.124646, 0.123311, 0.122246, 0.121551, 0.121306, 0.121166, 0.127818, 0.128382, 0.128993, 0.129531, 0.130074])
xs_stat_exp = array('d', [6.672545, 5.123715, 4.34233, 3.583315, 3.26023, 2.691545, 2.1238, 1.891625, 1.599015, 1.378815, 1.24918, 1.12243, 0.9088285, 0.806554, 0.746514, 0.660373, 0.5789305, 0.520127, 0.475583, 0.413365, 0.3943755, 0.3640775, 0.352227, 0.3290775, 0.286291, 0.265696, 0.24863, 0.221159, 0.214747, 0.203102, 0.196243, 0.185486, 0.1788865, 0.156613, 0.147346, 0.1417965, 0.136371, 0.133413, 0.1281915, 0.1244095, 0.1235155, 0.121296, 0.1205845, 0.1200365, 0.11643, 0.114805, 0.1155355, 0.1145285, 0.1149285, 0.1134665, 0.114351, 0.1165905, 0.117413, 0.115888, 0.116645, 0.1173625, 0.118092, 0.1191065])

xs_sys_all = array('d', [21.5467, 19.4443, 13.9651, 5.64433, 4.21498, 2.62887, 1.99384, 2.05658, 2.02319, 1.92938, 1.82981, 1.81885, 1.82763, 1.71325, 1.48047, 1.30744, 1.16305, 1.08868, 0.966329, 0.839295, 0.702483, 0.556467, 0.406964, 0.324904, 0.274241, 0.235227, 0.215299, 0.202827, 0.192051, 0.184307, 0.173092, 0.163129, 0.161657, 0.162681, 0.163073, 0.16266, 0.16058, 0.15762, 0.157977, 0.156501, 0.153534, 0.150511, 0.147414, 0.143951, 0.139558, 0.135926, 0.133416, 0.129062, 0.128845, 0.125138, 0.12743, 0.124658, 0.124679, 0.12957, 0.128295, 0.131978, 0.130951, 0.13251])
xs_sys_all_exp = array('d', [16.45385, 10.3911, 8.18725, 6.62469, 5.63671, 4.779185, 3.88036, 3.31879, 2.81761, 2.30023, 1.95999, 1.678195, 1.359495, 1.20333, 1.084315, 0.9283745, 0.769115, 0.691393, 0.627997, 0.5559335, 0.479187, 0.451661, 0.4314705, 0.3834885, 0.3574035, 0.327283, 0.292556, 0.2590355, 0.241763, 0.22954, 0.21139, 0.2070745, 0.193483, 0.1724265, 0.1641965, 0.151363, 0.1425065, 0.1397945, 0.133101, 0.12678, 0.1263265, 0.123092, 0.1208935, 0.1172835, 0.115057, 0.113609, 0.1119325, 0.1119955, 0.114325, 0.112124, 0.1144905, 0.1134145, 0.1140875, 0.1125075, 0.112975, 0.114093, 0.1147735, 0.115405])


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
CMS_lumi.lumi_sqrtS = "40.2 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_DijetLimitCode_qg_Run2_13TeV_DATA_40p2_invpb.eps')
