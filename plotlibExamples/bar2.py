import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
plt.style.use('ggplot')


x = ['perl', 'gcc', 'bwaves', 'mcf', 'cactus', 'lbm', 'omnet', ' wrf', 'xalan', 'x264', 'cam', 'pop2', 'deep', 'imigk', 'leela', 'nab', 'exchg2', 'fotonik', 'roms', 'xz', 'g-mean']



energy = [0.2543732, 0.361310427,0.316806904,0.198033838,0.490467145,0.265366572,0.142594007,0.3460786,0.270697675,0.33893756,0.350319044,0.21,0.145315933,0.000886878,0.264319929,0.465465408,0.223181708,0.38940012,0.335108436,0.009738944,0.178872091]

x_pos = [i for i, _ in enumerate(x)]
f = plt.figure()
f.set_size_inches(6.6, 3.07)

plt.bar(x_pos, energy, color='#729ece', edgecolor='black',)
# plt.xlabel("Benchmarks", fontname="Times New Roman", color='black')
plt.ylabel("Coverage", fontname="Times New Roman", color='black', size=15)
# plt.title("Energy output from various fuel sources", fontname="Times New Roman")

plt.xticks(x_pos, x, fontname="Times New Roman", color='black', rotation=70, fontsize=16)
plt.yticks(np.arange(0, 1.2, step=0.2), fontname="Times New Roman", color='black', fontsize=14)

f.tight_layout()
f.savefig("coverage.pdf", bbox_inches='tight')
plt.show()
