# performance_test.py

import time
import random
import string
import matplotlib.pyplot as plt 
from algorithm import huffman_coding, lzw_compress

# Helper function to generate random string
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Calculate the size of the original and compressed text
def calculate_compressed_size_huffman(text, codes):
    return sum(len(codes[char]) for char in text)  # Total bits for Huffman coding

def calculate_compressed_size_lzw(compressed):
    return len(compressed) * 12  # Assuming each LZW code is 12 bits long

def performance_test():
    # Input sizes to test
    input_sizes = [1000, 5000, 10000, 20000, 50000]

    # Lists to store results
    huffman_times = []
    lzw_times = []
    huffman_ratios = []
    lzw_ratios = []

    for size in input_sizes:
        text = generate_random_string(size)  # Generate random text of the given size
        original_size = len(text) * 8  # Original size in bits

        # Huffman Coding performance
        start_time = time.time()
        codes = huffman_coding(text)
        huffman_compressed_size = calculate_compressed_size_huffman(text, codes)
        huffman_time = time.time() - start_time
        huffman_ratio = huffman_compressed_size / original_size

        # LZW Compression performance
        start_time = time.time()
        compressed = lzw_compress(text)
        lzw_compressed_size = calculate_compressed_size_lzw(compressed)
        lzw_time = time.time() - start_time
        lzw_ratio = lzw_compressed_size / original_size

        # Store results
        huffman_times.append(huffman_time)
        lzw_times.append(lzw_time)
        huffman_ratios.append(huffman_ratio)
        lzw_ratios.append(lzw_ratio)

    # Plot results
    plot_results(input_sizes, huffman_times, lzw_times, huffman_ratios, lzw_ratios)

def plot_results(input_sizes, huffman_times, lzw_times, huffman_ratios, lzw_ratios):
    # Plot Execution Time
    plt.figure(figsize=(12, 6))
    
    # Plot 1: Execution Time
    plt.subplot(1, 2, 1)
    plt.plot(input_sizes, huffman_times, label="Huffman Coding", marker='o')
    plt.plot(input_sizes, lzw_times, label="LZW Compression", marker='o')
    plt.title("Execution Time vs Input Size")
    plt.xlabel("Input Size (characters)")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()

    # Plot 2: Compression Ratio
    plt.subplot(1, 2, 2)
    plt.plot(input_sizes, huffman_ratios, label="Huffman Coding", marker='o')
    plt.plot(input_sizes, lzw_ratios, label="LZW Compression", marker='o')
    plt.title("Compression Ratio vs Input Size")
    plt.xlabel("Input Size (characters)")
    plt.ylabel("Compression Ratio")
    plt.legend()

    # Display plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    performance_test()
