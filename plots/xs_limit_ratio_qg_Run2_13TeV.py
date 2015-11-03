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

xs_stat = array('d', [0.447681, 0.94047, 1.10444, 0.745052, 0.644595, 0.454945, 0.255557, 0.182351, 0.132791, 0.126116, 0.117443, 0.101507, 0.080383, 0.0669136, 0.0586514, 0.0560416, 0.0605396, 0.0696509, 0.0695102, 0.0668351, 0.0664088, 0.0705033, 0.0733576, 0.0749054, 0.0749544, 0.0706382, 0.0629769, 0.049911, 0.0348178, 0.0235178, 0.0161744, 0.0128611, 0.0101588, 0.00864743, 0.00827083, 0.00835925, 0.0087532, 0.00897128, 0.00893666, 0.00872392, 0.00858713, 0.00850894, 0.00852458, 0.00855364, 0.00854103, 0.00822973, 0.00792679, 0.00752776, 0.00704347, 0.00664995, 0.00643471, 0.00597274, 0.00581336, 0.00602666, 0.00605021, 0.00612627])
xs_stat_exp = array('d', [0.8984635, 0.640247, 0.5043485, 0.455606, 0.3892675, 0.311873, 0.2778305, 0.254107, 0.2145025, 0.182214, 0.1615205, 0.1456155, 0.1296985, 0.1133335, 0.109009, 0.09439195, 0.08066065, 0.06900675, 0.06234275, 0.0581321, 0.05080315, 0.0506102, 0.0434075, 0.0385302, 0.03351605, 0.0298698, 0.02787005, 0.0255655, 0.0247877, 0.0222575, 0.0216321, 0.0212116, 0.0187872, 0.0170246, 0.01571985, 0.01432545, 0.01308345, 0.01265335, 0.01157845, 0.0105372, 0.0101875, 0.00947435, 0.008713355, 0.0078738, 0.00728985, 0.00690672, 0.006655745, 0.00664655, 0.006434835, 0.00632706, 0.006274645, 0.00614841, 0.006042125, 0.00568562, 0.005583005, 0.00522359])

xs_sys_all = array('d', [1.13913, 1.8364, 1.71224, 1.26228, 0.924489, 0.683269, 0.433065, 0.295124, 0.222364, 0.201017, 0.185775, 0.160148, 0.132396, 0.112132, 0.0987242, 0.0936752, 0.0942825, 0.0955584, 0.0930272, 0.0894917, 0.0872137, 0.0869834, 0.0864531, 0.0853363, 0.0835342, 0.0787906, 0.0731486, 0.0633358, 0.0505204, 0.0353785, 0.0233455, 0.0164669, 0.0127346, 0.0105698, 0.00954164, 0.00931178, 0.00938082, 0.00940067, 0.00937174, 0.00920891, 0.00910763, 0.00894841, 0.00890596, 0.00883482, 0.00868046, 0.00839036, 0.00815086, 0.00783483, 0.00743567, 0.00703365, 0.00660032, 0.00620008, 0.00600268, 0.00608876, 0.00603658, 0.00604036])
xs_sys_all_exp = array('d', [1.85245, 1.46811, 1.150285, 0.8711975, 0.69388, 0.5288175, 0.4389155, 0.353787, 0.326327, 0.287821, 0.2452215, 0.217799, 0.192337, 0.17369, 0.15507, 0.1312545, 0.1150965, 0.09746505, 0.08556125, 0.077895, 0.0709935, 0.06355135, 0.05625585, 0.0499526, 0.04163165, 0.03722065, 0.0343471, 0.0319316, 0.028271, 0.0263215, 0.02440285, 0.0216478, 0.02020515, 0.01839645, 0.0171989, 0.01572625, 0.0146808, 0.0131165, 0.01241045, 0.0112964, 0.0108321, 0.009973795, 0.009315775, 0.0085743, 0.00802611, 0.00747832, 0.00714741, 0.00695533, 0.006667785, 0.00662194, 0.00658503, 0.006239935, 0.00597814, 0.00593276, 0.00570501, 0.00554191])


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

c.SaveAs('xs_limit_ratio_DijetLimitCode_qg_Run2_13TeV_DATA_1769_invpb.eps')
