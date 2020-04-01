#!/bin/bash
#automate initialization of speechApp, can work from any location

# We are running from sharan/Desktop


cd ./speech-app-display
open ./index.html

echo "opened app interface on chrome..."

cd ..
ls

echo "Running speechanalyser.py..."

python3 "./stutteranalyser.py"





