#!/usr/bin/env bash

if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi

cd ../LL_chunks
rm -rf *

cd ../LL-sentences
rm -rf *

cd ../nonLL-sentences
rm -rf *

cd ../nonLL_chunks
rm -rf *

cd ..

echo "emptied chunks"