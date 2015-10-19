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

  #cmd = "./stats " + str(int(mass)) + " qq"
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

  #log_file = open("stats_" + str(int(mass)) + "_qq.log",'r')
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
sig = array('d', [-0.521774, 0.288588, 0.389337, 0.199606, 0.227946, 0.0737168, -0.0227487, -0.0812857, -0.0842714, -0.0334397, -0.0372218, -0.0459295, -0.0656569, -0.0701572, -0.0604161, -0.0415202, -0.0139915, 0.00373331, 0.00700234, 0.00881104, 0.013708, 0.0211098, 0.0265519, 0.0307038, 0.0328534, 0.0313208, 0.0248751, 0.0144952, 0.00386286, -0.00310908, -0.00778014, -0.0103388, -0.0125485, -0.0116582, -0.00813777, -0.00492938, -0.00292537, -0.00203214, -0.0017462, -0.00147408, -0.000964566, -0.000209617, 0.000386329, 0.000962093, 0.00116937, 0.00112731, 0.000874326, 0.000444832, -6.89241e-05, -0.00072938, 0.0, 0.0, 0.0, 6.03925e-06, 0.000365178, 0.000538962])
sig_ex = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ey = array('d', [0.537223, 0.342346, 0.282989, 0.236132, 0.196672, 0.164826, 0.139642, 0.118744, 0.104913, 0.0866134, 0.0797798, 0.064273, 0.0555628, 0.048239, 0.0420712, 0.0369356, 0.0373818, 0.0331192, 0.0298159, 0.0231584, 0.0207516, 0.0186858, 0.0189536, 0.0153598, 0.015294, 0.0125914, 0.0113612, 0.0101965, 0.0097513, 0.00792182, 0.00725231, 0.00586851, 0.00556831, 0.00493036, 0.00409609, 0.0039794, 0.00366582, 0.00342246, 0.00318917, 0.00294917, 0.00265414, 0.00248515, 0.00233613, 0.00219616, 0.0020815, 0.0019285, 0.00178045, 0.0016441, 0.00149893, 0.00137712, 0.0, 0.0, 0.0, 0.0010921, 0.0010331, 0.000999481])

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
c.SaveAs('signal_xs_DijetLimitCode_qq_Run2_13TeV_DATA_1769_invpb.eps')
