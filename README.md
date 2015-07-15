Insight Data Engineering - Coding Challenge
===========================================================

## My Implementations

Both problems are using pure built-in libraries of Python, no other 3rd party libraries.

For word count, I used Counter (sub class of Dictionary) from Python's collection library as the data structure, and reads each line of the file, then updates each word of the line into the dictionary.

For running median, I only used local machine for the implementation, since the update of the running median depends highly on the previous file lines, and they should happen sequentially.

### To Run

  * Everything is coded in Python, and run.sh simply calls the two Python files. So
  just execute run.sh should be enough. 

### Inputs and Outputs

  This code was benchmarked against the NLTK subset of the Gutenberg corpus (http://www.nltk.org/nltk_data/packages/corpora/gutenberg.zip, cf. http://www.nltk.org/book/ch02.html), which comprise 2,102,546 tokens (53,340 unique - although this number is inflated due to the crude cleaning methodology) over 256,893 lines and 18 files.
  All of the output files are saved in the outputs folder, with the first feature named as "ft1" plus the input file name, and the second feature as "ft2" plus the file name. From executing these files, it will show the biggest file (one of the most popular version of the Bible) only takes probably 1 more second to run than the smallest file. The running time for each file will be printed out.


### Algorithm for Running Median

  Create a minHeap and a maxHeap, note that Python's heapq library only supports min heap, so in maxHeap a minus sign needs to be added for each element in order to maintain the invariants.

  For the first two elements add smaller one to the maxHeap on the left, and bigger one to the minHeap on the right. Then process stream data one by one,

  Step 1: Add next item to one of the heaps

     if next item is smaller than maxHeap root add it to maxHeap,
     else add it to minHeap

  Step 2: Balance the heaps (after this step heaps will be either balanced or
     one of them will contain 1 more item)

     if number of elements in one of the heaps is greater than the other by
     more than 1, remove the root element from the one containing more elements and
     add to the other one
  Then at any given time you can calculate median like this:

     If the heaps contain equal elements;
       median = (root of maxHeap + root of minHeap)/2
     Else
       median = root of the heap with more elements

### Reference: http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers


