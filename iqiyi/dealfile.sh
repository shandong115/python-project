#!/bin/sh
echo "flag is $1"
flag=$1
dir=$2
start=$3
end=$4
out=$5
echo $start
echo $end

function cvtSeconds(){
#	echo time is $1
	t=$1
	hh=${t:0:2}
	mm=${t:3:2}
	ss=${t:6:2}
	let h=${hh}
	let m=${mm}
	if [ "$ss" = "09" ];then
		let s=9
	else
		let s=${ss}
	fi
#	ms=${t:9}
#	echo "hour is $h"
#	echo "minutes is $m"
#	echo "seconds is $s" 
	let tt=${h}*60*60+${m}*60+${s}
	echo $tt
#	return $tt
}

if [ $flag -eq 1 ]; then
	cd $dir
	flist=`ls`
	i=1
	for ff in $flist
	do
		if test -f $ff
		then
			time=`ffmpeg -i $ff 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//`
			echo $ff total time is $time
	#		cvtSeconds $time
	#		ss=$?
			ss=`cvtSeconds $time`
			echo $ss
			let dd=$ss-$start-$end
			echo $dd
			if [ $dd -lt 0 ]; then
				start=0
				dd=$time
			fi

			a=`ffmpeg -ss $start -t $dd -accurate_seek -i $ff -codec copy -avoid_negative_ts 1 $out/${i}_${ff} -y`
		#	mv cut.mp4 $out/$ff
			let i+=1
		fi
		if test -d $ff
		then
			echo $ff is dir
		fi
	done
	cd -
fi

if [ $flag -eq 0 ]; then
	cd $dir
	ff=$6
	time=`ffmpeg -i $ff 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//`
	echo $ff total time is $time
	ss=`cvtSeconds $time`
	echo $ss
	let dd=$ss-$start-$end
	echo $dd
	if [ $dd -lt 0 ]; then
		start=0
		dd=$time
	fi

	a=`ffmpeg -ss $start -t $dd -accurate_seek -i $ff -codec copy -avoid_negative_ts 1 $out/${ff} -y`
	cd -
fi
