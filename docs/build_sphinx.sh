#!/bin/bash

export LC_ALL=C

sphinx-build -b html ./source ./build

make html

