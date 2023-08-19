# National Instruments
This company offered internship for commuincation engineers to work in 5G systems.

## Q1. Good number

A  **Good number** is one whose number of distinct prime factors is equal to the number of digits in its decimal representation
**NOTE:** The number **'1'** is considered as a Good Number.
Given **Q** queries, each query specifying two integers **a** and **b**, find the number of **Good Number** lying between **a** and **b** **(both included).**

### Input
The first line contains an integer **Q** denoting the number of queries.
Each of the next **Q** lines consists of two integers **a** and **b** denoting the range for this querry.

### Constraints
$1 <= Q <= 5*10^4$

$1<=a<=b<=10^5$

### Output
Print **Q** lines. The $i^{th}$ line contains the answer for the $i^{th}$ query.

### Example
Input:
```
3
1 10
55 59
100 105
```
Output:
```
9
4
2
```
Explanation:

In the range 1-10, all numbers except 6 are good numbers.
In the range 55-59 the good numbers are 55, 56, 57 and 58.
In the range 100-105 only 102 and 105 are good numbers.
### My Solutions: [python](good_number.py)

## Q2. Longest Cipher

A cipher is hidden within a sequence of charecters and has the following restrictions:
a. It has to contain at least one uppercase charecter
b. It cannot contain any digits

You are given a string **s** consisting of an alphanumeric characters. You need to find the longest substring of **s** that is valid cipher and return its length. A substring is defined as a continuous segment of a string.

For example, given "k3Cb", the substance that are valid ciphers are "C" and "Cb". Note that "kCb" is not a substring and "k3C" is not a valid cipher. In this case, your function should return to as the longest substring is "Cb". Alternatively given "k3cb" your function should return -1, since there is no substring that satisfies the restrictions on the format of a valid cipher.

### Input:
The input contains a string **s**.

### Output:
Print the length of the longest substring that is a valid cipher.
If there is no such substring, your function should return -1.

### Example #1
Input
```
a2Bac
```
Output
```
3
```
Explanation:

The three valid ciphers are (B, a, c), so the output is the length of "Bac", which is 3.

### Example #2
Input
```
aA0bCbd
```
Output
```
4
```
Explanation:

The three valid ciphers are (b, C, b, d), so the output is the length of "bCbd", which is 4.

### My Solutions: [python](cypher.py)

## Q3. Winning Stratagy

You are given a Snake and Ladder board of order **5x6**. Find the minimum number of dice throws required to reach the distination or the last cell(30^th cell) from the source(1^st cell), i.e., you start from 1 to reach 30.

### Example
![Snanes and Ladder](https://github.com/imraunav/Placement-coding-problems/blob/main/WhatsApp%20Image%202023-08-16%20at%2020.00.03.jpeg)

For the above board, the output will be 3.
Throws: 2, 6, 2

### Input
The first line of input contains an integer N representing the number of ladders and snakes present.
The second line of the input contains N space-seperated values as N/2 pairs (a,b), representing a ladder or a snake at position 'a' and which takes to a position 'b'.
**Note:** A ladder and a snake cannot share endpoints.

### Output
The required minimum number of dice throws.

### Constraints 
$1<=N<=10$

$1<=a<=30$

$1<=b<=30$

### Example #1

Input
```
12
11 26 3 22 5 8 20 29 27 1 21 9
```

Output
```
3
```

Explanation:

There are four ladder:(11->26), (3->22), (5->8), (20,29) and two snake:(27->1) and (21->9). Upon throwing 2, 6, 2, one reaches the destination using minimal throws.

### Example #2

Input
```
4
2 28 29 1
```

Output
```
2
```

Explanation:

There is one ladder:(2->28), and one snake:(29->1). Upon throwing 1, 2, one reaches the destination using minimal throws.
