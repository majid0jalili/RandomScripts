import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
plt.style.use('ggplot')


# set width of bar
barWidth = 0.35

#base=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1,1,1.0,1.0,1.0,1.0,1.0,1,1,1.0,1.0,1.0,1.0,1.0]
#prefetcher=[1.036016765,1.849904092,1.018072366,1.007112157,1.160727167,2.353522691,1.016536832,1.304150667,1.031399545,1.221602313,1.7147165,1.00203833,1,1,1.014834933,1.076266917,1.000956786,1.922187626,2.091199104,1,1,1.580140389,1.759607857,1.177522122,1.252384917,1.379548915]
#LP=[1.060940759,1.956707507,1.019709528,1.049969221,1.30027939,2.625571594,1.088490989,1.332231401,1.102476962,1.244780097,1.798966469,1.015532947,1.015612996,1.03966584,1.019786535,1.083583813,1.000770686,2.108731084,2.379139879,1.04554217,1.08076118,1.805617571,2.022084341,1.26657408,1.324165046,1.496106969]

base=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
prefetcher=[1.036790404, 1.863180014, 1.020038626, 1.113574946, 1.125183107, 2.334078366, 1.022985824, 1.310762975, 1.041336847, 1.13217058, 1.710027225, 1.003791902, 1, 1, 1.015533497, 1.084611713, 1.000219491, 2.139408089, 2.231771129, 1, 1, 1.774574065, 1.766195121, 1.212186338, 1.270436783]
LP=[1.057805065, 2.02035552, 1.023364526, 1.159751863, 1.146170695, 2.652823215, 1.115333946, 1.347062251, 1.083226721, 1.212991842, 1.801523452, 1.004974099, 1.00662261, 1.053899917, 1.020172308, 1.093682457, 1.000078765, 2.402264537, 2.601114721, 1.052296395, 1.100906764, 2.074830951, 2.081062597, 1.356807097, 1.351692678]

apps = ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnetpp', 'wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'imigk', 'leela', 'nab', 'exchg', 'fotonik', 'roms', 'xz', 'bc', 'bfs', 'cc', 'pr', 'Gmean']
 
# Set position of bar on X axis
r1 = np.arange(len(prefetcher))
r2 = [x + barWidth for x in r1]
r3 = [x-.175  for x in r2]

f = plt.figure()
f.set_size_inches(12.6, 3.0)
# Make the plot
l3=plt.bar(r3, LP, color='white', alpha=.5, width=2*barWidth, edgecolor='black', label='Base+Prefetcher+Zero Miss')
l1=plt.bar(r1, base, color='#729ece', width=barWidth, edgecolor='black', label='Base')
l2=plt.bar(r2, prefetcher, color='#f59542', width=barWidth, edgecolor='black', label='Base+Prefetcher')


plt.legend(handles=[l1,l2,l3], loc='upper center', fancybox=True, ncol=4)

# Add xticks on the middle of the group bars
#plt.xlabel('group', fontweight='bold', fontname="Times New Roman", color='black', fontsize=14)
plt.ylabel('Norm. IPC', fontweight='bold', fontname="Times New Roman", color='black', fontsize=14)
# plt.xticks([r + barWidth/2 for r in range(len(prefetcher))], ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnetpp', ' wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'imigk', 'leela', 'nab', 'exchg2', 'fotonik', 'roms', 'xz', 'gapbs.bc', 'gapbs.bfs', 'gapbs.cc', 'gapbs.pr', 'Average'], fontname="Times New Roman", color='black', fontsize=14, rotation=25)

plt.xticks(r1, apps, rotation=45, fontname="Times New Roman", color='black', size=15)

plt.yticks(np.arange(0, 3, step=0.5), fontname="Times New Roman", color='black', fontsize=14) 



# Create legend & Show graphic
f.tight_layout()
#plt.legend(loc='upper center', ncol=1)	
plt.axis([None, None, 0.8, 3])
f.savefig("opp.pdf", bbox_inches='tight')
plt.show()


