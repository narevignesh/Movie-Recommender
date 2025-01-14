import pickle
import gzip

# Load the original similarity matrix
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Compress the similarity matrix and save it
with gzip.open('similarity_compressed.pkl.gz', 'wb') as f:
    pickle.dump(similarity, f)

print("File compressed successfully!")
