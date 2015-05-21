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

masses = array('d', [1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0])
sig = array('d', [-0.165771, -0.0758109, -0.118682, -0.133728, -0.0441747, 0.0587429, 0.0776317, 0.0531022, 0.0191305, -0.00402197, -0.00611499, 0.000436741, 0.00422291, 0.00349904, -0.00243201, -0.00507647, -0.00508535, -0.00311102, -0.000332284, 0.0010759, 0.00086507, 0.000599653, 0.00154812, 0.0025645, 0.00259102, 0.00189053, 0.00106293, 0.000292536, -0.000387737, -0.000941906, -0.00121357, -0.0013353, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, -0.000202632, -0.000114479, -0.000112709])
sig_ex = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ey = array('d', [0.115688, 0.104783, 0.0702904, 0.0554669, 0.0445798, 0.0358743, 0.0294962, 0.0224321, 0.0200117, 0.0166961, 0.012329, 0.0102696, 0.00860289, 0.00838306, 0.00696521, 0.00591228, 0.0043422, 0.00369357, 0.00316151, 0.00273897, 0.00257084, 0.00206388, 0.00179646, 0.00165114, 0.00138141, 0.00123908, 0.00103591, 0.000893107, 0.000726516, 0.000614674, 0.000509356, 0.000404838, 0.000726718, 0.000694965, 0.000622489, 0.0005466, 0.00051643, 0.000447406, 0.000187244, 0.000190539, 0.000202816])

##
########################################################

graph_sig = TGraphErrors(len(masses),masses,sig,sig_ex,sig_ey)
graph_sig.GetXaxis().SetTitle("qq resonance mass [GeV]")
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
c.SaveAs('signal_xs_qq_Run1_8TeV.pdf')
