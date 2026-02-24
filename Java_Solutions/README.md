# Challenge 001 Split Strings

My solution -> *[P001SplitStrings](P001SplitStrings/StringSplit.java)*

## **_Task condition:_**

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ```('_')```.

**_Examples_**

```
Input: "abc" Output => ["ab", "c_"]

Input: "abcdef" => ["ab", "cd", "ef"]
```

#

<br/>

# Challenge 002 Duplicate Encoder

My solution -> *[P002DuplicateEncoder](P002DuplicateEncoder/DuplicateEncoder.java)*

## **_Task condition:_**

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

**_Examples_**

```
"din"       => "((("

"recede"    => "()()()"

"Success"   => ")())())"

"(( @"      => "))((" 
```

**_Notes_**

- Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

#

<br/>

# Challenge 003 Sum of Numbers

My solution -> *[P003SumOfNumbers](P003SumOfNumbers/Sum.java)*

## **_Task condition:_**

Given two integers ```a``` and ```b```, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return ```a``` or ```b```.

**_Examples_**

```
Input: (a, b) => Output: (explanation)
--------------------------------------

Input: (1, 0)  => Output: 1 (1 + 0 = 1)

Input: (1, 2)  => Output: 3 (1 + 2 = 3)

Input: (0, 1)  => Output: 1 (0 + 1 = 1)

Input: (1, 1)  => Output: 1 (1 since both are same)

Input: (-1, 0) => Output: -1 (-1 + 0 = -1)

Input: (-1, 2) => Output: 2 (-1 + 0 + 1 + 2 = 2)
```

**_Notes_**

- ```a``` and ```b``` are not ordered!

#

<br/>

# Challenge 004 Sum of odd numbers

My solution -> *[P004SumOfOddNumbers](P004SumOfOddNumbers/RowSumOddNumbers.java)*

## **_Task condition:_**

Given the triangle of consecutive odd numbers:

```
                 1
              3     5
           7     9    11
       13    15    17    19
    21    23    25    27    29
    ...
```

Calculate the sum of the numbers in the ```n-th``` row of this triangle (starting at index ```1```) e.g.: (Input --> Output)

**_Examples_**

```
Input: 1 => Output: 1

Input: 2 => Output: 3 + 5 = 8
```

#

<br/>

# Challenge 005 Break camelCase

My solution -> *[P005BreakCamelCase](P005BreakCamelCase/Solution.java)*

## **_Task condition:_**

Complete the solution so that the function will break up camel casing, using a space between words.

**_Examples_**

```
Input: "camelCasing" => Output: "camel Casing"

Input: "identifier"  => Output: "identifier"

Input: ""            => Output: ""
```

#

<br/>

# Challenge 006 Create Phone Number

My solution -> *[P006CreatePhoneNumber](P006CreatePhoneNumber/Kata.java)*

## **_Task condition:_**

Write a function that accepts an ```array of 10 integers``` (between 0 and 9), that returns a string of those numbers in the form of a phone number.

The returned format must be correct in order to complete this challenge.

**_Examples_**

```
Input: Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) => Output: "(123) 456-7890"
```

<br />

**_NOTES:_**

- Don't forget the space after the closing parentheses!

#

<br />

# Challenge 007 Count characters in your string

My solution -> *[P007CountCharactersInYourString](P007CountCharactersInYourString/Kata.java)*

## **_Task condition:_**

The main idea is to count all the occurring characters in a string.

**_Examples_**

```
Input: "aba" => Output: {'a': 2, 'b': 1}
```

<br />

**_NOTES:_**

- If the string is empty the result should be empty object literal, {}

#

<br />

# Challenge 008 Highest Scoring Word

My solution -> *[P008HighestScoringWord](P008HighestScoringWord/Kata.java)*

## **_Task condition:_**

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: ```a = 1, b = 2, c = 3``` etc.

For example, the score of ```abad``` is ```8``` ```(1 + 2 + 1 + 4)```.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

**_Examples_**

```
Input: 'man i need a taxi up to ubud' => Output: 'taxi'

Input: 'what time are we climbing up the volcano' => Output: 'volcano'
```

#

<br />

# Challenge 009 Statistics For An Athletic Association

My solution -> *[P009StatisticsForAnAthleticAssociation](P009StatisticsForAnAthleticAssociation/Stat.java)*

## **_Task condition:_**

You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5 runners:

```
"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"
```

Each part of the string is of the form: ```h|m|s``` where ```h```, ```m```, ```s``` (```h``` for hour, ```m``` for minutes, ```s``` for seconds) are positive or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by ```, ``` or ```,```.

To compare the results of the teams you are asked for giving three statistics; ```range```, ```average``` and ```median```.

- ```Range``` : difference between the lowest and highest values. In ```[4, 6, 9, 3, 7]``` the ```lowest value``` is ```3```, and the ```highest``` is ```9```, so the range is ```9 − 3 = 6```.

- ```Mean or Average``` : To calculate mean, add together all of the numbers and then divide the sum by the total count of numbers.

- ```Median``` : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of ```[3, 3, 5, 9, 11]``` is ```5```) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of ```[3, 5, 6, 9]``` is ```(5 + 6) / 2 = 5.5```).

Your task is to return a string giving these 3 values. For the example given above, the string result will be

```
"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"
```

of the form: ```"Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"```

where ```hh```, ```mm```, ```ss``` are integers (represented by strings) with each 2 digits.

**_Examples_**

```
Input: "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"

Output: "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00"
```

**_NOTES:_**

- if a result in seconds is ab.xy... it will be given truncated as ab.
- if the given string is "" you will return ""

#

<br />

# Challenge 010 Highest Scoring Word

My solution -> *[P010PlusOneArray](P010PlusOneArray/PlusOneArray.java)*

## **_Task condition:_**

Given an array of integers of any length, return an array that has ```1``` added to the value represented by the array.

If the array is invalid (empty, or contains negative integers or integers with more than 1 digit), return ```null```.

**Valid arrays**

```
[4, 3, 2, 5] would return [4, 3, 2, 6] (4325 + 1 = 4326)
[1, 2, 3, 9] would return [1, 2, 4, 0] (1239 + 1 = 1240)
[9, 9, 9, 9] would return [1, 0, 0, 0, 0] (9999 + 1 = 10000)
[0, 1, 3, 7] would return [0, 1, 3, 8] (0137 + 1 = 0138)
```

**Invalid arrays**

```
[] is invalid because it is empty
[1, -9] is invalid because -9 is not a non-negative integer
[1, 2, 33] is invalid because 33 is not a single-digit integer
```

**_Examples_**

```
Input: [2, 3, 9, 9] => Output: [2,4,0,0]

Input: [9,9] => Output: [1,0,0]

Input: [0,7] => Output: [0,8]

Input: [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0] => Output: [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,1]

Input: [1,10] => Output: null
```

#

<br />

# Challenge 011 Matrix Addition

My solution -> *[P011MatrixAddition](P011MatrixAddition/Kata.java)*

## **_Task condition:_**

Write a function that accepts two square matrices (`N x N` two dimensional arrays), and return the sum of the two. Both matrices being passed into the function will be of size `N x N` (square), containing only integers.

How to sum two matrices:

Take each cell `[n][m]` from the first matrix, and add it with the same `[n][m]` cell from the second matrix. This will be cell `[n][m]` of the solution matrix.

**_Visualization:_**

```
|1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
|3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
|1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|
```

**_Examples_**

```
matrixAddition(
  [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
//      +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] )

// returns:
  [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ]
```

#

<br />

# Challenge 012 Square Matrix Multiplication

My solution -> *[P012SquareMatrixMultiplication](P012SquareMatrixMultiplication/Kata.java)*

## **_Task condition:_**

Write a function that accepts two square `(NxN)` matrices (two dimensional arrays), and returns the product of the two. Only square matrices will be given.

**_How to multiply two square matrices:_**

We are given two matrices, `A` and `B`, of size `2x2` (note: tests are not limited to 2x2). Matrix `C`, the solution, will be equal to the product of `A` and `B`. To fill in cell `[0][0]` of matrix `C`, you need to compute: `A[0][0] * B[0][0] + A[0][1] * B[1][0]`.

More general: To fill in cell `[n][m]` of matrix `C`, you need to first multiply the elements in the `n-th` row of matrix `A` by the elements in the `m-th` column of matrix `B`, then take the sum of all those products. This will give you the value for cell `[m][n]` in matrix `C`. 

**_Examples_**

```
  A         B          C
|1 2|  x  |3 2|  =  | 5 4|
|3 2|     |1 1|     |11 8|
```

**Detailed calculation:**

```
C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0] = 1*3 + 2*1 =  5
C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1] = 1*2 + 2*1 =  4
C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0] = 3*3 + 2*1 = 11
C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1] = 3*2 + 2*1 =  8
```

#

<br />

# Challenge 013 Word a10n (abbreviation)

My solution -> *[P013WordA10nAbbreviation](P013WordA10nAbbreviation/Abbreviator.java)*

## **_Task condition:_**

The word `i18n` is a common abbreviation of `internationalization` in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, `a11y` is an abbreviation of `accessibility`.

Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

- A `"word"` is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. `"elephant-ride"`) will split up a series of letters into two words (eg. `"elephant"` and `"ride"`).

- The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. `"elephant ride"` => `"e6t r2e"`).

**_Examples_**

```
Input: "elephant-rides are really fun!"
        ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
words (^):   "elephant" "rides" "are" "really" "fun"
               123456     123     1     1234     1
ignore short words:               X              X

abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
all non-word characters (*) remain in place
                     "-"      " "    " "    " "     "!"
Output: "e6t-r3s are r4y fun!"
```

#

<br />

# Challenge 014 N High Scores

My solution -> *[P014NHighScores](P014NHighScores/Solution.java)*

## **_Task condition:_**

You've been given the task of retrieving the top N high scores from players of a video game.

You need to write the method `topScores(List<PlayerRecord> records, int nTop)`, where `records` is a list of players records in the form of:

```
List<PlayerRecord> records = Arrays.asList(
    new PlayerRecord("Bob", 100),
    new PlayerRecord("Jane", 120),
    new PlayerRecord("Alice", 10),
    new PlayerRecord("Bob", 110),
    new PlayerRecord("Bob", 10)
);
```

and `nTop` is an integer.

The method should return the top `n` records, where each user name can appear at most a single time. Records should be in from highest to lowest. Users with the same score should be in alphabetical order.

if `nTop` is negative or `0`, the returned value should be an `empty list`.

if `nTop` is greater than the total number of records, you should include as many valid records as possible.

**_Examples_**

```
List<PlayerRecord> records = Arrays.asList(
    new PlayerRecord("Bob", 100),
    new PlayerRecord("Jane", 120),
    new PlayerRecord("Alice", 10),
    new PlayerRecord("Bob", 110),
    new PlayerRecord("Bob", 10)
);

Input: topScores(records, 3)

Output: [[Jane, 120], [Bob, 110], [Alice, 10]]
```

#

<br />

# Challenge 015 Follow That Spy

My solution -> *[P015FollowThatSpy](P015FollowThatSpy/Routes.java)*

## **_Task condition:_**

We are diligently pursuing our elusive operative, Matthew Knight, who also goes by the alias Roy Miller. He employs a nomadic lifestyle to evade detection, constantly moving from one location to another, with each of his journeys following a perplexing and non-standard sequence of itineraries. Our mission is to decipher the routes he will undertake during each of his voyages.

You've been provided with an array of itinerary `routes`, decipher the precise destinations he will visit in the correct sequence according to his meticulously planned itineraries.

Based on the provided routes:

`[ ["USA", "BRA"], ["JPN", "PHL"], ["BRA", "UAE"], ["UAE", "JPN"] ]`

The correct sequence of destinations is:

`"USA, BRA, UAE, JPN, PHL"`

**_Examples_**

```
Input: [ ["MNL", "TAG"], ["CEB", "TAC"], ["TAG", "CEB"], ["TAC", "BOR"] ]
Output: "MNL, TAG, CEB, TAC, BOR"

Input: [ ["Chicago", "Winnipeg"], ["Halifax", "Montreal"], ["Montreal", "Toronto"], ["Toronto", "Chicago"], ["Winnipeg", "Seattle"] ]
Output: "Halifax, Montreal, Toronto, Chicago, Winnipeg, Seattle"
```

**_NOTES:_**

- You can safely assume that there will be no duplicate locations with distinct `routes`.
- All `routes` provided will have non-empty itineraries.
- There will always be at least one (1) route connecting one waypoint to another.

#

<br />

# Challenge 016 Simple Prime Streaming

My solution -> *[P016SimplePrimeStreaming](P016SimplePrimeStreaming/SimplePrimeStreaming.java)*

## **_Task condition:_**

Consider a sequence made up of the consecutive prime numbers. This infinite sequence would start with: 

```
"2357111317192329313741434753596167717379..."
```

You will be given two numbers: `a` and `b`, and your task will be to return `b` elements starting from index `a` in this sequence.

Tests go up to about index `20000`.

**_Examples_**

```
Input: solve(10, 5) => Output: "19232" // Because these are 5 elements from index 10 in the sequence.
```

#

<br />

# Challenge 017 Brute Force Detector

My solution -> *[P017BruteForceDetector](P017BruteForceDetector/BruteForceDetector.java)*

## **_Task condition:_**

You're analyzing authentication logs. Each log entry is a string like:

```
192.168.1.1 LOGIN_FAIL user=admin
192.168.1.1 LOGIN_SUCCESS user=admin
10.0.0.5 LOGIN_FAIL user=root
```

An IP is suspicious if it has 3 or more consecutive failures without a success in between. Return a list of suspicious IPs, sorted alphabetically.

```
String[] logs = {
    "192.168.1.1 LOGIN_FAIL user=admin",
    "192.168.1.1 LOGIN_FAIL user=admin",
    "192.168.1.1 LOGIN_FAIL user=root",
    "10.0.0.5 LOGIN_FAIL user=test",
    "10.0.0.5 LOGIN_SUCCESS user=test"
};
detectBruteForce(logs); // [192.168.1.1]
```

The `10.0.0.5` IP had a failure then a success, so its streak reset. The `192.168.1.1` IP hit 3 failures in a row - busted. Only respond with a list of the suspicious IPs.

A success resets that IP's failure count to zero. Empty list returns empty list.

**_Examples_**

```
String[] logs1 = {
        "192.168.1.1 LOGIN_FAIL user=admin",
        "192.168.1.1 LOGIN_FAIL user=admin",
        "192.168.1.1 LOGIN_FAIL user=admin"
};

Input: detectBruteForce(logs1) => Output: [192.168.1.1]

String[] logs2 = {
        "10.0.0.5 LOGIN_FAIL user=x",
        "10.0.0.5 LOGIN_FAIL user=x",
        "10.0.0.5 LOGIN_SUCCESS user=x",
        "10.0.0.5 LOGIN_FAIL user=x"
};

Input: detectBruteForce(logs2) => Output: []

String[] logs3 = {
        "1.1.1.1 LOGIN_FAIL user=a",
        "2.2.2.2 LOGIN_FAIL user=b",
        "1.1.1.1 LOGIN_FAIL user=a",
        "2.2.2.2 LOGIN_SUCCESS user=b",
        "1.1.1.1 LOGIN_FAIL user=a",
        "2.2.2.2 LOGIN_FAIL user=b"
};

Input: detectBruteForce(logs3) => Output: [1.1.1.1]

String[] logs4 = {
        "5.5.5.5 LOGIN_FAIL user=x",
        "5.5.5.5 LOGIN_FAIL user=x",
        "5.5.5.5 LOGIN_FAIL user=x",
        "5.5.5.5 LOGIN_SUCCESS user=x",
        "5.5.5.5 LOGIN_FAIL user=x",
        "5.5.5.5 LOGIN_FAIL user=x",
        "5.5.5.5 LOGIN_FAIL user=x"
};

Input: detectBruteForce(logs4) => Output: [5.5.5.5]

String[] logs5 = {};

Input: detectBruteForce(logs5) => Output: []

String[] logs6 = {
        "9.9.9.9 LOGIN_FAIL user=a",
        "1.1.1.1 LOGIN_FAIL user=b",
        "9.9.9.9 LOGIN_FAIL user=a",
        "1.1.1.1 LOGIN_FAIL user=b",
        "9.9.9.9 LOGIN_FAIL user=a",
        "1.1.1.1 LOGIN_FAIL user=b"
};

Input: detectBruteForce(logs6) => Output: [1.1.1.1, 9.9.9.9]
```

**_NOTES:_**

- You do not need to validate the IP addresses.

#

<br />

# Challenge 018 Pure Odd Digits Primes

My solution -> *[P018PureOddDigitsPrimes](P018PureOddDigitsPrimes/OddDigPrime.java)*

## **_Task condition:_**

Primes that have only odd digits are pure odd digits primes, obvious but necessary definition. Examples of pure odd digit primes are: `11, 13, 17, 19, 31...` If a prime has only one even digit does not belong to pure odd digits prime, no matter the amount of odd digits that may have.

Create a method, `onlyOddDigPrimes(long n)`, that receive a positive integer `n >= 3`, and output an array with three values:

```
[number pure odd digit primes less than or equal to n, largest pure odd digit prime smaller than or equal to n, smallest pure odd digit prime larger than n]
```

Let's see some cases:

```
onlyOddDigPrimes(20) ----> [7, 19, 31]
// 7, beacause we have seven pure odd digit primes below 20 and are 3, 5, 7, 11, 13, 17, 19
// 19, because is the nearest prime of this type to 20
// 31, is the first pure odd digit that we encounter after 20

onlyOddDigPrimes(40) ----> [9, 37, 53]
onlyOddDigPrimes(13) ----> [5, 13, 17]
```

**_Examples_**

```
Input: onlyOddDigPrimes(20) => Output: [7, 19, 31]

Input: onlyOddDigPrimes(40) => Output: [9, 37, 53]

Input: onlyOddDigPrimes(55) => Output: [10, 53, 59]

Input: onlyOddDigPrimes(60) => Output: [11, 59, 71]

Input: onlyOddDigPrimes(100) => Output: [15, 97, 113]
```

#

<br />

# Challenge 019 Find The Mine!

My solution -> *[P019FindTheMine](P019FindTheMine/MineFinder.java)*

## **_Task condition:_**

You've just discovered a square (`NxN`) field and you notice a warning sign. The sign states that there's a single bomb in the 2D grid-like field in front of you.

Write a method that accepts a 2D array, and returns the location of the mine. The mine is represented as the integer `1` in the 2D array. Areas in the 2D array that are not the mine will be represented as `0`s.

The location returned should be an array where the first element is the row index, and the second element is the column index of the bomb location (both should be 0 based). All 2D arrays passed into your function will be a square (`NxN`), and there will only be one mine in the array.

**_Examples_**

```
int[][] field1 = {{1, 0, 0}, {0, 0, 0}, {0, 0, 0}};

Input: findMine(field1) => Output: [0, 0]

int[][] field2 = {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}};

Input: findMine(field2) => Output: [1, 1]

int[][] field3 = {{0, 0, 0}, {0, 0, 0}, {0, 1, 0}};

Input: findMine(field3) => Output: [2, 1]

int[][] field4 = {{1, 0}, {0, 0}};

Input: findMine(field4) => Output: [0, 0]

int[][] field5 = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}};

Input: findMine(field5) => Output: [2, 2]
```

#

<br />

# Challenge 020 Rotate Array

My solution -> *[P020RotateArray](P020RotateArray/Rotator.java)*

## **_Task condition:_**

Create a method named `"rotate"` that returns a given array with the elements inside the array rotated `n` spaces.

If `n` is `greater` than `0` it should rotate the array to the right. If `n` is `less` than `0` it should rotate the array to the left. If `n` is `0`, then it should return the array unchanged.

```
with array [1, 2, 3, 4, 5]

n = 1      =>    [5, 1, 2, 3, 4]
n = 2      =>    [4, 5, 1, 2, 3]
n = 3      =>    [3, 4, 5, 1, 2]
n = 4      =>    [2, 3, 4, 5, 1]
n = 5      =>    [1, 2, 3, 4, 5]
n = 0      =>    [1, 2, 3, 4, 5]
n = -1     =>    [2, 3, 4, 5, 1]
n = -2     =>    [3, 4, 5, 1, 2]
n = -3     =>    [4, 5, 1, 2, 3]
n = -4     =>    [5, 1, 2, 3, 4]
n = -5     =>    [1, 2, 3, 4, 5]
```

The rotation shouldn't be limited by the indices available in the array. Meaning that if we exceed the indices of the array it keeps rotating.

```
with array [1, 2, 3, 4, 5]

n = 7        =>    [4, 5, 1, 2, 3]
n = 11       =>    [5, 1, 2, 3, 4]
n = 12478    =>    [3, 4, 5, 1, 2]
```

**_Examples_**

```
Input: rotate(new Object[]{1, 2, 3, 4, 5}, 1) => Output: [5, 1, 2, 3, 4]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, 2) => Output: [4, 5, 1, 2, 3]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, 3) => Output: [3, 4, 5, 1, 2]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, 4) => Output: [2, 3, 4, 5, 1]

Input: otate(new Object[]{1, 2, 3, 4, 5}, 5) => Output: [1, 2, 3, 4, 5]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, 6) => Output: [5, 1, 2, 3, 4]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, -1) => Output: [2, 3, 4, 5, 1]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, -2) => Output: [3, 4, 5, 1, 2]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, -3) => Output: [4, 5, 1, 2, 3]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, -4) => Output: [5, 1, 2, 3, 4]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, -5) => Output: [1, 2, 3, 4, 5]

Input: rotate(new Object[]{1, 2, 3, 4, 5}, -6) => Output: [2, 3, 4, 5, 1]
```

#

<br />

# Challenge 021 Decoder Arrow Pin Code

My solution -> *[P021DecoderArrowPinCode](P021DecoderArrowPinCode/Kata.java)*

## **_Task condition:_**

You are a junior employee hired to work in an office for a meager salary, but you are full of ambition to conquer the universe of professional heights. You were shown your workplace, which has a computer, but it is password protected. Your coworkers decided to play a joke on you by setting a password on your computer. They left you a bunch of stickers with a strange sequence of characters, always starting with a digit and continuing with arrows. Some stickers have an additional digit starting with *. Taking one sticker in your hands and looking at the keyboard, you realize that this is probably the computer's PIN code, encoded as a sequence of arrows, but which of the stickers contains the correct sequence? It seems that among the stickers there are impossible combinations of arrows that go beyond the limits of the numeric keypad. You try to enter the first PIN code from the sticker, get confused by the arrows, and decide to write a function to decode the PIN code with arrows. Fortunately, you have your laptop with you.

```
+---+---+---+     +---sticker---+ 
| 7 | 8 | 9 |     |             |
+---+---+---+     |  1→↑→       |
| 4 | 5 | 6 |     |             |
+---+---+---+     |             |
| 1 | 2 | 3 |     +-------------+
+---+---+---+   presumably encoded
| 0 |                1256
+---+
```

Your task is to write a decoder function for the arrow pin code that takes a string as input and returns a list containing a sequence of digits.

- The sticker contains between `4` and `8` characters.
- The `PIN` code on the sticker always begins with a digit and contains at least one arrow.
- There are no more than four types of arrows on the stickers `↓, ↑, →, ←`.
- In addition to the first digit, the sticker may contain another digit with an asterisk `*n`, which probably indicates the number of times the previous key was pressed. The digit is always in the range `0 < *n < 10`.
- The sticker may contain an incorrect `PIN` code consisting of an incorrect combination of arrows that goes beyond the digital keypad. In this case, return `[]`.

**correct sequence of arrows**

```
"1→↑→"       ==>   [1, 2, 5, 6]

"1*2↓"       ==>   [1, 1, 1, 0]

"0*2↑"       ==>   [0, 0, 0, 1]

"0↑↑↑"       ==>   [0, 1, 4, 7]

"5↓*1←↑↓"    ==>   [5, 2, 2, 1, 4, 1]

"1→→↑↑←←↓↓"  ==>   [1, 2, 3, 6, 9, 8, 7, 4, 1]
```

**incorrect sequence of arrows**

```
"0↑↑↑↑"      ==>   []

"8↑*5→"      ==>   []

"0←*2←"      ==>   []

"8↑↑↑"       ==>   []

"3↓←*4↑"     ==>   []

"6→←→↓↑"     ==>   []
```

**_Examples_**

```
Input: decArrowPinCode("1→↑→") => Output: [1, 2, 5, 6]

Input: decArrowPinCode("1*2↓") => Output: [1, 1, 1, 0]

Input: decArrowPinCode("0*2↑") => Output: [0, 0, 0, 1]

Input: decArrowPinCode("0↑↑↑") => Output: [0, 1, 4, 7]

Input: decArrowPinCode("0↑↑↑↑") => Output: []

Input: decArrowPinCode("8↑*5→") => Output: []

Input: decArrowPinCode("0←*2←") => Output: []
```

#

<br />

# Challenge 022 Backwards Read Primes

My solution -> *[P022BackwardsReadPrimes](P022BackwardsReadPrimes/BackWardsPrime.java)*

## **_Task condition:_**

Backwards-read-primes are primes that when read backwards in base 10 (from right to left) are a different prime. (This rules out primes which are palindromes.)

```
13 17 31 37 71 73
```

`13` is such because it's prime and read from right to left writes `31` which is prime too. Same for the others.

Find all Backwards-read-primes between two positive given numbers (both inclusive), the second one always being greater than or equal to the first one. The resulting array or the resulting string will be ordered following the natural order of the prime numbers.

Examples (in general form):

```
(start = 2, end = 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
(start = 9900, end = 10000) => [9923, 9931, 9941, 9967]
(start = 501, end = 599) => []
```

**_Examples_**

```
Input: backwardsPrime(1, 100) => Output: "13 17 31 37 71 73 79 97"

Input: backwardsPrime(9900, 10000) => Output: "9923 9931 9941 9967"
```

#

<br />

# Challenge 023 IP Address To Number

My solution -> *[P023IPAddressToNumber](P023IPAddressToNumber/IpTranslator.java)*

## **_Task condition:_**

An `IPv4` address is a 32-bit number that identifies a device on the internet.

While computers read and write IP addresses as a 32-bit number, we prefer to read them in dotted-decimal notation, which is basically the number split into 4 chunks of 8 bits, converted to decimal, and delmited by a dot.

You must create the method `ipToNum()` that takes an ip address and converts it to a number, as well as the method `numToIp()` that takes a number and converts it to an IP address string. Input will always be valid.

```
//original IP address
192.168.1.1

//breaks down into 4 binary octets
11000000 . 10101000 . 00000001 . 00000001

//which are merged together (unsigned 32-bit binary)
11000000101010000000000100000001

//and finally converted to base 10
3232235777

```

Note that the binary octets are unsigned (so we can't have negative numbers).

**_Examples_**

_ipToNum() method_

```
Input: ipToNum("192.168.1.1") => Output: 3232235777

Input: ipToNum("10.0.0.0") => Output: 167772160

Input: ipToNum("176.16.0.1") => Output: 2953838593
```

_numToIp() method_

```
Input: numToIp(3232235777) => Output: "192.168.1.1"

Input: numToIp(167772160) => Output: "10.0.0.0"

Input: numToIp(2953838593) => Output: "176.16.0.1"
```

#

<br />

# Challenge 024 Maze Runner

My solution -> *[P024MazeRunner](P024MazeRunner/MazeRunner.java)*

## **_Task condition:_**

Welcome Adventurer. Your aim is to navigate the maze and reach the finish point without touching any walls. Doing so will kill you instantly!

You will be given a `2D` array of the maze and an array of directions. Your task is to follow the directions given. If you reach the end point before all your moves have gone, you should return `Finish`. If you hit any walls or go outside the maze border, you should return `Dead`. If you find yourself still in the maze after using all the moves, you should return `Lost`.

The Maze array will look like

```
maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]
```

..with the following key

```
0 = Safe place to walk
1 = Wall
2 = Start Point
3 = Finish Point
```

```
direction = {"N","N","N","N","N","E","E","E","E","E"} == "Finish"
```

**_Rules_**

1. The Maze array will always be square i.e. `N x N` but its size and content will alter from test to test.

2. The `start` and `finish` positions will change for the final tests.

3. The directions array will always be in upper case and will be in the format of `N = North`, `E = East`, `W = West` and `S = South`.

4. If you reach the end point before all your moves have gone, you should return `Finish`.

5. If you hit any walls or go outside the maze border, you should return `Dead`.

6. If you find yourself still in the maze after using all the moves, you should return `Lost`.

Good luck, and stay safe!

**_Examples_**

```
int[][] maze = {
        {1, 1, 1, 1, 1, 1, 1},
        {1, 0, 0, 0, 0, 0, 3},
        {1, 0, 1, 0, 1, 0, 1},
        {0, 0, 1, 0, 0, 0, 1},
        {1, 0, 1, 0, 1, 0, 1},
        {1, 0, 0, 0, 0, 0, 1},
        {1, 2, 1, 0, 1, 0, 1}};

String[] directions1 = {"N", "N", "N", "N", "N", "E", "E", "E", "E", "E"};

Input: walk(maze, directions1) => Output: "Finish"

String[] directions2 = {"N", "N", "N", "N", "N", "E", "E", "S", "S", "E", "E", "N", "N", "E"};

Input: walk(maze, directions2) => Output: "Finish"

String[] directions3 = {"N", "N", "N", "N", "N", "E", "E", "E", "E", "E", "W", "W"};

Input: walk(maze, directions3) => Output: "Finish"

String[] directions4 = {"N", "N", "N", "W", "W"};

Input: walk(maze, directions4) => Output: "Dead"

String[] directions5 = {"N", "N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"};

Input: walk(maze, directions5) => Output: "Dead"

String[] directions6 = {"N", "E", "E", "E", "E"};

Input: walk(maze, directions6) => Output: "Lost"
```

#

<br />

# Challenge 025 Round And Round

My solution -> *[P025RoundAndRound](P025RoundAndRound/RoundAndRound.java)*

## **_Task condition:_**

Since there are lots of katas requiring you to round numbers to 2 decimal places, you decided to extract the method to ease out the process.

And you can't even get this right!

Quick, fix the bug before everyone in CodeWars notices that you can't even round a number correctly!

```
public class RoundAndRound {
    public static double roundTo2DecimalPlaces(double number) {
        return Math.round(number * 100.0)/100.0;
    }
}
```

**_Examples_**

```
Input: roundTo2DecimalPlaces(2D) => Output: 2D

Input: roundTo2DecimalPlaces(7.477D) => Output: 7.48D

Input: roundTo2DecimalPlaces(-4.999D) => Output: -5D

Input: roundTo2DecimalPlaces(18.123D) => Output: 18.12D

Input: roundTo2DecimalPlaces(0D) => Output: 0D

Input: roundTo2DecimalPlaces(1.455D) => Output: 1.46D

Input: roundTo2DecimalPlaces(-1.455D) => Output: -1.46D

Input: roundTo2DecimalPlaces(1.055D) => Output: 1.06D

Input: roundTo2DecimalPlaces(-1.055D) => Output: -1.06D

Input: roundTo2DecimalPlaces(16.765D) => Output: 16.77D

Input: roundTo2DecimalPlaces(-16.765D) => Output: -16.77D

Input: roundTo2DecimalPlaces(1.025D) => Output: 1.03D

Input: roundTo2DecimalPlaces(-1.025D) => Output: -1.03D

Input: roundTo2DecimalPlaces(16.355D) => Output: 16.36D

Input: roundTo2DecimalPlaces(-16.345D) => Output: -16.35D

Input: roundTo2DecimalPlaces(-1.1949999999999999D) => Output: -1.19D

Input: roundTo2DecimalPlaces(-1.1950000000000001D) => Output: -1.20D

Input: roundTo2DecimalPlaces(1.1949999999999999D) => Output: 1.19D

Input: roundTo2DecimalPlaces(1.1950000000000001D) => Output: 1.20D

Input: roundTo2DecimalPlaces(-1.1849999999999999D) => Output: -1.18D

Input: roundTo2DecimalPlaces(-1.1850000000000001D) => Output: -1.19D

Input: roundTo2DecimalPlaces(1.1849999999999999D) => Output: 1.18D

Input: roundTo2DecimalPlaces(1.1850000000000001D) => Output: 1.19D

```

#

<br />

# Challenge 026 Simple Frequency Sort

My solution -> *[P026SimpleFrequencySort](P026SimpleFrequencySort/Solution.java)*

## **_Task condition:_**

You have to sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

```
Solution.sortByFrequency(new int[]{2, 3, 5, 3, 7, 9, 5, 3, 7});
// Returns [3, 3, 3, 5, 5, 7, 7, 2, 9]
// We sort by highest frequency to lowest frequency.
// If two elements have same frequency, we sort by increasing value.
```

**_Examples_**

```
Input: Arrays.toString(sortByFrequency(new int[]{2, 3, 5, 3, 7, 9, 5, 3, 7})); => Output: [3, 3, 3, 5, 5, 7, 7, 2, 9]

Input: Arrays.toString(sortByFrequency(new int[]{1, 2, 3, 0, 5, 0, 1, 6, 8, 8, 6, 9, 1})); => Output: [1, 1, 1, 0, 0, 6, 6, 8, 8, 2, 3, 5, 9]

Input: Arrays.toString(sortByFrequency(new int[]{5, 9, 6, 9, 6, 5, 9, 9, 4, 4})); => Output: [9, 9, 9, 9, 4, 4, 5, 5, 6, 6]

Input: Arrays.toString(sortByFrequency(new int[]{4, 4, 2, 5, 1, 1, 3, 3, 2, 8})); => Output: [1, 1, 2, 2, 3, 3, 4, 4, 5, 8]

Input: Arrays.toString(sortByFrequency(new int[]{4, 9, 5, 0, 7, 3, 8, 4, 9, 0})); => Output: [0, 0, 4, 4, 9, 9, 3, 5, 7, 8]
```

#

<br />

# Challenge 027 Removing Each Second Person From A Circle

My solution -> *[P027RemovingEachSecondPersonFromACircle](P027RemovingEachSecondPersonFromACircle/CircleOfPeople.java)*

## **_Task condition:_**

You will be given list of names of people who are standing in circle. While counting off by twos in circle, each second leaves, until only one person is left standing. Return the list of people in order of their leaving.

Example:

1. [Bob, Lorna, Desiree, Melissa, Josh]
2. [Bob, Desiree, Melissa, Josh] - Lorna leaves
3. [Bob, Desiree, Josh] - Melissa leaves
4. [Desiree, Josh] - Bob leaves
5. [Desiree] - Josh leaves

The resulting list that should be returned is [Lorna, Melissa, Bob, Josh]

**_Examples_**

```
List<String> list = new ArrayList<>(Arrays.asList("Bob", "Lorna", "Desiree", "Melissa", "Josh"));

Input: crossingOut(list) => Output: [Lorna, Melissa, Bob, Josh]

```

#

<br />

# Challenge 028 Sums Of Parts

My solution -> *[P028SumsOfParts](P028SumsOfParts/SumParts.java)*

## **_Task condition:_**

Let us consider this example (array written in general format):

`ls = [0, 1, 3, 6, 10]`

Its following parts:

```
ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
```

The corresponding sums are (put together in an array): `[20, 20, 19, 16, 10, 0]`

The method `sumParts()` will take as parameter an array `ls` and return an array of the sums of its parts as defined above.

**_Examples_**

```
int[] ls1 = new int[0];

Input: sumParts(ls1) => Output: [0]

int[] ls2 = {0, 1, 3, 6, 10};

Input: sumParts(ls2) => Output: [20, 20, 19, 16, 10, 0]

int[] ls3 = {1, 2, 3, 4, 5, 6};

Input: sumParts(ls3) => Output: [21, 20, 18, 15, 11, 6, 0]

int[] ls4 = {744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358};

Input: sumParts(ls4) => Output: [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
```

**_Notes_**

- Take a look at performance: some arrays have thousands of elements.

#

<br />