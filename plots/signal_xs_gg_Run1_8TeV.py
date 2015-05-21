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

  #cmd = "./stats " + str(int(mass)) + " 1.0 gg"
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
sig = array('d', [-0.450499, -0.272787, -0.229776, -0.334448, -0.198444, 0.0776649, 0.186256, 0.150154, 0.0701829, 0.012796, -0.0108908, -0.00196764, 0.00559767, 0.00989547, 0.00189849, -0.00680431, -0.00875738, -0.00743241, -0.00217542, 0.00217318, 0.00309479, 0.00219599, 0.00258897, 0.00386941, 0.00469569, 0.00384541, 0.00210996, 0.000469412, -0.000913684, -0.00224512, -0.00320886, -0.0036272, -0.00373006, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, 1e-06, -0.000746796, -0.000631217])
sig_ex = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
sig_ey = array('d', [0.455294, 0.354258, 0.163355, 0.129052, 0.104339, 0.0816188, 0.0611115, 0.0480863, 0.0468201, 0.0309354, 0.0253066, 0.0265577, 0.0173486, 0.0144885, 0.0121679, 0.0102443, 0.0106681, 0.00732021, 0.00624107, 0.00630312, 0.00483265, 0.00425619, 0.00376249, 0.00332956, 0.00295847, 0.00279722, 0.00246621, 0.00203116, 0.00175657, 0.00155865, 0.00134124, 0.00112543, 0.000936576, 0.00171262, 0.00163868, 0.00153144, 0.00142642, 0.00135758, 0.00130312, 0.000588059, 0.00068964])

##
########################################################

graph_sig = TGraphErrors(len(masses),masses,sig,sig_ex,sig_ey)
graph_sig.GetXaxis().SetTitle("gg resonance mass [GeV]")
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
c.SaveAs('signal_xs_gg_Run1_8TeV.pdf')
