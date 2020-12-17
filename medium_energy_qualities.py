#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:32:48 2020

@author: massimopinto
"""

# Medium energy x-ray spectra

N60 =   {'name':'N-60',
         'kV': 60,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':4.02,
                     'Cu':0.61,
                     'Air': 1000
                     }
         }

N80 =   {'name':'N-80',
         'kV': 80,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':3.99,
                     'Cu':2.05,
                     'Air': 1000
                     }
         }

N100 =  {'name':'N-100',
         'kV': 100,
         'physics':'casim',
         'dk': 1, #energy bin width,
         'filters': {'Al':4.04,
                     'Cu':5.08,
                     'Air': 1000
                     }
         }

N120 =  {'name':'N-120',
         'kV': 120,
         'physics':'casim',
         'dk': 1, #energy bin width,
         'filters': {'Al':3.99,
                     'Cu':5.01,
                     'Sn':1.0,
                     'Air': 1000
                     }
         }

N150 =  {'name':'N-150',
         'kV': 150,
         'physics':'casim',
         'dk': 1, #energy bin width,
         'filters': {'Al':4.0,
                     'Sn':2.5,
                     'Air': 1000
                     }
         }
 
N200 =  {'name':'N-200', # 4,18 Al+2,02 Cu+3,0Sn+1,0Pb
         'kV': 200,
         'physics':'casim',
         'dk': 1, #energy bin width,
         'filters': {'Al':4.18,
                     'Cu':2.02,
                     'Sn':3.0,
                     'Pb':1.0,
                     'Air': 1000
                     }
         }

N250 =  {'name':'N-250', #4,17 Al + 2,0 Sn + 3,0 Pb
         'kV': 250,
         'physics':'casim',
         'dk': 1, #energy bin width,
         'filters': {'Al':4.17,
                     'Sn':2.0,
                     'Pb':3.0,
                     'Air': 1000
                     }
         }

N300 =  {'name':'N-300', #3,74 Al + 3,1 Sn + 5,0 Pb
         'kV': 300,
         'physics':'casim',
         'dk': 1, #energy bin width,
         'filters': {'Al':3.74,
                     'Sn':3.1,
                     'Pb':5.0,
                     'Air': 1000
                     }
         }

ISO_N_ME = [N60, N80, N100, N120, N150, N200, N250, N300]

RQR2 =  {'name':'RQR2',
         'kV': 40,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':2.7,
                     'Air': 1000
                     }
         }

RQR3 =  {'name':'RQR3',
         'kV': 50,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':2.59,
                     'Air': 1000
                     }
         }

RQR4 =  {'name':'RQR4',
         'kV': 60,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':2.88,
                     'Air': 1000
                     }
         }

RQR5 =  {'name':'RQR5',
         'kV': 70,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':3.19,
                     'Air': 1000
                     }
         }

RQR6 =  {'name':'RQR6',
         'kV': 80,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':3.39,
                     'Air': 1000
                     }
         }

RQR7 =  {'name':'RQR7',
         'kV': 90,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':3.57,
                     'Air': 1000
                     }
         }

RQR8 =  {'name':'RQR8',
         'kV': 100,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':3.70,
                     'Air': 1000
                     }
         }

RQR9 =  {'name':'RQR9',
         'kV': 120,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.13,
                     'Air': 1000
                     }
         }

RQR10 =  {'name':'RQR10',
         'kV': 150,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.72,
                     'Air': 1000
                     }
         }

RQR = [RQR2, RQR3, RQR4, RQR5, RQR6, RQR7, RQR8, RQR9, RQR10]

RQA2 =  {'name':'RQA2', #2,70 Al + 4 Al
         'kV': 40,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':6.70,
                     'Air': 1000
                     }
         }

RQA2 =  {'name':'RQA2', #2,70 Al + 4 Al
         'kV': 40,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':6.70,
                     'Air': 1000
                     }
         }

RQA3 =  {'name':'RQA3', #2,59 Al + 10 Al
         'kV': 50,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':12.59,
                     'Air': 1000
                     }
         }

RQA5 =  {'name':'RQA5', #3,19 Al + 21 Al
         'kV': 70,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':24.19,
                     'Air': 1000
                     }
         }

RQA7 =  {'name':'RQA7', #3,57 Al + 30 Al
         'kV': 90,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':33.57,
                     'Air': 1000
                     }
         }

RQA9 =  {'name':'RQA9', #4,13 Al + 40 Al
         'kV': 120,
         'physics':'casim',
         'dk': 1, #energy bin width,
         'filters': {'Al':44.13,
                     'Air': 1000
                     }
         }

RQA10 =  {'name':'RQA10', #4,72  Al + 45 Al
         'kV': 150,
         'physics':'casim',
         'dk': 1, #energy bin width,
         'filters': {'Al':49.72,
                     'Air': 1000
                     }
         }

RQA = [RQA2, RQA3, RQA5, RQA7, RQA9, RQA10]

W60 =  {'name':'W-60', #3,97 Al + 0,27 Cu
         'kV': 60,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':3.97,
                     'Cu':0.27,
                     'Air': 1000
                     }
         }

W80 =  {'name':'W-80', #4,18 Al + 0,49 Cu
         'kV': 80,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Al':4.18,
                     'Cu':0.49,
                     'Air': 1000
                     }
         }

W110 =  {'name':'W-110', #4,18 Al + 2,04 Cu
         'kV': 110,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.18,
                     'Cu':2.04,
                     'Air': 1000
                     }
         }

W150 =  {'name':'W-150', #4,16 Al + 1,0 Sn
         'kV': 150,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.16,
                     'Sn':1.0,
                     'Air': 1000
                     }
         }

W200 =  {'name':'W-200', #4,19 Al + 2,0 Sn
         'kV': 200,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.19,
                     'Sn':2.0,
                     'Air': 1000
                     }
         }

W250 =  {'name':'W-250', #4,18 Al + 4,0 Sn
         'kV': 250,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.18,
                     'Sn':4.0,
                     'Air': 1000
                     }
         }  

W300 =  {'name':'W-300', #4,18 Al + 6,5 Sn
         'kV': 250,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.18,
                     'Sn':6.5,
                     'Air': 1000
                     }
         } 

ISO_W_ME = [W60, W80, W110, W150, W200, W250, W300]

H100 =  {'name':'H-100', #4,27 Al + 0,15 Cu
         'kV': 100,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.27,
                     'Cu':0.15,
                     'Air': 1000
                     }
         }

H200 =  {'name':'H-200', #4,26 Al + 1,11 Cu
         'kV': 200,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.26,
                     'Cu':1.11,
                     'Air': 1000
                     }
         }

H250 =  {'name':'H-250', #4,18 Al + 1,63 Cu
         'kV': 250,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.18,
                     'Cu':1.63,
                     'Air': 1000
                     }
         }

H300 =  {'name':'H-300', #4,18 Al + 2,21 Cu
         'kV': 300,
         'physics':'casim',
         'dk': 1.0, #energy bin width,
         'filters': {'Al':4.18,
                     'Cu':2.21,
                     'Air': 1000
                     }
         }

ISO_H_ME = [H100, H200, H250, H300]

CCRI_100 =  {'name':'CCRI-100', #3,82Al
             'kV': 100,
             'physics':'casim',
             'dk': 0.5, #energy bin width,
             'filters': {'Al':3.82,
                         'Air': 1000
                         }
             }

CCRI_135 =  {'name':'CCRI-135', #2,47Al + 0,21Cu
             'kV': 135,
             'physics':'casim',
             'dk': 1.0, #energy bin width,
             'filters': {'Al':2.47,
                         'Cu':0.21,
                         'Air': 1000
                         }
             }

CCRI_180 =  {'name':'CCRI-180', #3,16Al + 0,49Cu
             'kV': 180,
             'physics':'casim',
             'dk': 1.0, #energy bin width,
             'filters': {'Al':3.16,
                         'Cu':0.49,
                         'Air': 1000
                         }
             }

CCRI_250 =  {'name':'CCRI-250', #3,26Al + 1,68Cu
             'kV': 250,
             'physics':'casim',
             'dk': 1.0, #energy bin width,
             'filters': {'Al':3.26,
                         'Cu':1.68,
                         'Air': 1000
                         }
             }

CCRI_ME = [CCRI_100, CCRI_135, CCRI_180, CCRI_250]

MEQuals = CCRI_ME+RQR+RQA+ISO_H_ME+ISO_W_ME+ISO_N_ME
