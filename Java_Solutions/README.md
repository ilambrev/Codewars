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