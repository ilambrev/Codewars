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