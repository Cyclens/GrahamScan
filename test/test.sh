#!/bin/bash
cd `dirname $0`
#cd ..
#javac-algs4 -cp .:$CLASSPATH GrahamScan.java
#cd - >/dev/null

for F in *.txt
do
  echo -n "$F:	"
  ../GrahamScan.py <$F >${F}.python
#  java-algs4 -cp ..:$CLASSPATH GrahamScan <$F >${F}.golden
  diff -q ${F}.golden ${F}.python
  [ $? -eq 0 ] && echo "PASSED"
done

rm -f ../*.class
rm -f *.python
