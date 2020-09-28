from joblib import Memory
import time
import numpy as np

# Define a location to store cache
location = '/somelocation/cache_dir'
memory = Memory(location, verbose=0)

result = []

def square_number(n):
    return n*n

# Function to compute square of a range of a number:
def get_square_range_cached(start_no, end_no):
    for i in np.arange(start_no, end_no):
        time.sleep(1)
        result.append(square_number(i))
    return result

get_square_range_cached = memory.cache(get_square_range_cached)

start = time.time()
# Getting square of 1 to 50:
final_result = get_square_range_cached(1, 21)
end = time.time()

# Total time to compute
print('\nThe function took {:.2f} s to compute.'.format(end - start))
print(final_result)
