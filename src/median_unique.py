"""
This is the implementation of the running median problem, below is the algorithm:

Create a minHeap and a maxHeap, note that Python's heapq library only supports min heap,
so in maxHeap a minus sign needs to be added for each element in order to maintain the invariants.

For the first two elements add smaller one to the maxHeap on the left, and bigger one
to the minHeap on the right. Then process stream data one by one,

Step 1: Add next item to one of the heaps:

   if next item is smaller than maxHeap root add it to maxHeap,
   else add it to minHeap

Step 2: Balance the heaps (after this step heaps will be either balanced or
   one of them will contain 1 more item):

   if number of elements in one of the heaps is greater than the other by
   more than 1, remove the root element from the one containing more elements and
   add to the other one

Then at any given time you can calculate median like this:

   If the heaps contain equal elements;
     median = (root of maxHeap + root of minHeap)/2
   Else
     median = root of the heap with more elements

The code below is following the algorithm
"""

import heapq
import time
import os

base_dir = './'
input_dir = base_dir + 'tweet_input/'
output_dir = base_dir + 'tweet_output/'

def running_median(filename):
    start_time = time.time()

    file_in = input_dir + filename
    file_out = output_dir + 'ft2_' + filename

    min_heap = []
    max_heap = []

    is_first_line = True
    is_second_line = True
    num_first_line = 0
    num_second_line = 0

    fin = open(file_in, 'r')
    fout = open(file_out, 'w')

    for line in fin:
        # Process the first two lines
        if is_first_line:
            num_first_line = len(set(line.split()))
            median = float(num_first_line)
            is_first_line = False
        elif is_second_line:
            num_second_line = len(set(line.split()))
            median = (num_first_line + num_second_line)/2.0
            is_second_line = False
            heapq.heappush(min_heap, max(num_first_line, num_second_line))
            heapq.heappush(max_heap, -min(num_first_line, num_second_line))
        # For rest of the lines
        else:
            num_this_line = len(set(line.split()))
            if num_this_line < -max_heap[0]:
                heapq.heappush(max_heap, -num_this_line)  # A trick here is to add a minus sign to the element
            else:
                heapq.heappush(min_heap, num_this_line)

            if len(max_heap) - len(min_heap) > 1:
                item = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, item)
            elif len(min_heap) - len(max_heap) > 1:
                item = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -item)

            if len(min_heap) == len(max_heap):
                median = (min_heap[0] - max_heap[0]) / 2.0
            else:
                if len(min_heap) > len(max_heap):
                    median = float(min_heap[0])
                else:
                    median = -float(max_heap[0])

        fout.write(str(median) + "\n")

    fin.close()
    fout.close()
    print("Total time for running median in {0} is {1:f} seconds".format(filename, time.time() - start_time))

def main():
    for filename in os.listdir(input_dir):
        running_median(filename)


if __name__ == '__main__':
    main()


