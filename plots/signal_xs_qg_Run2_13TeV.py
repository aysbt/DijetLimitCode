#!/usr/bin/env python

import sys, os, subprocess, string, re
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


masses = array('d')
sig = array('d')
sig_ex = array('d')
sig_ey = array('d')

mass_min = 1500
mass_max = 7000

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

  #foundLine = False

  #for line in outputlines:
    #if "Fitted signal xs:" in line:
      ##print line
      #foundLine = True
      #sig.append(float(line.split()[3]))
      #sig_ey.append(float(line.split()[5]))
      #break

  #if not foundLine:
    #print "Signal fit failed for m="+str(mass)+" GeV"
    #sig.append(0.)
    #sig_ey.append(0.)

  #sig_ex.append(0.)

#------------------------------------------------------

### for reading the limit code log files
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(mass)

  #log_file = open("stats_" + str(int(mass)) + "_qg.log",'r')
  #outputlines = log_file.readlines()
  #log_file.close()

  #foundLine = False

  #for line in outputlines:
    #if "Fitted signal xs:" in line:
      ##print line
      #foundLine = True
      #sig.append(float(line.split()[3]))
      #sig_ey.append(float(line.split()[5]))
      #break

  #if not foundLine:
    #print "Signal fit failed for m="+str(mass)+" GeV"
    #sig.append(0.)
    #sig_ey.append(0.)

  #sig_ex.append(0.)

##------------------------------------------------------

#print "masses =", masses
#print "sig =", sig
#print "sig_ex =", sig_ex
#print "sig_ey =", sig_ey

##
########################################################

########################################################
## Comment out this part if running the limit code

masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])
sig = array('d', [-0.598594, 0.405988, 0.66878, 0.37286, 0.320152, 0.171797, -0.0299851, -0.113695, -0.153695, -0.108064, -0.0778387, -0.0830151, -0.0922733, -0.0917562, -0.0835152, -0.063068, -0.031259, -0.00164356, 0.00904815, 0.0133213, 0.0190004, 0.0284727, 0.0361523, 0.0413927, 0.0443658, 0.0428156, 0.0375255, 0.0265172, 0.0128382, 0.00024535, -0.0078436, -0.0123853, -0.0155566, -0.0167313, -0.0139812, -0.00971722, -0.00624133, -0.00410092, -0.00300081, -0.00237193, -0.00132202, -0.000690573, -4.38494e-06, 0.000756831, 0.00129487, 0.00117032, 0.00109091, 0.000837405, 0.000441526, -1.82153e-05, -0.000524477, -0.00129951, -0.00127031, -0.000395558, 8.99942e-05, 0.000487801])
sig_ex = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ey = array('d', [0.607272, 0.471998, 0.522763, 0.330118, 0.30629, 0.233881, 0.197794, 0.167307, 0.141879, 0.120535, 0.103057, 0.0885508, 0.0894598, 0.0661992, 0.0575477, 0.0502536, 0.0442364, 0.0476883, 0.034706, 0.030983, 0.0277067, 0.029571, 0.0223773, 0.0202108, 0.0212582, 0.0165315, 0.0150109, 0.0136016, 0.0122458, 0.0109154, 0.0107016, 0.0091742, 0.00811372, 0.00660306, 0.00586598, 0.0056639, 0.00491022, 0.00483133, 0.00453467, 0.00406419, 0.00381959, 0.00356308, 0.00332313, 0.00311598, 0.00293675, 0.00272956, 0.00258907, 0.00246198, 0.00233996, 0.00227754, 0.00217111, 0.00210552, 0.00198672, 0.00178402, 0.00162883, 0.00157046])

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
graph_sig.GetXaxis().SetTitle("qg resonance mass [GeV]")
graph_sig.GetYaxis().SetTitle("Signal cross section [pb]")
graph_sig.GetYaxis().SetTitleOffset(1.2)
graph_sig.GetYaxis().SetRangeUser(1e-4,1e2)
graph_sig.SetMarkerStyle(20)
graph_sig.SetMarkerColor(1)
graph_sig.SetLineWidth(2)
graph_sig.SetLineStyle(1)
graph_sig.SetLineColor(1)

c = TCanvas("c", "",800,800)
c.cd()

graph_sig.Draw("AP")

#draw the lumi text on the canvas
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "1769 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SetGridx()
c.SetGridy()
c.SaveAs('signal_xs_DijetLimitCode_qg_Run2_13TeV_DATA_1769_invpb.eps')
