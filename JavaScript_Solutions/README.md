# Challenge 001 Replace With Alphabet Position

My solution -> *[001ReplaceWithAlphabetPosition](001ReplaceWithAlphabetPosition.js)*

<br />

## **_Task condition:_**

<br />

You are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

<br />

**_Examples_**

alphabetPosition("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

alphabetPosition("The narwhal bacons at midnight.")

Should return "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20" ( as a string )

#

<br />

# Challenge 002 Sum of two lowest positive integers

My solution -> *[002SumOfTwoLowestPositiveIntegers](002SumOfTwoLowestPositiveIntegers.js)*

<br />

## **_Task condition:_**

<br />

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

<br />

**_Examples_**

When an array is passed like:

[19, 5, 42, 2, 77], the output should be 7, 

[10, 343445353, 3453445, 3453545353453] should return 3453455.

#

<br />

# Challenge 003 Mumbling

My solution -> *[003Mumbling](003Mumbling.js)*

<br />

## **_Task condition:_**

<br />

This time no story, no theory. The examples below show you how to write function accum.

<br />

**_Examples_**

accum("abcd") --> "A-Bb-Ccc-Dddd"

accum("RqaEzty") --> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

accum("cwAt") --> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

#

<br />

# Challenge 004 Isograms

My solution -> *[004Isograms](004Isograms.js)*

<br />

## **_Task condition:_**

<br />

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

<br />

**_Examples_**

isIsogram("Dermatoglyphics") --> true

isIsogram("aba") --> false

isIsogram("moOse") --> false

Ignore letter case.

#

<br />

# Challenge 005 Two to One

My solution -> *[005TwoToOne](005TwoToOne.js)*

<br />

## **_Task condition:_**

<br />

Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

<br />

**_Examples_**

s1 = "xyaabbbccccdefww"

s2 = "xxxxyyyyabklmopq"

longest(s1, s2) -> "abcdefklmopqwxy"

<br />

s1 = "abcdefghijklmnopqrstuvwxyz"

longest(s1, s1) -> "abcdefghijklmnopqrstuvwxyz"

#

<br />

# Challenge 006 Highest Scoring Word

My solution -> *[006HighestScoringWord](006HighestScoringWord.js)*

<br />

## **_Task condition:_**

<br />

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

<br />

**_Examples_**

high('man i need a taxi up to ubud') --> 'taxi'

high('what time are we climbing up the volcano') --> 'volcano'

#

<br />

# Challenge 007 Extract the domain name from a URL

My solution -> *[007ExtractTheDomainNameFromAURL](007ExtractTheDomainNameFromAURL.js)*

<br />

## **_Task condition:_**

<br />

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

<br />

**_Examples_**

url = "http://github.com/carbonfive/raygun" -> domain name = "github"

url = "http://www.zombie-bites.com" -> domain name = "zombie-bites"

url = "https://www.cnet.com" -> domain name = cnet"

#

<br />

# Challenge 008 Write Number in Expanded Form

My solution -> *[008WriteNumberInExpandedForm](008WriteNumberInExpandedForm.js)*

<br />

## **_Task condition:_**

<br />

You will be given a number and you will need to return it as a string in Expanded Form. For example:

<br />

**_Examples_**

expandedForm(12); => Should return '10 + 2'

expandedForm(42); => Should return '40 + 2'

expandedForm(70304); => Should return '70000 + 300 + 4'

<br />

**_NOTES:_**

All numbers will be whole numbers greater than 0.

#

<br />

# Challenge 009 Array Diff

My solution -> *[009ArrayDiff](009ArrayDiff.js)*

<br />

## **_Task condition:_**

<br />

Your goal is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

If a value is present in b, all of its occurrences must be removed from the other.

<br />

**_Examples_**

arrayDiff([1,2],[1]) == [2]

arrayDiff([1,2,2,2,3],[2]) == [1,3]

#

<br />

# Challenge 010 The Vowel Code

My solution -> *[010TheVowelCode](010TheVowelCode.js)*

<br />

## **_Task condition:_**

<br />

Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1  
e -> 2  
i -> 3  
o -> 4  
u -> 5  

Then create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

<br />

**_Examples_**

encode("hello") would return "h2ll4"

decode("h3 th2r2") would return "hi there"

<br />

**_NOTES:_**

There is no need to worry about uppercase vowels. For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

#

<br />

# Challenge 011 Stop Spinning My Words

My solution -> *[011StopSpinningMyWords](011StopSpinningMyWords.js)*

<br />

## **_Task condition:_**

<br />

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed.

<br />

**_Examples_**

"Hey fellow warriors" => "Hey wollef sroirraw"

"This is a test" => "This is a test"

"This is another test" => "This is rehtona test"

<br />

**_NOTES:_**

Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

#

<br />

# Challenge 012 Highest And Lowest

My solution -> *[012HighestAndLowest](012HighestAndLowest.js)*

<br />

## **_Task condition:_**

<br />

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

<br />

**_Examples_**

highAndLow("1 2 3 4 5"); => return "5 1"

highAndLow("1 2 -3 4 5"); => return "5 -3"

highAndLow("1 9 3 4 -5"); => return "9 -5"

<br />

**_NOTES:_**

All numbers are valid Int32, no need to validate them.

There will always be at least one number in the input string.

Output string must be two numbers separated by a single space, and highest number is first.

#

<br />

# Challenge 013 Exes And Ohs

My solution -> *[013ExesAndOhs](013ExesAndOhs.js)*

<br />

## **_Task condition:_**

<br />

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

<br />

**_Examples_**

XO("ooxx") => true

XO("xooxx") => false

XO("ooxXm") => true

XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true

XO("zzoo") => false

#

<br />

# Challenge 014 Friend or Foe

My solution -> *[014FriendOrFoe](014FriendOrFoe.js)*

<br />

## **_Task condition:_**

<br />

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

<br />

**_Examples_**

Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

Input = ["Ryan", "Kieran", "Mark"], Output = ["Ryan", "Mark"]

<br />

**_NOTES:_**

Keep the original order of the names in the output.

#

<br />

# Challenge 015 Growth of a Population

My solution -> *[015GrowthOfAPopulation](015GrowthOfAPopulation.js)*

<br />

## **_Task condition:_**

<br />

In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?

At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.

More generally given parameters:

p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

the function nbYear should return n number of entire years needed to get a population greater or equal to p.

aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

<br />

**_Examples_**

nbYear(1500, 5, 100, 5000) -> 15

nbYear(1500000, 2.5, 10000, 2000000) -> 10

<br />

**_NOTES:_**

Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.

There are no fractions of people. At the end of each year, the population count is an integer: 252.8 people round down to 252 persons.

#

<br />

# Challenge 016 String ends with

My solution -> *[016StringEndsWith](016StringEndsWith.js)*

<br />

## **_Task condition:_**

<br />

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). 

<br />

**_Examples_**

solution('abc', 'bc') // returns true

solution('abc', 'd') // returns false

#

<br />

# Challenge 017 Descending Order

My solution -> *[017DescendingOrder](017DescendingOrder.js)*

<br />

## **_Task condition:_**

<br />

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

<br />

**_Examples_**

Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

#

<br />

# Challenge 018 Sum Strings as Numbers

My solution -> *[018SumStringsAsNumbers](018SumStringsAsNumbers.js)*

<br />

## **_Task condition:_**

<br />

Given the string representations of two integers, return the string representation of the sum of those integers.

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

<br />

**_Examples_**

sumStrings('1','2')  => '3'

#

<br />

# Challenge 019 Next smaller number with the same digits

My solution -> *[019NextSmallerNumberWithTheSameDigits](019NextSmallerNumberWithTheSameDigits.js)*

<br />

## **_Task condition:_**

<br />

Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

Return -1 when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

<br />

**_Examples_**

nextSmaller(21) == 12

nextSmaller(531) == 513

nextSmaller(2071) == 2017

nextSmaller(9) == -1

nextSmaller(111) == -1

nextSmaller(135) == -1

nextSmaller(1027) == -1 => 0721 is out since we don't write numbers with leading zeros

<br />

**_NOTES:_**

Some tests will include very large numbers.

Test data only employs positive integers.

#

<br />

# Challenge 020 Human Readable Time

My solution -> *[020HumanReadableTime](020HumanReadableTime.js)*

<br />

## **_Task condition:_**

<br />

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

<br />

**_Examples_**

humanReadable(0) => 00:00:00

humanReadable(59) => 00:00:59

humanReadable(60) => 00:01:00

humanReadable(90) => 00:01:30

humanReadable(3599) => 00:59:59

humanReadable(3600) => 01:00:00

humanReadable(45296) => 12:34:56

humanReadable(86399) => 23:59:59

humanReadable(86400) => 24:00:00

humanReadable(359999) => 99:59:59

#

<br />

# Challenge 021 Multiples of 3 or 5

My solution -> *[021MultiplesOf3Or5](021MultiplesOf3Or5.js)*

<br />

## **_Task condition:_**

<br />

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

<br />

**_Examples_**

solution(10) => 23

<br />

**_NOTES:_**

If the number is a multiple of both 3 and 5, only count it once.

#

<br />

# Challenge 022 Convert string to camel case

My solution -> *[022ConvertStringToCamelCase](022ConvertStringToCamelCase.js)*

<br />

## **_Task condition:_**

<br />

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

<br />

**_Examples_**

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

#

<br />

# Challenge 023 Sum of Digits / Digital Root

My solution -> *[023SumOfDigitsDigitalRoot](023SumOfDigitsDigitalRoot.js)*

<br />

## **_Task condition:_**

<br />

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

<br />

**_Examples_**

16 --> 1 + 6 = 7

942 --> 9 + 4 + 2 = 15  -->  1 + 5 = 6

132189 --> 1 + 3 + 2 + 1 + 8 + 9 = 24 --> 2 + 4 = 6

493193 --> 4 + 9 + 3 + 1 + 9 + 3 = 29 --> 2 + 9 = 11 --> 1 + 1 = 2

#

<br />

# Challenge 024 Split Strings

My solution -> *[024SplitStrings](024SplitStrings.js)*

<br />

## **_Task condition:_**

<br />

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

<br />

**_Examples_**

'abc' =>  ['ab', 'c_']

'abcdef' => ['ab', 'cd', 'ef']

#

<br />

# Challenge 025 Reversed Strings

My solution -> *[025ReversedStrings](025ReversedStrings.js)*

<br />

## **_Task condition:_**

<br />

Complete the solution so that it reverses the string passed into it.

<br />

**_Examples_**

'world' => 'dlrow'

'word' => 'drow'

#

<br />

# Challenge 026 Sum of positive

My solution -> *[026SumOfPositive](026SumOfPositive.js)*

<br />

## **_Task condition:_**

<br />

You get an array of numbers, return the sum of all of the positives ones.

<br />

**_Examples_**

[1, -4, 7, 12] => 1 + 7 + 12 = 20

<br />

**_NOTES:_**

If there is nothing to sum, the sum is default to 0.

#

<br />

# Challenge 027 Sort the odd

My solution -> *[027SortTheOdd](027SortTheOdd.js)*

<br />

## **_Task condition:_**

<br />

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

<br />

**_Examples_**

[7, 1]  =>  [1, 7]

[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

#

<br />

# Challenge 028 Remove String Spaces

My solution -> *[028RemoveStringSpaces](028RemoveStringSpaces.js)*

<br />

## **_Task condition:_**

<br />

Write a function that removes the spaces from the string, then return the resultant string.

<br />

**_Examples_**

"8 j 8 &nbsp; &nbsp; &nbsp; mBliB8g &nbsp; &nbsp; imjB8B8 &nbsp; &nbsp; jl &nbsp; &nbsp; B" -> "8j8mBliB8gimjB8B8jlB"

"8 8 Bi fk8h B 8 BB8B B B &nbsp; &nbsp; B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"

"8aaaaa dddd r &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;" -> "8aaaaaddddr"

#

<br />

# Challenge 029 Convert number to reversed array of digits

My solution -> *[029ConvertNumberToReversedArrayOfDigits](029ConvertNumberToReversedArrayOfDigits.js)*

<br />

## **_Task condition:_**

<br />

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

<br />

**_Examples_**

35231 => [1,3,2,5,3]

0 => [0]

#

<br />

# Challenge 030 Sum Arrays

My solution -> *[030SumArrays](030SumArrays.js)*

<br />

## **_Task condition:_**

<br />

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

<br />

**_Examples_**

Input: [1, 5.2, 4, 0, -1] => Output: 9.2

Input: [] => Output: 0

Input: [-2.398] => Output: -2.398

<br />

**_ASSUMPTIONS:_**

You can assume that you are only given numbers.

You cannot assume the size of the array.

You can assume that you do get an array and if the array is empty, return 0.

#

<br />

# Challenge 031 Your order, please

My solution -> *[031YourOrderPlease](031YourOrderPlease.js)*

<br />

## **_Task condition:_**

<br />

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

<br />

**_Examples_**

"is2 Thi1s T4est 3a" => "Thi1s is2 3a T4est"

"4of Fo1r pe6ople g3ood th5e the2" => "Fo1r the2 g3ood 4of th5e pe6ople"

"" => ""

<br />

**_NOTES:_**

Numbers can be from 1 to 9. So 1 will be the first word (not 0).

#

<br />

# Challenge 032 Odd or Even?

My solution -> *[032OddOrEven](032OddOrEven.js)*

<br />

## **_Task condition:_**

<br />

Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

<br />

**_Examples_**

Input: [0] => Output: "even"

Input: [0, 1, 4] => Output: "odd"

Input: [0, -1, -5] => Output: "even"

#

<br />

# Challenge 033 Reversed sequence

My solution -> *[033ReversedSequence](033ReversedSequence.js)*

<br />

## **_Task condition:_**

<br />

Build a function that returns an array of integers from n to 1 where n>0.

<br />

**_Examples_**

Input: n=5 => Output: [5,4,3,2,1]

#

<br />

# Challenge 034 Century From Year

My solution -> *[034CenturyFromYear](034CenturyFromYear.js)*

<br />

## **_Task condition:_**

<br />

The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Given a year, return the century it is in.

<br />

**_Examples_**

1705 --> 18

1900 --> 19

1601 --> 17

2000 --> 20

2742 --> 28

#

<br />

# Challenge 035 Directions Reduction

My solution -> *[035DirectionsReduction](035DirectionsReduction.js)*

<br />

## **_Task condition:_**

<br />

Once upon a time, on a way through the old wild mountainous west,…

… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.


Write a function which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

<br />

**_Examples_**

Input: => ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], Output: => ["WEST"]

Input: => ["NORTH", "SOUTH", "EAST", "WEST"], Output: => []

Input: => ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], Output: => ["WEST", "WEST"]

<br />

**_NOTES:_**

Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

#

<br />

# Challenge 036 Square(n) Sum

My solution -> *[036SquareNSum](036SquareNSum.js)*

<br />

## **_Task condition:_**

<br />

Complete the square sum function so that it squares each number passed into it and then sums the results together.

<br />

**_Examples_**

Input: [1, 2, 2] => Output: 9

#

<br />

# Challenge 037 Delete occurrences of an element if it occurs more than n times

My solution -> *[037DeleteOccurrencesOfAnElementIfItOccursMoreThanNtimes](037DeleteOccurrencesOfAnElementIfItOccursMoreThanNtimes.js)*

<br />

## **_Task condition:_**

<br />

Given a list and a number, create a new list that contains each number of list at most N times, without reordering.

<br />

**_Examples_**

Input list is [1,2,3,1,2,1,2,3] and the input number is 2 => result is [1,2,3,1,2,3];

Input list is [20,37,20,21] and the input number is 1 => result is [20,37,21];

#

<br />

# Challenge 038 Playing with digits

My solution -> *[038PlayingWithDigits](038PlayingWithDigits.js)*

<br />

## **_Task condition:_**

<br />

Some numbers have funny properties. For example:

    89 --> 8¹ + 9² = 89 * 1
    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that:

<em>(a<sup>p</sup> + b<sup>p+1</sup> + c<sup>p+2</sup> + d<sup>p+3</sup> + ...) = n ∗ k</em>

If it is the case we will return k, if not return -1.

<br />

**_Examples_**

Input: n = 89; p = 1 => Output: 1

Input: n = 92; p = 1 => Output: -1

Input: n = 695; p = 2 => Output: 2

Input: n = 46288; p = 3 => Output: 51

<br />

**_NOTES:_**

n and p will always be strictly positive integers.

#

<br />

# Challenge 039 Counting Duplicates

My solution -> *[039CountingDuplicates](039CountingDuplicates.js)*

<br />

## **_Task condition:_**

<br />

Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

<br />

**_Examples_**

Input: "abcde" => Output: 0

Input: "aabbcde" => Output: 2

Input: "aabBcde" => Output: 2

Input: "indivisibility" => Output: 1

Input: "Indivisibilities" => Output: 2

Input: "aA11" => Output: 2

Input: "ABBA" => Output: 2

#

<br />

# Challenge 040 Count by X

My solution -> *[040CountByX](040CountByX.js)*

<br />

## **_Task condition:_**

<br />

Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array.

<br />

**_Examples_**

countBy(1,10) === [1,2,3,4,5,6,7,8,9,10]

countBy(2,5) === [2,4,6,8,10]

#

<br />

# Challenge 041 Reverse words

My solution -> *[041ReverseWords](041ReverseWords.js)*

<br />

## **_Task condition:_**

<br />

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

<br />

**_Examples_**

Input: "This is an example!" => Output: "sihT si na !elpmaxe"

Input: "double &nbsp; &nbsp; spaces" => Output: "elbuod &nbsp; &nbsp; secaps"

#

<br />

# Challenge 042 Rock Paper Scissors

My solution -> *[042RockPaperScissors](042RockPaperScissors.js)*

<br />

## **_Task condition:_**

<br />

Let's play! You have to return which player won! In case of a draw return Draw!.

<br />

**_Examples_**

Input: "scissors", "paper" => Output: "Player 1 won!"

Input: "scissors", "rock" => Output: "Player 2 won!"

Input: "paper", "paper" => Output: "Draw!"

#

<br />

# Challenge 043 Remove the minimum

My solution -> *[043RemoveTheMinimum](043RemoveTheMinimum.js)*

<br />

## **_Task condition:_**

<br />

Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array, return an empty array.

Don't change the order of the elements that are left.

<br />

**_Examples_**

Input: [1,2,3,4,5] => Output: [2,3,4,5]

Input: [5,3,2,1,4] => Output: [5,3,2,4]

Input: [2,2,1,2,1] => Output: [2,2,2,1]

#

<br />

# Challenge 044 Count of positives / sum of negatives

My solution -> *[044CountOfPositivesSumOfNegatives](044CountOfPositivesSumOfNegatives.js)*

<br />

## **_Task condition:_**

<br />

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

<br />

**_Examples_**

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15] => Output: [10, -65]

#

<br />

# Challenge 045 Sum of Intervals

My solution -> *[045SumOfIntervals](045SumOfIntervals.js)*

<br />

## **_Task condition:_**

<br />

Write a function called sumIntervals that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

<br />

**_Examples_**

Input: [[1, 4], [7, 10], [3, 5]] => Output: 7

Input: [[1, 2], [6, 10], [11, 15]] => Output: 9

Input: [[1, 4], [7, 10], [3, 5]] => Output: 7

Input: [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]] => Output: 19

Input: [[0, 20], [-100000000, 10], [30, 40]] => Output: 100000030

#

<br />

# Challenge 046 Sum of Intervals

My solution -> *[046SquareEveryDigit](046SquareEveryDigit.js)*

<br />

## **_Task condition:_**

<br />

Square every digit of a number and concatenate them.

<br />

**_Examples_**

Input: 9119 => Output: 811181

Input: 765 => Output: 493625

<br />

**_NOTES:_**

The function accepts an integer and returns an integer.

#

<br />

# Challenge 047 Persistent Bugger

My solution -> *[047PersistentBugger](047PersistentBugger.js)*

<br />

## **_Task condition:_**

<br />

Write a function **_persistence_** that takes in a positive parameter **_num_** and returns its multiplicative persistence, which is the number of times you must multiply the digits in **_num_** until you reach a single digit.

<br />

**_Examples_**

Input: 39 => Output: 3

Input: 999 => Output: 4

Input: 4 => Output: 0

#

<br />

# Challenge 048 Regex validate PIN code

My solution -> *[048RegexValidatePINCode](048RegexValidatePINCode.js)*

<br />

## **_Task condition:_**

<br />

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return **_true_**, else return **_false_**.

<br />

**_Examples_**

Input: '1234' => Output: true

Input: '12345' => Output: false

Input: 'a234' => Output: false

#

<br />

# Challenge 049 Generate Chat Room Names

My solution -> *[049GenerateChatRoomNames](049GenerateChatRoomNames.js)*

<br />

## **_Task condition:_**

<br />

You are writing a chat room app for your company.

Users have provided feedback that seeing everyone's full names on the screen creates too much noise, and have asked for it to be reduced. However, we still want to be able to uniquely identify everyone.

Rules:

1.If only one person in the chat room has a specific first name, only their first name will be written out.

John Smith -> John

2.If two or more people have a specific first name, but don't share a second name initial, their first name and second name initial will be written out.

John Smith -> John S

John Adams -> John A

3.Finally, if two or more people have a specific first name and last name initial, their full name will be written out.

John Smith -> John Smith    

John Simms -> John Simms

To help tidy up the output, management have also asked that the chat room list should be alphabetised, by the users screen names and should all be in Title Case. 

<br />

**_Examples_**

Input: ['Joe Bloggs', 'John Smith'] => Output: ['Joe', 'John']

Input: ['Joe Bloggs', 'John Smith', 'Jane Doe'] => Output: ['Jane', 'Joe', 'John']

Input: ['Joe Bloggs', 'John Smith', 'Jane Doe', 'Jane Bloggs'] => Output: ['Jane B', 'Jane D', 'Joe', 'John']

Input: ['Joe Bloggs', 'John Smith', 'Jane Doe', 'Jane Bloggs', 'John Scott'] => Output: ['Jane B', 'Jane D', 'Joe', 'John Scott', 'John Smith']

<br />

**_NOTES:_**

It can be assumed that names are in the format of a first name and a last name consisting solely of letters from the English alphabet, both uppercase (A-Z) and lowercase (a-z), separated by a single space and if no names are provided, we should return an empty array.

Casing is not important, meaning JOHn SmiTh is equal to john smith, after we've tidied up the casings, these should be interpreted as the same name.

You don't have to worry about multiple instances of the same full name.

#

<br />

# Challenge 050 Which are in?

My solution -> *[050WhichAreIn](050WhichAreIn.js)*

<br />

## **_Task condition:_**

<br />

Given two arrays of strings **_a1_** and **_a2_** return a sorted array **_r_** in lexicographical order of the strings of **_a1_** which are substrings of strings of **_a2_**.

<br />

**_Examples_**

Input: a1 = ['arp', 'live', 'strong'], a2 = ['lively', 'alive', 'harp', 'sharp', 'armstrong'] => Output: ['arp', 'live', 'strong']

Input: a1 = ['tarp', 'mice', 'bull'], a2 = ['lively', 'alive', 'harp', 'sharp', 'armstrong'] => Output: []

#

<br />

# Challenge 051 First non-repeating character

My solution -> *[051FirstNonRepeatingCharacter](051FirstNonRepeatingCharacter.js)*

<br />

## **_Task condition:_**

<br />

Write a function that takes a string input, and returns the first character that is not repeated anywhere in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter.

If a string contains all repeating characters, it should return an empty string ("");

<br />

**_Examples_**

Input: 'stress' => Output: t

Input: 'sTreSS' => Output: T

#

<br />

# Challenge 052 Find the unique string

My solution -> *[052FindTheUniqueString](052FindTheUniqueString.js)*

<br />

## **_Task condition:_**

<br />

There is an array of strings. All strings contains similar letters except one. Try to find it!

<br />

**_Examples_**

Input: ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a'] => Output: 'BbBb'

Input: ['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba'] => Output: 'foo'

<br />

**_NOTES:_**

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.

#

<br />

# Challenge 053 The Hashtag Generator

My solution -> *[053TheHashtagGenerator](053TheHashtagGenerator.js)*

<br />

## **_Task condition:_**

<br />

Write a function that generates hashtag from given string.

- It must start with a hashtag (#).

- All words must have their first letter capitalized.

- If the final result is longer than 140 chars it must return false.

- If the input or the result is an empty string it must return false.


<br />

**_Examples_**

Input: '&nbsp;Hello there thanks for trying my Kata' => Output: '#HelloThereThanksForTryingMyKata'

Input: '&nbsp;&nbsp;&nbsp;&nbsp;Hello&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;World&nbsp;&nbsp;&nbsp;' => Output: '#HelloWorld'

Input: '' => Output: false

#

<br />

# Challenge 054 Moving Zeros To The End

My solution -> *[054MovingZerosToTheEnd](054MovingZerosToTheEnd.js)*

<br />

## **_Task condition:_**

<br />

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


<br />

**_Examples_**

Input: [false,1,0,1,2,0,1,3,"a"] => Output: [false,1,1,2,1,3,"a",0,0]

#

<br />

# Challenge 055 Tic-Tac-Toe Checker

My solution -> *[055TicTacToeChecker](055TicTacToeChecker.js)*

<br />

## **_Task condition:_**

<br />

Create a function that will check Tic-Tac-Toe game current state.

Assume that the board comes in the form of a 3x3 array, where the value is **_0_** if a spot is empty, **_1_** if it is an **_"X"_**, or **_2_** if it is an **_"O"_**.

We want our function to return:

- **_-1_** if the board is not yet finished AND no one has won yet (there are empty spots),

- **_1_** if **_"X"_** won,

- **_2_** if **_"O"_** won,

- **_0_** if it's a cat's game (i.e. a draw).

<br />

**_Examples_**

Input:
```
[
    [0, 0, 1],
    [0, 1, 2],
    [2, 1, 0]
]
```

Output: -1

<br />

**_NOTES:_**

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

#

<br />

# Challenge 056 Vowel Count

My solution -> *[056VowelCount](056VowelCount.js)*

<br />

## **_Task condition:_**

<br />

Return the number (count) of vowels in the given string.

We will consider **_a_**, **_e_**, **_i_**, **_o_**, **_u_** as vowels for this Kata (but not **_y_**).

<br />

**_Examples_**

Input: 'abracadabra' => Output: 5

<br />

**_NOTES:_**

The input string will only consist of lower case letters and/or spaces.

#

<br />

# Challenge 057 String incrementer

My solution -> *[057StringIncrementer](057StringIncrementer.js)*

<br />

## **_Task condition:_**

<br />

Write a function which increments a string, to create a new string.

- If the string already ends with a number, the number should be incremented by 1.
- If the string does not end with a number. the number 1 should be appended to the new string.


<br />

**_Examples_**

Input: 'foo' => Output: 'foo1'

Input: 'foobar23' => Output: 'foobar24'

Input: 'foo0042' => Output: 'foo0043'

Input: 'foo9' => Output: 'foo10'

Input: 'foo099' => Output: 'foo100'

<br />

**_NOTES:_**

If the number has leading zeros the amount of digits should be considered.

#

<br />

# Challenge 058 Play with two Strings

My solution -> *[058PlayWithTwoStrings](058PlayWithTwoStrings.js)*

<br />

## **_Task condition:_**

<br />

Your task is to Combine two Strings - Input Strings **_a_** and **_b_**: For every character in string **_a_** swap the casing of every occurrence of the same character in string **_b_**. Then do the same casing swap with the inputs reversed. Return a single string consisting of the changed version of **_a_** followed by the changed version of **_b_**. A char of **_a_** is in **_b_** regardless if it's in upper or lower case - see the testcases too.

<br />

**_Examples_**

Input: 'abc' and 'cde' => Output: 'abCCde'

Input: 'ab' and 'aba' => Output: 'aBABA'

Input: 'abab' and 'bababa' => Output: 'ABABbababa'

<br />

**_NOTES:_**

You don't have to check errors or incorrect input values, everything is ok without bad tricks, only two input strings and as result one output string;

#

<br />

# Challenge 059 Luck check

My solution -> *[059LuckCheck](059LuckCheck.js)*

<br />

## **_Task condition:_**

<br />

Ticket was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half.

Your task is to write a funtion, which returns **_true_** if argument is string decimal representation of a lucky ticket number, or **_false_** for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.

<br />

**_Examples_**

Input: '003111' => Output: true

Input: '813372' => Output: true

Input: '17935' => Output: true

Input: '56328116' => Output: true

<br />

**_NOTES:_**

If the length of string is odd, you should ignore the middle number when adding the halves.

#

<br />

# Challenge 060 Bowling Pins

My solution -> *[060BowlingPins](060BowlingPins.js)*

<br />

## **_Task condition:_**

<br />

You have to throw a bowl into 10 Pins arranged like this:

```
I I I I
 I I I 
  I I  
   I    
```

Each Pin has a Number:

```
7 8 9 10
 4 5 6
  2 3
   1
```

You will get an array of integers between 1 and 10.

<br />

**_Examples_**

Input: [3, 5, 9]

Output: Return a string with the current field.

```
I I   I
 I   I
  I   
   I  
```

<br />

**_NOTES:_**

- The pins rows are separated by a newline (\n)
- Each Line must be 7 chars long
- Fill the missing pins with a space character ( )

#

<br />

# Challenge 061 English beggars

My solution -> *[061EnglishBeggars](061EnglishBeggars.js)*

<br />

## **_Task condition:_**

<br />

Given an array of values and an amount of beggars, you are supposed to return an array with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.

Also note that not all beggars have to take the same amount of "offers", meaning that the length of the array is not necessarily a multiple of n. Length can be even shorter, in which case the last beggars will of course take nothing (0).

<br />

**_Examples_**

Input: [1,2,3,4,5], 2 => Output: [9,6]

Input: [1,2,3,4,5], 3 => Output: [5,7,3]

<br />

**_NOTES:_**

Do not modify the input array.

#

<br />

# Challenge 062 Sorting by bits

My solution -> *[062SortingByBits](062SortingByBits.js)*

<br />

## **_Task condition:_**

<br />

You're expected to sort an array of 32-bit integers in ascending order of the number of on bits they have.

In cases where two numbers have the same number of bits, compare their real values instead.

E.g between 10 (...1010) and 12 (...1100), they both have the same number of on bits '2' but the integer 10 is less than 12 so it comes first in sorted order.

Your task is to write a function that takes an array of integers and sort them as described above.

<br />

**_Examples_**

Input: [7, 6, 15, 8] => Output: [8, 6, 7, 15]

Input: [3, 8, 3, 6, 5, 7, 9, 1] => Output: [1, 8, 3, 3, 5, 6, 9, 7]

<br />

**_NOTES:_**

Your solution has to sort the array in place.

#

<br />

# Challenge 063 Two Sum

My solution -> *[063TwoSum](063TwoSum.js)*

<br />

## **_Task condition:_**

<br />

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: [index1, index2].

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

<br />

**_Examples_**

Input: [1, 2, 3], 4 => Output: [0, 2] or [2, 0]

Input: [3, 2, 4], 6 => Output: [1, 2] or [2, 1]

<br />

**_NOTES:_**

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

#

<br />

# Challenge 064 Simple card game

My solution -> *[064SimpleCardGame](064SimpleCardGame.js)*

<br />

## **_Task condition:_**

<br />

Write a function called winner, representing simple card game. Steve and Josh are the two players. Figure out who is going to win.

Players are dealt the same number of cards. They both flip the card on the top of their deck. Whoever has a card with higher value wins the round and gets one point (if the cards are of the same value, neither of them gets a point). After this, the two cards are discarded and they flip another card from the top of their deck. They do this until they have no cards left.

**_deckSteve_** and **_deckJosh_** are arrays representing their decks. They are filled with cards, represented by a single character. The card rank is as follows (from lowest to highest):

```
'2','3','4','5','6','7','8','9','T','J','Q','K','A'
```

Figure out who is going to win and return who wins and with what score:

```
    "Steve wins x to y" if Steve wins; where x is Steve's score, y is Josh's score;

    "Josh wins x to y" if Josh wins; where x is Josh's score, y is Steve's score;

    "Tie" if the score is tied at the end of the game.
```

<br />

**_Examples_**

```
Input: deckSteve = ['A','7','8'], deckJosh = ['K','5','9'] => Output: "Steve wins 2 to 1"
```

<br />

**_NOTES:_**

Every card may appear in the deck more than once.

#

<br />

# Challenge 065 How much hex is the fish

My solution -> *[065HowMuchHexIsTheFish](065HowMuchHexIsTheFish.js)*

<br />

## **_Task condition:_**

<br />

The ocean is full of colorful fishes. We as programmers want to know the hexadecimal value of these fishes.

Take all hexadecimal valid characters (a,b,c,d,e,f) of the given name and XOR them. Return the result as an integer.

<br />

**_Examples_**

Input: 'redlionfish' => Output: 12

<br />

**_NOTES:_**

The input is always a string, which can contain spaces, upper and lower case letters but no digits. 

#

<br />

# Challenge 066 Cat and Mouse - Harder Version

My solution -> *[066CatAndMouseHarderVersion.js](066CatAndMouseHarderVersion.js)*

<br />

## **_Task condition:_**

<br />

You will be given a string **_(x)_** featuring a cat **_'C'_**, a dog **_'D'_** and a mouse **_'m'_**. The rest of the string will be made up of **_'.'_**.

You need to find out if the cat can catch the mouse from its current position. The cat can jump at most **_(j)_** characters, and cannot jump over the dog.

- If there are not more than **_j_** characters between the cat and the mouse, so cat can jump far enough and jump is not over dog, return **_'Caught!'_**

- If there are more than **_j_** characters between the two, the cat cannot jump far enough, return **_'Escaped!'_**

- If cat can jump far enough, but dog is in the way, protecting the mouse, return **_'Protected!'_**

- If not all three animals are present, return **_'boring without all three'_**

<br />

**_Examples_**

Input: '..C.....m...D', 5 => Output: 'Caught!'

Input: '.....C............m......D', 5 => Output: 'Escaped!'

Input: '...m.........C...D', 10 => Output: 'Caught!'

Input: '...m....D....C.......', 10 => Output: 'Protected!'

Input: '...m.........C....', 10 => 'boring without all three'

#

<br />

# Challenge 067 New Cashier Does Not Know About Space or Shift

My solution -> *[067NewCashierDoesNotKnowAboutSpaceOrShift](067NewCashierDoesNotKnowAboutSpaceOrShift.js)*

<br />

## **_Task condition:_**

<br />

Some new cashiers started to work at your restaurant.

They are good at taking orders, but they don't know how to capitalize words, or use a space bar!

All the orders they create look something like this:

```
"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
```

The kitchen staff are threatening to quit, because of how difficult it is to read the orders.

Their preference is to get the orders as a nice clean string with spaces and capitals like so:

```
"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
```

The kitchen staff expect the items to be in the same order as they appear in the menu.

The menu items are fairly simple, there is no overlap in the names of the items:

```
1. Burger
2. Fries
3. Chicken
4. Pizza
5. Sandwich
6. Onionrings
7. Milkshake
8. Coke
```

<br />

**_Examples_**

Input: 'milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza' => Output: 'Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke'

Input: 'pizzachickenfriesburgercokemilkshakefriessandwich' => Output: 'Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke'

#

<br />

# Challenge 068 Merged String Checker

My solution -> *[0068MergedStringChecker.js](068MergedStringChecker.js)*

<br />

## **_Task condition:_**

<br />

Write an algorithm to check if a given string, **_s_**, can be formed from two other strings, **_part1_** and **_part2_**.

The restriction is that the characters in **_part1_** and **_part2_** should be in the same order as in **_s_**.

<br />

**_Examples_**

Input: 'codewars', 'cdw', 'oears' => Output: true

Input: 'xcyc', 'xc', 'yc' => Output: true

Input: 'xcyc', 'yc', 'xc' => Output: true

Input: 'xcyc', 'xc', 'cy' => Output: true

Input: 'xcyc', 'cy', 'xc' => Output: true

Input: 'codewars', 'code', 'wars' => Output: true

Input: 'codewars', 'cdwr', 'oeas' => Output: true

Input: 'Making progress', 'Mak pross', 'inggre' => Output: true

Input: 'codewars', 'code', 'code' => Output: false

Input: 'More progress', 'More ess', 'pro' => Output: false

#

<br />

# Challenge 069 Convert PascalCase string into snake_case

My solution -> *[069ConvertPascalCaseStringIntoSnakeCase](069ConvertPascalCaseStringIntoSnakeCase.js)*

<br />

## **_Task condition:_**

<br />

Complete the function so that it takes a **_PascalCase_** string and returns the string in **_snake_case_** notation. Lowercase characters can be numbers. If the function gets a number as input, it should return a string.

<br />

**_Examples_**

```
Input: 'TestController' => Output: 'test_controller'

Input: 'MoviesAndBooks' => Output: 'movies_and_books'

Input: 'App7Test'       => Output: 'app7_test'

Input: 1                => Output: '1'
```

#

<br />

# Challenge 070 Sort the columns of a csv-file

My solution -> *[070SortTheColumnsOfaCSVFile](070SortTheColumnsOfaCSVFile.js)*

<br />

## **_Task condition:_**

<br />

You get a string with the content of a csv-file. The columns are separated by semicolons.

The first line contains the names of the columns.

Write a method that sorts the columns by the names of the columns alphabetically and incasesensitive. 

<br />

**_Examples_**

```
Before sorting:
As table (only visualization):
|myjinxin2015|raulbc777|smile67|Dentzil|SteffenVogel_79|
|17945       |10091    |10088  |3907   |10132          |
|2           |12       |13     |48     |11             |

The csv-file:
myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n
17945;10091;10088;3907;10132\n
2;12;13;48;11

----------------------------------

After sorting:
As table (only visualization):
|Dentzil|myjinxin2015|raulbc777|smile67|SteffenVogel_79|
|3907   |17945       |10091    |10088  |10132          |
|48     |2           |12       |13     |11             |

The csv-file:
Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n
3907;17945;10091;10088;10132\n
48;2;12;13;11
```
<br />

**_NOTES:_**

There is no need for prechecks. You will always get a correct string with more than 1 line und more than 1 row. All columns will have different names.

#

<br />

# Challenge 071 Backspaces in string

My solution -> *[071BackspacesInString](071BackspacesInString.js)*

<br />

## **_Task condition:_**

<br />

Assume **_"#"_** is like a backspace in string. This means that string **_"a#bc#d"_** actually is **_"bd"_**.

Your task is to process a string with **_"#"_** symbols.

<br />

**_Examples_**

```
Input: "abc#d##c"     => Output: "ac"

Input: "abc##d######" => Output: ""

Input: "#######"      => Output: ""

Input: ""             => Output: ""
```

#

<br />

# Challenge 072 Find Added

My solution -> *[072FindAdded](072FindAdded.js)*

<br />

## **_Task condition:_**

<br />

You are given two strings (**_st1_**, **_st2_**) as inputs. Your task is to return a string containing the numbers in **_st2_** which are not in **_str1_**. Make sure the numbers are returned in ascending order. All inputs will be a string of numbers.

<br />

**_Examples_**

```
Input: '4455446', '447555446666' => Output: '56667'

Input: '44554466', '447554466'   => Output: '7'

Input: '9876521', '9876543211'   => Output: '134'

Input: '678', '876'              => Output: ''

Input: '678', '6'                => Output: ''
```

#