#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:18:33 2020

@author: massimopinto
"""

# Low energy x-ray qualities

CCRI10 =  {'name':'CCRI-10',
            'kV': 10,
            'physics':'spekcalc',
            'dk': 0.2, #energy bin width,
            'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                        'Air': 500
                        }
            }

CCRI25 =  {'name':'CCRI-25',
            'kV': 25,
            'physics':'casim',
            'dk': 0.2, #energy bin width,
            'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                        'Al':0.43,
                        'Air': 500
                        }
            }

CCRI30 =  {'name':'CCRI-30',
            'kV': 30,
            'physics':'casim',
            'dk': 0.2, #energy bin width,
            'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                        'Al':0.26,
                        'Air': 500
                        }
            }

CCRI50a =  {'name':'CCRI-50a',
            'kV': 50,
            'physics':'casim',
            'dk': 0.5, #energy bin width,
            'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                        'Al':4.72,
                        'Air': 500
                        }
            }

CCRI50b =  {'name':'CCRI-50b',
            'kV': 50,
            'physics':'casim',
            'dk': 0.5, #energy bin width,
            'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                        'Al':1.07,
                        'Air': 500
                        }
            }

CCRI_LE = [CCRI10, CCRI25, CCRI30, CCRI50a, CCRI50b]

N10 =  {'name':'N-10',
         'kV': 10,
         'physics':'spekcalc',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Al': 0.3, 
                     'Air': 500
                     }
         }

N15 =  {'name':'N-15',
         'kV': 15,
         'physics':'spekcalc',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Al': 0.91, 
                     'Air': 500
                     }
         }

N20 =  {'name':'N-20',
         'kV': 20,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Al': 1.9, 
                     'Air': 500
                     }
         }

N25 =  {'name':'N-25',
         'kV': 25,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Al': 2.0, 
                     'Air': 500
                     }
         }

N30 =  {'name':'N-30',
         'kV': 30,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Al': 5.5, 
                     'Air': 500
                     }
         }

N40 =  {'name':'N-40',
         'kV': 40,
         'physics':'casim',
         'dk': 0.5, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Al': 4.0,
                     'Cu': 0.21,
                     'Air': 500
                     }
         }

ISO_N_LE = [N10, N15, N20, N25, N30, N40]

H20 =  {'name':'H-20',
         'kV': 20,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Al': 0.15, 
                     'Air': 500
                     }
         }

H30 =  {'name':'H-30',
         'kV': 30,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Al': 0.52, 
                     'Air': 500
                     }
         }

ISO_H_LE = [H20, H30]


 

WMo23 =  {'name':'WMo-23',
         'kV': 23,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Mo': 0.06, 
                     'Air': 500
                     }
         }

WMo28 =  {'name':'WMo-28',
         'kV': 28,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Mo': 0.06, 
                     'Air': 500
                     }
         }

WMo30 =  {'name':'WMo-30',
         'kV': 30,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Mo': 0.06, 
                     'Air': 500
                     }
         }

WMo35 =  {'name':'WMo-35',
         'kV': 35,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Mo': 0.06, 
                     'Air': 500
                     }
         }

WMo = [WMo23, WMo28, WMo30, WMo35]

WMoA23 =  {'name':'WMoA-23',
         'kV': 23,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Mo': 0.06, 
                     'Al':2.0,
                     'Air': 500
                     }
         }

WMoA28 =  {'name':'WMoA-28',
         'kV': 28,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Mo': 0.06, 
                     'Al': 2.0,
                     'Air': 500
                     }
         }

WMoA30 =  {'name':'WMoA-30',
         'kV': 30,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Mo': 0.06,
                     'Al': 2.0,
                     'Air': 500
                     }
         }

WMoA35 =  {'name':'WMoA-35',
         'kV': 35,
         'physics':'casim',
         'dk': 0.2, #energy bin width,
         'filters': {'Be': 1, # Fixed filtration of the L.E. x-ray tube
                     'Mo': 0.06, 
                     'Al': 2.0,
                     'Air': 500
                     }
         }

WMoA = [WMoA23, WMoA28, WMoA30, WMoA35]

LEQuals = CCRI_LE+WMo+WMoA+ISO_H_LE+ISO_N_LE
