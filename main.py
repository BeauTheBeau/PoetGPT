import tensorrt as trt
import tensorflow as tf
import numpy as np

import os

# Load the raw text data
text = open('poems.txt', 'r').read()
# Create a list of unique characters
vocab = sorted(set(text))

# Create a mapping from characters to indices
char2idx = {u: i for i, u in enumerate(vocab)}

# Create a mapping from indices to characters
idx2char = np.array(vocab)

# Convert the text to a sequence of indices
text_as_int = np.array([char2idx[c] for c in text])

# Define the maximum sequence length and batch size
seq_length = 100
batch_size = 64

# Create a dataset of input sequences and target sequences
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)


# Define a function to split the sequences into input and target
def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text


# Map the sequences to input/target pairs
dataset = sequences.map(split_input_target)

# Create batches of input/target pairs
dataset = dataset.shuffle(10000).batch(batch_size, drop_remainder=True)

# Save the vocab and char2idx mappings for later use
np.save('idx2char.npy', idx2char)
np.save('char2idx.npy', char2idx)
