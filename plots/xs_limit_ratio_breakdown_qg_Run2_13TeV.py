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

xs_sys_all = array('d', [1.13913, 1.8364, 1.71224, 1.26228, 0.924489, 0.683269, 0.433065, 0.295124, 0.222364, 0.201017, 0.185775, 0.160148, 0.132396, 0.112132, 0.0987242, 0.0936752, 0.0942825, 0.0955584, 0.0930272, 0.0894917, 0.0872137, 0.0869834, 0.0864531, 0.0853363, 0.0835342, 0.0787906, 0.0731486, 0.0633358, 0.0505204, 0.0353785, 0.0233455, 0.0164669, 0.0127346, 0.0105698, 0.00954164, 0.00931178, 0.00938082, 0.00940067, 0.00937174, 0.00920891, 0.00910763, 0.00894841, 0.00890596, 0.00883482, 0.00868046, 0.00839036, 0.00815086, 0.00783483, 0.00743567, 0.00703365, 0.00660032, 0.00620008, 0.00600268, 0.00608876, 0.00603658, 0.00604036])
xs_sys_lumi = array('d', [0.442369, 0.941268, 1.11215, 0.751271, 0.639814, 0.45679, 0.254124, 0.177264, 0.130912, 0.125322, 0.116898, 0.0980347, 0.0787703, 0.0662481, 0.0582374, 0.0552691, 0.0607276, 0.069036, 0.0695602, 0.0670677, 0.0664025, 0.069755, 0.0733654, 0.0753058, 0.075291, 0.0712095, 0.063597, 0.0503412, 0.0349742, 0.0228349, 0.015858, 0.0122342, 0.00988526, 0.00852144, 0.00812946, 0.00822969, 0.00872334, 0.00883679, 0.00886666, 0.00861305, 0.00847136, 0.00840675, 0.00842466, 0.00859586, 0.00857567, 0.00826198, 0.00788294, 0.00755644, 0.00703023, 0.00658103, 0.00614795, 0.00572675, 0.00561917, 0.00580723, 0.00581761, 0.00594716])
xs_sys_jes = array('d', [0.45355, 0.943335, 1.11191, 0.773217, 0.64836, 0.469145, 0.265002, 0.180298, 0.134382, 0.125583, 0.117381, 0.0979193, 0.0798774, 0.0671149, 0.0594329, 0.0579247, 0.0612455, 0.0687535, 0.0690273, 0.0678716, 0.067872, 0.0705561, 0.0731473, 0.0748062, 0.0750682, 0.0719005, 0.0664208, 0.0562298, 0.0427753, 0.0284329, 0.0186965, 0.0136969, 0.010679, 0.00889136, 0.00841415, 0.0083731, 0.00857884, 0.00878804, 0.00881932, 0.00871287, 0.00865209, 0.00850226, 0.00843767, 0.00853583, 0.00844833, 0.00814983, 0.00791855, 0.00768477, 0.00718796, 0.00678967, 0.00637046, 0.00595592, 0.00579199, 0.00588633, 0.00584573, 0.00591371])
xs_sys_jer = array('d', [0.442088, 0.951345, 1.11626, 0.753315, 0.639573, 0.450894, 0.254323, 0.175633, 0.131252, 0.125516, 0.11699, 0.0972151, 0.0795085, 0.0656287, 0.0581767, 0.0563744, 0.0600573, 0.0691193, 0.070528, 0.067748, 0.0677521, 0.0707347, 0.0740811, 0.0763775, 0.0760343, 0.071259, 0.0629448, 0.0499688, 0.0349967, 0.0227172, 0.0160092, 0.0124552, 0.0100811, 0.00862987, 0.0081253, 0.00830331, 0.00872897, 0.00891062, 0.00883545, 0.00868497, 0.00855282, 0.00846273, 0.00849338, 0.00850769, 0.00850506, 0.00823137, 0.007898, 0.00756447, 0.00701111, 0.0065875, 0.0062392, 0.00577729, 0.00570472, 0.0058339, 0.00582768, 0.00595716])
xs_sys_allexceptbkg = array('d', [0.456645, 0.960428, 1.12653, 0.781884, 0.655229, 0.470065, 0.271607, 0.182123, 0.135633, 0.128199, 0.118783, 0.0996111, 0.0814488, 0.0683661, 0.0600871, 0.0575925, 0.0618196, 0.069538, 0.0704706, 0.068782, 0.0693651, 0.072072, 0.0747074, 0.076453, 0.0762631, 0.0731008, 0.0672898, 0.0569491, 0.0433993, 0.028907, 0.0191792, 0.0138462, 0.0108342, 0.00917123, 0.00848044, 0.00845203, 0.0087119, 0.00895065, 0.00886728, 0.00871185, 0.00871717, 0.00863709, 0.00851735, 0.00857807, 0.00853306, 0.00823712, 0.00802067, 0.0077661, 0.00732333, 0.00692641, 0.00654795, 0.00609308, 0.00591067, 0.00595546, 0.0059374, 0.00601798])
xs_sys_bkg = array('d', [1.10082, 1.66183, 1.58102, 1.07752, 0.85597, 0.616799, 0.38143, 0.275184, 0.210861, 0.193948, 0.179475, 0.151198, 0.124728, 0.106506, 0.0932373, 0.0863507, 0.0888841, 0.0941513, 0.0910053, 0.0853328, 0.081966, 0.0812415, 0.0821363, 0.0822667, 0.080507, 0.0753699, 0.0670712, 0.0534117, 0.0381316, 0.0255234, 0.0183186, 0.0140425, 0.0113352, 0.00960563, 0.00900709, 0.00899394, 0.00926943, 0.00933813, 0.0092585, 0.0090029, 0.00876475, 0.00870168, 0.00865828, 0.0086335, 0.00866619, 0.00835218, 0.00804924, 0.00764668, 0.00709634, 0.00672333, 0.00627404, 0.00587336, 0.00570424, 0.00584305, 0.00586927, 0.00594546])


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
g_all.GetYaxis().SetRangeUser(0.5,3.)
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
CMS_lumi.lumi_sqrtS = "1769 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

c.SetGridx()
c.SetGridy()

c.SaveAs('xs_limit_ratio_breakdown_DijetLimitCode_qg_Run2_13TeV_DATA_1769_invpb.eps')
