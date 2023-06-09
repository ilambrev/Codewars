# Challenge 001 Replace With Alphabet Position

My solution -> *[001ReplaceWithAlphabetPosition](001ReplaceWithAlphabetPosition.js)*

<br/>

## **_Task condition:_**

<br/>

You are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

<br/>

**_Examples_**

alphabetPosition("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

alphabetPosition("The narwhal bacons at midnight.")

Should return "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20" ( as a string )

#

<br/>

# Challenge 002 Sum of two lowest positive integers

My solution -> *[002SumOfTwoLowestPositiveIntegers](002SumOfTwoLowestPositiveIntegers.js)*

<br/>

## **_Task condition:_**

<br/>

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

<br/>

**_Examples_**

When an array is passed like:

[19, 5, 42, 2, 77], the output should be 7, 

[10, 343445353, 3453445, 3453545353453] should return 3453455.

#

<br/>

# Challenge 003 Mumbling

My solution -> *[003Mumbling](003Mumbling.js)*

<br/>

## **_Task condition:_**

<br/>

This time no story, no theory. The examples below show you how to write function accum.

<br/>

**_Examples_**

accum("abcd") --> "A-Bb-Ccc-Dddd"

accum("RqaEzty") --> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

accum("cwAt") --> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

#

<br/>

# Challenge 004 Isograms

My solution -> *[004Isograms](004Isograms.js)*

<br/>

## **_Task condition:_**

<br/>

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

<br/>

**_Examples_**

isIsogram("Dermatoglyphics") --> true

isIsogram("aba") --> false

isIsogram("moOse") --> false

Ignore letter case.

#

<br/>

# Challenge 005 Two to One

My solution -> *[005TwoToOne](005TwoToOne.js)*

<br/>

## **_Task condition:_**

<br/>

Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

<br/>

**_Examples_**

s1 = "xyaabbbccccdefww"

s2 = "xxxxyyyyabklmopq"

longest(s1, s2) -> "abcdefklmopqwxy"

<br>

s1 = "abcdefghijklmnopqrstuvwxyz"

longest(s1, s1) -> "abcdefghijklmnopqrstuvwxyz"

#

<br/>

# Challenge 006 Highest Scoring Word

My solution -> *[006HighestScoringWord](006HighestScoringWord.js)*

<br/>

## **_Task condition:_**

<br/>

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

<br/>

**_Examples_**

high('man i need a taxi up to ubud') --> 'taxi'

high('what time are we climbing up the volcano') --> 'volcano'

#

<br/>