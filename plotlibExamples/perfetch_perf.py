import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')



useful= np.array([0.1759778562,0.3486885833,0.3436441801,0.1327248083,0.4955622329,0.2789470787,0.06499832272,0.2845639875,0.1848230122,0.2376237775,0.3382103286,0.3284681852,0.04131168279,0.01199229215,0.1744148415,0.4446901656,0.3990983824,0.3056216721,0.2994863727,0.03244945106,0.01866018509,0.2056222614,0.2002242466,0.03621460456,0.2243341046])

useless= np.array([0.4550356508,0.2106561193,0.1848689183,0.4544638674,0.1474138803,0.3163029827,0.3287940825,0.2121154405,0.6791499452,0.2346896515,0.2449744825,0.6079129432,0.29537892,0.2310552924,0.4415369438,0.2953833648,0.5136568549,0.2461440121,0.1995083476,0.2967537754,0.3241269221,0.2264147541,0.2251760107,0.3295664464,0.320878317])

drop= np.array([0.368986493,0.4406552974,0.4714869016,0.4128113243,0.3570238868,0.4047499386,0.6062075948,0.503320572,0.1360270426,0.527686571,0.4168151889,0.06361887167,0.6633093972,0.7569524155,0.3840482148,0.2599264696,0.08724476266,0.4482343158,0.5010052797,0.6707967736,0.6572128928,0.5679629845,0.5745997428,0.6342189491,0.4547875784])

coverage= np.array([0.2806116723,0.5930604328,0.5753114965,0.274535852,0.6377683716,0.5096488392,0.1834503353,0.5920534279,0.2979527785,0.4321662635,0.5625496781,0.2180755396,0.158698888,0.07080971948,0.2307721713,0.5614163416,0.2650248531,0.607360319,0.6175668117,0.1184495078,0.1042621003,0.5102886307,0.503798889,0.03961624345,0.3727187151])



apps = ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnetpp', ' wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'imigk', 'leela', 'nab', 'exchg2', 'fotonik', 'roms', 'xz', 'gapbs.bc', 'gapbs.bfs', 'gapbs.cc', 'gapbs.pr', 'Average']

f = plt.figure()
f.set_size_inches(12.6, 3.0)
# plot details
bar_width = 0.35
epsilon = .015
line_width = 1
opacity = 0.7
bar_positions = np.arange(len(useful))


# make bar plots
hpv_neg_cna_bar1 = plt.plot(bar_positions, coverage, 
						  color="black",
						  linewidth=1.2,
						  marker='o',
						  label='Coverage')

						  
# plt.legend(handles=[hpv_neg_cna_bar1], loc=3)	 
# l0=plt.legend(framealpha=1, frameon=True, bbox_to_anchor=(1,1.25));

hpv_pos_mut_bar = plt.bar(bar_positions, useful, bar_width,
						  color='#2980B9',
						  edgecolor='black',
						  label='Useful')
						  



hpv_pos_cna_bar = plt.bar(bar_positions, useless, bar_width,
						  bottom=useful,
						  color='#85C1E9',
						  edgecolor='black',
						  label='Useless')
						  
hpv_pos_both_bar = plt.bar(bar_positions, drop, bar_width,
						   bottom=useful+useless,
						   color='#EBF5FB',
						   edgecolor='black',
						   label='Drop')

# l1 = plt.legend(handles=[hpv_pos_mut_bar,hpv_pos_cna_bar,hpv_pos_both_bar], bbox_to_anchor=(0.35, 1.25), title="Prefetcher Accurcy", fancybox=True, ncol=3)


 
						  
plt.legend(loc='upper center', ncol=4)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar], bbox_to_anchor=(0.75, 1.25), title="Speedup", ncol=2)						  
						  

# plt.gca().add_artist(l0)						  
# plt.gca().add_artist(l1)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar,hpv_neg_cna_bar1], loc='best')
# first_legend =plt.legend(handles=[hpv_pos_cna_bar,hpv_pos_both_bar], loc=1)


plt.xticks(bar_positions, apps, rotation=45, fontname="Times New Roman", color='black', size=15)
plt.ylabel('Ratio', fontname="Times New Roman", color='black', size=15)
plt.yticks(np.arange(0, 1.4, step=0.2), fontname="Times New Roman", color='black', fontsize=14)

f.tight_layout()
f.savefig("Motivation.pdf", bbox_inches='tight')
# plt.show()

