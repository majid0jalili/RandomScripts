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

pos_mut_pcts = np.array([0.1759778562, 0.3486885833, 0.3436441801, 0.1327248083, 0.4955622329, 0.2789470787, 0.06499832272, 0.2845639875, 0.1848230122, 0.2376237775, 0.3382103286, 0.3284681852, 0.04131168279, 0.01199229215, 0.1744148415, 0.4446901656, 0.3990983824, 0.3056216721, 0.2994863727, 0.03244945106, 0.01866018509, 0.2056222614, 0.2002242466, 0.03621460456, 0.1561624113, 0.137619096])
pos_cna_pcts = np.array([0.4550356508, 0.2106561193, 0.1848689183, 0.4544638674, 0.1474138803, 0.3163029827, 0.3287940825, 0.2121154405, 0.6791499452, 0.2346896515, 0.2449744825, 0.6079129432, 0.29537892, 0.2310552924, 0.4415369438, 0.2953833648, 0.5136568549, 0.2461440121, 0.1995083476, 0.2967537754, 0.3241269221, 0.2264147541, 0.2251760107, 0.3295664464, 0.2972035459, 0.2842565528])
pos_both_pcts = np.array([0.368986493, 0.4406552974, 0.4714869016, 0.4128113243, 0.3570238868, 0.4047499386, 0.6062075948, 0.503320572, 0.1360270426, 0.527686571, 0.4168151889, 0.06361887167, 0.6633093972, 0.7569524155, 0.3840482148, 0.2599264696, 0.08724476266, 0.4482343158, 0.5010052797, 0.6707967736, 0.6572128928, 0.5679629845, 0.5745997428, 0.6342189491, 0.3972121692, 0.4625899416])
neg_mut_pcts = np.array([0.03601676478, 0.8499040921, 0.01807236576, 0.007112156621, 0.160727167, 1.353522691, 0.01653683249, 0.3041506672, 0.03139954542, 0.221602313, 0.7147165004, 0.002038329855, 0.002038329855, 0.002038329855, 0.01483493281, 0.0762669166, 0.0009567858724, 0.9221876262, 1.091199104, 0.002038329855, 0.002038329855, 0.580140389, 0.7596078569, 0.1775221222, 0.05015492239, 0.106375651])
neg_cna_pcts = np.array([0.02405752019, 0.05773456858, 0.001608100246, 0.04255441071, 0.120228273, 0.1155922161, 0.07078361977, 0.02153181711, 0.06891356234, 0.01897326436, 0.04913346799, 0.01346716705, 0.015612996, 0.03969648029, 0.004879218933, 0.006798403455, 0.0001859222215, 0.09704747613, 0.1376917075, 0.04554216981, 0.08076117983, 0.1426943981, 0.1491676019, 0.07562656891, 0.03078926755, 0.08556450586])
neg_cna_pcts2 = np.array([0.3162921329, 0.5935227361, 0.5895879292, 0.2765196704, 0.6405492185, 0.5100658265, 0.1850859421, 0.5487844337, 0.2850738006, 0.4993280674, 0.5776490857, 0.3927655714, 0.1559419356, 0.07020146176, 0.3484348325, 0.5675776475, 0.2512940391, 0.6073870245, 0.6199715748, 0.1278151422, 0.05088172453, 0.5112745519, 0.5068062536, 0.03971955203, 0.3058738126, 0.2819958222])


genes = ['PIK3CA', 'PTEN', 'CDKN2A', 'FBXW7', 'KRAS', 'TP53']
apps = ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnetpp', ' wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'imigk', 'leela', 'nab', 'exchg2', 'fotonik', 'roms', 'xz', 'gapbs.bc', 'gapbs.bfs', 'gapbs.cc', 'gapbs.pr', 'Gmean', 'Hi-Gmean']

f = plt.figure()
f.set_size_inches(12.6, 4.57)
# plot details
bar_width = 0.35
epsilon = .015
line_width = 1
opacity = 0.7
pos_bar_positions = np.arange(len(pos_mut_pcts))
neg_bar_positions = pos_bar_positions + bar_width

# make bar plots
hpv_neg_cna_bar1 = plt.plot(neg_bar_positions, neg_cna_pcts2, 
						  color="black",
						  linewidth=1.2,
						  marker='o',
						  label='Coverage')

						  
# plt.legend(handles=[hpv_neg_cna_bar1], loc=3)	 
l0=plt.legend(framealpha=1, frameon=True, bbox_to_anchor=(1,1.25));

hpv_pos_mut_bar = plt.bar(pos_bar_positions, pos_mut_pcts, bar_width,
						  color='#2980B9',
						  edgecolor='black',
						  label='Useful')
						  



hpv_pos_cna_bar = plt.bar(pos_bar_positions, pos_cna_pcts, bar_width,
						  bottom=pos_mut_pcts,
						  color='#85C1E9',
						  edgecolor='black',
						  label='Useless')
						  
hpv_pos_both_bar = plt.bar(pos_bar_positions, pos_both_pcts, bar_width,
						   bottom=pos_cna_pcts+pos_mut_pcts,
						   color='#EBF5FB',
						   edgecolor='black',
						   label='Other')

l1 = plt.legend(handles=[hpv_pos_mut_bar,hpv_pos_cna_bar,hpv_pos_both_bar], bbox_to_anchor=(0.35, 1.25), title="Prefetcher Accurcy", fancybox=True, ncol=3)


 
hpv_neg_mut_bar = plt.bar(neg_bar_positions, neg_mut_pcts, bar_width,
						  color='#B4CDCD',
						  edgecolor='black',  
						  label='Prefetcher')
						  
hpv_neg_cna_bar = plt.bar(neg_bar_positions, neg_cna_pcts, bar_width,
					      bottom=neg_mut_pcts,
						  color="#F4F6F7",
						  edgecolor='black',   
						  label='Zero Miss')
						  
plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar], bbox_to_anchor=(0.75, 1.25), title="Speedup", ncol=2)						  
						  

plt.gca().add_artist(l0)						  
plt.gca().add_artist(l1)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar,hpv_neg_cna_bar1], loc='best')
# first_legend =plt.legend(handles=[hpv_pos_cna_bar,hpv_pos_both_bar], loc=1)


plt.xticks(neg_bar_positions, apps, rotation=45, fontname="Times New Roman", color='black', size=15)
plt.ylabel('Ratio', fontname="Times New Roman", color='black', size=15)
plt.yticks(np.arange(0, 2.0, step=0.5), fontname="Times New Roman", color='black', fontsize=14)

f.tight_layout()
f.savefig("Motivation.pdf", bbox_inches='tight')
plt.show()

