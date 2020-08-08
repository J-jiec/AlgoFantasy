# Sorting Algorithms

## Comparison Sorts
The following table contains a complete list of sorting algorithms from [this Wikipedia page](https://en.wikipedia.org/wiki/Sorting_algorithm#cite_note-8): 


| Algorithm             | Best      | Average           | Worst                | Memory   | Stable | Method                   |
|-----------------------|-----------|-------------------|----------------------|----------|--------|--------------------------|
| Quicksort             | $n\log n$ | $n\log n$         | $n^2$                | $\log n$ | No     | Partitioning             |
| Merge sort            | $n\log n$ | $n\log n$         | $n\log n$            | $n$      | Yes    | Merging                  |
| Inplace merge sort    | -         | -                 | $n\log^2 n$          | 1        | Yes    | Merging                  |
| Introsort             | $n\log n$ | $n\log n$         | $n\log n$            | $\log n$ | No     | Partitioning & Selection |
| Heapsort              | $n\log n$ | $n\log n$         | $n\log n$            | 1        | No     | Selection                |
| Insertion sort        | $n$       | $n^2$             | $n^2$                | 1        | Yes    | Insertion                |
| Block sort            | $n$       | $n\log n$         | $n\log n$            | 1        | Yes    | Insertion & Merging      |
| Quadsort              | $n$       | $n\log n$         | $n\log n$            | $n$      | Yes    | Merging                  |
| Timsort               | $n$       | $n\log n$         | $n\log n$            | $n$      | Yes    | Insertion & Merging      |
| Selection sort        | $n^2$     | $n^2$             | $n^2$                | 1        | No     | Selection                |
| Cubesort              | $n$       | $n\log n$         | $n\log n$            | $n$      | Yes    | Insertion                |
| Shellsort             | $n\log n$ | $n^{\frac{4}{3}}$ | $n^{\frac{3}{2}}$    | 1        | No     | Insertion                |
| Bubble sort           | $n$       | $n^2$             | $n^2$                | 1        | Yes    | Exchanging               |
| Tree sort             | $n\log n$ | $n\log n$         | $n\log n$ (balanced) | $n$      | Yes    | Insertion                |
| Cycle sort            | $n^2$     | $n^2$             | $n^2$                | 1        | No     | Insertion                |
| Library sort          | $n$       | $n\log n$         | $n^2$                | $n$      | Yes    | Insertion                |
| Patience sorting      | $n$       | -                 | $n\log n$            | $n$      | No     | Insertion & Selection    |
| Smoothsort            | $n$       | $n\log n$         | $n\log n$            | 1        | No     | Selection                |
| Strand sort           | $n$       | $n^2$             | $n^2$                | $n$      | Yes    | Selection                |
| Tournament sort       | $n\log n$ | $n\log n$         | $n\log n$            | $n$      | No     | Selection                |
| Cocktail shaker sort  | $n$       | $n^2$             | $n^2$                | 1        | Yes    | Exchanging               |
| Comb sort             | $n\log n$ | $n^2$             | $n^2$                | 1        | Yes    | Exchanging               |
| Gnome sort            | $n$       | $n^2$             | $n^2$                | 1        | Yes    | Exchanging               |
| Unshuffle sort        | $n$       | $kn$              | $kn$                 | $n$      | No     | Distribution and Merge   |
| Franceschini's method | -         | $n\log n$         | $n\log n$            | 1        | Yes    | -                        |
| Odd-even sort         | $n$       | $n^2$             | $n^2$                | 1        | Yes    | Exchanging               |        |        |
### Quicksort
