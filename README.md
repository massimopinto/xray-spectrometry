## X-ray spectrometry at ENEA-INMRI. Generation of x-ray spectra using spekpy and more

### Introduction

This **Python 3**-based project uses the package spekpy to generate x-ray specta, while the HpGe detector is not yet fully functional. `Spekpy` can be found at [https://bitbucket.org/spekpy/spekpy_release/](https://bitbucket.org/spekpy/spekpy_release/) [1]

### Package content
You will find 

- `xrays-spectra-INMRI.py`: a python code to generate `spekpy` spectra from input data on ENEA-INMRI's experimental realisations of x-ray beams in `low_energy_qualities.py` and `medium_energy_qualities.py`. These two latter python files contain our realizations of beams according to the ISO 4037:2019 norm, the ISO 4037:1996 norm the IEC 61627 norm and the CCRI standard qualities.
- `spectral_interpolation.py`: a python code to interpolate a dataset over a spectrum that was generated either using SpekCalc of `spekpy`. It is intended that spectra must exist, either created via `spekpy` or SpekCalc.
- a couple of bash scripts `.sh` to run `spectral_interpolation.py` over all input spectra files that are stored in a directory. Just run `bash kii_kW_loop_spekpy.sh` at your shell prompt. In this example, the dataset to use for averaging is the following.
- The `k_w-k_ii_data_set_ICRU90.csv` dataset containing the kii*kW correction factors, as listed on the ICRU 90 report.


### Package development
At the begininning of developing this repository, spectra were generated one at a time using SpekCalc. This was later superseded by spekpy, which allows scripting other than expanding the physics to Molybdenum filtrations, which is needed for mammography qualities.  
This code will move towards the (re)implementation of x-ray spectrometry at ENEA-INMRI with our new HpGe spectrometer, obtained in 2019. 
To do: 
1. Monte Carlo model of the detector and calculation of the response matrix
2. deconvolution code, based on the 'stripping' technique [2].

### References
1. Bujila R, Omar A and Poludniowski G 2020 A validation of SpekPy: a software toolkit for modelling X-ray tube spectra Physica Medica: European Journal of Medical Physics 75 44–54
2. Plagnard J 2017 Mesure de spectres en énergie de l’émission de tubes à rayons X au LNE-LNHB/LMD R. franç. métrol. 37–47