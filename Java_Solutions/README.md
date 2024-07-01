# Challenge 001 Split Strings

My solution -> *[P001SplitStrings](P001SplitStrings/StringSplit.java)*

<br/>

## **_Task condition:_**

<br/>

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

<br/>

**_Examples_**

'abc' =>  ['ab', 'c_']

'abcdef' => ['ab', 'cd', 'ef']

#

<br/>

# Challenge 002 Duplicate Encoder

My solution -> *[P002DuplicateEncoder](P002DuplicateEncoder/DuplicateEncoder.java)*

<br/>

## **_Task condition:_**

<br/>

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

<br/>

**_Examples_**

"din"      =>  "((("

"recede"   =>  "()()()"

"Success"  =>  ")())())"

"(( @"     =>  "))((" 

<br/>

**_Notes_**

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

#

<br/>

# Challenge 003 Sum of Numbers

My solution -> *[P003SumOfNumbers](P003SumOfNumbers/Sum.java)*

<br/>

## **_Task condition:_**

<br/>

Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

<br/>

**_Examples_**

(a, b) --> output (explanation)

(1, 0) --> 1 (1 + 0 = 1)

(1, 2) --> 3 (1 + 2 = 3)

(0, 1) --> 1 (0 + 1 = 1)

(1, 1) --> 1 (1 since both are same)

(-1, 0) --> -1 (-1 + 0 = -1)

(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

<br/>

**_Notes_**

a and b are not ordered!

#

<br/>

# Challenge 004 Sum of odd numbers

My solution -> *[P004SumOfOddNumbers](P004SumOfOddNumbers/RowSumOddNumbers.java)*

<br/>

## **_Task condition:_**

<br/>

Given the triangle of consecutive odd numbers:

                 1
              3     5
           7     9    11
       13    15    17    19
    21    23    25    27    29
    ...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

<br/>

**_Examples_**

1 -->  1

2 --> 3 + 5 = 8

#

<br/>

# Challenge 005 Break camelCase

My solution -> *[P005BreakCamelCase](P005BreakCamelCase/Solution.java)*

<br/>

## **_Task condition:_**

<br/>

Complete the solution so that the function will break up camel casing, using a space between words.

<br/>

**_Examples_**

"camelCasing"  =>  "camel Casing"

"identifier"   =>  "identifier"

""             =>  ""

#

<br/>

# Challenge 006 Create Phone Number

My solution -> *[P006CreatePhoneNumber](P006CreatePhoneNumber/Kata.java)*

<br />

## **_Task condition:_**

<br />

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

The returned format must be correct in order to complete this challenge.

<br />

**_Examples_**

Input: Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) => Output: '(123) 456-7890'

<br />

**_NOTES:_**

Don't forget the space after the closing parentheses!

#

<br />

# Challenge 007 Count characters in your string

My solution -> *[P007CountCharactersInYourString](P007CountCharactersInYourString/Kata.java)*

<br />

## **_Task condition:_**

<br />

The main idea is to count all the occurring characters in a string.

<br />

**_Examples_**

Input: "aba" => Output: {'a': 2, 'b': 1}

<br />

**_NOTES:_**

If the string is empty the result should be empty object literal, {}

#

<br />