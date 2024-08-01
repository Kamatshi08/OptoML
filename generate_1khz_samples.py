
import numpy as np

def generate_1khz_samples(sample_rate, duration, amplitude):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    real_part = amplitude * np.cos(2 * np.pi * 1000 * t)  # 1 KHz sine wave
    imag_part = amplitude * np.sin(2 * np.pi * 1000 * t)  # 1 KHz sine wave
    return real_part, imag_part

def save_samples_to_bin(real_part, imag_part, filename):
    complex_samples = real_part + 1j * imag_part
    complex_samples.astype(np.complex128).tofile(filename)

sample_rate = 10000  # 10 KHz sampling rate
duration = 1  # 1 second duration
amplitude = 1.0  # Amplitude of the sine wave

real_part, imag_part = generate_1khz_samples(sample_rate, duration, amplitude)
save_samples_to_bin(real_part, imag_part, '1khz_reference_samples.bin')

print("1 KHz reference samples have been saved to '1khz_reference_samples.bin'.")
