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
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
gROOT.ForceStyle()

masses = array('d')
xs_obs_limits = array('d')
xs_exp_limits = array('d')
masses_exp = array('d')
xs_exp_limits_1sigma = array('d')
xs_exp_limits_1sigma_up = array('d')
xs_exp_limits_2sigma = array('d')
xs_exp_limits_2sigma_up = array('d')


#syst = True
syst = False

mass_min = 1300
mass_max = 5500

########################################################
## Uncomment this part if running the limit code


### for running the limit code
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #cmd = "./stats " + str(int(mass)) + " qg | tee stats_" + str(int(mass)) + "_qg.log"
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

## for reading the limit code log files
#for mass in range(mass_min,mass_max+100,100):

  #masses.append(float(mass))
  #masses_exp.append(float(mass))

  #log_file = open("stats_" + str(int(mass)) + "_qg.log",'r')
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

masses = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0])
xs_obs_limits = array('d', [7.25507, 17.1307, 10.8215, 4.79149, 2.7376, 1.29163, 0.949093, 1.16675, 1.19361, 0.932634, 0.881593, 0.913527, 1.12694, 1.16666, 1.02261, 1.05618, 1.07974, 1.06796, 0.929969, 0.737113, 0.54551, 0.433827, 0.320105, 0.270328, 0.252588, 0.236294, 0.226046, 0.218287, 0.214905, 0.204526, 0.190822, 0.177164, 0.176421, 0.181791, 0.183187, 0.182788, 0.181373, 0.178143, 0.174509, 0.170595, 0.166164, 0.161166, 0.156399])
xs_exp_limits = array('d', [6.903025, 5.858505, 4.598335, 3.925245, 3.37995, 2.627575, 2.31947, 1.907285, 1.676115, 1.441325, 1.262305, 1.09838, 0.926013, 0.8493165, 0.742651, 0.660089, 0.574577, 0.501617, 0.4691995, 0.4417455, 0.4036935, 0.3948925, 0.359234, 0.3366815, 0.314655, 0.2826595, 0.2526355, 0.2442, 0.221084, 0.21594, 0.204294, 0.197648, 0.1812185, 0.165491, 0.1506755, 0.146772, 0.138733, 0.1363475, 0.1325565, 0.128325, 0.1277085, 0.1259875, 0.1252705])

masses_exp = array('d', [1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5500.0, 5400.0, 5300.0, 5200.0, 5100.0, 5000.0, 4900.0, 4800.0, 4700.0, 4600.0, 4500.0, 4400.0, 4300.0, 4200.0, 4100.0, 4000.0, 3900.0, 3800.0, 3700.0, 3600.0, 3500.0, 3400.0, 3300.0, 3200.0, 3100.0, 3000.0, 2900.0, 2800.0, 2700.0, 2600.0, 2500.0, 2400.0, 2300.0, 2200.0, 2100.0, 2000.0, 1900.0, 1800.0, 1700.0, 1600.0, 1500.0, 1400.0, 1300.0])
xs_exp_limits_1sigma = array('d', [3.35775954, 2.90136993, 2.38159603, 2.14520643, 1.81700762, 1.73066237, 1.46388353, 1.26107622, 1.10410224, 0.973317333, 0.881342936, 0.725178925, 0.644533688, 0.55675179, 0.498781175, 0.444354342, 0.41651519, 0.369888053, 0.329845177, 0.301622802, 0.290397081, 0.275642888, 0.254126473, 0.231443913, 0.221499088, 0.206957106, 0.188284007, 0.185868837, 0.17160456, 0.16120597, 0.150657868, 0.149007481, 0.14092569, 0.128321407, 0.125152746, 0.123038803, 0.118098764, 0.115854441, 0.113903616, 0.112729497, 0.11154268, 0.110057252, 0.109192019, 0.15579798, 0.166343818, 0.171091546, 0.177453354, 0.178172976, 0.189248657, 0.198585802, 0.204697028, 0.212470799, 0.233071738, 0.249173547, 0.270055623, 0.277396168, 0.292994913, 0.310016554, 0.341429546, 0.38264525, 0.411933383, 0.458066552, 0.483782848, 0.548500907, 0.551564907, 0.582228184, 0.671223508, 0.68775444, 0.776057115, 0.875408877, 1.04052092, 1.20062222, 1.29976769, 1.46276272, 1.69827149, 2.0650748, 2.43092482, 2.63684191, 3.00823361, 3.67436292, 4.37605679, 5.83527676, 6.97658159, 8.23593607, 10.8022084, 13.5274651])
xs_exp_limits_2sigma = array('d', [2.13323118, 1.80359646, 1.51407151, 1.44041999, 1.21301867, 1.13863216, 1.00593497, 0.86462238, 0.782909836, 0.680613612, 0.649985242, 0.557608611, 0.467794209, 0.407232386, 0.380321435, 0.33344896, 0.308165865, 0.29236911, 0.264624112, 0.247755857, 0.242371532, 0.229040746, 0.212426213, 0.192659347, 0.186110103, 0.173696462, 0.153985172, 0.141967681, 0.129547352, 0.127046667, 0.127529838, 0.125494517, 0.120837792, 0.11594756, 0.112903019, 0.109967064, 0.107071253, 0.105884809, 0.104670335, 0.104240363, 0.103989526, 0.103445522, 0.102041188, 0.223769661, 0.223917897, 0.234698896, 0.243796986, 0.250680953, 0.251805268, 0.262063058, 0.277230447, 0.281126859, 0.297868285, 0.328367393, 0.360909882, 0.36973886, 0.394159309, 0.469558448, 0.480777275, 0.519568818, 0.569074162, 0.619577824, 0.684312211, 0.763549719, 0.800164176, 0.833997633, 0.995543327, 0.974532628, 1.03667663, 1.25818767, 1.48996875, 1.69037595, 2.11128742, 2.14770296, 2.70353634, 3.20609678, 3.25831983, 3.8620992, 4.68059034, 5.42664927, 6.79442572, 8.27380398, 9.96685704, 13.3286179, 15.7917297, 19.6166279])

if syst:
  xs_obs_limits = array('d', [35.7264, 5.97138, 1.07455, 2.46052, 3.95921, 3.08949, 1.86666, 0.870688, 0.550472, 0.432721, 0.372332, 0.302224, 0.243555, 0.266118, 0.322454, 0.327492, 0.311861, 0.271667, 0.233994, 0.201787, 0.190201, 0.192072, 0.190403, 0.167939, 0.139344, 0.105079, 0.0832827, 0.0691544, 0.0645502, 0.0680858, 0.074493, 0.0761205, 0.0725783, 0.0632614, 0.054249, 0.0477713, 0.0445409, 0.042211, 0.0399109, 0.0363099, 0.031959, 0.0265896, 0.021285, 0.0166404, 0.0129277, 0.011293, 0.00950463, 0.00844172, 0.00751178, 0.00699131, 0.00659847, 0.00652256, 0.00620023, 0.00613404, 0.00608264, 0.00598963, 0.00589662, 0.00596361, 0.00591097])
  xs_exp_limits = array('d', [7.089085, 5.242335, 3.21493, 2.72778, 2.34251, 1.63937, 1.28518, 0.987911, 0.7813015, 0.65491, 0.5756145, 0.5110295, 0.4461375, 0.3843525, 0.356416, 0.309132, 0.278282, 0.2505985, 0.2180305, 0.187398, 0.170246, 0.14912, 0.1350605, 0.1142885, 0.105468, 0.0924162, 0.07800015, 0.07171155, 0.0638171, 0.05862455, 0.05148225, 0.0468188, 0.04034695, 0.0380869, 0.0330677, 0.031396, 0.02826355, 0.02571415, 0.0239881, 0.0217299, 0.02049585, 0.0190612, 0.0193599, 0.01804035, 0.0172123, 0.01540465, 0.01439935, 0.01377615, 0.01311775, 0.0125172, 0.01203865, 0.0116187, 0.0109783, 0.0107402, 0.0103624, 0.01000241, 0.00984678, 0.009574005, 0.00936249])

  xs_exp_limits_1sigma = array('d', [1.475787, 2.28121667, 1.62221826, 1.44712876, 1.25046142, 1.0659476, 0.833184258, 0.683329284, 0.525733923, 0.432363882, 0.393331915, 0.349203604, 0.323488401, 0.266384093, 0.225381584, 0.214064621, 0.194955611, 0.176009279, 0.156452077, 0.139829429, 0.121733622, 0.107500083, 0.0934713296, 0.0850639052, 0.073209014, 0.0643419646, 0.0560379362, 0.0500111072, 0.0434308321, 0.0392157383, 0.0358489939, 0.0321889994, 0.0295787663, 0.0281872174, 0.0241569668, 0.0208832281, 0.0200457544, 0.0184376231, 0.0174237824, 0.0153528221, 0.0146750228, 0.0133292488, 0.0132628559, 0.0124341305, 0.0123931866, 0.0112655891, 0.0106176306, 0.0101285434, 0.00962712923, 0.00938782169, 0.00905120441, 0.0086901281, 0.00840633994, 0.00817896618, 0.00789970558, 0.0076612717, 0.0074377151, 0.00731195388, 0.00716275536, 0.0132954533, 0.0131397732, 0.0132449313, 0.0139606309, 0.0141531933, 0.0146698368, 0.0153355005, 0.0160682273, 0.0165752194, 0.0171987885, 0.0182410022, 0.0194290665, 0.0207834033, 0.0228360251, 0.0255130017, 0.0261183852, 0.0283722994, 0.0273770182, 0.0290304976, 0.0329198644, 0.0352275705, 0.0379568213, 0.0410684741, 0.0457409368, 0.0519738678, 0.052511922, 0.0605206047, 0.0657203696, 0.0741547883, 0.0838825388, 0.0907790893, 0.103300832, 0.114098078, 0.127069276, 0.146876564, 0.164226946, 0.179221325, 0.202066506, 0.244482388, 0.262291542, 0.310821479, 0.345648173, 0.397908236, 0.455589647, 0.509432802, 0.586673427, 0.642538463, 0.758079314, 0.857157202, 0.938698484, 1.15078953, 1.43899156, 1.82722474, 2.33452448, 3.39677932, 4.78346888, 5.32799742, 8.30672272, 23.2700615])
  xs_exp_limits_2sigma = array('d', [0.842638215, 1.15255054, 1.01746804, 0.837967102, 0.821187156, 0.647689632, 0.582928886, 0.505156588, 0.372540322, 0.283296078, 0.280998375, 0.26446637, 0.217501629, 0.205443541, 0.169562586, 0.159944981, 0.133873489, 0.128960899, 0.118297456, 0.0958120684, 0.0827766614, 0.0787873773, 0.0735437185, 0.0645873793, 0.0557573936, 0.0487376639, 0.0418173241, 0.0373622425, 0.0335287558, 0.0267765406, 0.0274841096, 0.0239469318, 0.0202732429, 0.0209149578, 0.0193169731, 0.0177564289, 0.0159197478, 0.014193742, 0.0130020566, 0.01257179, 0.0121274473, 0.0106268133, 0.0103746351, 0.0103318045, 0.00961325281, 0.00935822043, 0.00892568222, 0.00839151432, 0.00773990793, 0.00737695238, 0.00733735735, 0.00717460253, 0.00689137727, 0.00661924618, 0.00643147668, 0.00629262184, 0.00629096628, 0.00610789873, 0.00611092772, 0.0162242428, 0.0166756068, 0.0170598159, 0.0175054644, 0.0179300262, 0.018928264, 0.0199011882, 0.021466227, 0.0225018484, 0.0235630953, 0.0258159269, 0.0281147957, 0.0297847768, 0.0310824379, 0.0342298326, 0.033002971, 0.0377589743, 0.0411144966, 0.0402851534, 0.0458133571, 0.0493989163, 0.0541710797, 0.0581032981, 0.065493347, 0.0680039457, 0.0680594854, 0.0799581113, 0.0851630422, 0.101478336, 0.117207546, 0.116378856, 0.138469874, 0.149731205, 0.161184684, 0.190852512, 0.211923658, 0.252774648, 0.264444795, 0.333784232, 0.347763613, 0.413145471, 0.480990833, 0.568144834, 0.627568806, 0.744924832, 0.801314254, 0.884660589, 1.08385459, 1.18371187, 1.25040334, 1.60743286, 1.94640446, 2.49054958, 3.3073766, 4.46034542, 6.48514454, 7.70456114, 10.9901871, 31.950059])

##
########################################################


massesString = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0,9100.,9200.,9300.,9400.,9500.,9600.,9700.,9800.,9900.,10000.])
xsString = array('d', [8316.184311558545,5312.93137758767,3435.0309937336524,2304.4139502741305,1569.8115447896687,1090.9516635659693,770.901859690924,551.9206062572061,399.69535383507633,293.77957451762086,218.15126842827823,162.87634729465125,123.17685479653694,93.63530805932386,71.53697229809124,55.37491301647483,42.75271508357369,33.36378355470234,26.06619302090876,20.311817606835643,16.1180931789545,12.768644973921226,10.142660425967444,8.057990848043234,6.400465846290908,5.115134438331436,4.132099789492928,3.3193854239538734,2.6581204529344302,2.157554604919995,1.7505176068913348,1.4049155245498584,1.140055677916783,0.9253251132104159,0.7522038169131606,0.6119747371392215,0.49612321727328523,0.40492020959456737,0.33091999402250655,0.27017917021492555,0.2201693919322846,0.17830700070267996,0.14564253802358157,0.11940534430331146,0.09694948234356839,0.0793065371847468,0.06446186373361917,0.05282660618352478,
                       0.0428516302310620888,0.0348997638039910363,0.0283334766442618227,0.0231416918363592127,0.0187417921340763783,0.0153501307395115115,0.0124396534127133717,0.0100542205744949455,0.0081744954858627415,0.0066338099362915941,0.0053365711503318145,0.00430912459914657443,0.00346381039244064343,0.00278602671711227174,0.00225154342228859257,0.0018082930150063248,0.00143929440338502119,0.0011581373956044489,0.00091869589873893118,0.00073410823691329855,0.00058669382997948734,0.0004661568745858897,0.000368716655469570365,0.000293168485206959169,0.000230224535021638668,0.000182317101888465142,0.000143263359883433282,0.000112630538527214965,0.000088189175598406759,0.000068708474367442343,0.000053931726669273556,0.0000416417855733682702,0.0000326529676755488658,0.0000254365480426201587,0.0000198410151166864761,0.0000154034425617473576,0.0000119095554601641413,9.2537574320108232e-6,7.2155417437856749e-6,5.6130924422251982e-6,4.36634755605624901e-6,3.39717456406994868e-6,2.6766018046173896e-6])

massesQstar = array('d', [1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0])
xsQstar = array('d', [0.4101E+03,0.2620E+03,0.1721E+03,0.1157E+03,0.7934E+02,0.5540E+02,0.3928E+02,0.2823E+02,0.2054E+02,0.1510E+02,0.1121E+02,0.8390E+01,0.6328E+01,0.4807E+01,0.3674E+01,0.2824E+01,0.2182E+01,0.1694E+01,0.1320E+01,0.1033E+01,0.8116E+00,0.6395E+00,0.5054E+00,0.4006E+00,0.3182E+00,0.2534E+00,0.2022E+00,0.1616E+00,0.1294E+00,0.1038E+00,0.8333E-01,0.6700E-01,0.5392E-01,0.4344E-01,0.3503E-01,0.2827E-01,0.2283E-01,0.1844E-01,0.1490E-01,0.1205E-01,0.9743E-02,0.7880E-02,0.6373E-02,0.5155E-02,0.4169E-02,0.3371E-02,0.2725E-02,0.2202E-02,0.1779E-02,0.1437E-02,0.1159E-02,0.9353E-03,0.7541E-03,0.6076E-03,0.4891E-03,0.3935E-03,0.3164E-03,0.2541E-03,0.2039E-03,0.1635E-03,0.1310E-03,0.1049E-03,0.8385E-04,0.6699E-04,0.5347E-04,0.4264E-04,0.3397E-04,0.2704E-04,0.2151E-04,0.1709E-04,0.1357E-04,0.1077E-04,0.8544E-05,0.6773E-05,0.5367E-05,0.4251E-05,0.3367E-05,0.2666E-05,0.2112E-05,0.1673E-05,0.1326E-05])

graph_xsString = TGraph(len(massesString),massesString,xsString)
graph_xsString.SetLineWidth(3)
graph_xsString.SetLineStyle(8)
graph_xsString.SetLineColor(9)

graph_xsQstar = TGraph(len(massesQstar),massesQstar,xsQstar)
graph_xsQstar.SetLineWidth(3)
graph_xsQstar.SetLineStyle(2)
graph_xsQstar.SetLineColor(1)

graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
graph_exp_2sigma.SetFillColor(kYellow)
graph_exp_2sigma.GetXaxis().SetTitle("qg resonance mass [GeV]")
graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_exp_2sigma.GetYaxis().SetRangeUser(1e-02,1e+03)
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
graph_obs.SetLineWidth(2)
#graph_obs.SetLineStyle(1)
graph_obs.SetLineColor(1)


c = TCanvas("c", "",800,800)
c.cd()

graph_exp_2sigma.Draw("AF")
graph_exp_1sigma.Draw("F")
graph_exp.Draw("L")
graph_obs.Draw("LP")
graph_xsQstar.Draw("L")
graph_xsString.Draw("L")

legend = TLegend(.50,.63,.80,.78)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader('95% CL upper limits' + ('' if syst else ' (stat. only)'))
legend.AddEntry(graph_obs,"Observed (pseudo-data)","lp")
legend.AddEntry(graph_exp,"Expected","lp")
legend.AddEntry(graph_exp_1sigma,"#pm 1#sigma","F")
legend.AddEntry(graph_exp_2sigma,"#pm 2#sigma","F")
legend.Draw()

legendTh = TLegend(.50,.80,.80,.88)
legendTh.SetBorderSize(0)
legendTh.SetFillColor(0)
legendTh.SetFillStyle(0)
legendTh.SetTextFont(42)
legendTh.SetTextSize(0.03)
legendTh.AddEntry(graph_xsString,"String","l")
legendTh.AddEntry(graph_xsQstar,"Excited quark","l")
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

# draw the lumi text on the canvas
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "37 pb^{-1} (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

CMS_lumi.CMS_lumi(c, iPeriod, iPos)

gPad.RedrawAxis()

c.SetLogy()
c.SaveAs('xs_limit_DijetLimitCode_qg_exp' + ('_syst' if syst else '') + '_Run2_13TeV_DATA_37_invpb.eps')
