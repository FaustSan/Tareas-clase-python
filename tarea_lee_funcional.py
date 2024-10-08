import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np

file= "fmri.nii.gz"

brain_vol = nib.load(file)

print(type(brain_vol))
print(brain_vol.shape)

vol = brain_vol.get_fdata()
print(type(vol))
print(vol.shape)

img = vol[:,:,10,10]

x=18
y=20
z=10

vector = np.zeros(180)
x2=np.arange(len(vector))

for i in range(180):
    vector[i]=vol[x,y,z,i]

plt.plot(x2,vector)
plt.show()





