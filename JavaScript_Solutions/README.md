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

# Challenge 007 Extract the domain name from a URL

My solution -> *[007ExtractTheDomainNameFromAURL](007ExtractTheDomainNameFromAURL.js)*

<br/>

## **_Task condition:_**

<br/>

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

<br/>

**_Examples_**

url = "http://github.com/carbonfive/raygun" -> domain name = "github"

url = "http://www.zombie-bites.com" -> domain name = "zombie-bites"

url = "https://www.cnet.com" -> domain name = cnet"

#

<br/>

# Challenge 008 Write Number in Expanded Form

My solution -> *[008WriteNumberInExpandedForm](008WriteNumberInExpandedForm.js)*

<br/>

## **_Task condition:_**

<br/>

You will be given a number and you will need to return it as a string in Expanded Form. For example:

<br/>

**_Examples_**

expandedForm(12); => Should return '10 + 2'

expandedForm(42); => Should return '40 + 2'

expandedForm(70304); => Should return '70000 + 300 + 4'

<br>

**_NOTE:_**

All numbers will be whole numbers greater than 0.

#

<br/>

# Challenge 009 Array Diff

My solution -> *[009ArrayDiff](009ArrayDiff.js)*

<br/>

## **_Task condition:_**

<br/>

Your goal is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

If a value is present in b, all of its occurrences must be removed from the other.

<br/>

**_Examples_**

arrayDiff([1,2],[1]) == [2]

arrayDiff([1,2,2,2,3],[2]) == [1,3]

#

<br/>

# Challenge 010 The Vowel Code

My solution -> *[010TheVowelCode](010TheVowelCode.js)*

<br/>

## **_Task condition:_**

<br/>

Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1  
e -> 2  
i -> 3  
o -> 4  
u -> 5  

Then create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

<br/>

**_Examples_**

encode("hello") would return "h2ll4"

decode("h3 th2r2") would return "hi there"

<br>

**_NOTE:_**

There is no need to worry about uppercase vowels. For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

#

<br/>

# Challenge 011 Stop Spinning My Words

My solution -> *[011StopSpinningMyWords](011StopSpinningMyWords.js)*

<br/>

## **_Task condition:_**

<br/>

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed.

<br/>

**_Examples_**

"Hey fellow warriors" => "Hey wollef sroirraw"

"This is a test" => "This is a test"

"This is another test" => "This is rehtona test"

<br>

**_NOTE:_**

Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

#

<br/>