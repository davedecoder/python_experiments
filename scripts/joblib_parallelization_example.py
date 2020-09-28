from joblib import Parallel, delayed
from joblib import Memory
import numpy as np
import time

rng = np.random.RandomState(42)
data = rng.randn(int(1e4), 4)


def costly_compute(data, column):
    """Emulate a costly function by sleeping and returning a column."""
    time.sleep(2)
    return data[column]

location = '/somelocatio/cache_dir'
memory = Memory(location, verbose=0)
costly_compute_cached = memory.cache(costly_compute)



def data_processing_mean_using_cache(data, column):
    """Compute the mean of a column."""
    return costly_compute_cached(data, column).mean()


start = time.time()
results = Parallel(n_jobs=4)(
    delayed(data_processing_mean_using_cache)(data, col)
    for col in range(data.shape[1])
)
stop = time.time()

print('\nSequential processing')
print('Elapsed time for the entire processing: {:.2f} s'
      .format(stop - start))
