import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as font_manager

plt.style.use('ggplot')





L2Miss= np.array([0,0.97,0.90,0.8,0,0.94,0.79,0.98,0.96,0,0.87,0.89,0,0.0,0.00,0.00,0,0.87,0.94,0.95,0.9])
OffMiss= np.array([0,0.92,0.90,0.76,0,0.9,0.79,0.23,0.98,0,0.81,0.86,0,0.0,0.00,0.00,0,0.79,0.91,0.17,0.72])

MetaMiss= np.array([0,0.000194347,0.000882485,1.32737E-05,0,0.015,0.000596986,0.000502967,8.59475E-05,0,0.00155701,0.00105857,0,9.87531E-05,0.00650688,0.000274243,0,8.50042E-06,7.35815E-05,0.05725638,0.00062937026])



apps = ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnetpp', ' wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'immagic', 'leela', 'nab', 'exchg2', 'fotonik', 'roms', 'xz', 'g-mean' ]

f = plt.figure()
f.set_size_inches(12.6, 3.0)
# plot details
bar_width = 0.35
epsilon = .015
line_width = 1
opacity = 0.7
first = np.arange(len(L2Miss))

sec=first + bar_width
third=sec + bar_width
fourth=third + bar_width
fifth=fourth + bar_width



# make bar plots


						  
# plt.legend(handles=[hpv_neg_cna_bar1], loc=3)	 
# l0=plt.legend(framealpha=1, frameon=True, bbox_to_anchor=(1,1.25));

p1 = plt.bar(first, L2Miss, bar_width,
						  color='#7aa6c2',
						  edgecolor='black',
						  label='Useful')
						  



p2 = plt.bar(sec, OffMiss, bar_width,
						  color='#346888',
						  edgecolor='black',
						  label='Useless')




e1 = plt.plot(first, MetaMiss, 
						  color="red",
						  linewidth=0,
						  marker='s',
						  label='MissRatio')




# l1 = plt.legend(handles=[hpv_pos_mut_bar,hpv_pos_cna_bar,hpv_pos_both_bar], bbox_to_anchor=(0.35, 1.25), title="Prefetcher Accurcy", fancybox=True, ncol=3)


 
						  
#plt.legend(loc='upper center', ncol=1)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar], bbox_to_anchor=(0.75, 1.25), title="Speedup", ncol=2)						  
						  

# plt.gca().add_artist(l0)						  
# plt.gca().add_artist(l1)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar,hpv_neg_cna_bar1], loc='best')
# first_legend =plt.legend(handles=[hpv_pos_cna_bar,hpv_pos_both_bar], loc=1)


plt.xticks(first, apps, rotation=45, fontname="Times New Roman", color='black', size=15)
plt.ylabel('Ratio', fontname="Times New Roman", color='black', size=15)
plt.yticks(np.arange(0, 1.5, step=0.25), fontname="Times New Roman", color='black', fontsize=14)

font = font_manager.FontProperties(family='Times New Roman',
                                   style='normal', size=15)

plt.legend([p1, p2, e1[0]], ["L2 Miss Prediction Accuracy", "Offchip Miss Prediction Accuracy", "Metadata Miss Ratio"], bbox_to_anchor=(0, 1), loc='lower left', ncol=3, prop=font)





#plt.legend(handles=[hpv_pos_cna_bar,hpv_neg_cna_bar1,hpv_pos_mut_bar], loc='upper center', ncol=4)
f.tight_layout()
f.savefig("prediction_acc.pdf", bbox_inches='tight')
# plt.show()

