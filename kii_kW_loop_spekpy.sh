#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Tue Nov  3 14:18:43 2020
#@author: massimopinto
#Bash script for running spectral_interpolation on multiple beam spectras


for file in ./spekpy_spectra/*.txt
#subfile=${file}
#echo $subfile
do
    [ -f "$file" ] || continue
    python3 ./spectral_interpolation.py ./k_w-k_ii_data_set_ICRU90.csv "$file" mids >> kii_kW_spekpy.csv
done