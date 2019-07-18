#!/bin/bash
#automate initialization of speechApp, can work from any location

# We are running from sharan/Desktop

cd ~

cd ./speechappserver
open ./index.html

echo "opened app interface on chrome..."

cd ../speechApp

echo "Running speechanalyser.py..."

python2 "./stutteranalyser.py"





