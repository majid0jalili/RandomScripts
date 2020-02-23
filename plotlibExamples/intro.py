import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as font_manager
#%matplotlib inline
plt.style.use('ggplot')


# set width of bar
barWidth = 0.35
 
# set height of bar
bars1 = [0.3937402143, 0.2559698306, 0.3727187151, 0.3736545678, 0.2479945581, 0.247167252, 0.3619413923, 0.338167874, 0.3748280326, 0.2509141733, 0.321709661]
bars2 = [0.4438250722, 0.4799191291 , 0.375937699, 0.4253877432, 0.484359048, 0.4817454827, 0.4834968665, 0.5080803117, 0.4256431927, 0.2619447115, 0.4370339257]

 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
f = plt.figure()
f.set_size_inches(6.6, 3.07)
# Make the plot
plt.bar(r1, bars1, color='#7aa6c2', width=barWidth, edgecolor='black', label='Coverage')
plt.bar(r2, bars2, color='#346888', width=barWidth, edgecolor='black', label='Accuracy')

 
# Add xticks on the middle of the group bars
#plt.xlabel('group', fontweight='bold', fontname="Times New Roman", color='black', fontsize=14)
plt.ylabel('Ratio', fontweight='bold', fontname="Times New Roman", color='black', fontsize=14)
plt.xticks([r + barWidth/2 for r in range(len(bars1))], ['AMPM', 'BOP', 'DCPTP', 'Indirect', 'ISB', 'SPP', 'SBOOE', 'SPPV2', 'SAMPM', 'STeMS', 'Average'], fontname="Times New Roman", color='black', fontsize=14, rotation=25)
plt.yticks(np.arange(0, 1.2, step=0.2), fontname="Times New Roman", color='black', fontsize=14) 
# Create legend & Show graphic
f.tight_layout()
font = font_manager.FontProperties(family='Times New Roman',
                                   style='normal', size=13)
plt.legend( prop=font)
f.savefig("Coverage_all.pdf", bbox_inches='tight')
plt.show()


