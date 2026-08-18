# Hyperspectral Mineral Analysis using Continuum Removal Algorithm (CRA)

## Description
This project analyzes hyperspectral data from the Cuprite mining area (AVIRIS sensor) to enhance and identify spectral absorption features of key minerals. The Continuum Removal Algorithm (CRA) is applied to isolate absorption features by normalizing each spectrum against a fitted baseline (continuum), making it easier to distinguish between different minerals.

## Data
- **Source:** AVIRIS (Airborne Visible/Infrared Imaging Spectrometer)
- **Files used (MATLAB format):**
  - `CupriteS1_R188.mat` — hyperspectral image data (188 effective spectral channels, after removing noisy/water-absorption bands)
  - `groundTruth_Cuprite_nEnd12.mat` — ground truth spectral signatures for 12 minerals
- **Minerals analyzed in this script:** Alunite, Andradite, Buddingtonite, Dumortierite, Kaolinite1, Kaolinite2

## Method
1. **Load data** — read the `.mat` files containing the hyperspectral image and ground truth signatures.
2. **Continuum removal** — fit a 2nd-degree polynomial to each spectrum as its baseline (continuum), then divide the spectrum by this baseline to flatten the overall trend and highlight absorption features.
3. **Visualization** — plot the continuum-removed spectra for the selected minerals for comparison.

## Results
The continuum-removed spectra clearly show distinct absorption features for each mineral, supporting the use of CRA as a simple and effective spectral-matching technique for mineral differentiation in hyperspectral imaging.

![Continuum Removed Spectral Signatures](outputs/continuum_removed_spectra.png)

## ENVI Processing
In addition to the Python-based continuum removal, the dataset was also processed in **ENVI** software as a complementary workflow:

**1. Radiometric Calibration**
The AVIRIS dataset was opened in ENVI and calibrated using the 'Radiometric Calibration' tool to produce a true-color composite.

![RGB Composite](outputs/envi/rgb_composite.png)

**2. MNF (Minimum Noise Fraction) Pre-processing**
The MNF algorithm was applied to reduce dimensionality, enhance signal-to-noise ratio, and separate meaningful information from noise. The eigenvalue plot shows most of the useful signal is concentrated in the first ~10-20 bands.

![MNF Eigenvalues](outputs/envi/mnf_eigenvalues.png)
![MNF False Color](outputs/envi/mnf_false_color.png)

**3. Continuum Removal in ENVI**
Continuum removal was also performed directly in ENVI to isolate and enhance absorption features, enabling comparison across different spectra and improving material identification.

![Continuum Removal Image](outputs/envi/continuum_removal_image.png)

**4. Spectral Matching (Discussion)**
Using spectral signature similarity from the image, the local ground truth for the Chalcedony mineral was compared against the USGS spectral library. The result shows good alignment in absorption position and depth, supporting the use of continuum removal as a simple spectral-matching technique. With higher-resolution data, pure pixels could be identified via the PPI algorithm for more accurate mineral assessment.

![Spectral Profile Comparison - Chalcedony](outputs/envi/spectral_profile_chalcedony.png)

The output from the continuum removal algorithm can also serve as an input for classification methods such as Minimum Distance, SVM, Random Forest, and Maximum Likelihood Classification.

## How to Run
```bash
pip install numpy scipy matplotlib
python continuum_removal.py
```
Make sure `CupriteS1_R188.mat` and `groundTruth_Cuprite_nEnd12.mat` are in the same folder as the script.

## Notes / Future Work
- Explore machine learning approaches to automate mineral classification.
- Compare CRA against other spectral unmixing algorithms.
- Incorporate field validation data to improve reliability.

## Author
Mahsa Jahanbakhsh
