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
xs_obs_limits = array('d')
xs_exp_limits = array('d')
masses_exp = array('d')
xs_exp_limits_1sigma = array('d')
xs_exp_limits_1sigma_up = array('d')
xs_exp_limits_2sigma = array('d')
xs_exp_limits_2sigma_up = array('d')


syst = True
#syst = False

mass_min = 1500
mass_max = 7200

########################################################
## Uncomment this part if running the limit code


### for running the limit code
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #cmd = "./stats " + str(int(mass)) + " qq | tee stats_" + str(int(mass)) + "_qq.log"
  #print "Running: " + cmd
  #proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
  #output = proc.communicate()[0]
  #if proc.returncode != 0:
    #print output
    #sys.exit(1)
  ##print output

  #outputlines = output.split("\n")

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

##------------------------------------------------------

### for reading the limit code log files
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_file = open("stats_" + str(int(mass)) + "_qq.log",'r')
  #outputlines = log_file.readlines()
  #log_file.close()

  #for line in outputlines:
    #if re.search("observed bound =", line):
      #xs_obs_limits.append(float(line.split()[6]))
    #if re.search("median:", line):
      #xs_exp_limits.append(float(line.split()[1]))
    #if re.search("1 sigma band:", line):
      #xs_exp_limits_1sigma.append(float(line.split()[4]))
      #xs_exp_limits_1sigma_up.append(float(line.split()[6]))
    #if re.search("2 sigma band:", line):
      #xs_exp_limits_2sigma.append(float(line.split()[4]))
      #xs_exp_limits_2sigma_up.append(float(line.split()[6]))

##------------------------------------------------------

#for i in range(0,len(masses)):
  #masses_exp.append( masses[len(masses)-i-1] )
  #xs_exp_limits_1sigma.append( xs_exp_limits_1sigma_up[len(masses)-i-1] )
  #xs_exp_limits_2sigma.append( xs_exp_limits_2sigma_up[len(masses)-i-1] )


#print "masses =", masses
#print "xs_obs_limits =", xs_obs_limits
#print "xs_exp_limits =", xs_exp_limits
#print ""
#print "masses_exp =", masses_exp
#print "xs_exp_limits_1sigma =", xs_exp_limits_1sigma
#print "xs_exp_limits_2sigma =", xs_exp_limits_2sigma

##
########################################################

########################################################
## Comment out this part if running the limit code

masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7100.0, 7200.0])
xs_obs_limits = array('d', [0.445766, 0.531756, 0.660085, 0.462665, 0.259771, 0.176882, 0.11975, 0.0883606, 0.0911673, 0.091631, 0.0673097, 0.0576683, 0.0663765, 0.0715058, 0.0707653, 0.0679017, 0.0648869, 0.0605661, 0.0551873, 0.0536497, 0.0525322, 0.0449858, 0.0376862, 0.0386666, 0.0394637, 0.032315, 0.0210878, 0.0132809, 0.00920013, 0.00718502, 0.00635795, 0.00565515, 0.00524019, 0.00555239, 0.00664857, 0.00749758, 0.00812448, 0.00821765, 0.00778863, 0.0072654, 0.00689535, 0.00641743, 0.00594571, 0.00542539, 0.00487017, 0.00432282, 0.00385402, 0.00345907, 0.00325031, 0.0029336, 0.00266552, 0.00247031, 0.0023408, 0.00224978, 0.00218731, 0.0021452, 0.00214538, 0.0021549])
xs_exp_limits = array('d', [0.477582, 0.401964, 0.363716, 0.289744, 0.23842, 0.210805, 0.184404, 0.156756, 0.133975, 0.116447, 0.101665, 0.0899399, 0.0785615, 0.07051, 0.059203, 0.0554069, 0.0494558, 0.0459754, 0.0401039, 0.0355165, 0.031371, 0.0280482, 0.0250272, 0.0237096, 0.0207305, 0.0191532, 0.0166698, 0.0160243, 0.0137829, 0.0132228, 0.0124812, 0.0118259, 0.010205, 0.00943852, 0.0084869, 0.00801166, 0.00735571, 0.00677923, 0.0063039, 0.00570682, 0.00525888, 0.0049462, 0.00463206, 0.00440061, 0.00415374, 0.00370666, 0.00357487, 0.00338426, 0.00335521, 0.00328086, 0.00321736, 0.003065, 0.0029891, 0.00288091, 0.00276867, 0.00267989, 0.0026509, 0.0026118])

masses_exp = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7100.0, 7200.0, 7200.0, 7100.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0])
xs_exp_limits_1sigma = array('d', [0.263178, 0.234748, 0.224652, 0.179777, 0.152412, 0.129835, 0.108368, 0.0970841, 0.0915296, 0.0750243, 0.0678212, 0.0566056, 0.0534461, 0.0465205, 0.0424667, 0.0373433, 0.0328536, 0.0305547, 0.0272021, 0.0247684, 0.0214411, 0.0202588, 0.0175209, 0.0151822, 0.014361, 0.0133605, 0.0120571, 0.0106639, 0.00997822, 0.00884849, 0.00852133, 0.00792054, 0.00680026, 0.00673866, 0.00583551, 0.00557768, 0.00500044, 0.00466544, 0.00443709, 0.00406596, 0.00373416, 0.00358599, 0.00348265, 0.00323947, 0.00307937, 0.00281487, 0.00273794, 0.00254038, 0.0025423, 0.00245653, 0.00237304, 0.00229849, 0.00223548, 0.00215721, 0.00211602, 0.00207189, 0.00208276, 0.00209582, 0.00349295, 0.00350561, 0.00358605, 0.00369137, 0.00377417, 0.00396151, 0.00413929, 0.0043804, 0.00452086, 0.00467094, 0.00485855, 0.00513458, 0.00538816, 0.00590626, 0.00635441, 0.00680014, 0.00716117, 0.00762124, 0.00805238, 0.00876694, 0.00957286, 0.0111866, 0.0117984, 0.0130179, 0.0138104, 0.015258, 0.0170009, 0.0186741, 0.0199252, 0.0207558, 0.0230475, 0.0262269, 0.0279303, 0.0301622, 0.034724, 0.0369757, 0.0401604, 0.0457646, 0.055022, 0.0618427, 0.0670297, 0.0697109, 0.0824436, 0.0894626, 0.113581, 0.116346, 0.140677, 0.160056, 0.192597, 0.211474, 0.243009, 0.288593, 0.331943, 0.373119, 0.469671, 0.572021, 0.759571, 0.924344])
xs_exp_limits_2sigma = array('d', [0.169716, 0.155997, 0.1346, 0.124751, 0.107863, 0.0860352, 0.0734498, 0.0620996, 0.0578684, 0.0545188, 0.0479836, 0.0384862, 0.0383182, 0.0324485, 0.0283644, 0.0261524, 0.0249307, 0.0222972, 0.0199062, 0.0176515, 0.0147575, 0.0154333, 0.0127418, 0.0111916, 0.0107129, 0.00942763, 0.00837832, 0.00766431, 0.00706077, 0.00691626, 0.00632623, 0.00585496, 0.00496128, 0.00467607, 0.00432573, 0.00405127, 0.00375612, 0.00366854, 0.00346122, 0.0034499, 0.00324831, 0.00302459, 0.00280982, 0.0025625, 0.00236202, 0.00211091, 0.00206958, 0.00199197, 0.0019624, 0.00191732, 0.00185805, 0.00183947, 0.00182105, 0.00180951, 0.00180205, 0.00179986, 0.00182184, 0.0018562, 0.00533469, 0.0053133, 0.00524814, 0.00540566, 0.00567425, 0.00579876, 0.00614897, 0.00640721, 0.00670605, 0.00708195, 0.00717591, 0.0073686, 0.00767851, 0.00818318, 0.00879872, 0.009734, 0.010295, 0.010783, 0.0113261, 0.0121944, 0.0133156, 0.0160805, 0.0165597, 0.0182655, 0.0210501, 0.0212347, 0.0249604, 0.0253604, 0.0284897, 0.031081, 0.0334059, 0.0352302, 0.0395898, 0.041841, 0.0480632, 0.0522287, 0.0578574, 0.0668002, 0.074515, 0.0820672, 0.0997265, 0.101039, 0.120407, 0.133622, 0.160518, 0.179016, 0.195348, 0.227508, 0.262664, 0.3058, 0.36116, 0.424177, 0.462427, 0.54603, 0.696327, 0.819949, 1.20284, 1.46542])

if syst:
  masses = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7100.0, 7200.0])
  xs_obs_limits = array('d', [0.895858, 0.965575, 0.900752, 0.697496, 0.423405, 0.26049, 0.181675, 0.132657, 0.125319, 0.119397, 0.0987246, 0.0877885, 0.0911367, 0.0928461, 0.0908348, 0.0858027, 0.0808088, 0.0741853, 0.0681326, 0.0642383, 0.060582, 0.0544358, 0.0476643, 0.0443734, 0.0423859, 0.037657, 0.0311503, 0.0211091, 0.0130474, 0.00900213, 0.00728843, 0.00637582, 0.00597609, 0.00623773, 0.00705963, 0.00787881, 0.0082644, 0.00835833, 0.00805248, 0.00763612, 0.00711483, 0.00660508, 0.00613461, 0.00565583, 0.00512362, 0.00461948, 0.00412781, 0.00375494, 0.00339019, 0.003035, 0.00278894, 0.00257018, 0.00243658, 0.00227797, 0.00219318, 0.00215883, 0.00214122, 0.0021581])
  xs_exp_limits = array('d', [0.9946315, 0.8051145, 0.627147, 0.475644, 0.374002, 0.304605, 0.2522265, 0.208702, 0.183822, 0.161106, 0.1410845, 0.123595, 0.1101135, 0.0996241, 0.0878194, 0.0777768, 0.0679316, 0.05905805, 0.0536272, 0.0459997, 0.0409238, 0.0364848, 0.0330868, 0.0286179, 0.0252488, 0.02282465, 0.02144215, 0.0180953, 0.0170692, 0.0151538, 0.01402765, 0.01239115, 0.01140105, 0.01064755, 0.00952408, 0.00845977, 0.00801375, 0.007042805, 0.006565405, 0.00586786, 0.00550331, 0.00508579, 0.00470573, 0.00448573, 0.00417389, 0.003885045, 0.0036984, 0.00356998, 0.003465925, 0.00331277, 0.0031561, 0.003022025, 0.00295003, 0.00287352, 0.002794315, 0.002722985, 0.002670735, 0.00265583])

  masses_exp = array('d', [1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7100.0, 7200.0, 7200.0, 7100.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0])
  xs_exp_limits_1sigma = array('d', [0.609869214, 0.52115338, 0.413442029, 0.34974705, 0.270895485, 0.217091907, 0.17605387, 0.144859859, 0.123263543, 0.112674597, 0.0993400535, 0.086984566, 0.0803555741, 0.0716346701, 0.0632265081, 0.0562293914, 0.0516513318, 0.0433566986, 0.0381886938, 0.031833592, 0.0273415789, 0.0251596806, 0.0227727084, 0.0191935135, 0.0175730019, 0.0159331814, 0.0148962362, 0.0130281248, 0.0121419646, 0.0109049942, 0.0104277392, 0.0089879186, 0.00847308723, 0.00770416664, 0.00687087214, 0.00610733871, 0.00571931879, 0.0049755487, 0.00469600697, 0.00433241202, 0.00403365923, 0.00374003166, 0.0034744687, 0.00331487771, 0.00311945932, 0.00302399098, 0.00286991394, 0.00276832486, 0.00264461387, 0.00257949142, 0.00246347001, 0.0023547843, 0.00226701033, 0.00219973051, 0.00213863393, 0.00208723249, 0.0020867228, 0.00208967702, 0.00348527795, 0.0035367298, 0.00360873422, 0.0037956104, 0.00388385826, 0.00402190743, 0.00418753809, 0.0044480696, 0.00468098793, 0.00491235132, 0.00521134065, 0.00540415892, 0.00562056177, 0.00595334263, 0.0064494304, 0.00692681654, 0.00738104582, 0.00789032748, 0.00851196091, 0.00932072322, 0.00983167081, 0.0113298792, 0.0122997633, 0.0132245979, 0.0154828902, 0.017413698, 0.0189383687, 0.0194176852, 0.0213211905, 0.0245330518, 0.0257906834, 0.0290759005, 0.0321022463, 0.034848081, 0.0398854781, 0.0453886985, 0.0523359995, 0.0598069234, 0.0646537247, 0.076029572, 0.0841573843, 0.0957495811, 0.10384867, 0.121538968, 0.139143534, 0.158713731, 0.176371842, 0.205506726, 0.22960221, 0.263487012, 0.306384496, 0.357650422, 0.421176979, 0.538925884, 0.69902857, 0.889583955, 1.15740248, 1.49370854])
  xs_exp_limits_2sigma = array('d', [0.413883505, 0.35084799, 0.303540477, 0.258582295, 0.191345939, 0.154165077, 0.120505882, 0.108910914, 0.0943462025, 0.082778669, 0.0767235811, 0.0680476069, 0.05885282, 0.0526809966, 0.0478690263, 0.0396387763, 0.0362878224, 0.0320076177, 0.028207423, 0.0243468882, 0.0205292242, 0.0185762989, 0.0168444162, 0.0149242323, 0.0132136189, 0.0115096437, 0.0104786279, 0.0097995732, 0.00929387668, 0.00792584752, 0.00746661918, 0.00701085542, 0.00616617191, 0.00555352737, 0.00530213407, 0.00444441585, 0.00429046462, 0.00404924736, 0.00382299905, 0.0036297385, 0.00317482106, 0.00292725475, 0.00270882003, 0.00252720375, 0.00242391072, 0.00241910993, 0.00239987053, 0.00213528871, 0.00216625998, 0.00205793025, 0.0019819098, 0.00195219419, 0.00191572325, 0.00187160028, 0.00185678914, 0.00184277556, 0.00188714219, 0.00190341069, 0.00531570048, 0.00541906249, 0.00544777286, 0.00563386404, 0.00576846288, 0.00586599037, 0.00617531385, 0.00642206989, 0.00673068263, 0.00709186152, 0.00728055853, 0.00735681532, 0.00760238609, 0.00829435253, 0.00863729829, 0.00906560251, 0.00986540247, 0.01091953, 0.0117612326, 0.0128085264, 0.0135558979, 0.0148045739, 0.0171122651, 0.0192948837, 0.0215290741, 0.0229396495, 0.0255929942, 0.0282022091, 0.0311684827, 0.0342088504, 0.0335938864, 0.0428858189, 0.042198882, 0.0490065613, 0.0554493602, 0.0663099308, 0.0713793099, 0.0790832126, 0.0858485517, 0.0990309971, 0.108167713, 0.127058445, 0.144172471, 0.172698651, 0.194051652, 0.21447632, 0.244439968, 0.267019402, 0.304724463, 0.36221299, 0.42424812, 0.490197292, 0.579710029, 0.673697004, 0.929488156, 1.19642072, 1.63548722, 2.02249191])

##
########################################################

massesTh = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0])

xsAxi = array('d', [0.1849E+03,0.1236E+03,0.8473E+02,0.5937E+02,0.4235E+02,0.3069E+02,0.2257E+02,0.1680E+02,0.1263E+02,0.9577E+01,0.7317E+01,0.5641E+01,0.4374E+01,0.3411E+01,0.2672E+01,0.2103E+01,0.1658E+01,0.1312E+01,0.1041E+01,0.8284E+00,0.6610E+00,0.5294E+00,0.4250E+00,0.3417E+00,0.2752E+00,0.2220E+00,0.1792E+00,0.1449E+00,0.1172E+00,0.9487E-01,0.7686E-01,0.6219E-01,0.5033E-01,0.4074E-01,0.3298E-01,0.2671E-01,0.2165E-01,0.1755E-01,0.1422E-01,0.1152E-01,0.9322E-02,0.7539E-02,0.6092E-02,0.4917E-02,0.3965E-02,0.3193E-02,0.2568E-02,0.2062E-02,0.1653E-02,0.1323E-02,0.1057E-02,0.8442E-03,0.6728E-03,0.5349E-03,0.4242E-03,0.3357E-03,0.2644E-03,0.2077E-03,0.1627E-03,0.1271E-03,0.9891E-04,0.7686E-04,0.5951E-04,0.4592E-04,0.3530E-04,0.2704E-04,0.2059E-04,0.1562E-04,0.1180E-04,0.8882E-05,0.6657E-05,0.4968E-05,0.3693E-05,0.2734E-05,0.2016E-05,0.1481E-05,0.1084E-05,0.7903E-06,0.5744E-06,0.4160E-06,0.3007E-06])
xsDiquark = array('d', [0.5824E+02,0.4250E+02,0.3172E+02,0.2411E+02,0.1862E+02,0.1457E+02,0.1153E+02,0.9211E+01,0.7419E+01,0.6019E+01,0.4912E+01,0.4031E+01,0.3323E+01,0.2750E+01,0.2284E+01,0.1903E+01,0.1590E+01,0.1331E+01,0.1117E+01,0.9386E+00,0.7900E+00,0.6658E+00,0.5618E+00,0.4745E+00,0.4010E+00,0.3391E+00,0.2869E+00,0.2428E+00,0.2055E+00,0.1740E+00,0.1473E+00,0.1246E+00,0.1055E+00,0.8922E-01,0.7544E-01,0.6376E-01,0.5385E-01,0.4546E-01,0.3834E-01,0.3231E-01,0.2720E-01,0.2288E-01,0.1922E-01,0.1613E-01,0.1352E-01,0.1132E-01,0.9463E-02,0.7900E-02,0.6584E-02,0.5479E-02,0.4551E-02,0.3774E-02,0.3124E-02,0.2581E-02,0.2128E-02,0.1750E-02,0.1437E-02,0.1177E-02,0.9612E-03,0.7833E-03,0.6366E-03,0.5160E-03,0.4170E-03,0.3360E-03,0.2700E-03,0.2162E-03,0.1725E-03,0.1372E-03,0.1087E-03,0.8577E-04,0.6742E-04,0.5278E-04,0.4114E-04,0.3192E-04,0.2465E-04,0.1894E-04,0.1448E-04,0.1101E-04,0.8322E-05,0.6253E-05,0.4670E-05])
xsWprime = array('d', [0.8811E+01,0.6024E+01,0.4216E+01,0.3010E+01,0.2185E+01,0.1610E+01,0.1200E+01,0.9043E+00,0.6875E+00,0.5271E+00,0.4067E+00,0.3158E+00,0.2464E+00,0.1932E+00,0.1521E+00,0.1201E+00,0.9512E-01,0.7554E-01,0.6012E-01,0.4792E-01,0.3827E-01,0.3059E-01,0.2448E-01,0.1960E-01,0.1571E-01,0.1259E-01,0.1009E-01,0.8090E-02,0.6483E-02,0.5193E-02,0.4158E-02,0.3327E-02,0.2660E-02,0.2125E-02,0.1695E-02,0.1351E-02,0.1075E-02,0.8546E-03,0.6781E-03,0.5372E-03,0.4248E-03,0.3353E-03,0.2642E-03,0.2077E-03,0.1629E-03,0.1275E-03,0.9957E-04,0.7757E-04,0.6027E-04,0.4670E-04,0.3610E-04,0.2783E-04,0.2140E-04,0.1641E-04,0.1254E-04,0.9561E-05,0.7269E-05,0.5510E-05,0.4167E-05,0.3143E-05,0.2364E-05,0.1774E-05,0.1329E-05,0.9931E-06,0.7411E-06,0.5523E-06,0.4108E-06,0.3055E-06,0.2271E-06,0.1687E-06,0.1254E-06,0.9327E-07,0.6945E-07,0.5177E-07,0.3863E-07,0.2888E-07,0.2162E-07,0.1622E-07,0.1218E-07,0.9156E-08,0.6893E-08])
xsZprime = array('d', [0.5027E+01,0.3398E+01,0.2353E+01,0.1663E+01,0.1196E+01,0.8729E+00,0.6450E+00,0.4822E+00,0.3638E+00,0.2769E+00,0.2123E+00,0.1639E+00,0.1272E+00,0.9933E-01,0.7789E-01,0.6134E-01,0.4848E-01,0.3845E-01,0.3059E-01,0.2440E-01,0.1952E-01,0.1564E-01,0.1256E-01,0.1010E-01,0.8142E-02,0.6570E-02,0.5307E-02,0.4292E-02,0.3473E-02,0.2813E-02,0.2280E-02,0.1848E-02,0.1499E-02,0.1216E-02,0.9864E-03,0.8002E-03,0.6490E-03,0.5262E-03,0.4264E-03,0.3453E-03,0.2795E-03,0.2260E-03,0.1826E-03,0.1474E-03,0.1188E-03,0.9566E-04,0.7690E-04,0.6173E-04,0.4947E-04,0.3957E-04,0.3159E-04,0.2516E-04,0.2001E-04,0.1587E-04,0.1255E-04,0.9906E-05,0.7795E-05,0.6116E-05,0.4785E-05,0.3731E-05,0.2900E-05,0.2247E-05,0.1734E-05,0.1334E-05,0.1022E-05,0.7804E-06,0.5932E-06,0.4492E-06,0.3388E-06,0.2544E-06,0.1903E-06,0.1417E-06,0.1051E-06,0.7764E-07,0.5711E-07,0.4186E-07,0.3055E-07,0.2223E-07,0.1612E-07,0.1164E-07,0.8394E-08])

xs_max = 2e+01
idx = 0

for i, xs in enumerate(xsAxi):
  if xs < xs_max:
    idx = i
    break

graph_xsAxi = TGraph(len(massesTh[idx:-1]),massesTh[idx:-1],xsAxi[idx:-1])
graph_xsAxi.SetLineWidth(3)
graph_xsAxi.SetLineStyle(3)
graph_xsAxi.SetLineColor(63)

for i, xs in enumerate(xsDiquark):
  if xs < xs_max:
    idx = i
    break

graph_xsDiquark = TGraph(len(massesTh[idx:-1]),massesTh[idx:-1],xsDiquark[idx:-1])
graph_xsDiquark.SetLineWidth(3)
graph_xsDiquark.SetLineStyle(9)
graph_xsDiquark.SetLineColor(42)

graph_xsWprime = TGraph(len(massesTh),massesTh,xsWprime)
graph_xsWprime.SetLineWidth(3)
graph_xsWprime.SetLineStyle(7)
graph_xsWprime.SetLineColor(46)

graph_xsZprime = TGraph(len(massesTh),massesTh,xsZprime)
graph_xsZprime.SetLineWidth(3)
graph_xsZprime.SetLineStyle(5)
graph_xsZprime.SetLineColor(38)

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("qq resonance mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma #times #it{B} #times #it{A} [pb]")
graph_exp_2sigma.GetYaxis().SetTitleOffset(1.1)
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-03,1e+02)
#graph_exp_2sigma.GetXaxis().SetNdivisions(1005)

graph_exp_1sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_1sigma)
graph_exp_1sigma.SetFillColor(kGreen+1)

graph_exp = TGraph(len(masses),masses,xs_exp_limits)
#graph_exp.SetMarkerStyle(24)
graph_exp.SetLineWidth(3)
graph_exp.SetLineStyle(2)
graph_exp.SetLineColor(4)

graph_obs = TGraph(len(masses),masses,xs_obs_limits)
graph_obs.SetMarkerStyle(20)
graph_obs.SetLineWidth(3)
#graph_obs.SetLineStyle(1)
graph_obs.SetLineColor(1)


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")
graph_xsAxi.Draw("L")
graph_xsDiquark.Draw("L")
graph_xsWprime.Draw("L")
graph_xsZprime.Draw("L")

legend = TLegend(.59,.48,.94,.68)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.SetMargin(0.20)
legend.SetHeader('95% CL upper limits')
legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected","lp")
legend.AddEntry(graph_exp_1sigma,"#pm 1#sigma","F")
legend.AddEntry(graph_exp_2sigma,"#pm 2#sigma","F")
legend.Draw()

legendTh = TLegend(.59,.72,.94,.88)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.035)
legendTh.SetMargin(0.20)
legendTh.AddEntry(graph_xsAxi,"Axigluon/coloron","l")
legendTh.AddEntry(graph_xsDiquark,"Scalar diquark","l")
legendTh.AddEntry(graph_xsWprime,"W'","l")
legendTh.AddEntry(graph_xsZprime,"Z'","l")
legendTh.Draw()

#l1 = TLatex()
#l1.SetTextAlign(12)
#l1.SetTextFont(42)
#l1.SetNDC()
#l1.SetTextSize(0.04)
#l1.SetTextSize(0.04)
#l1.DrawLatex(0.18,0.40, "CMS Preliminary")
#l1.DrawLatex(0.18,0.32, "#intLdt = 1 fb^{-1}")
#l1.DrawLatex(0.19,0.27, "#sqrt{s} = 13 TeV")

#draw the lumi text on the canvas
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "2.4 fb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.15
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SaveAs('xs_limit_DijetLimitCode_qq' + ('_NoSyst' if not syst else '') + '_Run2_13TeV_DATA_2445_invpb.eps')
