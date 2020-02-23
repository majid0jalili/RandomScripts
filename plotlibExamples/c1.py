import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib   
import matplotlib.font_manager as font_manager
plt.style.use('ggplot')


#BasePar= np.array([1.024081613,1.021594652,1.00050935,1.018764791,1.131028788,1.038395908,1.016709636,1.00814161,1.017696637,1.01865448,1.01654178,1.010435382,1.021046688,1.000614088,1.006076894,1.000557379,1.000120055,1.001696204,1.005763988,1.011648885,1.018150763,1.023737432])
#LPSeq= np.array([1.001744722,1.049180763,0.9990211882,1.0178849,0.9999558886,1.118514578,1.064873146,1.003234274,1.117248362,1.00090002,1.035463999,1.021065957,0.9999092081,1.004252662,0.9999594766,1.00007123,1.00026012,1.080328458,1.153144846,1.0025493,1.032453257,1.0432561])
#LPPar= np.array([1.024081613,1.079523639,1.001105638,1.019845401,1.131028788,1.090066496,1.052418139,1.006841643,1.115535994,1.01865448,1.036283691,1.020946102,1.021046688,1.004880674,1.006076894,1.000557379,1.000120055,1.092389892,1.156722723,1.006988044,1.043201703,1.057117029])
#Ideal= np.array([1.027609335,1.073205477,1.002536524,1.047915568,1.153176848,1.17461688,1.097913786,1.016846383,1.143230125,1.040345187,1.059462975,1.034438359,1.029359818,1.005924345,1.006454572,1.005247312,0.9995987624,1.109849595,1.182994639,1.020140115,1.059935254,1.07928273])

BasePar= np.array([1.024081613,1.021594652,1.00050935,1.018764791,1.131028788,1.038395908,1.016709636,1.00814161,1.017696637,1.01865448,1.01654178,1.010435382,1.021046688,1.000614088,1.006076894,1.000557379,1.000120055,1.001696204,1.005763988,1.011648885,1.018150763,1.023737432])
LPSeq= np.array([1,1.049180763,0.9990211882,1.0178849,1,1.118514578,1.064873146,1.003234274,1.117248362,1,1.035463999,1.021065957,1,1.004252662,1,1.00007123,1,1.080328458,1.153144846,1.0025493,1.032312467,1.043081688])
LPPar= np.array([1.024081613,1.073523639,1.001105638,1.019845401,1.131028788,1.090066496,1.052418139,1.006841643,1.115535994,1.01865448,1.036283691,1.020946102,1.021046688,1.004880674,1.006076894,1.000557379,1.000120055,1.092389892,1.156722723,1.006988044,1.043201703,1.057117029])
Ideal= np.array([1.027609335,1.079205477,1.002536524,1.047915568,1.153176848,1.17461688,1.097913786,1.016846383,1.143230125,1.040345187,1.059462975,1.034438359,1.029359818,1.005924345,1.006454572,1.005247312,0.9995987624,1.109849595,1.182994639,1.020140115,1.059935254,1.07928273])


EnergyBasePar= np.array([2.360010751,2.58560651,2.446211931,2.660715488,2.354590481,2.628541058,2.766750945,2.409444838,3.51971264,2.437063669,2.526862695,2.416377247,2.390564041,2.452939356,2.357295812,2.359110807,2.384517891,2.956091092,2.542948086,2.448087129,2.537826623,2.585629766])
EnergyLPSeq= np.array([1,2.229860324,1.697192612,2.387080952,1,2.341635838,2.334257673,2.49452389,4.31831693,1,2.088493882,1.652114153,1,1,1,1,1,3.160660878,2.148350155,2.777969984,1.832049264,1.937789482])
EnergyLPPar= np.array([2.360010751,3.750467091,3.135823209,3.95185412,2.354590481,3.887493792,3.961400647,2.760946523,6.388282198,2.437063669,3.574564767,3.073203076,2.390564041,2.214790578,2.357295812,2.359110807,2.384517891,4.899155253,3.643875806,2.904324077,3.071421364,3.353455715])
EnergyIdeal= np.array([2.287303254,1.94172959,2.219386739,1.900713949,2.32903403,1.87102494,1.988733926,1.999064803,1.178020454,2.245570937,1.99931353,2.16364124,2.340214244,2.452939356,2.334293664,2.322033356,2.346512536,1.6099933,1.975317452,1.829941669,1.859020148,1.952176985])




apps = ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnetpp', ' wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'immagic', 'leela', 'nab', 'exchg2', 'fotonik', 'roms', 'xz', 'g-mean', 'sensetive' ]

#f = plt.figure()
f, ax1 = plt.subplots()

f.set_size_inches(12.6, 3.0)
# plot details
bar_width = 0.185
epsilon = .015
line_width = 1
opacity = 0.7
first = np.arange(len(BasePar))

sec=first + bar_width
third=sec + bar_width
fourth=third + bar_width
fifth=fourth + bar_width



# make bar plots


						  
# plt.legend(handles=[hpv_neg_cna_bar1], loc=3)	 
# l0=plt.legend(framealpha=1, frameon=True, bbox_to_anchor=(1,1.25));

p1 = ax1.bar(first, BasePar, bar_width,
						  color='#c1e7ff',
						  edgecolor='black',
						  label='Useful')
						  



p2 = ax1.bar(sec, LPSeq, bar_width,
						  color='#9dc6e0',
						  edgecolor='black',
						  label='Useless')

p3 = ax1.bar(third, LPPar, bar_width,
						  color='#7aa6c2',
						  edgecolor='black',
						  label='Useful')
						  

p4 = ax1.bar(fourth, Ideal, bar_width,
						  color='#346888',
						  edgecolor='black',
						  label='Useful')
						  


ax2 = ax1.twinx()



e1 = ax2.plot(first, EnergyBasePar, 
						  color="red",
						  linewidth=0,
						  marker='^',
						  label='Coverage')

e2 = ax2.plot(sec, EnergyLPSeq, 
						  color="red",
						  linewidth=0,
						  marker='^',
						  label='Coverage')

e3 = ax2.plot(third, EnergyLPPar, 
						  color="red",
						  linewidth=0,
						  marker='^',
						  label='Coverage')

e4 = ax2.plot(fourth, EnergyIdeal, 
						  color="red",
						  linewidth=0,
						  marker='^',
						  label='Coverage')




# l1 = plt.legend(handles=[hpv_pos_mut_bar,hpv_pos_cna_bar,hpv_pos_both_bar], bbox_to_anchor=(0.35, 1.25), title="Prefetcher Accurcy", fancybox=True, ncol=3)


 
						  
#plt.legend(loc='upper center', ncol=1)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar], bbox_to_anchor=(0.75, 1.25), title="Speedup", ncol=2)						  
						  

# plt.gca().add_artist(l0)						  
# plt.gca().add_artist(l1)						  
# plt.legend(handles=[hpv_neg_mut_bar,hpv_neg_cna_bar,hpv_neg_cna_bar1], loc='best')
# first_legend =plt.legend(handles=[hpv_pos_cna_bar,hpv_pos_both_bar], loc=1)


#plt.xticks(first, apps, rotation=45, fontname="Times New Roman", color='black', size=15)
#plt.ylabel('Ratio', fontname="Times New Roman", color='black', size=15)
#plt.yticks(np.arange(0, 7, step=1), fontname="Times New Roman", color='black', fontsize=14)
font = font_manager.FontProperties(family='Times New Roman',
                                   style='normal', size=13)

plt.legend([p1, p2, p3, p4, e1[0]], ["Base(Parallel L2)", "LP(Sequentioal L2)", 
				"LP(Parallel L2)", "Ideal(Parallel L2)", "Read Energy"], bbox_to_anchor=(0, 1), loc='lower left', ncol=5, prop=font)
ax1.set_xticks(first)
ax1.set_xticklabels(apps, rotation=45, fontname="Times New Roman", color='black', size=15)

ax1.set_ylabel("Norm. IPC", fontname="Times New Roman", color='black', size=15)
ax1.set_yticks(np.arange(0.9, 1.3, step=.1))
ax1.set_yticklabels(np.arange(0.9, 1.3, step=.1), fontname="Times New Roman", color='black', size=12)

ax1.set_ylim([0.9,1.2])


ax2.set_ylabel("Norm. Read Energy", fontname="Times New Roman", color='black', size=14)
ax2.set_yticks(np.arange(0, 7, step=1))
ax2.set_yticklabels(np.arange(0, 7, step=1), fontname="Times New Roman", color='black', size=12)


#plt.setp(ax1.get_xticklabels(), rotation=45, fontname="Times New Roman", color='black', size=10)

#ax2.tick_params(axis='y', labelcolor=color)


#plt.legend(handles=[hpv_pos_cna_bar,hpv_neg_cna_bar1,hpv_pos_mut_bar], loc='upper center', ncol=4)
f.tight_layout()
f.savefig("IPCEnergy.pdf", bbox_inches='tight')
# plt.show()

