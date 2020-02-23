import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')


# make up some fake data
#pos_mut_pcts = np.array([20, 10, 5, 7.5, 30, 10])
#pos_cna_pcts = np.array([10, 0, 0, 7.5, 10, 0])
#pos_both_pcts = np.array([10, 0, 0, 0, 0, 0])
#neg_mut_pcts = np.array([10, 30, 5, 0, 10, 25])
#neg_cna_pcts = np.array([5, 0, 7.5, 0, 0, 10])
#neg_cna_pcts2 = np.array([12.5, 10.5, 17.5, 0, 0, 10])







L2 = np.array([0.976490549,0.9830824546,0.8758024266,0.9996940954,0.9363676589,0.9049649497,0.9895713974,0.8807953256,0.9533507064,0.9672041074,0.1367484283,0.9725238122,0.9882572349,0.1296039306,0.9198500711,0.9578196053,0.2192537711])
Useful = np.array([0.01817195099,0.01202977122,0.09733063486,0.0001717813725,0.0577629572,0.07300369949,0.006522204318,0.08902593073,0.03354746262,0.02174896275,0.8534551885,0.02126293377,0.00816714097,0.8075551195,0.0615446404,0.03799986208,0.6572446349])
useless= np.array([0.004739342146,0.00435964458,0.0192717009,0.000133451314,0.004319974894,0.01435346852,0.003751226876,0.006758852362,0.01178960362,0.008949706411,0.007295568468,0.005201012769,0.003411183647,0.01442401332,0.01498100032,0.002741516508,0.008426128688])
harmful= np.array([0.0005981578171,0.0005281295971,0.007595237679,6.72E-07,0.001549409014,0.007677882333,0.0001551713997,0.02341989136,0.00131222737,0.002097223438,0.002500814687,0.001012241224,0.0001644404673,0.04841693659,0.003624288212,0.001439016134,0.1150754653])



useful2= np.array([0.7729636488,0.711082544,0.7836758172,0.5615521389,0.9077609938,0.7681765751,0.6254149834,0.7468325478,0.7191419211,0.6631611774,0.9886517633,0.7738676833,0.6955040752,0.9278018914,0.7678689328,0.9008892005,0.8418159583])
useless2= np.array([0.2015930595,0.257699594,0.1551697056,0.4362514381,0.06788961114,0.1510334184,0.3597056118,0.05669955807,0.2527284489,0.2728910757,0.008451265781,0.1892916446,0.2904923689,0.01657178131,0.1869122097,0.06499504156,0.01079240395])
harmful2= np.array([0.02544329165,0.03121786198,0.06115447724,0.002196422968,0.02434939508,0.08079000648,0.01487940482,0.1964678941,0.02812963002,0.06394774684,0.002896970905,0.0368406721,0.0140035559,0.05562632725,0.04521885746,0.0341157579,0.1473916377])

apps = ['perl', 'gcc', 'mcf', 'cactus', 'lbm', 'omnetpp', 'wrf', 'xalan', 'x264', 'cam', 'imigk', 'fotonik', 'roms', 'bc', 'bfs', 'cc', 'pr']

f = plt.figure()
f.set_size_inches(12.6, 3.0)
# plot details
bar_width = 0.35
epsilon = .015
line_width = 1
opacity = 0.7
pos_bar_positions = np.arange(len(L2))
neg_bar_positions = pos_bar_positions + bar_width

# make bar plots
# hpv_neg_cna_bar1 = plt.plot(neg_bar_positions, neg_cna_pcts2, 
						  # color="black",
						  # linewidth=1.2,
						  # marker='o',
						  # label='Coverage')

						  
# plt.legend(handles=[hpv_neg_cna_bar1], loc=3)	 
# l0=plt.legend(framealpha=1, frameon=True, bbox_to_anchor=(1,1.25));

hpv_pos_mut_bar = plt.bar(pos_bar_positions, L2, bar_width,
						  color='#2980B9',
						  edgecolor='black',
						  label='L2')
						  



hpv_pos_cna_bar = plt.bar(pos_bar_positions, Useful, bar_width,
						  bottom=L2,
						  color='#85C1E9',
						  edgecolor='black',
						  label='Useful')
						  
hpv_pos_both_bar = plt.bar(pos_bar_positions, useless, bar_width,
						   bottom=L2+Useful,
						   color='#0394fc',
						   edgecolor='black',
						   label='Useless')
						   
hpv_pos_both_bar2 = plt.bar(pos_bar_positions, harmful, bar_width,
						   bottom=L2+Useful+useless,
						   color='#03d3fc',
						   edgecolor='black',
						   label='Harmful')
						   

l1 = plt.legend(handles=[hpv_pos_mut_bar,hpv_pos_cna_bar,hpv_pos_both_bar,hpv_pos_both_bar2], bbox_to_anchor=(0.25, 1), fancybox=True, ncol=4)


 
hpv_neg_mut_bar = plt.bar(neg_bar_positions, useful2, bar_width,
						  color='#85C1E9',
						  edgecolor='black',  
						  label='Useful')
						  
hpv_neg_cna_bar = plt.bar(neg_bar_positions, useless2, bar_width,
					      bottom=useful2,
						  color="#0394fc",
						  edgecolor='black',   
						  label='Useless')
hpv_neg_cna_bar2 = plt.bar(neg_bar_positions, harmful2, bar_width,
					      bottom=useful2+useless2,
						  color="#03d3fc",
						  edgecolor='black',    
						  label='Harmful')						  
#plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar, hpv_neg_cna_bar2], bbox_to_anchor=(0.65, 1), fancybox=True, ncol=3)  
						  

# plt.gca().add_artist(l0)						  
plt.gca().add_artist(l1)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar,hpv_neg_cna_bar1], loc='best')
# first_legend =plt.legend(handles=[hpv_pos_cna_bar,hpv_pos_both_bar], loc=1)


plt.xticks(neg_bar_positions, apps, rotation=45, fontname="Times New Roman", color='black', size=15)
plt.ylabel('Fraction', fontname="Times New Roman", color='black', size=15)
plt.yticks(np.arange(0, 1.2, step=0.2), fontname="Times New Roman", color='black', fontsize=14)

f.tight_layout()
f.savefig("Acc.pdf", bbox_inches='tight')
plt.show()

