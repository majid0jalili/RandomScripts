import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

apps = ['perl', 'gcc', 'mcf', 'cactus', 'lbm', 'omnetpp', 'wrf', 'xalan', 'x264', 'cam', 'imigk', 'fotonik', 'roms', 'bc', 'bfs', 'cc', 'pr', 'Amean']


codes_1= np.array([0.9591815936,	0.9855846668, 0.945410654, 0.9974829988, 0.9797085687, 0.9502157138, 0.9735377594, 0.9397850527, 0.9343382838, 0.9575567288, 0.4303425926, 0.9846680051, 0.9805726833, 0.6079908997, 0.960455092, 0.9768821743, 0.6190661215, 0.8931046817])
codes_2= np.array([0.0003847540757, 0.001820619141, 0.01869269205, 2.13E-07, 0.003557351322, 0.002978632833, 0.0004692548026, 0.02952725165, 0.001722580066, 0.002998061283, 0.007820060433, 0.0007038957617, 0.000167255318, 8.54E-05, 0.01570021058, 0.006630101685, 0.005390179602, 0.005802852601])
codes_3= np.array([0.00882745126, 0.00169325788, 0.0119664423, 0.0002537641325, 0.002526774085, 0.004063934915, 0.01008389148, 0.01862476271, 0.008191622381, 0.01594210674, 0.006072924847, 0.006072779207, 0.003926350262, 0.002078535416, 0.007002227185, 0.004490009973, 0.01160952799, 0.00726037428])
codes_4= np.array([0.0004899386432, 9.81E-06, 0.0007057104772, 0, 4.64E-05, 0.0101712024, 0, 0.0001521761214, 0.00143580363, 0.001977003646, 0.5190449624, 0, 1.57E-05, 0.3338700992, 0.0005420929243, 0.0002459297635, 0.2438686065, 0.06544561109])
codes_5= np.array([0.00245472597, 0.0003678243302, 0.0001186954149, 1.45E-05, 0.0005575182168, 0.001536368874, 0.000806465458, 0.0001244639677, 0.007933667698, 0.0008135295624, 0.005070838945, 0.0001668876371, 0.0004890453455, 0.002776945049, 0.0009677741912, 0.0009809912553, 0.006438449517, 0.001859924814])
codes_6= np.array([0.00101259019, 0.0003804839422, 0.005339590049, 1.46E-06, 0.00183397893, 0.003298846034, 0.000115936033, 5.56E-05, 0.002217353481, 0.001104459049, 0.006829819518, 6.49E-05, 0.0001923604214, 0.01305871382, 0.002394806889, 0.002168118506, 0.01496111608, 0.00323706308])
codes_7= np.array([0.02764894625, 0.0101433402, 0.01776621574, 0.00224703318, 0.0117694218, 0.02773530109, 0.01498669279, 0.01173071451, 0.04416068896, 0.01960811091, 0.02481880131, 0.008323572299, 0.01463663724, 0.04013942563, 0.01293779626, 0.008602674473, 0.09866599879, 0.02328949244])
extra = np.array([0.06759266, 0.022728247, 0.052957159, 0.004763822, 0.028457115, 0.064369752, 0.040979679, 0.042266234, 0.106664021, 0.057076317, 0.067611186, 0.022951671, 0.033881031, 0.098193046, 0.036240401, 0.024844469, 0.230341091, 0.058936347])
													
																	
																	
cc1 = np.array([0.009425994538, 0.1262974025, 0.3424238136, 8.44E-05, 0.1753129819, 0.05983078324, 0.01773299587, 0.4903641531, 0.02623416147, 0.07063690425, 0.01372765513, 0.0459102527, 0.008609285625, 0.000217803902, 0.397022306, 0.2867960761, 0.0141499087, 0.1226339358])
cc2 = np.array([0.2162615359, 0.1174622782, 0.2192083835, 0.1008200268, 0.1245241921, 0.08163087651, 0.3810671835, 0.3093046417, 0.1247549235, 0.3756097561, 0.0106606616, 0.396085391, 0.2021046103, 0.005302263173, 0.177070261, 0.1942228495, 0.03047649117, 0.1803862544])
cc3 = np.array([0.01200288513, 0.0006803673018, 0.01292762285, 0, 0.0022860347, 0.2043054784, 0, 0.002527215055, 0.02186667837, 0.0465799075, 0.9111528361, 0, 0.0008064966902, 0.8516896649, 0.01370828638, 0.01063810097, 0.6401861853, 0.1606681035])
cc4 = np.array([0.06013772186, 0.02551618647, 0.00217433297, 0.005772904288, 0.02747554913, 0.03086051831, 0.03047608368, 0.002066994546, 0.1208263834, 0.01916745669, 0.008901558864, 0.01088492645, 0.02517307738, 0.007083879042, 0.02447278902, 0.0424344084, 0.01690175088, 0.02707803067])
cc5 = np.array([0.02480719557, 0.02639439107, 0.09781377573, 0.0005804565555, 0.09038194033, 0.06626279674, 0.004381187326, 0.0009229995759, 0.03376935007, 0.0260220058, 0.01198934558, 0.004230370985, 0.009901543523, 0.03331227213, 0.06055917206, 0.09378557216, 0.03927483726, 0.0367287772])
cc6 = np.array([0.677364667, 0.7036493744, 0.3254520713, 0.8927421823, 0.5800193019, 0.5571095468, 0.5663425496, 0.1948139961, 0.6725485032, 0.4619839697, 0.04356794274, 0.5428890589, 0.7534049864, 0.1023941169, 0.3271671856, 0.3721229929, 0.2590108267, 0.4725048984])


f = plt.figure()
f.set_size_inches(12.6, 3.0)
# plot details
bar_width = 0.35
epsilon = .015
line_width = 1
opacity = 0.7
pos_bar_positions = np.arange(len(codes_1))
neg_bar_positions = pos_bar_positions + bar_width

ex= plt.plot(pos_bar_positions, extra, 
						  color="black",
						  linewidth=1.2,
						  marker='o',
						  label='Extra Accesses')
l0=plt.legend(framealpha=1, frameon=True, bbox_to_anchor=(0.80,1.0));						  

a1 = plt.bar(pos_bar_positions, codes_1, bar_width,
						  color='#2980B9',
						  edgecolor='black',
						  label='001')
						  
a2 = plt.bar(pos_bar_positions, codes_2, bar_width,
						  bottom=codes_1,
						  color='#037bfc',
						  edgecolor='black',
						  label='010')
						  
a3 = plt.bar(pos_bar_positions, codes_3, bar_width,
						   bottom=codes_1+codes_2,
						   color='#03adfc',
						   edgecolor='black',
						   label='011')
						   
a4 = plt.bar(pos_bar_positions, codes_4, bar_width,
						   bottom=codes_1+codes_2+codes_3,
						   color='#03dffc',
						   edgecolor='black',
						   label='100')
a5 = plt.bar(pos_bar_positions, codes_5, bar_width,
						   bottom=codes_1+codes_2+codes_3+codes_4,
						   color='#03fcdf',
						   edgecolor='black',
						   label='101')
a6 = plt.bar(pos_bar_positions, codes_6, bar_width,
						   bottom=codes_1+codes_2+codes_3+codes_4+codes_5,
						   color='green',
						   edgecolor='black',
						   label='101')							   

a7 = plt.bar(pos_bar_positions, codes_7, bar_width,
						   bottom=codes_1+codes_2+codes_3+codes_4+codes_5+codes_6,
						   color='white',
						   edgecolor='black',
						   label='111')
						   
l1 = plt.legend(handles=[a1,a2,a3,a4,a5,a6,a7], bbox_to_anchor=(0.20, 1), fancybox=True, ncol=8)
plt.gca().add_artist(l0)		

###########################
a1 = plt.bar(neg_bar_positions, cc1, bar_width,
						  color='#037bfc',
						  edgecolor='black',
						  label='L2')
						  



a2 = plt.bar(neg_bar_positions, cc2, bar_width,
						  bottom=cc1,
						  color='#03adfc',
						  edgecolor='black',
						  label='Useful')
						  
a3 = plt.bar(neg_bar_positions, cc3, bar_width,
						   bottom=cc1+cc2,
						   color='#03dffc',
						   edgecolor='black',
						   label='Useless')
						   
a4 = plt.bar(neg_bar_positions, cc4, bar_width,
						   bottom=cc1+cc2+cc3,
						   color='#03fcdf',
						   edgecolor='black',
						   label='Harmful')
a5 = plt.bar(neg_bar_positions, cc5, bar_width,
						   bottom=cc1+cc2+cc3+cc4,
						   color='green',
						   edgecolor='black',
						   label='Harmful')
a6 = plt.bar(neg_bar_positions, cc6, bar_width,
						   bottom=cc1+cc2+cc3+cc4+cc5,
						   color='white',
						   edgecolor='black',
						   label='Harmful')	

 
# hpv_neg_mut_bar = plt.bar(neg_bar_positions, useful2, bar_width,
						  # color='#B4CDCD',
						  # edgecolor='black',  
						  # label='Useful')
						  
# hpv_neg_cna_bar = plt.bar(neg_bar_positions, useless2, bar_width,
					      # bottom=useful2,
						  # color="#F4F6F7",
						  # edgecolor='black',   
						  # label='Useless')
# hpv_neg_cna_bar2 = plt.bar(neg_bar_positions, harmful2, bar_width,
					      # bottom=useful2+useless2,
						  # color="#F4F6F7",
						  # edgecolor='black',    
						  # label='Harmful')						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar, hpv_neg_cna_bar2], bbox_to_anchor=(0.65, 1), fancybox=True, ncol=3)  
						  

# plt.gca().add_artist(l0)						  
# plt.gca().add_artist(l1)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar,hpv_neg_cna_bar1], loc='best')
# first_legend =plt.legend(handles=[hpv_pos_cna_bar,hpv_pos_both_bar], loc=1)


plt.xticks(neg_bar_positions, apps, rotation=45, fontname="Times New Roman", color='black', size=15)
plt.ylabel('Fraction', fontname="Times New Roman", color='black', size=15)
plt.yticks(np.arange(0, 1.2, step=0.2), fontname="Times New Roman", color='black', fontsize=14)

f.tight_layout()
f.savefig("codes_single.pdf", bbox_inches='tight')
plt.show()

