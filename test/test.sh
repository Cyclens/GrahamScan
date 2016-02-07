#!/bin/bash
cd `dirname $0`
cd ..
javac-algs4 -cp .:$CLASSPATH GrahamScan.java
cd - >/dev/null

for F in *.txt
do
  echo $F:
  ../GrahamScan.py <$F >${F}.lstpy
  java-algs4 -cp ..:$CLASSPATH GrahamScan <$F >${F}.lstja
  diff ${F}.lstja ${F}.lstpy
done

rm -f ../*.class
rm -f *.lstja *.lstpy
