#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import CMS_lumi

CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "19.7 fb^{-1} (8 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

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


masses = array('d')
sig = array('d')
sig_ex = array('d')
sig_ey = array('d')

mass_min = 1200
mass_max = 5200

########################################################
## Uncomment this part if running the limit code

### for running the limit code
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(mass)

  #cmd = "./stats " + str(int(mass)) + " 1.0 qq"
  #print "Running: " + cmd
  #proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
  #output = proc.communicate()[0]
  #if proc.returncode != 0:
    #print output
    #sys.exit(1)
  ##print output

  #outputlines = output.split("\n")

  #foundLine = False

  #for line in outputlines:
    #if "Fitted signal xs:" in line:
      ##print line
      #foundLine = True
      #sig.append(float(line.split()[3]))
      #sig_ey.append(float(line.split()[5]))

  #if not foundLine:
    #print "Signal fit failed for m="+str(mass)+" GeV"
    #sig.append(0.)
    #sig_ey.append(0.)

  #sig_ex.append(0.)
##------------------------------------------------------

#print "masses:"
#print masses
#print "sig:"
#print sig
#print "sig_ex:"
#print sig_ex
#print "sig_ey:"
#print sig_ey

##
########################################################

########################################################
## Comment out this part if running the limit code

masses = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0])
sig = array('d', [-0.165771, -0.0755148, -0.118578, -0.133867, -0.0441818, 0.0587162, 0.0776576, 0.0530941, 0.0191482, -0.00388361, -0.00607564, 0.000432122, 0.0042181, 0.00335501, -0.00242348, -0.00507061, -0.00508639, -0.00311096, -0.000266431, 0.00106523, 0.000854914, 0.000452309, 0.00154219, 0.00256397, 0.00259016, 0.00189058, 0.0010542, 0.000289527, -0.000386842, -0.000941989, -0.00121392, -0.00133519, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.000202577, -0.000111272, -0.000112788])
sig_ex = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ey = array('d', [0.115704, 0.103423, 0.0773992, 0.0575312, 0.0437233, 0.0347578, 0.0301908, 0.0224373, 0.0200258, 0.0170404, 0.0146775, 0.0102662, 0.0102613, 0.00722738, 0.00609555, 0.00512841, 0.00490458, 0.0036941, 0.00316257, 0.00300693, 0.00259695, 0.00206253, 0.00179686, 0.00165266, 0.00142458, 0.00126547, 0.00103568, 0.000894565, 0.000741311, 0.000614564, 0.000506185, 0.000414196, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00018741, 0.000190057, 0.00020359])

##
########################################################

sig_pos = array('d')
sig_exl = array('d')
sig_exh = array('d')
sig_eyl = array('d')
sig_eyh = array('d')

# create final arrays
for i in range(0,len(masses)):
  sig_pos.append(sig[i] if sig[i]>0. else 0.)
  sig_exl.append(sig_ex[i])
  sig_exh.append(sig_ex[i])
  sig_eyl.append(sig_ey[i] if sig[i]>0. else 0.)
  sig_eyh.append(sig_ey[i])

graph_sig = TGraphAsymmErrors(len(masses),masses,sig_pos,sig_exl,sig_exh,sig_eyl,sig_eyh)
graph_sig.GetXaxis().SetTitle("qq resonance mass [GeV]")
graph_sig.GetYaxis().SetTitle("Signal cross section [pb]")
graph_sig.GetYaxis().SetRangeUser(1e-4,2e0)
graph_sig.GetXaxis().SetNdivisions(1005)
graph_sig.SetMarkerStyle(20)
graph_sig.SetMarkerColor(1)
graph_sig.SetLineWidth(2)
graph_sig.SetLineStyle(1)
graph_sig.SetLineColor(1)

c = TCanvas("c", "",800,800)
c.cd()

graph_sig.Draw("AP")

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SetGridx()
c.SetGridy()
c.SaveAs('signal_xs_qq_Run1_8TeV.pdf')
