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

  #cmd = "./stats " + str(int(mass)) + " 1.0 qg"
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
sig = array('d', [-0.295351, -0.164875, -0.170615, -0.207966, -0.0920555, 0.071096, 0.122302, 0.0901768, 0.0390112, 0.00218427, -0.0077671, -0.00146772, 0.00413169, 0.0061146, -0.000740408, -0.00517954, -0.00673097, -0.00484254, -0.00124275, 0.00138961, 0.0017393, 0.00132318, 0.00191168, 0.00288448, 0.00322708, 0.00250055, 0.00145849, 0.000399842, -0.000584227, -0.00146444, -0.00202053, -0.00229084, -0.00231558, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, -0.000377441, -0.000341164])
sig_ex = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ey = array('d', [0.2389, 0.165173, 0.103059, 0.0856475, 0.0634611, 0.0495, 0.0427065, 0.0312065, 0.025011, 0.0246217, 0.0168714, 0.0140168, 0.0147079, 0.0098579, 0.0109643, 0.00883929, 0.00598354, 0.00510232, 0.00530217, 0.0043864, 0.00372225, 0.00292875, 0.00284586, 0.00225574, 0.00199191, 0.00175577, 0.00154113, 0.00139656, 0.00114048, 0.000999901, 0.000877794, 0.000710722, 0.000585662, 0.00108017, 0.00101268, 0.00092181, 0.000855673, 0.000786253, 0.000684556, 0.000315482, 0.00034036])

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
c.SaveAs('signal_xs_qg_Run1_8TeV.pdf')
