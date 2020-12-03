#!/usr/bin/env python3
"""
# -*- coding: utf-8 -*-
Linear interpolation of k_ii*k_W over x-ray spectra
Usage:
    xxxx input_data spectral_data 
Created on Tue Nov  3 05:58:35 2020

@author: massimopinto

"""

import sys
import pandas as pd
import numpy as np
import os
cwd = os.getcwd()  # Get the current working directory (cwd)

#pd.set_option("display.precision", 4)
#pd.options.display.precision(4)

def main():

    #script = sys.argv[0]
    input_data = sys.argv[1]
    spec = sys.argv[2]
    df_input_tab = pd.read_csv(cwd+"/"+input_data, index_col='keV')
    df_spec = pd.read_csv(cwd+"/"+spec, delim_whitespace=True, index_col='keV')
    
    ''' Calculating the mean energy value of each bin '''
    E_mean = (df_spec.index[0:-1] + df_spec.index[1:] ) /2.0
    #E_mean = np.mean(df_spec.index[0:-1],df_spec.index[1:])
    
    '''Appending the last bin energy value, whose frequency is zero'''
    E_mean = E_mean.append(df_spec.index[-1:])
    #print(type(df_spec))
    #df_spec.rename(columns = {"keV" : "low_E"}, inplace=True)
    df_spec = pd.concat((df_spec, pd.Series(E_mean, index=df_spec.index)), axis = 1)
    df_spec.rename(columns={"keV": "mid_E"}, inplace=True)
    df_spec = df_spec.reset_index(drop=True).set_index(df_spec['mid_E'])
    df_spec.index.rename("idx", inplace=True)
    #df_spec.drop(df_spec['mid_E'], inplace=True)
    ''' interpolating the values listed in the last column, df_input_tab.columns[-1]
        in the middle of the energy bins of the energy spectrum'''
    f_interp = lambda xx: np.interp(xx, df_input_tab.index, df_input_tab['kii_kW'])
    # for en in (18, 23, 24, 350):
    #     print("k_ii*k_W at "+ str(en) + " keV= "+str(f_interp(en)))
    # print(df_spec.columns[-1])
    ser_kii_kW = pd.Series(f_interp(df_spec['mid_E']), index=df_spec['mid_E'], name="kii_kW")
    #print(ser_kii_kW)
    #print(df_spec)
    
    df_kii_kW = pd.concat((df_spec, ser_kii_kW), axis=1)
    #print(df_kii_kW)
    
    df_kii_kW = pd.concat((df_kii_kW, pd.Series(df_kii_kW["freq"]*df_kii_kW["kii_kW"],
                        name='partials'),
                        pd.Series(df_kii_kW["freq"]*df_kii_kW["kii_kW"]*df_kii_kW["mid_E"],
                        name = 'partials_Ka-weighted'),
                        pd.Series(df_kii_kW["freq"]*df_kii_kW["mid_E"],
                        name = 'freqXmid_E')
                        ),
                        axis=1)
    #print(df_kii_kW)
    
    mean_kii_kW = df_kii_kW["partials"].sum() / df_kii_kW["freq"].sum()
    Ka_wgt_kii_kW = df_kii_kW["partials_Ka-weighted"].sum() / df_kii_kW["freqXmid_E"].sum()
    
    #print(type(df_kii_kW["partials"].sum()))
    
    '''Rounding the result to 4 decimals and writing to screen'''
    print(spec.split()[0] + ", " + str(Ka_wgt_kii_kW.round(4)))
    #print("mean kii_kW is: " + str(mean_kii_kW))
    #print("kerma-weighted kii_kW is: " + str(Ka_wgt_kii_kW))
    #print(df_spec.index[0:-1])
    #print(df_spec.index[1:])
    
    #print(E_mean)
    
    #print(df_spec)
    #print(str(df_spec.index)+", " +str(ser_kii_kW))
if __name__ == '__main__':
    main()
   