import h5py

f = h5py.File("./models/average9.h5")

print(list(f))

print(f['dense_1'])