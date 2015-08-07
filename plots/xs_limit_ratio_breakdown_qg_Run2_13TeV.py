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

xs_sys_all = array('d', [21.5467, 19.4443, 13.9651, 5.64433, 4.21498, 2.62887, 1.99384, 2.05658, 2.02319, 1.92938, 1.82981, 1.81885, 1.82763, 1.71325, 1.48047, 1.30744, 1.16305, 1.08868, 0.966329, 0.839295, 0.702483, 0.556467, 0.406964, 0.324904, 0.274241, 0.235227, 0.215299, 0.202827, 0.192051, 0.184307, 0.173092, 0.163129, 0.161657, 0.162681, 0.163073, 0.16266, 0.16058, 0.15762, 0.157977, 0.156501, 0.153534, 0.150511, 0.147414, 0.143951, 0.139558, 0.135926, 0.133416, 0.129062, 0.128845, 0.125138, 0.12743, 0.124658, 0.124679, 0.12957, 0.128295, 0.131978, 0.130951, 0.13251])
xs_sys_lumi = array('d', [10.6544, 14.3647, 6.72534, 2.41863, 2.23027, 1.2308, 0.898466, 1.12176, 1.40073, 1.27925, 1.25476, 1.47548, 1.65966, 1.38356, 1.02626, 1.00966, 1.03289, 0.967935, 0.784174, 0.581159, 0.426204, 0.333644, 0.25261, 0.222283, 0.211041, 0.200702, 0.190529, 0.188829, 0.179202, 0.171933, 0.16034, 0.15067, 0.151917, 0.156056, 0.16047, 0.160169, 0.16027, 0.159736, 0.156351, 0.154179, 0.148366, 0.143367, 0.139916, 0.134982, 0.131361, 0.130608, 0.125379, 0.124327, 0.122639, 0.121971, 0.12051, 0.119038, 0.119765, 0.126307, 0.126521, 0.127584, 0.127652, 0.130741])
xs_sys_jes = array('d', [10.7412, 14.0398, 7.98877, 2.92425, 2.33301, 1.36821, 1.01829, 1.13317, 1.32161, 1.2802, 1.27872, 1.44131, 1.57592, 1.42172, 1.15392, 1.06817, 1.03148, 0.979264, 0.855717, 0.718826, 0.578996, 0.455065, 0.329454, 0.274357, 0.238905, 0.215708, 0.197557, 0.18899, 0.181396, 0.1738, 0.163443, 0.152826, 0.151969, 0.157273, 0.156402, 0.156365, 0.15649, 0.153956, 0.152439, 0.152236, 0.148702, 0.146753, 0.143548, 0.138107, 0.134693, 0.131485, 0.127257, 0.124335, 0.122966, 0.12093, 0.12119, 0.119558, 0.11996, 0.126729, 0.127033, 0.126634, 0.127575, 0.127338])
xs_sys_jer = array('d', [10.4948, 13.8659, 6.49585, 2.4051, 2.186, 1.19909, 0.905055, 1.12752, 1.38016, 1.29028, 1.23259, 1.4597, 1.62504, 1.36258, 1.0296, 0.990468, 1.01658, 0.93868, 0.765073, 0.573648, 0.427556, 0.327175, 0.249295, 0.223267, 0.208285, 0.199796, 0.187344, 0.183846, 0.178852, 0.17103, 0.158648, 0.148763, 0.148882, 0.154503, 0.157235, 0.159136, 0.158652, 0.156221, 0.154182, 0.15004, 0.1449, 0.142896, 0.137653, 0.134742, 0.130939, 0.127877, 0.124739, 0.122896, 0.120868, 0.12029, 0.119328, 0.118264, 0.119229, 0.125039, 0.125461, 0.125901, 0.126009, 0.12825])
xs_sys_allexceptbkg = array('d', [11.0793, 14.6576, 8.18387, 2.98808, 2.41434, 1.39306, 1.03622, 1.16891, 1.36118, 1.31078, 1.31462, 1.4726, 1.61203, 1.47434, 1.19894, 1.11198, 1.0655, 1.01151, 0.885947, 0.739265, 0.593545, 0.469988, 0.340932, 0.282242, 0.247505, 0.220325, 0.202759, 0.193835, 0.185701, 0.177745, 0.16549, 0.157727, 0.156754, 0.158977, 0.160684, 0.161161, 0.159075, 0.156246, 0.157341, 0.157514, 0.151399, 0.148385, 0.146308, 0.141131, 0.138308, 0.135539, 0.131246, 0.128201, 0.126297, 0.123946, 0.123568, 0.121577, 0.122788, 0.129682, 0.13028, 0.129908, 0.128889, 0.13071])
xs_sys_bkg = array('d', [17.8233, 17.0672, 8.87882, 4.14336, 3.71141, 2.26242, 1.64284, 1.83717, 2.03994, 1.81246, 1.7008, 1.76563, 1.83215, 1.53355, 1.16343, 1.09413, 1.08034, 0.990918, 0.807054, 0.605093, 0.447392, 0.356746, 0.272279, 0.234907, 0.221857, 0.207012, 0.196883, 0.189535, 0.183055, 0.172591, 0.163252, 0.153093, 0.152472, 0.155269, 0.159703, 0.160374, 0.15914, 0.156509, 0.155251, 0.151014, 0.147913, 0.141795, 0.137857, 0.134822, 0.130628, 0.128374, 0.125283, 0.122871, 0.122779, 0.120804, 0.119247, 0.120287, 0.121811, 0.125298, 0.125578, 0.12732, 0.127192, 0.128601])


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

legend = TLegend(.40,.6,.60,.8)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.AddEntry(g_all, "All / Stat. only","lp")
legend.AddEntry(g_lumi, "Lumi / Stat. only","lp")
legend.AddEntry(g_jes, "JES / Stat. only","lp")
legend.AddEntry(g_jer, "JER / Stat. only","lp")
legend.AddEntry(g_allexceptbkg, "All except bkg / Stat. only","lp")
legend.AddEntry(g_bkg, "Bkg / Stat. only","lp")

legend.Draw()

#draw the lumi text on the canvas
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "40.2 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_breakdown_DijetLimitCode_qg_Run2_13TeV_DATA_40p2_invpb.eps')
