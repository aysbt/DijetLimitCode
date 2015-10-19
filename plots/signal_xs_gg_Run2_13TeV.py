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

  #cmd = "./stats " + str(int(mass)) + " gg"
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

  #log_file = open("stats_" + str(int(mass)) + "_gg.log",'r')
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
sig = array('d', [1.45033, -0.373826, 0.797245, 0.980286, 0.553761, 0.264963, 0.058821, 0.077851, -0.264369, -0.325396, -0.219324, -0.314249, -0.383092, -0.297332, -0.223625, -0.165454, -0.100588, -0.0447174, -0.0156518, 0.0199776, 0.0630915, 0.0910869, 0.103669, 0.113195, 0.128742, 0.138884, 0.137179, 0.113437, 0.0799199, 0.0477287, 0.0225616, 0.00423402, -0.00667289, -0.0168736, -0.0170494, -0.0143897, -0.0153603, -0.0184819, 0.0, 0.0, 0.0, -0.00839788, -0.00470909, -0.0019471, -0.00102785, -0.000469627, -0.000666616, -0.00140035, -0.00277954, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ex = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ey = array('d', [1.42604, 1.08912, 1.3353, 0.747609, 0.625249, 0.531047, 0.44878, 0.37699, 0.319012, 0.269339, 0.228178, 0.194682, 0.167198, 0.143887, 0.124044, 0.107851, 0.0945725, 0.0834048, 0.0932719, 0.066332, 0.0734073, 0.0533043, 0.0482866, 0.0440349, 0.0401183, 0.0364627, 0.0334485, 0.0305903, 0.027861, 0.0250683, 0.022148, 0.0193463, 0.016975, 0.0148049, 0.0126041, 0.0115151, 0.00957472, 0.00890771, 0.0, 0.0, 0.0, 0.00573923, 0.00553704, 0.00543526, 0.00514312, 0.00483155, 0.00457905, 0.00436374, 0.00423467, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

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
graph_sig.GetXaxis().SetTitle("gg resonance mass [GeV]")
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
CMS_lumi.lumi_sqrtS = "809 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SetGridx()
c.SetGridy()
c.SaveAs('signal_xs_DijetLimitCode_gg_Run2_13TeV_DATA_809_invpb.eps')
