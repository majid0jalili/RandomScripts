import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
plt.style.use('ggplot')


# set width of bar
barWidth = 0.35
 
 

LP=[1.036790404, 1.863180014, 1.113574946, 1.125183107, 2.334078366, 1.022985824, 1.310762975, 1.041336847, 1.13217058, 1.710027225, 1, 2.139408089, 2.231771129, 1, 1.774574065, 1.766195121, 1.212186338, 1.392128641]
Ideal=[1.057805065, 2.02035552, 1.159751863, 1.146170695, 2.652823215, 1.115333946, 1.347062251, 1.083226721, 1.212991842, 1.801523452, 1.053899917, 2.402264537, 2.601114721, 1.100906764, 2.074830951, 2.081062597, 1.356807097, 1.512799247]
Speedup=[1.020268957, 1.084358733, 1.041467273, 1.018652598, 1.136561331, 1.09027312, 1.027693242, 1.040227016, 1.071386117, 1.053505714, 1.053899917, 1.122864099, 1.16549349, 1.100906764, 1.169199411, 1.178274457, 1.119305716, 1.086680643]

S2=[0.02026895748,0.08435873337,0.04146727297,0.01865259776,0.1365613314,0.09027311995,0.02769324168,0.04022701576,0.07138611701,0.05350571366,0.05389991742,0.1228640995,0.1654934896,0.1009067636,0.1691994106,0.1782744565,0.1193057163,0.07070892033]


apps = ['perl', 'gcc', 'mcf', 'cactus', 'lbm', 'omnetpp', 'wrf', 'xalan', 'x264', 'cam', 'imigk', 'fotonik', 'roms', 'bc', 'bfs', 'cc', 'pr', 'Gmean']
 
# Set position of bar on X axis
r1 = np.arange(len(LP))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
fig, ax1 = plt.subplots()
fig.set_size_inches(6.3, 3.0)
# Make the plot



ax1.bar(r1, LP, color='#729ece', width=barWidth, edgecolor='black', label='Prefetcher+LP')
ax1.bar(r2, Ideal, color='#fbad6a', width=barWidth, edgecolor='black', label='Prefetcher+Zero miss')
ax1.tick_params(axis='x')
ax1.set_ylabel('Norm. IPC', fontname="Times New Roman", color='black', fontsize=14)


#ax2 = ax1.twinx() 
#ex= ax2.plot(r1, S2,  color="black",  linewidth=1.2,  marker='o',  label='Speed up')



plt.ylabel('Norm. IPC', fontweight='bold', fontname="Times New Roman", color='black', fontsize=14)
plt.xticks(r1, apps, rotation=45, fontname="Times New Roman", color='black', size=15)
plt.yticks(np.arange(0.0, 4, step=0.5), fontname="Times New Roman", color='black', fontsize=14) 
# Create legend & Show graphic
fig.tight_layout()
plt.legend(loc='upper center', ncol=4)
fig.savefig("ipc_single.pdf", bbox_inches='tight')
plt.show()


