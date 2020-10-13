## 1. Arrays Left Rotation:
A left rotation operation on an array shifts each of the array's elements $1$ unit to the left.  
For example, if $2$ left rotations are performed on array $[1, 2, 3, 4, 5]$, then the array would become $[2, 4, 5, 1, 2]$.  

Given an array $a$ of $n$ integers and a number, $d$, perform $d$ left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.  


### Function Description
Complete the function rotLeft in the editor below. It should return the resulting array of integers.
rotLeft has the following parameter(s):
- An array of integers $a$
- An integer $d$, the number of rotations.

### Input format
The first line contains two space-separated integers $n$ and $d$, the size of $a$ and the number of left rotations you must perform. 
The second line contains $n$ space-separated integers $a[i]$.

### Constraints
- $1 <= n <= 10^5$
- $1 <= d <= n$
- $1 <=a[i] <= 10^6$

### Output Format
Print a single line of $n$ space-separated integers denoting the final state of the array after performing $d$ left rotations.

### Explanation
When we perform $d=4$ left rotations, the array undergoes the following sequence of changes:
- $[1, 2, 3, 4, 5]$ -> $[2, 3, 4, 5, 1]$ -> $[3, 4, 5, 1, 2]$ -> $[4, 5, 1, 2, 3]$ -> $[5, 1, 2, 3, 4]$

### Thinking process:
- getting items in a list by index: O(1)




## 2. Repeated String
Lilah has a string, $s$, of lowercase English letters that she repeated infinitely many times.  

Given an integer, $n$, find and print the number of letter a's in the first $n$ letters of Lilah's infinite string.  

For example, if the string $s=abcac$ and $n=10$, the substring we consider is $abcacabcac$, the first $10$ characters of her infinite string. There are $4$ occurrences of a in the substring.


### Function Description

Complete the _repeatedString_ function in the editor below. It should return an **integer** representing the number of occurrences of $a$ in the prefix of length $n$ in the infinitely repeating string.  

_repeatedString_ has the following parameter(s):
- s: a string to repeat
- n: the number of characters to consider


**Input Format**
- The first line contains a single string, $s$. 
- The second line contains an integer, $n$.


### Constraints
- $1<= |s| <= 100$
- $1 <= n <= 10^{12}$
- For 25% of the test cases, $n<= 10^6$


### Output Format
Print a single integer denoting the number of letter a's in the first $n$ letters of the infinite string created by repeating  infinitely many times.

### Thinking process:
- the code needs to be **optimized** as the constrains show it should work with quite large lists
- accessing lists by index is O(1)
- easiest would be to count the number of occurences of the letter in the original string s using _count_
- multiply the resulting number with the total number of times the string goes into the total string (without remainder) using _\\\ _
- calculate the remainder and slice the string for that number of characters


## New Year Chaos

It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by $1$ from $1$ at the front of the line to _n_ at the back.  

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. **One person can bribe at most two others.** For example, if $n=8$ and Person5 bribes Person4, the queue will look like this: $1, 2, 3, 5, 4, 7, 8.  

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!  



### 3. New Year Chaos
Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or _Too chaotic_ if the line configuration is not possible.  
minimumBribes has the following parameter(s):
- q: an array of integers

### Input Format
The first line contains an integer _t_, the number of test cases.
Each of the next _t_ pairs of lines are as follows: 
- The first line contains an integer _t_, the number of people in the queue 
- The second line has _n_ space-separated integers describing the final state of the queue.

### Constraints
- $1<=t<=10$
- $1<=n<=10^5$

### Output Format
Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than 2 people.