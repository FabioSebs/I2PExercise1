"""5. Write a program that calculates the wavelength of a wave traveling at a constant velocity given the speed
and the frequency. Use the formula lambda = v/f, where lambda is wavelength in meters, v is velocity in
meters per second, and f is frequency in Hertz (cycles per second). Print the velocity, frequency, and
wavelength. Assign each of these values to a variable and use the variables in your print() statements.
The following demonstrates what the program prints:"""

speedMPS= 343
frequencyHz= 256
wavelengthM= speedMPS/frequencyHz

print("The speed (m/s)", speedMPS)
print("The frequency (Hz):", frequencyHz)
print("The wavelength (m): ", wavelengthM)
