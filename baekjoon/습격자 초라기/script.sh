for (( ; ; ))
do
  N="$(($RANDOM% 10000 + 1))"
  W="$(($RANDOM% 10000 + 1))"
  echo 1 > input.txt
  echo $N $W>> input.txt

  r=''

  for ((i = 0; i < $N; i++))
  do
    r+="$(($RANDOM% $W + 1)) "
  done

  echo $r >> input.txt

  r=''
  for ((i = 0; i < $N; i++))
  do
    r+="$(($RANDOM% $W + 1)) "
  done
  echo $r >> input.txt

  cat input.txt | ./a.out > myanswer.txt
  cat input.txt | python3 answer.py > answer.txt

  ret=$(diff myanswer.txt answer.txt)

  if [ "$ret" != "" ]
  then
    break
  fi
done