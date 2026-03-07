# COP4533 Programming Assignment 2: Greedy Algorithms

## Yi Su [31833267]
An implementation and comparison of FIFO, LRU, and OPTFF cache eviction policies on the same request sequence.

## Input File
- First line: integers `k` cache capacity and `m` number of requests
- Second line: list of `m` requests as integers
```text
k m
r1 r2 r3 ... rm
```
## Usage
Using an input file (e.g., `tests/test1.in`), you can pass the input file's filepath as a command line argument.
```bash
python src/main.py tests/test1.in
```
The output misses are printed and written to the `.out` of the same filepath (e.g., `tests/test1.out`).

## Assumptions
- `k >= 1` (cache capacity)

## Test Generator
`tests/generateTest.py` generates a test to the filepath given as a command line argument. It selects random values for the following values:
- `k` in `[1, 50]`
- `m` in `[50, 500]`
- `r_i` in `[0, 50]`

## Written Component

## Question 1
Using the test generator, the following tests using random values were created. The number of cache misses for each policy is given.

| Input File | k  | m   | FIFO | LRU | OPTFF |
|------------|----|-----|------|-----|-------|
| test2.in   | 24 | 122 | 77   | 75  | 49    |
| test3.in   | 2  | 465 | 450  | 450 | 402   |
| test4.in   | 49 | 489 | 79   | 79  | 57    |

We can see that the OPTFF policy has the least amount of misses across the three tests. Meanwhile, FIFO does show more misses compared to LRU in one of the tests, but has the same amount of misses in the other two. It seems that
`OPTFF <= LRU <= FIFO` for these tests.

## Question 2
There does exist a request sequence for which OPTFF incurs strictly fewer misses than LRU when `k = 3`. One such sequence is in `tests/test5.in`:
```
1 2 3 4 1
```
#### LRU Cache
| Step | Request | Cache   | Result         |
|------|---------|---------|----------------|
| 1    | 1       | [1]     | Miss           |
| 2    | 2       | [1,2]   | Miss           |
| 3    | 3       | [1,2,3] | Miss           |
| 4    | 4       | [2,3,4] | Miss (evict 1) |
| 5    | 1       | [3,4,1] | Miss (evict 2) |

#### OPTFF Cache
| Step | Request | Cache   | Result                              |
|------|---------|---------|-------------------------------------|
| 1    | 1       | [1]     | Miss                                |
| 2    | 2       | [1,2]   | Miss                                |
| 3    | 3       | [1,2,3] | Miss                                |
| 4    | 4       | [1,2,4] | Miss (evict 3, never used again) |
| 5    | 1       | [1,2,4] | Hit                                 |

#### Total Misses
Here, the LRU policy resulted in `5` misses, whereas the OPTFF policy resulted in only `4` misses.

#### Reasoning
LRU evicts the object that was least recently used, relying only on past access patterns. In this sequence, LRU evicts `1` from the cache despite being needed again. Meanwhile, OPTFF uses future knowledge, evicting pages where the next use is farthest in the future (or never used again). This allows the OPTFF policy to keep `1` because it will be requested again soon. This leads to fewer total misses for OPTFF compared to LRU.

## Question 3
Let OPTFF be Belady’s Farthest-in-Future algorithm. Let A be any offline algorithm that knows the full request sequence. To prove that the number of misses of OPTFF is no larger than that of A on any fixed request sequence, we can use the exchange argument.

#### Setup
- Cache size: `k`
- Request sequence: `r1, r2, r3, ..., rm`
- Suppose A differs from OPTFF for the first time at some request `r_i` where a page replacement occurs.

At this point, both algorithms have the same cache contents before the eviction. The cache is full and a page must be evicted.

#### Eviction
Let:
- `x` = page evicted by OPTFF
- `y` = page evicted by A

Here, `x` also equals the page whose next use occurs farthest in the future, or possibly never used again. Meanwhile, algorithm A instead evicts page `y`.

We can transform algorithm A into A', where at request `r_i`, A' evicts `x` instead of `y` to match OPTFF. Then we can compare A and A', where two possibilities exist.

#### Possibility 1: `y` is never used again

Since `y` never appears again in the sequence, keeping `y` in the cache cannot cause additional misses. Therefore, A' is no worse than A.

#### Possibility 2: `y` is used again later

Let the next use of `y` occur at request `r_j`. Because OPTFF chose `x` instead of `y`, we know that `y` is needed sooner than `x`. Keeping `y` avoids a miss that A would experience earlier. Eventually, when `x` is requested, A' may incur a miss, but this occurs no earlier than the miss that A would experience. Therefore, `Misses(A') <= Misses(A)`.

#### Repeating the Exchange
If A' still differs from OPTFF later in the sequence, we can repeat the same exchange argument. Each time we adjust the eviction decision to match OPTFF, we do not increase the amount of misses. After going through the finite amount of requests, we have transformed A into OPTFF.

#### Conclusion
Since any offline algorithm A can be transformed into OPTFF without increasing the number of misses, we can conclude that the number of misses of OPTFF is no larger than that of A on any fixed sequence. 
