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

mass_min = 1300
mass_max = 7000

########################################################
## Uncomment this part if running the limit code


### for running the limit code
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #cmd = "./stats " + str(int(mass)) + " gg | tee stats_" + str(int(mass)) + "_gg.log"
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

  #log_file = open("stats_" + str(int(mass)) + "_gg.log",'r')
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

masses = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])
xs_obs_limits = array('d', [22.3337, 10.786, 17.3995, 12.9119, 3.97864, 2.74638, 2.07942, 1.38697, 1.22781, 1.45198, 1.59933, 1.36466, 1.33414, 1.73327, 2.28521, 2.13213, 1.41946, 1.08788, 1.2452, 1.3944, 1.34101, 1.12676, 0.862794, 0.677736, 0.511847, 0.393714, 0.322891, 0.302415, 0.285506, 0.268335, 0.260514, 0.255765, 0.244383, 0.232223, 0.222849, 0.207364, 0.204008, 0.207945, 0.216137, 0.219047, 0.219261, 0.21814, 0.215519, 0.21177, 0.205814, 0.199433, 0.19427, 0.190228, 0.191367, 0.192586, 0.193879, 0.19674, 0.200283, 0.203947, 0.20829, 0.213258, 0.219107, 0.22589])
xs_exp_limits = array('d', [9.49284, 7.96023, 6.67129, 5.71589, 4.66765, 4.27515, 3.75304, 3.25249, 2.79173, 2.52338, 2.15927, 1.81585, 1.6515, 1.5108, 1.25607, 1.07202, 0.961419, 0.91267, 0.794071, 0.709098, 0.620592, 0.577106, 0.527946, 0.491945, 0.436141, 0.443247, 0.411217, 0.399545, 0.364645, 0.335363, 0.309874, 0.280883, 0.250506, 0.240625, 0.241478, 0.222516, 0.208779, 0.205653, 0.194101, 0.190014, 0.176588, 0.173191, 0.168672, 0.161794, 0.160532, 0.162141, 0.15666, 0.155047, 0.157784, 0.16172, 0.162313, 0.168112, 0.172665, 0.177607, 0.179842, 0.186106, 0.191509, 0.200528])

masses_exp = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0])
xs_exp_limits_1sigma = array('d', [4.76442, 4.39228, 3.59221, 2.8544, 2.62343, 2.54919, 2.27815, 1.9444, 1.77968, 1.49152, 1.30905, 1.20694, 1.03561, 0.936949, 0.848813, 0.701311, 0.66971, 0.602138, 0.511506, 0.480566, 0.44262, 0.419077, 0.382696, 0.367209, 0.33113, 0.317088, 0.287389, 0.27174, 0.24873, 0.233627, 0.229198, 0.209412, 0.201492, 0.196182, 0.189638, 0.176921, 0.165461, 0.159644, 0.151966, 0.147312, 0.141204, 0.139499, 0.137651, 0.135089, 0.135305, 0.136885, 0.131666, 0.131923, 0.134089, 0.135833, 0.140709, 0.143938, 0.146797, 0.149316, 0.154462, 0.159797, 0.166477, 0.171942, 0.23428, 0.225432, 0.226673, 0.216996, 0.218618, 0.211128, 0.211372, 0.207111, 0.213359, 0.20644, 0.200785, 0.208384, 0.214082, 0.212218, 0.216448, 0.224532, 0.228928, 0.231939, 0.259954, 0.262858, 0.277215, 0.293801, 0.318571, 0.338729, 0.348573, 0.362995, 0.401202, 0.432102, 0.48029, 0.51282, 0.58769, 0.629553, 0.686667, 0.646428, 0.762268, 0.794119, 0.861865, 0.986781, 1.07827, 1.19752, 1.52058, 1.55712, 1.74151, 1.93987, 2.33816, 2.70248, 2.94788, 3.40851, 4.02756, 4.48621, 5.74213, 6.44445, 7.47799, 9.36003, 12.4126, 13.6299, 16.2566, 23.4348])
xs_exp_limits_2sigma = array('d', [2.99408, 2.77288, 1.98593, 1.81743, 1.69713, 1.86303, 1.5468, 1.218, 1.21612, 0.98463, 0.940073, 0.882869, 0.800144, 0.661763, 0.535441, 0.520289, 0.485528, 0.407404, 0.39753, 0.389809, 0.362199, 0.340807, 0.306356, 0.288861, 0.262697, 0.251361, 0.235026, 0.229308, 0.211027, 0.198294, 0.185006, 0.169548, 0.16611, 0.154282, 0.153562, 0.14416, 0.137385, 0.135304, 0.131088, 0.128626, 0.128995, 0.12889, 0.127584, 0.126099, 0.125848, 0.126907, 0.125441, 0.123928, 0.127965, 0.127485, 0.128886, 0.131466, 0.134062, 0.136861, 0.141197, 0.143907, 0.150335, 0.153104, 0.329816, 0.304218, 0.318639, 0.296938, 0.296493, 0.264359, 0.264574, 0.260251, 0.287935, 0.271045, 0.26534, 0.282562, 0.286728, 0.30189, 0.29445, 0.283242, 0.289942, 0.334064, 0.345962, 0.359753, 0.389368, 0.412824, 0.450631, 0.471773, 0.491971, 0.532805, 0.557198, 0.597274, 0.666282, 0.690058, 0.795974, 0.894411, 0.963743, 0.996432, 1.06454, 1.15826, 1.21833, 1.36663, 1.55276, 1.7947, 2.03184, 2.26311, 2.67428, 2.91707, 3.60262, 4.24821, 4.34847, 5.10885, 6.06775, 7.03547, 9.17048, 9.69622, 11.6668, 15.4484, 17.8886, 22.8381, 26.2498, 39.2693])

if syst:
  masses = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0])                   
  xs_obs_limits = array('d', [54.1968, 25.7766, 23.8135, 20.1944, 9.76688, 6.15776, 4.42915, 3.0816, 2.60814, 2.56899, 2.46285, 2.29042, 2.22468, 2.35236, 2.55077, 2.532, 2.13867, 1.77697, 1.60557, 1.55888, 1.48962, 1.3785, 1.22234, 1.08345, 0.91135, 0.684575, 0.535158, 0.438331, 0.370818, 0.323687, 0.297412, 0.278558, 0.266534, 0.251505, 0.235409, 0.221672, 0.216499, 0.217276, 0.217524, 0.216956, 0.215982, 0.21772, 0.216478, 0.213417, 0.213675, 0.207917, 0.210197, 0.202443, 0.20232, 0.202019, 0.203688, 0.205038, 0.206911, 0.209445, 0.212497, 0.218607, 0.224202, 0.229246])                                                                                               
  xs_exp_limits = array('d', [28.1625, 18.166, 15.2484, 11.5414, 10.5614, 8.3932, 7.09015, 5.84451, 5.18569, 4.336505, 3.637985, 3.19093, 2.677445, 2.29711, 1.882415, 1.61154, 1.529295, 1.32494, 1.1069, 0.974663, 0.872959, 0.7570055, 0.717379, 0.6329035, 0.5850115, 0.54332, 0.523087, 0.454718, 0.4139265, 0.3780525, 0.3616705, 0.337585, 0.3143135, 0.292594, 0.273277, 0.2666565, 0.242272, 0.2319665, 0.2084985, 0.203577, 0.20065, 0.190455, 0.185494, 0.1803555, 0.171907, 0.169828, 0.166008, 0.163576, 0.1611855, 0.1659605, 0.1710605, 0.172834, 0.175707, 0.1794665, 0.186162, 0.1930865, 0.201742, 0.205289])                                                                   

  masses_exp = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7000.0, 6900.0, 6800.0, 6700.0, 6600.0, 6500.0, 6400.0, 6300.0, 6200.0, 6100.0, 6000.0, 5900.0, 5800.0, 5700.0, 5600.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0])
  xs_exp_limits_1sigma = array('d', [12.87743, 10.5324682, 8.39720062, 6.94276996, 6.78577798, 5.50499241, 5.01305531, 4.17555926, 3.55019178, 3.12202113, 2.69472044, 2.31867168, 1.9469875, 1.60991838, 1.33546187, 1.12981708, 1.0456133, 0.897995434, 0.780732524, 0.681511487, 0.603336003, 0.544006679, 0.497685888, 0.457190034, 0.420489826, 0.400571358, 0.37344657, 0.332134409, 0.309208101, 0.28835184, 0.266096036, 0.247754148, 0.225672733, 0.213776724, 0.201884136, 0.194573436, 0.181933207, 0.170811566, 0.154875242, 0.151610792, 0.147145302, 0.146586866, 0.140806734, 0.140222075, 0.136676758, 0.135547818, 0.135353672, 0.13335312, 0.134864945, 0.138589803, 0.143157859, 0.14449682, 0.148541476, 0.153003617, 0.158275078, 0.163360855, 0.168415804, 0.17381941, 0.25250438, 0.252390889, 0.241060712, 0.242271426, 0.233843921, 0.229776136, 0.234006676, 0.230028554, 0.224709181, 0.218747162, 0.219038318, 0.22531119, 0.23260483, 0.236248608, 0.242762745, 0.255165813, 0.267460362, 0.277758708, 0.288096204, 0.299940097, 0.321428093, 0.340450038, 0.385516871, 0.390454842, 0.423855068, 0.445521102, 0.476666006, 0.51328903, 0.574037064, 0.617323386, 0.653336226, 0.764289782, 0.787609893, 0.865129131, 0.881399944, 0.974513366, 1.17291291, 1.20634369, 1.40371177, 1.65934388, 2.01443031, 2.28403361, 2.38305504, 2.83288602, 3.43204628, 3.92803323, 4.57680168, 5.24467679, 5.9417049, 7.42040302, 7.96918902, 10.2005972, 12.4610726, 15.2488038, 18.4540028, 23.0643368, 32.201671, 53.3028776])
  xs_exp_limits_2sigma = array('d', [7.47089118, 6.59726594, 5.14186908, 4.38159468, 4.3126344, 3.78669339, 3.75094272, 3.1131959, 2.70040002, 2.41876224, 1.92550425, 1.68766902, 1.46890337, 1.19508242, 0.954360923, 0.806322928, 0.728574443, 0.671932599, 0.602581716, 0.535855946, 0.482380889, 0.419740519, 0.410549544, 0.370504724, 0.334958831, 0.305912661, 0.2963383, 0.251361496, 0.240716509, 0.224760014, 0.213541799, 0.200665726, 0.179007685, 0.176952724, 0.162038744, 0.158345391, 0.146655106, 0.140073793, 0.129810357, 0.129129992, 0.131024682, 0.126770326, 0.12530212, 0.126835853, 0.122340568, 0.121262542, 0.121978374, 0.120454962, 0.122148749, 0.126002695, 0.129341281, 0.131924882, 0.13510982, 0.139245274, 0.14531511, 0.148913883, 0.152853368, 0.157790978, 0.342783505, 0.362816502, 0.343812221, 0.313596384, 0.315637768, 0.317484294, 0.325647938, 0.316278644, 0.318212172, 0.310699237, 0.313769778, 0.318411696, 0.316947744, 0.322445489, 0.308493021, 0.325127264, 0.341105924, 0.352525194, 0.386022479, 0.415282032, 0.443197314, 0.519016838, 0.545061343, 0.587658354, 0.56774896, 0.568081263, 0.63419708, 0.779391989, 0.787591922, 0.860308762, 0.890413095, 1.000744486, 1.1397882, 1.16963836, 1.1783744, 1.3463265, 1.54708187, 1.79938354, 2.02794018, 2.2609263, 2.80818922, 3.3331376, 3.59692284, 4.03845838, 4.67239046, 5.43747024, 7.07792604, 7.58058436, 8.40390983, 9.99093552, 11.1917638, 13.3948534, 18.3660136, 21.41914, 25.4329444, 34.3959822, 48.3117372, 78.5231894])

##
########################################################

massesS8 = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0])
xsS8 = array('d', [5.46E+02,3.12E+02,1.85E+02,1.12E+02,7.19E+01,4.59E+01,3.02E+01,2.01E+01,1.37E+01,9.46E+00,6.55E+00,4.64E+00,3.27E+00,2.36E+00,1.70E+00,1.24E+00,9.11E-01,6.69E-01,4.97E-01,3.71E-01,2.78E-01,2.07E-01,1.55E-01,1.19E-01,9.26E-02,7.08E-02,5.43E-02,4.15E-02,3.22E-02,2.50E-02,1.92E-02,1.51E-02,1.19E-02,9.25E-03,7.35E-03,5.86E-03,4.53E-03,3.66E-03,2.91E-03,2.33E-03,1.86E-03,1.45E-03,1.12E-03,8.75E-04,6.90E-04,5.55E-04,4.47E-04,3.63E-04,2.92E-04,2.37E-04,1.97E-04])

xs_max = 6e+01
idx = 0

for i, xs in enumerate(xsS8):
  if xs < xs_max:
    idx = i
    break

graph_xsS8 = TGraph(len(massesS8[idx:-1]),massesS8[idx:-1],xsS8[idx:-1])
graph_xsS8.SetLineWidth(3)
graph_xsS8.SetLineStyle(8)
graph_xsS8.SetLineColor(6)

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("gg resonance mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma #times #it{B} #times #it{A} [pb]")
graph_exp_2sigma.GetYaxis().SetTitleOffset(1.1)
graph_exp_2sigma.GetYaxis().SetRangeUser(5e-02,2e+02)
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
graph_xsS8.Draw("L")

legend = TLegend(.55,.50,.90,.70)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.SetHeader('95% CL upper limits')
legend.AddEntry(graph_obs,"Observed","lp")
legend.AddEntry(graph_exp,"Expected","lp")
legend.AddEntry(graph_exp_1sigma,"#pm 1#sigma","F")
legend.AddEntry(graph_exp_2sigma,"#pm 2#sigma","F")
legend.Draw()

legendTh = TLegend(.55,.80,.90,.84)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.035)
legendTh.AddEntry(graph_xsS8,"S8","l")
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
CMS_lumi.lumi_sqrtS = "42 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.15
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SaveAs('xs_limit_DijetLimitCode_gg' + ('_NoSyst' if not syst else '') + '_Run2_13TeV_DATA_42_invpb.eps')
