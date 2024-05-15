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

**_NOTES:_**

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

**_NOTES:_**

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

**_NOTES:_**

Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

#

<br/>

# Challenge 012 Highest And Lowest

My solution -> *[012HighestAndLowest](012HighestAndLowest.js)*

<br/>

## **_Task condition:_**

<br/>

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

<br/>

**_Examples_**

highAndLow("1 2 3 4 5"); => return "5 1"

highAndLow("1 2 -3 4 5"); => return "5 -3"

highAndLow("1 9 3 4 -5"); => return "9 -5"

<br>

**_NOTES:_**

All numbers are valid Int32, no need to validate them.

There will always be at least one number in the input string.

Output string must be two numbers separated by a single space, and highest number is first.

#

<br/>

# Challenge 013 Exes And Ohs

My solution -> *[013ExesAndOhs](013ExesAndOhs.js)*

<br/>

## **_Task condition:_**

<br/>

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

<br/>

**_Examples_**

XO("ooxx") => true

XO("xooxx") => false

XO("ooxXm") => true

XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true

XO("zzoo") => false

#

<br/>

# Challenge 014 Friend or Foe

My solution -> *[014FriendOrFoe](014FriendOrFoe.js)*

<br/>

## **_Task condition:_**

<br/>

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

<br/>

**_Examples_**

Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

Input = ["Ryan", "Kieran", "Mark"], Output = ["Ryan", "Mark"]

<br>

**_NOTES:_**

Keep the original order of the names in the output.

#

<br/>

# Challenge 015 Growth of a Population

My solution -> *[015GrowthOfAPopulation](015GrowthOfAPopulation.js)*

<br/>

## **_Task condition:_**

<br/>

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

<br/>

**_Examples_**

nbYear(1500, 5, 100, 5000) -> 15

nbYear(1500000, 2.5, 10000, 2000000) -> 10

<br>

**_NOTES:_**

Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.

There are no fractions of people. At the end of each year, the population count is an integer: 252.8 people round down to 252 persons.

#

<br/>

# Challenge 016 String ends with

My solution -> *[016StringEndsWith](016StringEndsWith.js)*

<br/>

## **_Task condition:_**

<br/>

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). 

<br/>

**_Examples_**

solution('abc', 'bc') // returns true

solution('abc', 'd') // returns false

#

<br/>

# Challenge 017 Descending Order

My solution -> *[017DescendingOrder](017DescendingOrder.js)*

<br/>

## **_Task condition:_**

<br/>

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

<br/>

**_Examples_**

Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

#

<br/>

# Challenge 018 Sum Strings as Numbers

My solution -> *[018SumStringsAsNumbers](018SumStringsAsNumbers.js)*

<br/>

## **_Task condition:_**

<br/>

Given the string representations of two integers, return the string representation of the sum of those integers.

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

<br/>

**_Examples_**

sumStrings('1','2')  => '3'

#

<br/>

# Challenge 019 Next smaller number with the same digits

My solution -> *[019NextSmallerNumberWithTheSameDigits](019NextSmallerNumberWithTheSameDigits.js)*

<br/>

## **_Task condition:_**

<br/>

Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

Return -1 when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

<br/>

**_Examples_**

nextSmaller(21) == 12

nextSmaller(531) == 513

nextSmaller(2071) == 2017

nextSmaller(9) == -1

nextSmaller(111) == -1

nextSmaller(135) == -1

nextSmaller(1027) == -1 => 0721 is out since we don't write numbers with leading zeros

<br>

**_NOTES:_**

Some tests will include very large numbers.

Test data only employs positive integers.

#

<br/>

# Challenge 020 Human Readable Time

My solution -> *[020HumanReadableTime](020HumanReadableTime.js)*

<br/>

## **_Task condition:_**

<br/>

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

<br/>

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

<br/>

# Challenge 021 Multiples of 3 or 5

My solution -> *[021MultiplesOf3Or5](021MultiplesOf3Or5.js)*

<br/>

## **_Task condition:_**

<br/>

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

<br/>

**_Examples_**

solution(10) => 23

<br>

**_NOTES:_**

If the number is a multiple of both 3 and 5, only count it once.

#

<br/>

# Challenge 022 Convert string to camel case

My solution -> *[022ConvertStringToCamelCase](022ConvertStringToCamelCase.js)*

<br/>

## **_Task condition:_**

<br/>

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

<br/>

**_Examples_**

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

#

<br/>

# Challenge 023 Sum of Digits / Digital Root

My solution -> *[023SumOfDigitsDigitalRoot](023SumOfDigitsDigitalRoot.js)*

<br/>

## **_Task condition:_**

<br/>

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

<br/>

**_Examples_**

16 --> 1 + 6 = 7

942 --> 9 + 4 + 2 = 15  -->  1 + 5 = 6

132189 --> 1 + 3 + 2 + 1 + 8 + 9 = 24 --> 2 + 4 = 6

493193 --> 4 + 9 + 3 + 1 + 9 + 3 = 29 --> 2 + 9 = 11 --> 1 + 1 = 2

#

<br/>

# Challenge 024 Split Strings

My solution -> *[024SplitStrings](024SplitStrings.js)*

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

# Challenge 025 Reversed Strings

My solution -> *[025ReversedStrings](025ReversedStrings.js)*

<br/>

## **_Task condition:_**

<br/>

Complete the solution so that it reverses the string passed into it.

<br/>

**_Examples_**

'world' => 'dlrow'

'word' => 'drow'

#

<br/>

# Challenge 026 Sum of positive

My solution -> *[026SumOfPositive](026SumOfPositive.js)*

<br/>

## **_Task condition:_**

<br/>

You get an array of numbers, return the sum of all of the positives ones.

<br/>

**_Examples_**

[1, -4, 7, 12] => 1 + 7 + 12 = 20

<br>

**_NOTES:_**

If there is nothing to sum, the sum is default to 0.

#

<br/>

# Challenge 027 Sort the odd

My solution -> *[027SortTheOdd](027SortTheOdd.js)*

<br/>

## **_Task condition:_**

<br/>

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

<br/>

**_Examples_**

[7, 1]  =>  [1, 7]

[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

#

<br/>

# Challenge 028 Remove String Spaces

My solution -> *[028RemoveStringSpaces](028RemoveStringSpaces.js)*

<br/>

## **_Task condition:_**

<br/>

Write a function that removes the spaces from the string, then return the resultant string.

<br/>

**_Examples_**

"8 j 8 &nbsp; &nbsp; &nbsp; mBliB8g &nbsp; &nbsp; imjB8B8 &nbsp; &nbsp; jl &nbsp; &nbsp; B" -> "8j8mBliB8gimjB8B8jlB"

"8 8 Bi fk8h B 8 BB8B B B &nbsp; &nbsp; B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"

"8aaaaa dddd r &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;" -> "8aaaaaddddr"

#

<br/>

# Challenge 029 Convert number to reversed array of digits

My solution -> *[029ConvertNumberToReversedArrayOfDigits](029ConvertNumberToReversedArrayOfDigits.js)*

<br/>

## **_Task condition:_**

<br/>

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

<br/>

**_Examples_**

35231 => [1,3,2,5,3]

0 => [0]

#

<br/>

# Challenge 030 Sum Arrays

My solution -> *[030SumArrays](030SumArrays.js)*

<br/>

## **_Task condition:_**

<br/>

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

<br/>

**_Examples_**

Input: [1, 5.2, 4, 0, -1] => Output: 9.2

Input: [] => Output: 0

Input: [-2.398] => Output: -2.398

<br>

**_ASSUMPTIONS:_**

You can assume that you are only given numbers.

You cannot assume the size of the array.

You can assume that you do get an array and if the array is empty, return 0.

#

<br/>

# Challenge 031 Your order, please

My solution -> *[031YourOrderPlease](031YourOrderPlease.js)*

<br/>

## **_Task condition:_**

<br/>

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

<br/>

**_Examples_**

"is2 Thi1s T4est 3a" => "Thi1s is2 3a T4est"

"4of Fo1r pe6ople g3ood th5e the2" => "Fo1r the2 g3ood 4of th5e pe6ople"

"" => ""

<br>

**_NOTES:_**

Numbers can be from 1 to 9. So 1 will be the first word (not 0).

#

<br/>