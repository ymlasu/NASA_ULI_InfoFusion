#!/bin/bash

LIB_DIR=${PWD}/../lib

tar -xvf hdf5-1.8.11.tar.gz

cd hdf5-1.8.11/

./configure --prefix=${LIB_DIR}/hdf5 --enable-cxx CFLAGS='-fPIC'
make
make check
make install
