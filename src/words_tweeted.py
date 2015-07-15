"""
This is the code for the implementation of the word count problem.
It uses a Counter (sub class of Dictionary) from Python's collection library as the data structure,
and reads each line of the file, then updates each word of the line into the dictionary.
"""

from collections import Counter
import time
import os

base_dir = './'
input_dir = base_dir + 'tweet_input/'
output_dir = base_dir + 'tweet_output/'

def word_count(filename):
    start_time = time.time()

    file_in = input_dir + filename
    file_out = output_dir + 'ft1_' + filename

    with open(file_in, 'r') as fin:
        wc = Counter(fin.read().strip().split())

    with open(file_out, 'w') as fout:
        for key, value in sorted(wc.items()):
            fout.write("{}\t{}\n".format(key, value))

    print("Total time for word count in {0}: {1:f} seconds".format(filename, time.time() - start_time))


def main():
    for filename in os.listdir(input_dir):
        word_count(filename)


if __name__ == '__main__':
    main()
