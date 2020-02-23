import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
plt.style.use('ggplot')


# set width of bar
barWidth = 0.35
 
# set height of bar
bars1 = [0.3937402143, 0.2559698306, 0.3727187151, 0.3736545678, 0.2479945581, 0.247167252, 0.3619413923, 0.338167874, 0.3748280326, 0.2509141733, 0.321709661]
bars2 = [0.4438250722, 0.4799191291 , 0.375937699, 0.4253877432, 0.484359048, 0.4817454827, 0.4834968665, 0.5080803117, 0.4256431927, 0.2619447115, 0.4370339257]

prefetcher=[1.036016765,1.849904092,1.018072366,1.007112157,1.160727167,2.353522691,1.016536832,1.304150667,1.031399545,1.221602313,1.7147165,1.00203833,1,1,1.014834933,1.076266917,1.000956786,1.922187626,2.091199104,1,1,1.580140389,1.759607857,1.177522122,1.252384917,1.379548915]
LP=[1.060940759,1.956707507,1.019709528,1.049969221,1.30027939,2.625571594,1.088490989,1.332231401,1.102476962,1.244780097,1.798966469,1.015532947,1.015612996,1.03966584,1.019786535,1.083583813,1.000770686,2.108731084,2.379139879,1.04554217,1.08076118,1.805617571,2.022084341,1.26657408,1.324165046,1.496106969]
apps = ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnetpp', ' wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'imigk', 'leela', 'nab', 'exchg2', 'fotonik', 'roms', 'xz', 'gapbs.bc', 'gapbs.bfs', 'gapbs.cc', 'gapbs.pr', 'Gmean', 'Hi-Gmean']
 
# Set position of bar on X axis
r1 = np.arange(len(prefetcher))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
f = plt.figure()
f.set_size_inches(12.6, 3.0)
# Make the plot
plt.bar(r1, prefetcher, color='#729ece', width=barWidth, edgecolor='black', label='Base+Prefetcher')
plt.bar(r2, LP, color='#fbad6a', width=barWidth, edgecolor='black', label='Base+Prefetcher+Zero Miss')

 
# Add xticks on the middle of the group bars
#plt.xlabel('group', fontweight='bold', fontname="Times New Roman", color='black', fontsize=14)
plt.ylabel('Fraction', fontweight='bold', fontname="Times New Roman", color='black', fontsize=14)
# plt.xticks([r + barWidth/2 for r in range(len(prefetcher))], ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnetpp', ' wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'imigk', 'leela', 'nab', 'exchg2', 'fotonik', 'roms', 'xz', 'gapbs.bc', 'gapbs.bfs', 'gapbs.cc', 'gapbs.pr', 'Average'], fontname="Times New Roman", color='black', fontsize=14, rotation=25)

plt.xticks(r1, apps, rotation=45, fontname="Times New Roman", color='black', size=15)

plt.yticks(np.arange(0, 2, step=0.5), fontname="Times New Roman", color='black', fontsize=14) 
# Create legend & Show graphic
f.tight_layout()
plt.legend(loc='upper center', ncol=4)	
f.savefig("Opportunity.pdf", bbox_inches='tight')
# plt.show()


