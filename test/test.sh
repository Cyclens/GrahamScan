#!/bin/bash
cd `dirname $0`
#cd ..
#javac-algs4 -cp .:$CLASSPATH GrahamScan.java
#cd - >/dev/null

for F in *.txt
do
  echo $F
  ../GrahamScan.py <$F >${F}.python
#  java-algs4 -cp ..:$CLASSPATH GrahamScan <$F >${F}.golden
  diff ${F}.golden ${F}.python
done

rm -f ../*.class
rm -f *.python
