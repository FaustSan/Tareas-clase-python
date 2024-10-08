import matplotlib.pyplot as plt
import nibabel as nib

file= "structural_brain.nii.gz"

brain_vol = nib.load(file)

print(type(brain_vol))
print(brain_vol.shape)

vol = brain_vol.get_fdata()
print(type(vol))
print(vol.shape)

#x = int(input("Ingresa la coordenada x (entero): "))
#y = int(input("Ingresa la coordenada y (entero): "))
#z = int(input("Ingresa la coordenada z (entero): "))

x=130
y=100
z=60


imgx = vol[x,:,:]
imgy = vol[:,y,:]
imgz = vol[:,:,z] 


fig, axs = plt.subplots(1, 3)

axs[0].imshow(imgx)
axs[0].axis('off')  # Para ocultar los ejes
axs[0].set_title('Corte sagital')

axs[1].imshow(imgy)
axs[1].axis('off')
axs[1].set_title('Corte coronal')

axs[2].imshow(imgz)
axs[2].axis('off')
axs[2].set_title('Corte axial')

 
plt.show()


