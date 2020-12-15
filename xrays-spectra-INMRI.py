#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:55:21 2020

@author: massimopinto
"""

import spekpy as sp
import os 
# from matplotlib import pyplot as plt
import pandas as pd
# import sys

cwd = os.getcwd()  # Get the current working directory (cwd)
dir_spec = os.path.join(cwd, 'spekpy_spectra') # for spectral outputs
# sys.path.append(cwd) # Appending the current directory for module importing 

import low_energy_qualities as le
import medium_energy_qualities as me

def gen_spectrum(inputs, angle=30, mu_data='pene'):
    '''
    This function generates a Spekpy spectrum from a dictionary of input params
    Parameters
    ----------
    spectrum_inputs : Dict of input filtrations and applied voltage, in kV
        Keys include Mo, Al, Sn, Pb, Cu, and items are expressed in thickness (mm)
        Keys should aldo include the tube voltage, in kV
        Keys should also include the anode angle.

    Returns a Spekpy spectrum object
    '''
    
    phys = 'spekcalc'
    if (('physics' in inputs) and ('kV' in inputs)):
        phys = inputs['physics']
    s = sp.Spek(kvp=inputs['kV'], 
                th=angle,
                physics=phys, 
                mu_data_source = mu_data,
                comment=inputs['name']) 
    filter_list = [(k, v) for k, v in inputs['filters'].items()] 
    s.multi_filter(filter_list)
    if 'mu_data' in inputs:
        s.set(mu_data_source = inputs['mu_data'])
    if 'dk' in inputs:
        s.set(dk=inputs['dk'])
    if 'angle' in inputs:
        s.angle= inputs['angle']
    return s

# flt = (str(WMo28['filters'][key])+str(WMo28['filters'][val]) for key,val in WMo28['filters'].items())
#(WMo28['filters'][key]+ WMo28['filters'][val] for key,val in WMo28['filters'].items())
# spek_name = WMo28['name'] + (WMo28['filters'][key]+ WMo28['filters'][val] for key,val in WMo28['filters'].items()) + '.spec'

''' Trying to create the file name via string concatenation '''

def spectrum_filename(dic):
    '''

    Parameters
    ----------
    dic : Dictionary of spectrum input data
        Creates a file name via string concatenation, using
        the dictionary as a source of information

    Returns
    -------
    String: filename
    '''
    name = ''
    for key, item in dic['filters'].items(): # zip(WMo28.keys(), WMo28.values()):
        name=name+' ' + key+str(item)
        spek_name = dic['name'] + ' ' + str(dic['kV']) + 'kV' + name + '.spec'
    return spek_name

''' Generating one spectra at a time, reading from the lists.
to avoid code smell, you could consider writing a quick function and then call 
it by using
list[:] = [fun(x) for x in list]
see for example: https://stackoverflow.com/questions/4081217/how-to-modify-list-entries-during-for-loop
'''

AllQualities = le.LEQuals+me.MEQuals

for idx in range(len(AllQualities)): # Considerato 'code smell' in Python, ma chest'è.
    fname_qual = spectrum_filename(AllQualities[idx])
    s = gen_spectrum(AllQualities[idx])
    AllQualities[idx]['spekpy_spectrum'] = s
    # s_qual.export_spectrum(file_name = os.path.join(dir_spec,fname_qual), delim=',') 
    # Sopprimo l'expoert dello spectrum perché ignora il path di esportazione e contiene lo spettro intero
    ''' 
    outputs spectrum to .spec file for later uses. Note that this includes
    information such as HVL1, HVL2, mean energy etc 
    ''' 
    kbins, spk = s.get_spectrum(edges=False) # returns mid-bin energy and freq.
    AllQualities[idx]['spectrum_df'] = pd.DataFrame({'keV': kbins, 'freq': spk}, index = None)
    AllQualities[idx]['spectrum_df'].to_csv(os.path.join(dir_spec,fname_qual+'.txt'), index=False, sep='\t')
    AllQualities[idx]['HVL1'] = s.get_hvl1() # Get the 1st HVL in mm Al
    AllQualities[idx]['HVL2'] = s.get_hvl2() # Get the 2nd HVL in mm Al
 
    
# plt.plot(karr, spkarr)
# plt.xlabel('Energy [keV]')
# plt.ylabel('Fluence per mAs per unit energy [photons/cm2/mAs/keV]')
# plt.title('ISO-IEC 61674 WMo28')
# plt.show()

# s = sp.Spek(kvp=35,th=30, physics='spekcalc') # Generate a spectrum
# s.filter('Be', 1) # Filter by 1 mm of Beryllium, our low energy x-ray tube
# s.filter('Mo', 0.06) # Filter by 60 um of Molybdenum
# #s.filter('Al', 4.72) # Filter by 1 mm of Beryllium
# s.filter('Air', 500) # Spectrum is sought at 500mm from the focus
#s.set(z=50)

# hvl1 = s.get_hvl1() # Get the 1st HVL in mm Al
# hvl2 = s.get_hvl2()

# print("HVL1: " + str(hvl1)) # Print out the HVL value (Python3 syntax)
# print("HVL2: " + str(hvl2)) # Print out the HVL value (Python3 syntax)
# A series of quick-access functions
# s.get_k()  # energy bins
# s.get_spk()
# s.get_spectrum()
# s.summarize()
# s.export_spectrum(file_name=cwd+'/WMo35 35kVp 30deg 500Air 1Be 0.06Mo-legacy.spc', 
                   # comment=None, delim=',')