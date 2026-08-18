import numpy as np  
import scipy.io as sio
import matplotlib.pyplot as plt

def load_data(mat_file):
    # Load MATLAB data file
    return sio.loadmat(mat_file)

def continuum_removal(spectrum):
    # Fit a polynomial to the spectrum for continuum removal (degree 2 as an example)
    continuum = np.poly1d(np.polyfit(range(len(spectrum)), spectrum, 2))
    # Normalize the spectrum by the continuum
    return spectrum / (continuum(range(len(spectrum))) + 1e-10)  # Avoid division by zero

def plot_spectra(spectra, names):
    plt.figure(figsize=(12, 8))
    
    for i, spectrum in enumerate(spectra):
        plt.plot(spectrum, label=names[i])
    
    plt.title('Continuum Removed Spectral Signatures')
    plt.xlabel('Wavelength Index')
    plt.ylabel('Reflectance')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Load the data
    image_data = load_data(r'CupriteS1_R188.mat') 
    ground_truth = load_data(r'groundTruth_Cuprite_nEnd12.mat')

    # Extract spectral data and names
    spectral_signatures = ground_truth['M']  # Assuming 'M' contains the spectral signatures
    mineral_names = ['Alunite', 'Andradite', 'Buddingtonite', 'Dumortierite', 'Kaolinite1', 'Kaolinite2']
    
    # Select 6 minerals for demonstration
    selected_indices = [0, 1, 2, 3, 4, 5]
    selected_spectra = spectral_signatures[selected_indices, :]

    # Perform continuum removal on selected spectra
    cr_spectra = np.array([continuum_removal(spectrum) for spectrum in selected_spectra])

    # Plot the spectra
    plot_spectra(cr_spectra, mineral_names)

if __name__ == "__main__":
    main()

