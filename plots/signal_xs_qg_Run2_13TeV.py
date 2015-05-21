#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import CMS_lumi

CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "1 fb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
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
mass_max = 6000

########################################################
## Uncomment this part if running the limit code

### for running the limit code
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(mass)

  #cmd = "./stats " + str(int(mass)) + " qg"
  #print "Running: " + cmd
  #proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
  #output = proc.communicate()[0]
  #if proc.returncode != 0:
    #print output
    #sys.exit(1)
  ##print output

  #outputlines = output.split("\n")

  #for line in outputlines:
    #if "Fitted signal xs:" in line:
      ##print line
      #sig.append(float(line.split()[3]))
      #sig_ey.append(float(line.split()[5]))

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

masses = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0])
sig = array('d', [18.8057, 0.798707, -3.9119, -0.32558, 1.98378, 1.48775, 0.53242, -0.235843, -0.44172, -0.410635, -0.329208, -0.362087, -0.389282, -0.215928, -0.0131875, 0.0423749, 0.0473262, 0.0385139, 0.0247067, 0.0146037, 0.0212599, 0.0502669, 0.0689047, 0.063439, 0.0366732, 0.011845, -0.00379047, -0.0092201, -0.00418309, 0.0104909, 0.0272268, 0.0347521, 0.03368, 0.0263805, 0.0185127, 0.0147886, 0.015182, 0.016703, 0.0167795, 0.0149432, 0.011436, 0.00682969, 0.00127902, -0.00355423, -0.0079879])
sig_ex = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ey = array('d', [5.18662, 2.31884, 1.32492, 0.968799, 0.765493, 0.6294, 0.533728, 0.44612, 0.372985, 0.314977, 0.26637, 0.228893, 0.195715, 0.167621, 0.144248, 0.125194, 0.109162, 0.0948967, 0.0834621, 0.0739401, 0.0655216, 0.0582621, 0.0520274, 0.0465849, 0.0418454, 0.0374542, 0.033487, 0.0300683, 0.0271009, 0.0246396, 0.0225845, 0.0207465, 0.0191094, 0.0175948, 0.016194, 0.0148005, 0.0134478, 0.0122975, 0.0112893, 0.0104096, 0.00954489, 0.00869468, 0.00778754, 0.00681257, 0.00583314])

##
########################################################

graph_sig = TGraphErrors(len(masses),masses,sig,sig_ex,sig_ey)
graph_sig.GetXaxis().SetTitle("qg resonance mass [GeV]")
graph_sig.GetYaxis().SetTitle("Signal cross section [pb]")
#graph_sig.GetYaxis().SetRangeUser(-15.,40.)
graph_sig.SetMarkerStyle(20)
graph_sig.SetMarkerColor(1)
graph_sig.SetLineWidth(2)
graph_sig.SetLineStyle(1)
graph_sig.SetLineColor(1)

c = TCanvas("c", "",800,800)
c.cd()

graph_sig.Draw("ALP")

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

#c.SetLogy()
c.SaveAs('signal_xs_qg_Run2_13TeV.pdf')
