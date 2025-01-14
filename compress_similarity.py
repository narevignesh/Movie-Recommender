<<<<<<< HEAD
import pickle
import gzip

# Load the original similarity matrix
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Compress the similarity matrix and save it
with gzip.open('similarity_compressed.pkl.gz', 'wb') as f:
    pickle.dump(similarity, f)

print("File compressed successfully!")
=======
import pickle
import gzip

# Load the original similarity matrix
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Compress the similarity matrix and save it
with gzip.open('similarity_compressed.pkl.gz', 'wb') as f:
    pickle.dump(similarity, f)

print("File compressed successfully!")
>>>>>>> fee83ef29ef5bc7982a935e5c7f8cbac9b8c6923
