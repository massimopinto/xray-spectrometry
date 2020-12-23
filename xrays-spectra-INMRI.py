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
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as pyplt
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

def scarto_rel(a,b):
    return np.abs(a-b) / np.min([a,b])

AllQualities = le.LEQuals+me.MEQuals

for idx in range(len(AllQualities)): # Considerato 'code smell' in Python, ma chest'è.
    # Poi se vuoi abbellirlo puoi provare con un metodo basato sulla list comprehension
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
    AllQualities[idx]['HVL1_Al_spekpy'] = s.get_hvl1() # Get the 1st HVL in mm Al
    AllQualities[idx]['HVL2_Al_spekpy'] = s.get_hvl2() # Get the 2nd HVL in mm Al
    AllQualities[idx]['HVL1_Cu_spekpy'] = s.get_hvl1(matl='Cu') # Get the 1st HVL in mm Cu
    AllQualities[idx]['HVL2_Cu_spekpy'] = s.get_hvl2(matl='Cu') # Get the 2nd HVL in mm Cu
    AllQualities[idx]['mean_E'] = s.get_emean()
    AllQualities[idx]['HVL_deviation'] = np.nan
    if ('HVL_Cu_DB' in  AllQualities[idx].keys()):
        AllQualities[idx]['HVL_deviation'] = scarto_rel(AllQualities[idx]['HVL_Cu_DB'],
                                                        AllQualities[idx]['HVL1_Cu_spekpy'])
    if ('HVL_Al_DB' in  AllQualities[idx].keys()):
        AllQualities[idx]['HVL_deviation'] = scarto_rel(AllQualities[idx]['HVL_Al_DB'],
                                                        AllQualities[idx]['HVL1_Al_spekpy'])

'''
Adesso ci sarebbe da fare un grafico a faccette con matplotlib
Dovresti recuperarlo da dove lo hai usato di più, i run calorimetrici.
'''

dfAllQualities = pd.concat([pd.Series(AllQualities[idx]) for idx in range(len(AllQualities))], axis=1)
dfAllQualities = dfAllQualities.transpose()
dfAllQualities.drop(columns=['spekpy_spectrum', 'spectrum_df'], inplace=True)
#print(dfAllQualities)

dfAllQualities.to_csv(os.path.join(cwd,'spekpy_qualities_summary.csv'), index=False, sep=',')

def plot_spectra(dict_list,cols=5,maxrows=4):
    '''
    Function for plotting spectra in factes. 
    Parameters
    ----------
    dict_list : list of dictionary elements
        Each dictionary (list element) can contain several keys, such as: 
        dict_keys(['name', 'kV', 'physics', 'dk', 'filters', 
                   'spekpy_spectrum', 'spectrum_df', 'HVL1_Al_spekpy', 
                   'HVL2_Al_spekpy', 'HVL1_Cu_spekpy', 'HVL2_Cu_spekpy', 
                   'mean_E'])   
        which will be used in the plot facet. Each plot is based on the content
        of the key 'spectrum_df', which is a dataframe with two columns vectors.
        Here, the 'keV' column is the x-axis (energy values) and the 'freq' column 
        is the y-axis, i.e. the spectrum data.
    Returns
    -------
    A list of tuples containing (figures and their axes)
    '''
    numplots = len(dict_list) # How many plots you need?
    cols = cols         # number of columns
    maxrows = maxrows
    numfigs = int(np.ceil(numplots/(maxrows*cols))) # How many figures?
    subfigure = 1 + np.arange(numfigs)
    ''' separate the dictionary list in 'numfigs' chunks'''
    run_dic_chunks = [dict_list[i:i + maxrows*cols] \
                  for i in range(0, len(dict_list), maxrows*cols)]
    numsubplots = []
    props = dict(boxstyle='round', facecolor='white', edgecolor='black', alpha=0.9)
    for chunk in run_dic_chunks:
        numsubplots.append(len(chunk))
    figtitle = "ENEA-INMRI x-ray spectra simulated using spekpy"
    output_figures = []
    for chunk, subf, subplots in zip(run_dic_chunks, subfigure, numsubplots):
        fig, axes = pyplt.subplots(nrows=maxrows, ncols=cols)
        fig.subplots_adjust(hspace=0.35, wspace=0.25)
        fig.set_size_inches(20, 10)
        fig.suptitle(figtitle, fontsize=15)
        for run_dic, ax in zip(chunk, axes.flatten()):
            ax.text(0.05, 0.89, str(run_dic['name']) + r", $\bar{E}$:"+ \
                str(run_dic['mean_E'])[:4]+ " keV, HVL dev:" + \
                    str(run_dic['HVL_deviation'])[:6],
                transform=ax.transAxes, horizontalalignment='left', 
                bbox=props)
            # ax.text(0.01, 0.8, "<E>: "+ str(run_dic['mean_E'])[:4]+ " keV", 
            #         transform=ax.transAxes, horizontalalignment='left')
            ax.plot(run_dic['spectrum_df']['keV'], run_dic['spectrum_df']['freq'],
                    color='black', linewidth=2.0)
            if ax == axes.flatten()[0]:
                ax.set_ylabel("frequency")  # y axis label on the first axes only
            #if cols*maxrows > subplots:
            #    for ax in axes.flatten()[subplots:]:
            #        ax.remove()  # ax.set_visible(False)
            #axes.flatten()[subplots-1].set_xlabel("Energy [keV]")  # x axis label \
            output_figures.append((fig, axes))
        fig.savefig(cwd+"/"+"test_spectra_facets_" + str(subf)+".png")
    return output_figures

# figure, axes = plot_spectra(AllQualities[:10])
figures = plot_spectra(AllQualities)