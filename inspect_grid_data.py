import h5py
import numpy as np

file_path = 'outputs/MyGridNaviCoords-v1_random.h5'

try:
    with h5py.File(file_path, 'r') as f:
        print("Keys:", list(f.keys()))
        if 'observations' in f:
            obs = f['observations'][:]
            print("Observations shape:", obs.shape)
            print("Observations dtype:", obs.dtype)
            print("Min:", np.min(obs, axis=0))
            print("Max:", np.max(obs, axis=0))
            print("First 10 observations:\n", obs[:10])
except Exception as e:
    print(e)
