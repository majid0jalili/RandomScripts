#!/bin/bash
wd=/home/majid/LP/outputs/

declare -a prefetchers=("TaggedPrefetcher" "BOPPrefetcher" "STeMSPrefetcher" "IrregularStreamBufferPrefetcher" "DCPTPrefetcher" "SBOOEPrefetcher" "IndirectMemoryPrefetcher" "SignaturePathPrefetcher" "SignaturePathPrefetcherV2" "PIFPrefetcher" "SlimAMPMPrefetcher" "AMPMPrefetcher" "StridePrefetcher")

declare -a names=("T" "BOP" "STeMS" "ISB" "DCPT" "SBOOE" "IMP" "SPP" "SPP2" "PIF" "SMPM" "AMPM" "S")


if [ ! -d $wd/outputs/$1-out ]; then
  mkdir $wd/outputs/$1-out;
fi
if [ ! -d $wd/stats/$1-stats ]; then
  mkdir $wd/stats/$1-stats;
fi

count=0
count1=0
count2=0
count3=0
for pl1 in "${prefetchers[@]}"; do
	count2=0
	for pl2 in "${prefetchers[@]}"; do
		count3=0
		for pl3 in "${prefetchers[@]}"; do
			( echo "#!/bin/bash"
			echo "#no of cpus"
			echo "#PBS -u 'majid'"
			echo "#PBS -N P.${names[count1]}.${names[count2]}.${names[count3]}"
			echo ""
			echo "#name of queue"
			echo "#PBS -q batch"
			echo ""
			echo "#change working directory"
			echo "cd $wd"
			echo "#run the program"
			echo "/home/majid/LP/sim/metadata/build/X86/$2 --outdir=$wd/outputs/$1-out --stats-file=$wd/stats/$1-stats/${names[count1]}.${names[count2]}.${names[count3]}.txt --dump-config=$wd/outputs/$1-out/${names[count1]}.${names[count2]}.${names[count3]}.config.txt /home/majid/LP/sim/metadata/configs2/example/fs.py --disk-image=/home/majid/LP/disks/disks/linux-x86.spec.img --kernel=/home/majid/LP/disks/binaries/vmlinux --caches --l3cache --cpu-clock=4GHz --mem-type=DDR4_2400_8x8 --restore-simpoint-checkpoint --checkpoint-dir=/home/majid/LP/sim/metadata/m5out --l1d-hwp-type=$pl2 --l2-hwp-type=$pl2 --l3-hwp-type=$pl3 --cpu-type=DerivO3CPU --restore-with-cpu=X86KvmCPU -r 1 >  $wd/outputs/$1-out/${names[count1]}.${names[count2]}.${names[count3]}.txt" ) > job.sh
			#submit the job
			qsub job.sh
			#rm job.sh
			count=$(( $count + 1 ))
			count1=$(( $count1 + 1 ))
		done
		count2=$(( $count2 + 1 ))
	done
	count3=$(( $count3 + 1 ))
done


date
