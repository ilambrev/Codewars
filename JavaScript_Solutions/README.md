# Challenge 001 Replace With Alphabet Position

My solution -> *[001ReplaceWithAlphabetPosition](001ReplaceWithAlphabetPosition.js)*

## **_Task condition:_**

You are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

```"a" = 1```, ```"b" = 2```, etc.

**_Examples_**

```
Input: "The sunset sets at twelve o' clock."

Output: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

Input: "The narwhal bacons at midnight."

Output: "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20" (as a string)
```

#

<br />

# Challenge 002 Sum Of Two Lowest Positive Integers

My solution -> *[002SumOfTwoLowestPositiveIntegers](002SumOfTwoLowestPositiveIntegers.js)*

## **_Task condition:_**

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

**_Examples_**

```
Input: [19, 5, 42, 2, 77] => Output: 7 

Input: [10, 343445353, 3453445, 3453545353453] => Output: 3453455.
```

#

<br />

# Challenge 003 Mumbling

My solution -> *[003Mumbling](003Mumbling.js)*

## **_Task condition:_**

This time no story, no theory. The examples below show you how to write function ```accum```.

**_Examples_**

```
Input: accum("abcd") => Output: "A-Bb-Ccc-Dddd"

Input: accum("RqaEzty") => Output: "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

Input: accum("cwAt") => Output: "C-Ww-Aaa-Tttt"
```

**_NOTES:_**

- The parameter of accum is a string which includes only letters from ```a..z``` and ```A..Z```.

#

<br />

# Challenge 004 Isograms

My solution -> *[004Isograms](004Isograms.js)*

## **_Task condition:_**

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

**_Examples_**

```
Input: "Dermatoglyphics" => Output: true

Input: "aba" => Output: false

Input: "moOse" => Output: false
```

#

<br />

# Challenge 005 Two To One

My solution -> *[005TwoToOne](005TwoToOne.js)*

## **_Task condition:_**

Take 2 strings ```s1``` and ```s2``` including only letters from ```a``` to ```z```. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from ```s1``` or ```s2```.

**_Examples_**

```
Input: s1 = "xyaabbbccccdefww" s2 = "xxxxyyyyabklmopq"

Output: longest(s1, s2) => "abcdefklmopqwxy"

Input: s1 = "abcdefghijklmnopqrstuvwxyz" s2 = "abcdefghijklmnopqrstuvwxyz"

Output: longest(s1, s2) => "abcdefghijklmnopqrstuvwxyz"
```

#

<br />

# Challenge 006 Highest Scoring Word

My solution -> *[006HighestScoringWord](006HighestScoringWord.js)*

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

# Challenge 007 Extract The Domain Name From A URL

My solution -> *[007ExtractTheDomainNameFromAURL](007ExtractTheDomainNameFromAURL.js)*

## **_Task condition:_**

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

**_Examples_**

```
url = "http://github.com/carbonfive/raygun" => domain name = "github"

url = "http://www.zombie-bites.com" => domain name = "zombie-bites"

url = "https://www.cnet.com" => domain name = "cnet"
```

#

<br />

# Challenge 008 Write Number In Expanded Form

My solution -> *[008WriteNumberInExpandedForm](008WriteNumberInExpandedForm.js)*

## **_Task condition:_**

You will be given a number and you will need to return it as a string in Expanded Form.

**_Examples_**

```
Input: 12    => Output: '10 + 2'

Input: 42    => Output: '40 + 2'

Input: 70304 => Output: '70000 + 300 + 4'
```

**_NOTES:_**

- All numbers will be whole numbers greater than 0.

#

<br />

# Challenge 009 Array Diff

My solution -> *[009ArrayDiff](009ArrayDiff.js)*

## **_Task condition:_**

Your goal is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list ```a```, which are present in list ```b``` keeping their order.

If a value is present in ```b```, all of its occurrences must be removed from the other.

**_Examples_**

```
Input: [1,2], [1] => Output: [2]

Input: [1,2,2,2,3], [2] => Output: [1,3]
```

#

<br />

# Challenge 010 The Vowel Code

My solution -> *[010TheVowelCode](010TheVowelCode.js)*

## **_Task condition:_**

Create a function called ```encode()``` to replace all the lowercase vowels in a given string with numbers according to the following pattern:

```
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
```

Then create a function called ```decode()``` to turn the numbers back into vowels according to the same pattern shown above.

**_Examples_**

```
encode("hello") would return "h2ll4"

decode("h3 th2r2") would return "hi there"
```

**_NOTES:_**

- There is no need to worry about uppercase vowels.
- For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

#

<br />

# Challenge 011 Stop Spinning My Words

My solution -> *[011StopSpinningMyWords](011StopSpinningMyWords.js)*

## **_Task condition:_**

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed.

<br />

**_Examples_**

```
Input: "Hey fellow warriors" => Output: "Hey wollef sroirraw"

Input: "This is a test" => Output: "This is a test"

Input: "This is another test" => Output: "This is rehtona test"
```

**_NOTES:_**

- Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

#

<br />

# Challenge 012 Highest And Lowest

My solution -> *[012HighestAndLowest](012HighestAndLowest.js)*

## **_Task condition:_**

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

**_Examples_**

```
Input: '1 2 3 4 5' => Output: '5 1'

Input: '1 2 -3 4 5' => Output: '5 -3'

Input: '1 9 3 4 -5' => Output: '9 -5'
```

**_NOTES:_**

- All numbers are valid ```Int32```, no need to validate them.

- There will always be at least one number in the input string.

- Output string must be two numbers separated by a single space, and highest number is first.

#

<br />

# Challenge 013 Exes And Ohs

My solution -> *[013ExesAndOhs](013ExesAndOhs.js)*

## **_Task condition:_**

Check to see if a string has the same amount of ```'x'```s and ```'o'```s. The method must return a boolean and be case insensitive. The string can contain any char.

**_Examples_**

```
Input: 'ooxx' => Output: true

Input: 'xooxx' => Output: false

Input: 'ooxXm' => Output: true

Input: 'zpzpzpp' => Output: true // when no 'x' and 'o' is present should return true

Input: 'zzoo' => Output: false
```

#

<br />

# Challenge 014 Friend Or Foe

My solution -> *[014FriendOrFoe](014FriendOrFoe.js)*

## **_Task condition:_**

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

<br />

**_Examples_**

```
Input: ['Ryan', 'Kieran', 'Jason', 'Yous'] => Output: ['Ryan', 'Yous']

Input: ['Ryan', 'Kieran', 'Mark'] => Output: ['Ryan', 'Mark']

Input: ['Peter', 'Stephen', 'Joe'] => Output: []
```

**_NOTES:_**

- Keep the original order of the names in the output.

#

<br />

# Challenge 015 Growth Of A Population

My solution -> *[015GrowthOfAPopulation](015GrowthOfAPopulation.js)*

## **_Task condition:_**

In a small town the population is ```p0 = 1000``` at the beginning of a year. The population regularly increases by ```2 percent``` per year and moreover ```50``` new inhabitants per year come to live in the town. How many years does the town need to see its population greater than or equal to ```p = 1200``` inhabitants?

```
At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.
```

More generally given parameters:

```p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)```

the function ```nbYear(p0, percent, aug, p)``` should return ```n``` number of entire years needed to get a population greater or equal to ```p```.

```aug``` is an integer, percent a positive or null floating number, ```p0``` and ```p``` are positive integers (> 0)

**_Examples_**

```
Input: 1500, 5, 100, 5000 => Output: 15

Input: 1500000, 2.5, 10000, 2000000 => Output: 10
```

**_NOTES:_**

- Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is ```2``` you have to convert it to ```0.02```.

- There are no fractions of people. At the end of each year, the population count is an integer: ```252.8``` people round down to ```252``` persons.

#

<br />

# Challenge 016 String Ends With

My solution -> *[016StringEndsWith](016StringEndsWith.js)*

## **_Task condition:_**

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). 

**_Examples_**

```
Input: 'abc', 'bc' => Output: true

Input: 'abc', 'd' => Output: false
```

#

<br />

# Challenge 017 Descending Order

My solution -> *[017DescendingOrder](017DescendingOrder.js)*

## **_Task condition:_**

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

**_Examples_**

```
Input: 42145 => Output: 54421

Input: 145263 => Output: 654321

Input: 123456789 => Output: 987654321
```

#

<br />

# Challenge 018 Sum Strings As Numbers

My solution -> *[018SumStringsAsNumbers](018SumStringsAsNumbers.js)*

## **_Task condition:_**

Given the string representations of two integers, return the string representation of the sum of those integers.

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

**_Examples_**

```
Input: '1', '2' => Output: '3'

Input: '123', '456' => Output: '579'
```

#

<br />

# Challenge 019 Next Smaller Number With The Same Digits

My solution -> *[019NextSmallerNumberWithTheSameDigits](019NextSmallerNumberWithTheSameDigits.js)*

## **_Task condition:_**

Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

Return ```-1``` when there is no smaller number that contains the same digits. Also return ```-1``` when the next smaller number with the same digits would require the leading digit to be zero.

**_Examples_**

```
Input: 21 => Output: 12

Input: 531 => Output: 513

Input: 2071 => Output: 2017

Input: 9 => Output: -1

Input: 111 => Output: -1

Input: 135 => Output: -1

Input: 1027 => Output: -1 (0721 is out since we don't write numbers with leading zeros)
```

**_NOTES:_**

- Some tests will include very large numbers.

- Test data only employs positive integers.

#

<br />

# Challenge 020 Human Readable Time

My solution -> *[020HumanReadableTime](020HumanReadableTime.js)*

## **_Task condition:_**

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (```HH:MM:SS```)

- ```HH``` = hours, padded to 2 digits, range: 00 - 99
- ```MM``` = minutes, padded to 2 digits, range: 00 - 59
- ```SS``` = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (```99:59:59```)

**_Examples_**

```
Input: 0      => Output: 00:00:00

Input: 59     => Output: 00:00:59

Input: 60     => Output: 00:01:00

Input: 90     => Output: 00:01:30

Input: 3599   => Output: 00:59:59

Input: 3600   => Output: 01:00:00

Input: 45296  => Output: 12:34:56

Input: 86399  => Output: 23:59:59

Input: 86400  => Output: 24:00:00

Input: 359999 => Output: 99:59:59
```

#

<br />

# Challenge 021 Multiples Of 3 Or 5

My solution -> *[021MultiplesOf3Or5](021MultiplesOf3Or5.js)*

## **_Task condition:_**

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 **below** the number passed in.

Additionally, if the number is negative, return 0.

**_Examples_**

```
Input: 10 => Output: 23
```

**_NOTES:_**

- If the number is a multiple of both 3 and 5, only count it once.

#

<br />

# Challenge 022 Convert String To Camel Case

My solution -> *[022ConvertStringToCamelCase](022ConvertStringToCamelCase.js)*

## **_Task condition:_**

Complete the function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

**_Examples_**

```
Input: 'the-stealth-warrior' => Output: 'theStealthWarrior'

Input: 'The_Stealth_Warrior' => 'TheStealthWarrior'

Input: 'The_Stealth-Warrior' => 'TheStealthWarrior'
```

#

<br />

# Challenge 023 Sum Of Digits / Digital Root

My solution -> *[023SumOfDigitsDigitalRoot](023SumOfDigitsDigitalRoot.js)*

## **_Task condition:_**

Digital root is the recursive sum of all the digits in a number.

Given ```n```, take the sum of the digits of ```n```. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

**_Examples_**

```
Input: 16 --> 1 + 6 = 7 => Output: 7

Input: 942 --> 9 + 4 + 2 = 15  -->  1 + 5 = 6 => Output: 6

Input: 132189 --> 1 + 3 + 2 + 1 + 8 + 9 = 24 --> 2 + 4 = 6 => Output: 6

Input: 493193 --> 4 + 9 + 3 + 1 + 9 + 3 = 29 --> 2 + 9 = 11 --> 1 + 1 = 2 => Output: 2
```

#

<br />

# Challenge 024 Split Strings

My solution -> *[024SplitStrings](024SplitStrings.js)*

## **_Task condition:_**

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

**_Examples_**

```
Input: 'abc' => Output: ['ab', 'c_']

Input: 'abcdef' => Output: ['ab', 'cd', 'ef']
```

#

<br />

# Challenge 025 Reversed Strings

My solution -> *[025ReversedStrings](025ReversedStrings.js)*

## **_Task condition:_**

Complete the solution so that it reverses the string passed into it.

**_Examples_**

```
Input: 'world' => Output: 'dlrow'

Input: 'word' => Output: 'drow'
```

#

<br />

# Challenge 026 Sum Of Positive

My solution -> *[026SumOfPositive](026SumOfPositive.js)*

## **_Task condition:_**

You get an array of numbers, return the sum of all of the positives ones.

**_Examples_**

```
Input: [1, -4, 7, 12] => Output: 20 // 1 + 7 + 12 = 20
```

**_NOTES:_**

If there is nothing to sum, the sum is default to 0.

#

<br />

# Challenge 027 Sort The Odd

My solution -> *[027SortTheOdd](027SortTheOdd.js)*

## **_Task condition:_**

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

**_Examples_**

```
Input: [7, 1] => Output: [1, 7]

Input: [5, 8, 6, 3, 4] => Output: [3, 8, 6, 5, 4]

Input: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] => Output: [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

#

<br />

# Challenge 028 Remove String Spaces

My solution -> *[028RemoveStringSpaces](028RemoveStringSpaces.js)*

## **_Task condition:_**

Write a function that removes the spaces from the string, then return the resultant string.

**_Examples_**

```
Input: "8 j 8   mBliB8g  imjB8B8  jl  B" => Output: "8j8mBliB8gimjB8B8jlB"

Input: "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" => Output: "88Bifk8hB8BB8BBBB888chl8BhBfd"

Input: "8aaaaa dddd r     " => Input: "8aaaaaddddr"
```

#

<br />

# Challenge 029 Convert number to reversed array of digits

My solution -> *[029ConvertNumberToReversedArrayOfDigits](029ConvertNumberToReversedArrayOfDigits.js)*

## **_Task condition:_**

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

**_Examples_**

```
Input: 35231 => Output: [1,3,2,5,3]

Input: 0 => Output: [0]
```

#

<br />

# Challenge 030 Sum Arrays

My solution -> *[030SumArrays](030SumArrays.js)*

## **_Task condition:_**

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

**_Examples_**

```
Input: [1, 5.2, 4, 0, -1] => Output: 9.2

Input: [] => Output: 0

Input: [-2.398] => Output: -2.398
```

**_ASSUMPTIONS:_**

- You can assume that you are only given numbers.

- You cannot assume the size of the array.

- You can assume that you do get an array and if the array is empty, return 0.

#

<br />

# Challenge 031 Your Order, Please

My solution -> *[031YourOrderPlease](031YourOrderPlease.js)*

## **_Task condition:_**

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

**_Examples_**

```
Input: "is2 Thi1s T4est 3a" => Output: "Thi1s is2 3a T4est"

Input: "4of Fo1r pe6ople g3ood th5e the2" => Output: "Fo1r the2 g3ood 4of th5e pe6ople"

Input: "" => Output: ""
```

**_NOTES:_**

- Numbers can be from 1 to 9. So 1 will be the first word (not 0).

#

<br />

# Challenge 032 Odd Or Even?

My solution -> *[032OddOrEven](032OddOrEven.js)*

## **_Task condition:_**

Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching ```"odd"``` or ```"even"```.

If the input array is empty consider it as: ```[0]``` (array with a zero).

**_Examples_**

```
Input: [0] => Output: "even"

Input: [0, 1, 4] => Output: "odd"

Input: [0, -1, -5] => Output: "even"
```

#

<br />

# Challenge 033 Reversed Sequence

My solution -> *[033ReversedSequence](033ReversedSequence.js)*

## **_Task condition:_**

Build a function that returns an array of integers from ```n``` to ```1``` where ```n > 0```.

**_Examples_**

```
Input: n = 5 => Output: [5, 4, 3, 2, 1]
```

#

<br />

# Challenge 034 Century From Year

My solution -> *[034CenturyFromYear](034CenturyFromYear.js)*

## **_Task condition:_**

The first century spans from the ```year 1``` up to and including the ```year 100```, the second century - from the ```year 101``` up to and including the ```year 200```, etc.

Given a year, return the century it is in.

**_Examples_**

```
Input: 1705 => Output: 18

Input: 1900 => Output: 19

Input: 1601 => Output: 17

Input: 2000 => Output: 20

Input: 2742 => Output: 28
```

#

<br />

# Challenge 035 Directions Reduction

My solution -> *[035DirectionsReduction](035DirectionsReduction.js)*

## **_Task condition:_**

Once upon a time, on a way through the old wild mountainous west,…

… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.

Write a function which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

**_Examples_**

```
Input: => ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], Output: => ["WEST"]

Input: => ["NORTH", "SOUTH", "EAST", "WEST"], Output: => []

Input: => ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], Output: => ["WEST", "WEST"]
```

**_NOTES:_**

- Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

#

<br />

# Challenge 036 Square(n) Sum

My solution -> *[036SquareNSum](036SquareNSum.js)*

## **_Task condition:_**

Complete the square sum function so that it squares each number passed into it and then sums the results together.

**_Examples_**

```
Input: [1, 2, 2] => Output: 9
```

#

<br />

# Challenge 037 Delete Occurrences Of An Element If It Occurs More Than N Times

My solution -> *[037DeleteOccurrencesOfAnElementIfItOccursMoreThanNtimes](037DeleteOccurrencesOfAnElementIfItOccursMoreThanNtimes.js)*

## **_Task condition:_**

Given a list and a number, create a new list that contains each number of list at most N times, without reordering.

**_Examples_**

```
Input: [1,2,3,1,2,1,2,3], 2 => Output: [1,2,3,1,2,3]

Input: [20,37,20,21], 1 => Output: [20,37,21]
```

#

<br />

# Challenge 038 Playing With Digits

My solution -> *[038PlayingWithDigits](038PlayingWithDigits.js)*

## **_Task condition:_**

Some numbers have funny properties. For example:

```
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```

Given two positive integers ```n``` and ```p```, we want to find a positive integer ```k```, if it exists, such that the sum of the digits of ```n``` raised to consecutive powers starting from ```p``` is equal to ```k * n```.

In other words, writing the consecutive digits of ```n``` as ```a, b, c, d ...```, is there an integer ```k``` such that:

<em>(a<sup>p</sup> + b<sup>p+1</sup> + c<sup>p+2</sup> + d<sup>p+3</sup> + ...) = n ∗ k</em>

If it is the case we will return k, if not return -1.

**_Examples_**

```
Input: n = 89; p = 1 => Output: 1

Input: n = 92; p = 1 => Output: -1

Input: n = 695; p = 2 => Output: 2

Input: n = 46288; p = 3 => Output: 51
```

**_NOTES:_**

- ```n``` and ```p``` will always be strictly positive integers.

#

<br />

# Challenge 039 Counting Duplicates

My solution -> *[039CountingDuplicates](039CountingDuplicates.js)*

## **_Task condition:_**

Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

**_Examples_**

```
Input: "abcde" => Output: 0

Input: "aabbcde" => Output: 2

Input: "aabBcde" => Output: 2

Input: "indivisibility" => Output: 1

Input: "Indivisibilities" => Output: 2

Input: "aA11" => Output: 2

Input: "ABBA" => Output: 2
```

#

<br />

# Challenge 040 Count By X

My solution -> *[040CountByX](040CountByX.js)*

## **_Task condition:_**

<br />

Create a function with two arguments that will return an array of the first ```n``` multiples of ```x```.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array.

**_Examples_**

```
Input: 1, 10 => Output: [1,2,3,4,5,6,7,8,9,10]

Input: 2, 5 => Output: [2,4,6,8,10]
```

#

<br />

# Challenge 041 Reverse Words

My solution -> *[041ReverseWords](041ReverseWords.js)*

## **_Task condition:_**

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

**_Examples_**

```
Input: "This is an example!" => Output: "sihT si na !elpmaxe"

Input: "double  spaces" => Output: "elbuod  secaps"
```

#

<br />

# Challenge 042 Rock Paper Scissors

My solution -> *[042RockPaperScissors](042RockPaperScissors.js)*

## **_Task condition:_**

Let's play! You have to return which player won! In case of a draw return Draw!.

**_Examples_**

```
Input: "scissors", "paper" => Output: "Player 1 won!"

Input: "scissors", "rock" => Output: "Player 2 won!"

Input: "paper", "paper" => Output: "Draw!"
```

#

<br />

# Challenge 043 Remove The Minimum

My solution -> *[043RemoveTheMinimum](043RemoveTheMinimum.js)*

## **_Task condition:_**

Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array, return an empty array.

Don't change the order of the elements that are left.

**_Examples_**

```
Input: [1,2,3,4,5] => Output: [2,3,4,5]

Input: [5,3,2,1,4] => Output: [5,3,2,4]

Input: [2,2,1,2,1] => Output: [2,2,2,1]
```

#

<br />

# Challenge 044 Count Of Positives / Sum Of Negatives

My solution -> *[044CountOfPositivesSumOfNegatives](044CountOfPositivesSumOfNegatives.js)*

## **_Task condition:_**

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

**_Examples_**

```
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15] => Output: [10, -65]
```

#

<br />

# Challenge 045 Sum Of Intervals

My solution -> *[045SumOfIntervals](045SumOfIntervals.js)*

## **_Task condition:_**

Write a function called sumIntervals that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

**_Examples_**

```
Input: [[1, 4], [7, 10], [3, 5]] => Output: 7

Input: [[1, 2], [6, 10], [11, 15]] => Output: 9

Input: [[1, 4], [7, 10], [3, 5]] => Output: 7

Input: [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]] => Output: 19

Input: [[0, 20], [-100000000, 10], [30, 40]] => Output: 100000030
```

#

<br />

# Challenge 046 Square Every Digit

My solution -> *[046SquareEveryDigit](046SquareEveryDigit.js)*

## **_Task condition:_**

Square every digit of a number and concatenate them.

**_Examples_**

```
Input: 9119 => Output: 811181

Input: 765 => Output: 493625
```

**_NOTES:_**

- The function accepts an integer and returns an integer.

#

<br />

# Challenge 047 Persistent Bugger

My solution -> *[047PersistentBugger](047PersistentBugger.js)*

## **_Task condition:_**

Write a function **_persistence_** that takes in a positive parameter **_num_** and returns its multiplicative persistence, which is the number of times you must multiply the digits in **_num_** until you reach a single digit.

**_Examples_**

```
Input: 39 => Output: 3

Input: 999 => Output: 4

Input: 4 => Output: 0
```

#

<br />

# Challenge 048 Regex Validate PIN Code

My solution -> *[048RegexValidatePINCode](048RegexValidatePINCode.js)*

## **_Task condition:_**

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return **_true_**, else return **_false_**.

**_Examples_**

```
Input: '1234' => Output: true

Input: '12345' => Output: false

Input: 'a234' => Output: false
```

#

<br />

# Challenge 049 Generate Chat Room Names

My solution -> *[049GenerateChatRoomNames](049GenerateChatRoomNames.js)*

## **_Task condition:_**

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

**_Examples_**

```
Input: ['Joe Bloggs', 'John Smith'] => Output: ['Joe', 'John']

Input: ['Joe Bloggs', 'John Smith', 'Jane Doe'] => Output: ['Jane', 'Joe', 'John']

Input: ['Joe Bloggs', 'John Smith', 'Jane Doe', 'Jane Bloggs'] => Output: ['Jane B', 'Jane D', 'Joe', 'John']

Input: ['Joe Bloggs', 'John Smith', 'Jane Doe', 'Jane Bloggs', 'John Scott'] => Output: ['Jane B', 'Jane D', 'Joe', 'John Scott', 'John Smith']
```

<br />

**_NOTES:_**

- It can be assumed that names are in the format of a first name and a last name consisting solely of letters from the English alphabet, both uppercase (A-Z) and lowercase (a-z), separated by a single space and if no names are provided, we should return an empty array.

- Casing is not important, meaning JOHn SmiTh is equal to john smith, after we've tidied up the casings, these should be interpreted as the same name.

- You don't have to worry about multiple instances of the same full name.

#

<br />

# Challenge 050 Which Are In?

My solution -> *[050WhichAreIn](050WhichAreIn.js)*

## **_Task condition:_**

Given two arrays of strings ```a1``` and ```a2``` return a sorted array ```r``` in lexicographical order of the strings of ```a1``` which are substrings of strings of ```a2```.

**_Examples_**

```
Input: a1 = ['arp', 'live', 'strong'], a2 = ['lively', 'alive', 'harp', 'sharp', 'armstrong'] => Output: ['arp', 'live', 'strong']

Input: a1 = ['tarp', 'mice', 'bull'], a2 = ['lively', 'alive', 'harp', 'sharp', 'armstrong'] => Output: []
```

#

<br />

# Challenge 051 First Non-Repeating Character

My solution -> *[051FirstNonRepeatingCharacter](051FirstNonRepeatingCharacter.js)*

## **_Task condition:_**

Write a function that takes a string input, and returns the first character that is not repeated anywhere in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter.

If a string contains all repeating characters, it should return an empty string ("");

**_Examples_**

```
Input: 'stress' => Output: t

Input: 'sTreSS' => Output: T
```

#

<br />

# Challenge 052 Find The Unique String

My solution -> *[052FindTheUniqueString](052FindTheUniqueString.js)*

## **_Task condition:_**

There is an array of strings. All strings contains similar letters except one. Try to find it!

**_Examples_**

```
Input: ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a'] => Output: 'BbBb'

Input: ['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba'] => Output: 'foo'
```

**_NOTES:_**

- Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

- It’s guaranteed that array contains more than 2 strings.

#

<br />

# Challenge 053 The Hashtag Generator

My solution -> *[053TheHashtagGenerator](053TheHashtagGenerator.js)*

## **_Task condition:_**

Write a function that generates hashtag from given string.

- It must start with a hashtag (#).

- All words must have their first letter capitalized.

- If the final result is longer than 140 chars it must return false.

- If the input or the result is an empty string it must return false.

**_Examples_**

```
Input: ' Hello there thanks for trying my Kata' => Output: '#HelloThereThanksForTryingMyKata'

Input: '    Hello     World   ' => Output: '#HelloWorld'

Input: '' => Output: false
```

#

<br />

# Challenge 054 Moving Zeros To The End

My solution -> *[054MovingZerosToTheEnd](054MovingZerosToTheEnd.js)*

## **_Task condition:_**

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

**_Examples_**

```
Input: [false, 1, 0, 1, 2, 0, 1, 3, "a"] => Output: [false, 1, 1, 2, 1, 3, "a", 0, 0]
```

#

<br />

# Challenge 055 Tic-Tac-Toe Checker

My solution -> *[055TicTacToeChecker](055TicTacToeChecker.js)*

## **_Task condition:_**

Create a function that will check Tic-Tac-Toe game current state.

Assume that the board comes in the form of a 3x3 array, where the value is ```0``` if a spot is empty, ```1``` if it is an ```"X"```, or ```2``` if it is an ```"O"```.

We want our function to return:

- ```-1``` if the board is not yet finished AND no one has won yet (there are empty spots),

- ```1``` if **_"X"_** won,

- ```2``` if **_"O"_** won,

- ```0``` if it's a cat's game (i.e. a draw).

**_Examples_**

Input:
```
[
    [0, 0, 1],
    [0, 1, 2],
    [2, 1, 0]
]

Output: -1
```

**_NOTES:_**

- You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

#

<br />

# Challenge 056 Vowel Count

My solution -> *[056VowelCount](056VowelCount.js)*

## **_Task condition:_**

Return the number (count) of vowels in the given string.

We will consider **_a_**, **_e_**, **_i_**, **_o_**, **_u_** as vowels for this Kata (but not **_y_**).

**_Examples_**

```
Input: 'abracadabra' => Output: 5
```

**_NOTES:_**

- The input string will only consist of lower case letters and/or spaces.

#

<br />

# Challenge 057 String Incrementer

My solution -> *[057StringIncrementer](057StringIncrementer.js)*

## **_Task condition:_**

Write a function which increments a string, to create a new string.

- If the string already ends with a number, the number should be incremented by 1.
- If the string does not end with a number. the number 1 should be appended to the new string.

**_Examples_**

```
Input: 'foo' => Output: 'foo1'

Input: 'foobar23' => Output: 'foobar24'

Input: 'foo0042' => Output: 'foo0043'

Input: 'foo9' => Output: 'foo10'

Input: 'foo099' => Output: 'foo100'
```

**_NOTES:_**

- If the number has leading zeros the amount of digits should be considered.

#

<br />

# Challenge 058 Play With Two Strings

My solution -> *[058PlayWithTwoStrings](058PlayWithTwoStrings.js)*

## **_Task condition:_**

Your task is to Combine two Strings - Input Strings **_a_** and **_b_**: For every character in string **_a_** swap the casing of every occurrence of the same character in string **_b_**. Then do the same casing swap with the inputs reversed. Return a single string consisting of the changed version of **_a_** followed by the changed version of **_b_**. A char of **_a_** is in **_b_** regardless if it's in upper or lower case - see the testcases too.

**_Examples_**

```
Input: 'abc' and 'cde' => Output: 'abCCde'

Input: 'ab' and 'aba' => Output: 'aBABA'

Input: 'abab' and 'bababa' => Output: 'ABABbababa'
```

**_NOTES:_**

- You don't have to check errors or incorrect input values, everything is ok without bad tricks, only two input strings and as result one output string;

#

<br />

# Challenge 059 Luck Check

My solution -> *[059LuckCheck](059LuckCheck.js)*

## **_Task condition:_**

Ticket was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half.

Your task is to write a funtion, which returns **_true_** if argument is string decimal representation of a lucky ticket number, or **_false_** for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.

**_Examples_**

```
Input: '003111' => Output: true

Input: '813372' => Output: true

Input: '17935' => Output: true

Input: '56328116' => Output: true
```

**_NOTES:_**

- If the length of string is odd, you should ignore the middle number when adding the halves.

#

<br />

# Challenge 060 Bowling Pins

My solution -> *[060BowlingPins](060BowlingPins.js)*

## **_Task condition:_**

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

**_Examples_**

```
Input: [3, 5, 9]

Output: Return a string with the current field.

I I   I
 I   I
  I   
   I  
```

**_NOTES:_**

- The pins rows are separated by a newline ```(\n)```
- Each Line must be 7 chars long
- Fill the missing pins with a space character ```( )```

#

<br />

# Challenge 061 English Beggars

My solution -> *[061EnglishBeggars](061EnglishBeggars.js)*

## **_Task condition:_**

Given an array of values and an amount of beggars, you are supposed to return an array with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.

Also note that not all beggars have to take the same amount of "offers", meaning that the length of the array is not necessarily a multiple of n. Length can be even shorter, in which case the last beggars will of course take nothing (0).

**_Examples_**

```
Input: [1,2,3,4,5], 2 => Output: [9,6]

Input: [1,2,3,4,5], 3 => Output: [5,7,3]
```

**_NOTES:_**

- Do not modify the input array.

#

<br />

# Challenge 062 Sorting By Bits

My solution -> *[062SortingByBits](062SortingByBits.js)*

## **_Task condition:_**

You're expected to sort an array of 32-bit integers in ascending order of the number of on bits they have.

In cases where two numbers have the same number of bits, compare their real values instead.

E.g between 10 (...1010) and 12 (...1100), they both have the same number of on bits '2' but the integer 10 is less than 12 so it comes first in sorted order.

Your task is to write a function that takes an array of integers and sort them as described above.

**_Examples_**

```
Input: [7, 6, 15, 8] => Output: [8, 6, 7, 15]

Input: [3, 8, 3, 6, 5, 7, 9, 1] => Output: [1, 8, 3, 3, 5, 6, 9, 7]
```

**_NOTES:_**

- Your solution has to sort the array in place.

#

<br />

# Challenge 063 Two Sum

My solution -> *[063TwoSum](063TwoSum.js)*

## **_Task condition:_**

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: ```[index1, index2]```.

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

**_Examples_**

```
Input: [1, 2, 3], 4 => Output: [0, 2] or [2, 0]

Input: [3, 2, 4], 6 => Output: [1, 2] or [2, 1]
```

**_NOTES:_**

- The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

#

<br />

# Challenge 064 Simple Card Game

My solution -> *[064SimpleCardGame](064SimpleCardGame.js)*

## **_Task condition:_**

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

**_Examples_**

```
Input: deckSteve = ['A','7','8'], deckJosh = ['K','5','9'] => Output: "Steve wins 2 to 1"
```

**_NOTES:_**

- Every card may appear in the deck more than once.

#

<br />

# Challenge 065 How Much Hex Is The Fish

My solution -> *[065HowMuchHexIsTheFish](065HowMuchHexIsTheFish.js)*

## **_Task condition:_**

The ocean is full of colorful fishes. We as programmers want to know the hexadecimal value of these fishes.

Take all hexadecimal valid characters (```a,b,c,d,e,f```) of the given name and ```XOR``` them. Return the result as an integer.

**_Examples_**

```
Input: 'redlionfish' => Output: 12
```

**_NOTES:_**

- The input is always a string, which can contain spaces, upper and lower case letters but no digits. 

#

<br />

# Challenge 066 Cat Аnd Mouse - Harder Version

My solution -> *[066CatAndMouseHarderVersion.js](066CatAndMouseHarderVersion.js)*

## **_Task condition:_**

You will be given a string **_(x)_** featuring a cat **_'C'_**, a dog **_'D'_** and a mouse **_'m'_**. The rest of the string will be made up of **_'.'_**.

You need to find out if the cat can catch the mouse from its current position. The cat can jump at most **_(j)_** characters, and cannot jump over the dog.

- If there are not more than **_j_** characters between the cat and the mouse, so cat can jump far enough and jump is not over dog, return **_'Caught!'_**
- If there are more than **_j_** characters between the two, the cat cannot jump far enough, return **_'Escaped!'_**
- If cat can jump far enough, but dog is in the way, protecting the mouse, return **_'Protected!'_**
- If not all three animals are present, return **_'boring without all three'_**

**_Examples_**

```
Input: '..C.....m...D', 5               => Output: 'Caught!'

Input: '.....C............m......D', 5  => Output: 'Escaped!'

Input: '...m.........C...D', 10         => Output: 'Caught!'

Input: '...m....D....C.......', 10      => Output: 'Protected!'

Input: '...m.........C....', 10         => 'boring without all three'
```

#

<br />

# Challenge 067 New Cashier Does Not Know About Space Or Shift

My solution -> *[067NewCashierDoesNotKnowAboutSpaceOrShift](067NewCashierDoesNotKnowAboutSpaceOrShift.js)*

## **_Task condition:_**

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

**_Examples_**

```
Input: 'milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza'
Output: 'Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke'

Input: 'pizzachickenfriesburgercokemilkshakefriessandwich'
Output: 'Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke'
```

#

<br />

# Challenge 068 Merged String Checker

My solution -> *[0068MergedStringChecker.js](068MergedStringChecker.js)*

## **_Task condition:_**

Write an algorithm to check if a given string, **_s_**, can be formed from two other strings, **_part1_** and **_part2_**.

The restriction is that the characters in **_part1_** and **_part2_** should be in the same order as in **_s_**.

**_Examples_**

```
Input: 'codewars', 'cdw', 'oears'               => Output: true

Input: 'xcyc', 'xc', 'yc'                       => Output: true

Input: 'xcyc', 'yc', 'xc'                       => Output: true

Input: 'xcyc', 'xc', 'cy'                       => Output: true

Input: 'xcyc', 'cy', 'xc'                       => Output: true

Input: 'codewars', 'code', 'wars'               => Output: true

Input: 'codewars', 'cdwr', 'oeas'               => Output: true

Input: 'Making progress', 'Mak pross', 'inggre' => Output: true

Input: 'codewars', 'code', 'code'               => Output: false

Input: 'More progress', 'More ess', 'pro'       => Output: false
```

#

<br />

# Challenge 069 Convert PascalCase String Into snake_case

My solution -> *[069ConvertPascalCaseStringIntoSnakeCase](069ConvertPascalCaseStringIntoSnakeCase.js)*

## **_Task condition:_**

Complete the function so that it takes a **_PascalCase_** string and returns the string in **_snake_case_** notation. Lowercase characters can be numbers. If the function gets a number as input, it should return a string.

**_Examples_**

```
Input: 'TestController' => Output: 'test_controller'

Input: 'MoviesAndBooks' => Output: 'movies_and_books'

Input: 'App7Test'       => Output: 'app7_test'

Input: 1                => Output: '1'
```

#

<br />

# Challenge 070 Sort The Columns Of A csv-file

My solution -> *[070SortTheColumnsOfaCSVFile](070SortTheColumnsOfaCSVFile.js)*

## **_Task condition:_**

You get a string with the content of a csv-file. The columns are separated by semicolons.

The first line contains the names of the columns.

Write a method that sorts the columns by the names of the columns alphabetically and incasesensitive. 

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

**_NOTES:_**

- There is no need for prechecks. You will always get a correct string with more than 1 line und more than 1 row. All columns will have different names.

#

<br />

# Challenge 071 Backspaces In String

My solution -> *[071BackspacesInString](071BackspacesInString.js)*

## **_Task condition:_**

Assume **_"#"_** is like a backspace in string. This means that string **_"a#bc#d"_** actually is **_"bd"_**.

Your task is to process a string with **_"#"_** symbols.

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

## **_Task condition:_**

You are given two strings (**_st1_**, **_st2_**) as inputs. Your task is to return a string containing the numbers in **_st2_** which are not in **_str1_**. Make sure the numbers are returned in ascending order. All inputs will be a string of numbers.

**_Examples_**

```
Input: '4455446', '447555446666' => Output: '56667'

Input: '44554466', '447554466'   => Output: '7'

Input: '9876521', '9876543211'   => Output: '134'

Input: '678', '876'              => Output: ''

Input: '678', '6'                => Output: ''
```

#

<br />

# Challenge 073 Who Likes It?

My solution -> *[073WhoLikesIt](073WhoLikesIt.js)*

## **_Task condition:_**

Through "like" system from Facebook and other pages пeople can "like" blog posts, pictures or other items. The goal is to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

**_Examples_**

```
Input: []                                => Output: "no one likes this"

Input: ["Peter"]                         => Output: "Peter likes this"

Input: ["Jacob", "Alex"]                 => Output: "Jacob and Alex like this"

Input: ["Max", "John", "Mark"]           => Output: "Max, John and Mark like this"

Input: ["Alex", "Jacob", "Mark", "Max"]  => Output: "Alex, Jacob and 2 others like this"
```

**_NOTES:_**

- For 4 or more names, the number in **_"and 2 others"_** simply increases.

#

<br />

# Challenge 074 CamelCase Method

My solution -> *[074CamelCaseMethod](074CamelCaseMethod.js)*

## **_Task condition:_**

Write a function that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

**_Examples_**

```
Input: 'hello case'      => Output: "HelloCase"

Input: "camel case word" => Output: "CamelCaseWord"
```

#

<br />

# Challenge 075 Reverse Or Rotate?

My solution -> *[075ReverseOrRotate](075ReverseOrRotate.js)*

## **_Task condition:_**

The input is a string **_str_** of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size **_sz_** (ignore the last chunk if its size is less than **_sz_**).

If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If **_sz_** is <= 0 or if **_str_** == '' return ''

If **_sz_** is greater (>) than the length of **_str_** it is impossible to take a chunk of size **_sz_** hence return ''.

**_Examples_**

```
Input: '123456987654', 6       => Output: '234561876549'

Input: '123456987653', 6       => Output: '234561356789'

Input: '66443875', 4           => Output: '44668753'

Input: '66443875', 8           => Output: '64438756'

Input: '664438769', 8          => Output: '67834466'

Input: '123456779', 8          => Output: '23456771'

Input: '', 8                   => Output: ''

Input: '123456779', 0          => Output: '' 

Input: '563000655734469485', 4 => Output: '0365065073456944'
```

#

<br />

# Challenge 076 Prize Draw

My solution -> *[076PrizeDraw](076PrizeDraw.js)*

## **_Task condition:_**

To participate in a prize draw each one gives his/her firstname.

Each letter of a firstname has a value which is its rank in the English alphabet. **_A_** and **_a_** have rank **_1_**, **_B_** and **_b_** rank **_2_** and so on.

The length of the firstname is added to the sum of these ranks hence a number **_som_**.

An array of random weights is linked to the firstnames and each **_som_** is multiplied by its corresponding weight to get what they call a **_winning number_**.

Now one can sort the firstnames in decreasing order of the **_winning numbers_**. When two people have the same **_winning number_** sort them alphabetically by their firstnames.

Function parameters:
- **_st_** a string of firstnames,
- **_we_** an array of weights,
- **_n_** a rank

Return: the firstname of the participant whose rank is **_n_** (ranks are numbered from 1)

**_Examples_**

```
names: 'COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH'
weights: [1, 4, 4, 5, 2, 1]
n: 4

The function should return: 'PauL'
```

**_NOTES:_**

- The weight array is at least as long as the number of names, it may be longer.

- If **_st_** is empty return "No participants".

- If **_n_** is greater than the number of participants then return "Not enough participants".

#

<br />

# Challenge 077 Sort The Inner Content In Descending Order

My solution -> *[077SortTheInnerContentInDescendingOrder](077SortTheInnerContentInDescendingOrder.js)*

## **_Task condition:_**

You have to sort the inner content of every word of a string in descending order.

The inner content is the content of a word without first and the last char.

**_Examples_**

```
Input: 'sort the inner content in descending order' => Output: 'srot the inner ctonnet in dsnnieedcg oredr'

Input: 'wait for me'                                => Output: 'wiat for me'

Input: 'this kata is easy'                          => Output: 'tihs ktaa is esay'
```

**_NOTES:_**

- Words are made up of lowercase letters.

- The string will never be null and will never be empty.

#

<br />

# Challenge 078 Lottery Ticket

My solution -> *[078LotteryTicket](078LotteryTicket.js)*

## **_Task condition:_**

Given a lottery ticket, represented by an array of 2-value arrays, you must find out if you've won the jackpot.

To do this, you must first count the 'mini-wins' on your ticket. Each subarray has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini win. Note you can only have one mini win per sub array.

Once you have counted all of your mini wins, compare that number to the other input provided (win). If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

**_Examples_**

```
Input: [['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2 => Output: 'Loser!'

Input: [['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1 => Output: 'Winner!'

Input: [['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3 => Output: 'Loser!'
```

**_NOTES:_**

- All inputs will be in the correct format.

- Strings on tickets are not always the same length.

#

<br />

# Challenge 079 What century is it?

My solution -> *[079WhatCenturyIsIt](079WhatCenturyIsIt.js)*

## **_Task condition:_**

Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

**_Examples_**

```
Input: '1999' => Output: '20th'

Input: '2011' => Output: '21st'

Input: '2154' => Output: '22nd'

Input: '2259' => Output: '23rd'

Input: '1124' => Output: '12th'

Input: '2000' => Output: '20th'
```

#

<br />

# Challenge 080 Inside Out Strings

My solution -> *[080InsideOutStrings](080InsideOutStrings.js)*

## **_Task condition:_**

You are given a string of words (x), for each word within the string you need to turn the word 'inside out' - the internal letters will move out, and the external letters move toward the centre.

If the word is even length, all letters will move. If the length is odd, you are expected to leave the 'middle' letter of the word where it is.

**_Examples_**

```
Input: 'taxi' => Output: 'atix'

Input: 'taxis' => Output: 'atxsi'

Input: 'man i need a taxi up to ubud' => Output: 'man i ende a atix up to budu'
```

#

<br />

# Challenge 081 String average

My solution -> *[081StringAverage](081StringAverage.js)*

## **_Task condition:_**

You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string.

If the string is empty or includes a number greater than 9, return **_"n/a"_**.

**_Examples_**

```
Input: 'zero nine five two' => Output: 'four'
```

#

<br />

# Challenge 082 Binary to Text (ASCII) Conversion

My solution -> *[082BinaryToTextASCIIConversion](082BinaryToTextASCIIConversion.js)*

## **_Task condition:_**

Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

Each 8 bits on the binary string represent 1 character on the ASCII table.

The input string will always be a valid binary string.

Characters can be in the range from "00000000" to "11111111" (inclusive).

**_Examples_**

```
Input: '01100001' => Output: 'a'

Input: '01001011010101000100100001011000010000100101100101000101' => Output: 'KTHXBYE'

Input: '00110001001100000011000100110001' => Output: '1011'

Input: '001111000011101000101001' => Output: '<:)'

Input: '' => Output: ''
```

**_NOTES:_**

- In the case of an empty binary string function should return an empty string.

#

<br />

# Challenge 083 Run-length encoding

My solution -> *[083RunLengthEncoding](083RunLengthEncoding.js)*

## **_Task condition:_**

**_RLE_** is a very simple form of data compression. It's only suitable for runs of data.

It's very effective if the same data value occurs in many consecutive data elements.

Your task is to write a run-length encoding **_(RLE)_**. For a given string, return a list (or array) of pairs (or arrays) **_[ (i1, s1), (i2, s2), …, (in, sn) ]_**, such that one can reconstruct the original string by replicating the character **_sx ix_** times and concatening all those strings. Your run-length encoding should be minimal, ie. for all **_i_** the values **_si_** and **_si+1_** should differ.

**_Examples_**

```
Input: 'hello world!' => Output: [[1,'h'], [1,'e'], [2,'l'], [1,'o'], [1,' '], [1,'w'], [1,'o'], [1,'r'], [1,'l'], [1,'d'], [1,'!']]

Input: 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb' => Output: [[34,'a'], [3,'b']]
```

#

<br />

# Challenge 084 Convert A Hex String To RGB

My solution -> *[084ConvertAHexStringToRGB](084ConvertAHexStringToRGB.js)*

## **_Task condition:_**

When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:

- Accepts a case-insensitive hexadecimal color string as its parameter (ex. **_"#FF9933"_** or **_"#ff9933"_**).

- Returns a Map<String, int> with the structure **_{r: 255, g: 153, b: 51}_** where r, g, and b range from 0 through 255.

**_Examples_**

```
Input: '#FF9933' => Output: {r: 255, g: 153, b: 51}
```

**_NOTES:_**

- Your implementation does not need to support the shorthand form of hexadecimal notation (ie **_"#FFF"_**).

#

<br />

# Challenge 085 Poker cards encoder/decoder

My solution -> *[085PokerCardsEncoderDecoder](085PokerCardsEncoderDecoder.js)*

## **_Task condition:_**

Consider a deck of 52 cards, which are represented by a string containing their suit and face value.

Your task is to write two functions **_encode_** and **_decode_** that translate an array of cards to/from an array of integer codes.

### Function **_encode_**:

- Input: array of strings (symbols)

- Output: array of integers (codes) sorted in ascending order

### Function **_decode_**:

- Input: array of integers (codes)

- Output: array of strings (symbols) sorted by code values

The returned array must be sorted from lowest to highest priority (value or precedence order, see below).

### Card suits:

```
name    |  symbol   |  precedence
---------------------------------
club          c            0
diamond       d            1
heart         h            2
spade         s            3
```

### 52-card deck:

```
  c     |     d     |    h     |    s
----------------------------------------
 0: A      13: A      26: A      39: A
 1: 2      14: 2      27: 2      40: 2
 2: 3      15: 3      28: 3      41: 3
 3: 4      16: 4      29: 4      42: 4
 4: 5      17: 5      30: 5      43: 5
 5: 6      18: 6      31: 6      44: 6
 6: 7      19: 7      32: 7      45: 7
 7: 8      20: 8      33: 8      46: 8
 8: 9      21: 9      34: 9      47: 9
 9: T      22: T      35: T      48: T
10: J      23: J      36: J      49: J
11: Q      24: Q      37: Q      50: Q
12: K      25: K      38: K      51: K
```

**_Examples_**

```
- encoding

Input: ['Ac', 'Ks', '5h', 'Td', '3c'] => Output: [0, 2 ,22, 30, 51]

- decoding

Input: [0, 51, 30, 22, 2] => Output: ['Ac', '3c', 'Td', '5h', 'Ks']
```

#

<br />

# Challenge 086 String Insert Values

My solution -> *[086StringInsertValues](086StringInsertValues.js)*

## **_Task condition:_**

Given a string and an object/array you need to return a formatted string. Replace all occurrences in the string where the name of a key in the object is surrounded by curly brackets.

Inherited object properties should not be applied

### **_Examples_**

```
Examples using object

Input: 'Hello {foo} - make me a {bar}', { foo: 'Jack', bar: 'sandwich' }
Output: 'Hello Jack - make me a sandwich'

Input: 'Hello {foo} - {foobar} make me a {bar}... {foo}!!?', { bar: 'sandwich {foo}', foo: 'Jack' }
Output: 'Hello Jack - {foobar} make me a sandwich {foo}... Jack!!?'

Example using array

Input: 'Hello {0} - {foobar} make me {2} {1} - I\'m full..', ['Jack', 'sandwiches', 0]
Output: 'Hello Jack - {foobar} make me 0 sandwiches - I'm full..'
```

#

<br />

# Challenge 087 Closest Friends

My solution -> *[087ClosestFriends](087ClosestFriends.js)*

## **_Task condition:_**

Timmy spends a lot of time talking on the phone and he would like to see which friends he talks to the most.

Complete the function ```closestFriends``` that takes an array ```history``` as input. Each element of history is a string in the following format ```"(000) 000-0000 00:00:00"``` (where the first part ```"(000) 000-0000"```) represents the phone number Timmy talked to and the second ```"00:00:00"``` is the call duration ```(hours : minutes : seconds)```. Your job is to find the three contacts Timmy talked to the most and return their names in an array sorted by total call durations.

A global variable ```phonebook``` is preloaded and contains all the contacts and their phone numbers.

```
let phonebook = {
    'John': '(555) 010-3535',
    'Melissa': '(442) 130-5165',
    'Jack': '(333) 010-5135',
    //and so on...
};
```

The input ```history``` array will always have at least three different phone numbers.

### **_Examples_**

```
Input: ['(555) 010-3535 00:13:24', '(442) 130-5165 01:36:26', '(333) 010-5135 01:38:24']

Output: ['Jack','Melissa','John']
```

#

<br />

# Challenge 088 Strip Comments

My solution -> *[088StripComments](088StripComments.js)*

## **_Task condition:_**

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

### **_Examples_**

```
Input: 'aa / bb\ncc ^ dd\nee $ ff', ['/', '^', '$']

Output: 'aa\ncc\nee'
```

#

<br />

# Challenge 089 Human Readable Duration Format

My solution -> *[089HumanReadableDurationFormat](089HumanReadableDurationFormat.js)*

## **_Task condition:_**

Your task is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns ```"now"```. Otherwise, the duration is expressed as a combination of ```years```, ```days```, ```hours```, ```minutes``` and ```seconds```.

```
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
```

For the purpose of this task, a year is 365 days and a day is 24 hours.

Note that spaces are important.

### **_Detailed rules_**

The resulting expression is made of components like ```4 seconds```, ```1 year```, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space ```(", ")```. Except the last component, which is separated by ```" and "```, just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, ```1 second and 1 year``` is not correct, but ```1 year and 1 second``` is.

Different components have different unit of times. So there is not repeated units like in ```5 seconds and 1 second```.

A component will not appear at all if its value happens to be zero. Hence, ```1 minute and 0 seconds``` is not valid, but it should be just ```1 minute```.

A unit of time must be used "as much as possible". It means that the function should not return ```61 seconds```, but ```1 minute and 1 second``` instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

### **_Examples_**

```
Input: 1 => Output: '1 second'

Input: 62 => Output: '1 minute and 2 seconds'

Input: 120 => Output: '2 minutes'

Input: 3600 => Output: '1 hour'

Input: 3662 => Output: '1 hour, 1 minute and 2 seconds'
```

#

<br />

# Challenge 090 Salesman's Travel

My solution -> *[090SalesmansTravel](090SalesmansTravel.js)*

## **_Task condition:_**

A traveling salesman has to visit clients. He got each client's address e.g. ```"432 Main Long Road St. Louisville OH 43071"``` as a list.

The basic zipcode format usually consists of two capital letters followed by a white space and five digits. The list of clients to visit was given as a string of all addresses, each separated from the others by a comma, e.g. :

```"123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432".```

To ease his travel he wants to group the list by zipcode.

The function ```travel``` will take two parameters ```r``` (addresses' list of all clients' as a string) and ```zipcode``` and returns a string in the following format:

```zipcode:street and town,street and town,.../house number,house number,...```

The street numbers must be in the same order as the streets where they belong.

If a given zipcode doesn't exist in the list of clients' addresses return ```"zipcode:/"```.

### **_Examples_**

```
Input: "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432", "OH 43071"

Output: "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"

Input: "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432", "NY 56432"

Output: "NY 56432:High Street Pollocksville/786"

Input: "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432", "NY 5643"

Output: "NY 5643:/"
```

#

<br />

# Challenge 091 Rotated String

My solution -> *[091RotatedString](091RotatedString.js)*

## **_Task condition:_**

Write to function that takes as argument two strings and returns positive ```True/true/1``` if one string is a rotation of the other or else it returns ```False/false/0```.

### **_Examples_**

```
Input: 'hello', 'ohell' => Output: true

Input: 'hello', 'elloh' => Output: true

Input: 'hello', 'lloeh' => Output: fslse
```

#

<br />

# Challenge 092 RGB To Hex Conversion

My solution -> *[092RGBToHexConversion](092RGBToHexConversion.js)*

## **_Task condition:_**

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

### **_Examples_**

```
Input: 55, 255, 255  => Output: 'FFFFFF'

Input: 255, 255, 300 => Output: 'FFFFFF'

Input: 0, 0, 0       => Output: '000000'

Input: 148, 0, 211   => Output: '9400D3'
```

**_NOTES:_**

- Your answer should always be 6 characters long, the shorthand with 3 will not work here.

#

<br />

# Challenge 093 Count Repeats

My solution -> *[093CountRepeats](093CountRepeats.js)*

## **_Task condition:_**

Write a function that returns the count of characters that have to be removed in order to get a string with no consecutive repeats.

This includes any characters

### **_Examples_**

```
Input: 'abbbbc' => Output: 'abc'

Input: 'abbcca' => Output: 'abca'

Input: 'ab cca' => Output: 'ab ca'
```

#

<br />

# Challenge 094 Only Duplicates

My solution -> *[094OnlyDuplicates](094OnlyDuplicates.js)*

## **_Task condition:_**

Given a string, remove any characters that are unique from the string.

### **_Examples_**

```
Input: 'abccdefee' => Output: 'cceee'
```

#

<br />

# Challenge 095 Detect Pangram

My solution -> *[095DetectPangram](095DetectPangram.js)*

## **_Task condition:_**

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters ```A-Z``` at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return ```true``` if it is, ```false``` if not. Ignore numbers and punctuation.

### **_Examples_**

```
Input: "The quick brown fox jumps over the lazy dog." => Output: true

Input: "This is not a pangram." => Output: false
```

#

<br />

# Challenge 096 Write Number In Expanded Form - Part 2

My solution -> *[096WriteNumberInExpandedFormPart2](096WriteNumberInExpandedFormPart2.js)*

## **_Task condition:_**

You will be given a number and you will need to return it as a string in expanded form.

```
Number: 7286.45

        Hundred   Ten                                       One   One       One
Milions Thousands Thousands Thousands Hundreds Tens Units . tenth hundredth thousandth
   |        |         |         |        |      |     |       |       |          |
   -        -         -         7        2      8     6       4       5          -

Expanded Form: 7000 + 200 + 80 + 6 + 4/10 + 5/100
```

### **_Examples_**

```
Input: 807.304 => Output: '800 + 7 + 3/10 + 4/1000'

Input: 1.24    => Output: '1 + 2/10 + 4/100'

Input: 7.304   => Output: '7 + 3/10 + 4/1000'

Input: 0.04    => Output: '4/100'
```

#

<br />

# Challenge 097 Title Case

My solution -> *[097TitleCase](097TitleCase.js)*

## **_Task condition:_**

A string is considered to be in title case if each word in the string is either ```(a)``` capitalised (that is, only the first letter of the word is in upper case) or ```(b)``` considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions ```(minor words)```. The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string - it should behave in the same way even if the case of the minor word string is changed.

Arguments:

- First argument (required): the original string to be converted.
- Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.


### **_Examples_**

```
Input: 'a clash of KINGS', 'a an the of' => Output: 'A Clash of Kings'

Input: 'THE WIND IN THE WILLOWS', 'The In' => Output: 'The Wind in the Willows'

Input: 'the quick brown fox' => Output: 'The Quick Brown Fox'
```

#

<br />

# Challenge 098 Alphabetized

My solution -> *[098Alphabetized](098Alphabetized.js)*

## **_Task condition:_**

Re-order the characters of a string, so that they are concatenated into a new string in ```"case-insensitively-alphabetical-order-of-appearance"``` order. Whitespace and punctuation shall simply be removed!

The input is restricted to contain no numerals and only words containing the english alphabet letters.

### **_Examples_**

```
Input: 'The Holy Bible' => Output: 'BbeehHilloTy'

Input: '^_`'            => Output: ''
```

#

<br />

# Challenge 099 Build Tower

My solution -> *[099BuildTower](099BuildTower.js)*

## **_Task condition:_**

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer ```number of floors```. A tower block is represented with ```"*"``` character.

### **_Examples_**

```
Input: 3

[
  "  *  ",
  " *** ", 
  "*****"
]

Input: 6

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

#

<br />

# Challenge 100 Simple Encryption #1 - Alternating Split

My solution -> *[100SimpleEncryptionN1AlternatingSplit](100SimpleEncryptionN1AlternatingSplit.js)*

## **_Task condition:_**

Implement a pseudo-encryption algorithm which given a string ```S``` and an integer ```N``` concatenates all the odd-indexed characters of ```S``` with all the even-indexed characters of ```S```, this process should be repeated ```N``` times.

Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string ```S``` is an empty value or the integer ```N``` is not positive, return the first argument without changes.

### **_Examples_**

```
encrypt:

Input: '01234', 1 => Output: '13024'
Input: '012345', 1 => Output: '135024'
Input: '012345', 2 => Output: '135024' -> '304152'
Input: '012345', 3 => Output: '135024' -> '304152' -> '012345'
Input: '', 1 => Output: ''
Input: '012345', -1 => Output: '012345'
Input: '012345', 0 => Output: '012345'

decrypt:

Input: '13024', 1 => Output: '01234'
Input: '135024', 1 => Output: '012345'
```

#

<br />

# Challenge 101 Consonant Value

My solution -> *[101ConsonantValue](101ConsonantValue.js)*

## **_Task condition:_**

Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except ```"aeiou"```.

We shall assign the following values: ```a = 1, b = 2, c = 3, .... z = 26```.

For example, for the word "zodiacs", let's cross out the vowels. We get: **"z~~o~~d~~ia~~cs"**.

### **_Examples_**

```
Input: 'zodiacs' => Output: 26

Input: 'strength' => Output: 57

Input: 'az' => Output: 26
```

#

<br />

# Challenge 102 Phone Directory

My solution -> *[102PhoneDirectory](102PhoneDirectory.js)*

## **_Task condition:_**

John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the phone number (formated as ```+X-abc-def-ghij``` where ```X``` stands for one or two digits), the corresponding name between ```<``` and ```>``` and the address.

Unfortunately everything is mixed, things are not always in the same order; parts of lines are cluttered with non-alpha-numeric characters (except inside phone number and name).

Examples of John's phone book lines:

```"/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"```

```" 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"```

```"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"```

Could you help John with a program that, given the lines of his phone book and a phone number ```num``` returns a string for this number : ```"Phone => num, Name => name, Address => adress"```?

- It can happen that there are many people for a phone number ```num```, then return : ```"Error => Too many people: num"```.

- Or it can happen that the number ```num``` is not in the phone book, in that case return: ```"Error => Not found: num"```.

### **_Examples_**

```
Input: "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n", "1-541-754-3010"

Output: "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
```

#

<br />

# Challenge 103 Sort Arrays - 3

My solution -> *[103SortArrays3](103SortArrays3.js)*

## **_Task condition:_**

This time the input is a sequence of course-ids that are formatted in the following way:

```
name-yymm
```

The return of the function shall first be sorted by **yymm**, then by the **name** (which varies in length).

### **_Examples_**

```
Input:  ['web-1305', 'site-1305', 'web-1304', 'site-1304']
Output: ['site-1304', 'web-1304', 'site-1305', 'web-1305']

Input:  ['aeb-1305', 'site-1305', 'play-1215', 'web-1304', 'site-1304', 'beb-1305']
Output: ['play-1215', 'site-1304', 'web-1304', 'aeb-1305', 'beb-1305', 'site-1305']

Input:  ['aeb-1305', 'aeb-1305']
Output: ['aeb-1305', 'aeb-1305']

Input:  []
Output: []
```

#

<br />

# Challenge 104 Sports League Table Ranking

My solution -> *[104SportsLeagueTableRanking](104SportsLeagueTableRanking.js)*

## **_Task condition:_**

You organize a sports league in a round-robin-system. Each team meets all other teams. In your league a win gives a team ```2 points```, a draw gives both teams ```1 point```. After some games you have to compute the order of the teams in your league. You use the following criteria to arrange the teams:

- Points
- Scoring differential (the difference between goals scored and those conceded)
- Goals scored

First you sort the teams by their points. If two or more teams reached the same number of points, the second criteria comes into play and so on. Finally, if all criteria are the same, the teams share a place.

#### Input

- ```number```: Number of teams in your league.
- ```games```: An array of arrays. Each item represents a played game with an array of four elements ```[TeamA,TeamB,GoalA,GoalB]``` (```TeamA``` played against ```TeamB``` and scored ```GoalA``` goals and conceded ```GoalB``` goals ).

#### Output

- ```positions```: An array of positions. The ```i```-th item should be the position of the ```i```-th team in your league.

### **_Examples_**

```
Input:  

number = 6

games = [[0, 5, 2, 2],   // Team 0 - Team 5 => 2:2
         [1, 4, 0, 2],   // Team 1 - Team 4 => 0:2
         [2, 3, 1, 2],   // Team 2 - Team 3 => 1:2
         [1, 5, 2, 2],   // Team 1 - Team 5 => 2:2
         [2, 0, 1, 1],   // Team 2 - Team 0 => 1:1
         [3, 4, 1, 1],   // Team 3 - Team 4 => 1:1
         [2, 5, 0, 2],   // Team 2 - Team 5 => 0:2
         [3, 1, 1, 1],   // Team 3 - Team 1 => 1:1
         [4, 0, 2, 0]]   // Team 4 - Team 0 => 2:0

Output: [4, 4, 6, 3, 1, 2]
```

You may compute the following table:

```
Rank  Team    For : Against   GD  Points
----------------------------------------
1.    Team 4    5 : 1         +4    5
2.    Team 5    6 : 4         +2    4
3.    Team 3    4 : 3         +1    4
4.    Team 0    3 : 5         -2    2
4.    Team 1    3 : 5         -2    2
6.    Team 2    2 : 5         -3    1
```

Team 5 and Team 3 reached the same number of points. But since Team 5 got a better scoring differential, it ranks better than Team 3. All values of Team 0 and Team 1 are the same, so these teams share the fourth place.

#

<br />

# Challenge 105 Grab CSV Columns

My solution -> *[105GrabCSVColumns](105GrabCSVColumns.js)*

## **_Task condition:_**

Write a function that takes a CSV (format shown below) and a sequence of indices, which represents the columns of the CSV, and returns a CSV with only the columns specified in the indices sequence.

#### CSV format:

The CSV passed in will be a string and will have one or more columns, and one or more rows. The CSV will be of size NxM. Each row is separated by a new line character \n. There will be no spaces in the CSV string.

Example format of passed in CSV: ```"1,2,3\n4,5,6\n7,8,9\n10,11,12"```

How it would look:

```
1,2,3
4,5,6
7,8,9
10,11,12
```

#### Indices Array info:


- The indices will be zero based, so the first column will be represented as a 0 in the indices sequence.
- All values in the indices sequence will be integers from 0 and up.
- All test cases will have an indices sequence of one or more integers.
- Ignore indices that map to a column that doesn't exist.
- If all the values in the indices array do NOT map to any existing column, return an empty string "".

The columns of the result must be ordered and not repeated.

### **_Examples_**

```
csv,                                indices       =>  expected
---------------------------------------------------------------------
"1,2,3\n4,5,6",                     [0, 1]        =>  "1,2\n4,5"
"1,2\n3,4\n5,6",                    [5, 6, 7]     =>  ""
"a,b,c,d,e\n1,2,3,4,5\nf,g,h,i,j",  [1, 3, 5, 7]  =>  "b,d\n2,4\ng,i"
```

#

<br />

# Challenge 106 Don't Drink the Water

My solution -> *[106DoNotDrinkTheWater](106DoNotDrinkTheWater.js)*

## **_Task condition:_**

Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the glass based on their density. (Lower density floats to the top) The width of the glass will not change from top to bottom.

```
=======================
|   Density Chart     |
=======================
| Honey   | H | 1.36  |
| Water   | W | 1.00  |
| Alcohol | A | 0.87  |
| Oil     | O | 0.80  |
-----------------------
```

### **_Examples_**

```
Input:

[
  ['H', 'H', 'W', 'O'],
  ['W', 'W', 'O', 'W'],
  ['H', 'H', 'O', 'O']
]

Output:

[
  ['O', 'O', 'O', 'O'],
  ['W', 'W', 'W', 'W'],
  ['H', 'H', 'H', 'H']
]
```

#

<br />

# Challenge 107 Remove The Parentheses

My solution -> *[107RemoveTheParentheses](107RemoveTheParentheses.js)*

## **_Task condition:_**

You are given a string that may contains parenthesis - ```'('``` and ```')'```.

Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

### **_Examples_**

```
Input: 'example(unwanted thing)example' => Output: 'exampleexample'

Input: 'example (unwanted thing) example' => Output: 'example  example'

Input: 'a (bc d)e' => Output: 'a e'

Input: 'a(b(c))' => Output: 'a'

Input: 'hello example (words(more words) here) something' => Output: 'hello example  something'

Input: '(first group) (second group) (third group)' => Output: '  '
```

**_NOTES:_**

- Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like ```"[]"``` and ```"{}"``` as these will never appear.
- There can be multiple parentheses.
- The parentheses can be nested.

#

<br />

# Challenge 108 Pirate Island Conquer Part 1

My solution -> *[108PirateIslandConquerPart1](108PirateIslandConquerPart1.js)*

## **_Task condition:_**

You are a captain on a pirate ship. You are looking to conquer islands, so that you can do lots of piratey stuff on those islands. Let's take a look at your pirate map of the area:

## Map

```
                          y
        0     1    2    3    4    5    6    7

  0   [['p', '~', '~', '~', '~', '~', '~', '~'],
  1    ['~', '~', '~', '~', '~', '~', '~', '~'],
  2    ['~', '~', '~', '~', '~', '~', '~', '~'],
  3    ['~', '~', 'u', '~', '~', '~', '~', '~'],
x 4    ['~', '~', '~', '~', 'm', '~', '~', '~'],
  5    ['~', '~', '~', '~', '~', '~', '~', '~'],
  6    ['~', '~', '~', '~', '~', '~', '~', '~'],
  7    ['~', '~', '~', '~', '~', '~', '~', '~']];
```

Where:

- ```'p'``` = pirate (that's our home island). There will always be one home island, always in the top left corner of the sea.
- ```'u'``` = unoccupied island
- ```'m'``` = island occupied by marines
- ```'~'``` = ocean waves

The map size will always be ```8 x 8```. Each of ```'u'```, ```'m'``` and ```'~'``` can occur in any space of the map.
Coordinates are given as ```[x,y]``` (examples from the above map: ```'p'``` at ```[0, 0]```, ```'u'``` at ```[3, 2]```, ```'m'``` at ```[4, 4]```).

### Input

A see map, formatted as an array of arrays of strings.

### Output

Return an array containing all the best candidates (ordered by lowest ```x``` coordinate, then lowest ```y```), or an empty array if no island to conquer.

### Rules (highest priority first)

- Conquer an unoccupied island.
- If there are no unoccupied islands, conquer one of the marines' islands.
- Conquer the island closest to any of our home islands (the ```p``` items / distances are computed as ```Manhattan distances```).

### Distance

Pirates can only move vertically and horizontally, not diagonally. Moving one index in the array is one unit of distance.

Example 1: The ```'u'``` island is 2 units away:

```
['p', '~', 'u', '~', '~', '~', '~', '~'],
['~', '~', '~', '~', '~', '~', '~', '~'],
['~', '~', '~', '~', '~', '~', '~', '~'],
...
```

Example 2: The ```'u'``` island is 3 + 2 = 5 units away.

```
  | ['p', '~', '~', '~', '~', '~', '~', '~'],
  | ['~', '~', '~', '~', '~', '~', '~', '~'],
3 | ['~', '~', '~', '~', '~', '~', '~', '~'],
  | ['~', '~', 'u', '~', '~', '~', '~', '~'],
  |---------->
      2
```

### **_Examples_**

Example 1:
```
map = [
    ['p', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', 'm', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', 'u', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~']];
```
solution = [[4, 4]]

There is a ```'u'``` and an ```'m'```. Rules say we conquer a ```'u'``` if possible, so...

Example 2:

```
map = [
    ['p', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', 'm', '~', '~', '~', '~'],
    ['m', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', 'm', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', 'm', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~']];
```
solution = [[2,0]] 

Example 3:
```
map = [
    ['p', '~', '~', '~', '~', '~', '~', '~'],
    ['~', 'm', '~', 'm', '~', '~', '~', '~'],
    ['m', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', 'm', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', 'm', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~']];
```
There are no ```'u'``` islands, so we'll take an ```'m'```. But wait! There are two the same distance away.

solution = [[1, 1], [2, 0]], not [[2, 0], [1, 1]] (lowest 'x' value first)

#

<br />

# Challenge 109 Pirate Island Conquer Part 2

My solution -> *[109PirateIslandConquerPart21](109PirateIslandConquerPart2.js)*

## **_Task condition:_**

#### Part 2 is similar to part 1 with the following changes:

#### - The pirate home island is not only at [0, 0].

#### - There is between 1 and 3 pirate home islands.

You are a captain on a pirate ship. You are looking to conquer islands, so that you can do lots of piratey stuff on those islands. Let's take a look at your pirate map of the area:

## Map

```
                          y
        0     1    2    3    4    5    6    7

  0   [['p', '~', '~', '~', '~', '~', '~', '~'],
  1    ['~', '~', '~', '~', '~', '~', '~', '~'],
  2    ['~', '~', '~', '~', '~', '~', '~', '~'],
  3    ['~', '~', 'u', '~', '~', '~', '~', '~'],
x 4    ['~', '~', '~', '~', 'm', '~', '~', '~'],
  5    ['~', '~', '~', '~', '~', '~', '~', '~'],
  6    ['~', '~', '~', '~', '~', '~', '~', '~'],
  7    ['~', '~', '~', '~', '~', '~', '~', '~']];
```

Where:

- ```'p'``` = pirate (that's our home island). There will always be one home island, always in the top left corner of the sea.
- ```'u'``` = unoccupied island
- ```'m'``` = island occupied by marines
- ```'~'``` = ocean waves

The map size will always be ```8 x 8```. Each of ```'u'```, ```'m'``` and ```'~'``` can occur in any space of the map.
Coordinates are given as ```[x,y]``` (examples from the above map: ```'p'``` at ```[0, 0]```, ```'u'``` at ```[3, 2]```, ```'m'``` at ```[4, 4]```).

### Input

A see map, formatted as an array of arrays of strings.

Number of each label in one map:

- ```'p'```: 1 to 3
- ```'u'```: 0 to 5
- ```'m'```: 0 to 5

### Output

Return an array containing all the best candidates (ordered by lowest ```x``` coordinate, then lowest ```y```), or an empty array if no island to conquer.

### Rules (highest priority first)

- Conquer an unoccupied island.
- If there are no unoccupied islands, conquer one of the marines' islands.
- Conquer the island(s) closest to any of our home islands (the ```p``` items / distances are computed as ```Manhattan distances```).

### Distance

Pirates can only move vertically and horizontally, not diagonally. Moving one index in the array is one unit of distance.

Example 1: The ```'u'``` island is 2 units away:

```
['p', '~', 'u', '~', '~', '~', '~', '~'],
['~', '~', '~', '~', '~', '~', '~', '~'],
['~', '~', '~', '~', '~', '~', '~', '~'],
...
```

Example 2: The ```'u'``` island is 3 + 2 = 5 units away.

```
  | ['p', '~', '~', '~', '~', '~', '~', '~'],
  | ['~', '~', '~', '~', '~', '~', '~', '~'],
3 | ['~', '~', '~', '~', '~', '~', '~', '~'],
  | ['~', '~', 'u', '~', '~', '~', '~', '~'],
  |---------->
      2
```

### **_Examples_**

Example 1:
```
map = [
    ['p', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', 'm', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', 'u', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~']];
```
solution = [[4, 4]]

There is a ```'u'``` and an ```'m'```. Rules say we conquer a ```'u'``` if possible, so...

Example 2:

```
map = [
    ['p', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', 'm', '~', '~', '~', '~'],
    ['m', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', 'm', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', 'm', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~']];
```
solution = [[2,0]] 

Example 3:
```
map = [
    ['p', '~', '~', '~', '~', '~', '~', '~'],
    ['~', 'm', '~', 'm', '~', '~', '~', '~'],
    ['m', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', 'm', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', 'm', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~']];
```
There are no ```'u'``` islands, so we'll take an ```'m'```. But wait! There are two the same distance away.

solution = [[1, 1], [2, 0]], not [[2, 0], [1, 1]] (lowest 'x' value first)

Example 4:
```
map = [
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', 'p', 'm', '~', '~', '~', '~'],
    ['m', '~', 'm', 'p', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', 'm', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', 'm', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~']];
```
solution = [[1, 3], [2, 2]]

There are no ```'u'``` islands, so we'll take the closest two ```'m'``` islands. 

#

<br />

# Challenge 110 Mastermind

My solution -> *[110Mastermind](110Mastermind.js)*

## **_Task condition:_**

### Rules

1. The Mastermind (computer) will select 4 colours. The colours are randomly selected from ```["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]```. Colours can be duplicated but there will always be exactly ```4```.
2. The Mastermind will return an array back to you. For every correctly positioned colour in the array an element of ```"Black"``` is returned. For every correct colour but in the wrong position an element of ```"White"``` will be returned.
3. Passing the correct array will pass the Kata test and return ```"WON!"```.
4. Passing an invalid colour will fail the test with the error ```"Error: you have given an invalid colour!"```.
5. Passing an invalid array length will fail the test with the error ```"Error: you must pass 4 colours!"```.
6. Guessing more than ```60``` times will fail the test with the error ```"Error: you have had more than 60 tries!"```.
7. All colours are capitalised.
8. The return array will be shuffled!

### Task

Your task is to create a method called ```mastermind()``` that will take an object called ```game```. The object has already been preloaded so you do not need to worry about it.

Within your method you must pass an array into the game object method ```.check()```. This will evoke the object to check your array to see if it is correct.

### **_Examples_**

If the Mastermind selected the following colours:

```
  0     1     2     3
Red, Blue, Green, Yellow
```

Then the array you are trying to solve is ```["Red", "Blue", "Green", "Yellow"]```

So you guess with:

```
  0     1       2      3
Red, Orange, Yellow, Orange
```

```["Red", "Orange", "Yellow", "Orange"]```

Your method would look like this.

```
function mastermind(game){
  answer = game.check(["Red", "Orange", "Yellow", "Orange"]);
}
```

The element ```0 => Red``` is at the correct index so ```Black``` is added to the return array. Element ```2 => Yellow``` is in the array but at the wrong index position so ```White``` is added to the return array.

The Mastermind would then return ```["Black", "White"]``` (But not necessarily in that order as the return array is shuffled by the Mastermind).

Keep guessing until you pass the correct solution which will pass the Kata.

### Check result

To check the Masterminds return value

```
answer = game.check(["Red", "Orange", "Yellow", "Orange"]);
console.log(answer);
```

#

<br />

# Challenge 111 Not Very Secure

My solution -> *[111NotVerySecure](111NotVerySecure.js)*

## **_Task condition:_**

In this task you have to validate if a user input string is alphanumeric. The given string is not ```null```, so you don't have to check that.

The string has the following conditions to be alphanumeric:

- At least one character (```""``` is not valid)
- Allowed characters are uppercase / lowercase latin letters and digits from ```0``` to ```9```
- No whitespaces / underscore

### **_Examples_**

```
Input: 'Mazinkaiser' => Output: true

Input: 'hello world_' => Output: false

Input: 'PassW0rd' => Output: true

Input: '     ' => Output: false
```

#

<br />

# Challenge 112 Value Of X

My solution -> *[112ValueOfX](112ValueOfX.js)*

## **_Task condition:_**

Jack's teacher gave him a ton of equations for homework. The thing is they are all kind of same so they are boring.

So help him by making a equation solving function that will return the value of ```x```.

- All test cases are valid.
- Every ```+```, ```-``` and numbers will be separated by space.
- There will be only one ```x``` either on the left or right.
- ```x``` can have a ```-``` mark before it.
- Returned object will be a integer.

### **_Examples_**

```
Input: 'x + 1 = 9 - 2'    => Output: 6

Input: 'x - 2 + 3 = 2'    => Output: 1

Input: 'x = + 2 - 5 + 9'  => Output: 6

Input: '- 10 = x'         => Output: -10

Input: '- x = - 1'        => Output: 1

Input: 'x - 0 + 0 = 0'    => Output: 0
```

#

<br />

# Challenge 113 Mean Square Error

My solution -> *[113MeanSquareError](113MeanSquareError.js)*

## **_Task condition:_**

Complete the function that

- accepts two integer arrays of equal length
- compares the value each member in one array to the corresponding member in the other
- squares the absolute value difference between those two values
- and returns the average of those squared absolute value difference between each member pair.

### **_Examples_**

```
Input: [1, 2, 3], [4, 5, 6]             => Output: 9    because (9 + 9 + 9) / 3

Input: [10, 20, 10, 2], [10, 25, 5, -2] => Output: 16.5 because (0 + 25 + 25 + 16) / 4

Input: [-1, 0], [0, -1]                 => Output: 1    because (1 + 1) / 2
```

#

<br />

# Challenge 114 Numbers That Are A Power Of Their Sum Of Digits

My solution -> *[114NumbersThatAreAPowerOfTheirSumOfDigits](114NumbersThatAreAPowerOfTheirSumOfDigits.js)*

## **_Task condition:_**

The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). Eighty one (81), is the first number in having this property (not considering numbers of one digit). The next one, is 512. Let's see both cases with the details:

*8 + 1 = 9 and 9<sup>2</sup> = 81*

*512 = 5 + 1 + 2 = 8 and 8<sup>3</sup> = 512*

We need to make a function that receives a number as argument n and returns the *```n-th term```* of this sequence of numbers.

### **_Examples_**

```
Input: 1 => Output: 81

Input: 2 => Output: 512

Input: 3 => Output: 2401

Input: 4 => Output: 4913
```

#

<br />

# Challenge 115 Sorting Poker

My solution -> *[115SortingPoker](115SortingPoker.js)*

## **_Task condition:_**

John learns to play poker with his uncle. His uncle told him: Poker to be in accordance with the order of ```"2 3 4 5 6 7 8 9 10 J Q K A"```. The same suit should be put together. But his uncle did not tell him the order of the four suits.

Give you John's cards and Uncle's cards(two string ```john``` and ```uncle```). Please reference to the order of Uncle's cards, sorting John's cards. 

### **_Examples_**

```
Input:  john = '♦6♥2♠3♦5♠J♣Q♠K♣7♦2♣5♥5♥10♠A'
        uncle = '♠2♠3♠5♥J♥Q♥K♣8♣9♣10♦4♦5♦6♦7'

Output: '♠3♠J♠K♠A♥2♥5♥10♣5♣7♣Q♦2♦5♦6'

Input:  john = '♦6♥2♠3♦5♠J♣Q♠K♣7♦2♣5♥5♥10♠A'
        uncle = '♣8♣9♣10♦4♦5♦6♦7♠2♠3♠5♥J♥Q♥K'

Output: '♣5♣7♣Q♦2♦5♦6♠3♠J♠K♠A♥2♥5♥10'
```

#

<br />

# Challenge 116 Pete, The Baker

My solution -> *[116PeteTheBaker](116PeteTheBaker.js)*

## **_Task condition:_**

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function ```cakes()```, which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

### **_Examples_**

```
Input: {flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}

Output: 2

Input: {apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000}

Output: 0
```

#

<br />

# Challenge 117 Can Santa Save Christmas?

My solution -> *[117CanSantaSaveChristmas](117CanSantaSaveChristmas.js)*

## **_Task condition:_**

Oh no! Santa's little elves are sick this year. He has to distribute the presents on his own.

But he has only 24 hours left. Can he do it?

You will get an array as input with time durations as string in the following format: ```HH:MM:SS```. Each duration represents the time taken by Santa to deliver a present. Determine whether he can do it in ```24``` hours or not. In case the time required to deliver all of the presents is exactly ```24``` hours, Santa can complete the delivery.

### **_Examples_**

```
Input: ['00:30:00', '02:30:00', '00:15:00'] => Output: true

Input: [] => Output: true

Input: ['04:30:00', '02:00:00', '01:30:00', '16:00:00'] => Output: true

Input: ['12:00:00', '12:00:00'] => Output: true

Input: ['12:00:00', '12:00:01'] => Output: false

Input: ['06:00:00', '12:00:00', '06:30:00'] => Output: false
```

#

<br />

# Challenge 118 Sort Santa's Reindeer

My solution -> *[118SortSantasReindeer](118SortSantasReindeer.js)*

## **_Task condition:_**

Now, Dasher! Now, Dancer! Now, Prancer, and Vixen! On, Comet! On, Cupid! On, Donder and Blitzen! That's the order Santa wanted his reindeer...right? What do you mean he wants them in order by their last names!?

Write a function that accepts a sequence of Reindeer names, and returns a sequence with the Reindeer names sorted by their last names.

### **_Examples_**

```
Input:
[
  'Dasher Tonoyan', 
  'Dancer Moore', 
  'Prancer Chua', 
  'Vixen Hall', 
  'Comet Karavani',        
  'Cupid Foroutan', 
  'Donder Jonker', 
  'Blitzen Claus'
]

Output:
[
  'Prancer Chua',
  'Blitzen Claus',
  'Cupid Foroutan', 
  'Vixen Hall', 
  'Donder Jonker', 
  'Comet Karavani',
  'Dancer Moore', 
  'Dasher Tonoyan',
]
```
**_NOTES:_**

- It's guaranteed that each string is composed of two words, separated by a single space.
- In case of two identical last names, keep the original order.

#

<br />

# Challenge 119 Guess The Gifts!

My solution -> *[119GuessTheGifts](119GuessTheGifts.js)*

## **_Task condition:_**

It's **_Christmas!_** You had to wait the whole year for this moment. You can already see all the presents under the **_Christmas tree_**. But you have to wait for the next morning in order to unwrap them. You really want to know, what's inside those boxes. But as a clever child, you can do your assumptions already.

You know, you were a good child this year. So you may assume, that you'll only get things from your wishlist. You see those presents, you can lift them and you can shake them a bit. Now you can make you assumptions about what you'll get.

You will be given a wishlist (array), containing all possible items. Each item is in the format:

```{name: 'toy car', size: 'medium', clatters: 'a bit', weight: 'medium'}```

You also get a list of presents (array), you see under the christmas tree, which have the following format each:

```{size: 'small', clatters: 'no', weight: 'light'}```

Your task is to return the names of all wishlisted presents that you might have gotten.

### **_Rules_**

- Possible values for ```size: 'small', 'medium', 'large'```
- Possible values for ```clatters: 'no', 'a bit', 'yes'```
- Possible values for ```weight: 'light', 'medium', 'heavy'```
- Don't add any item more than once to the result
- The order of names in the output doesn't matter
- It's possible, that multiple items from your wish list have the same attribute values. If they match the attributes of one of the presents, add all of them.

### **_Examples_**

```
guessGifts(wishlist, presents);

Input:

let wishlist =
  [
    {name: 'Mini Puzzle', size: 'small', clatters: 'yes', weight: 'light},
    {name: 'Toy Car', size: 'medium', clatters: 'a bit', weight: 'medium'},
    {name: 'Card Game', size: 'small', clatters: 'no', weight: 'light'}
  ];
let presents =
  [
    {size: 'medium', clatters: 'a bit', weight: 'medium'},
    {size: 'small', clatters: 'yes', weight: 'light'}
  ];

Output:

  ['Toy Car', 'Mini Puzzle']
```

#

<br />

# Challenge 120 Valid Binary Christmas Tree

My solution -> *[120ValidBinaryChristmasTree](120ValidBinaryChristmasTree.js)*

## **_Task condition:_**

Santa just finished taking a data structures course, and thought it would be a great idea to build a Binary Christmas Tree! All of Santa's helpers created a Binary Christmas Tree, but not all of them meet his requirements. Can you write some code to validate the Binary Christmas Trees?

### **_Valid Binary Christmas Tree_**

Write a function ```isValidTree``` that accepts a Binary Tree, and returns true if it meets Santa's requirements, false otherwise. Since the tree is a binary tree, each node can have 0, 1, or 2 children. The ```left``` and ```right``` properties can be used to access the current nodes left and right children. All nodes have an ```ornament``` property, which is the name of the ornament, and a ```color``` property, which represents the color of the ```ornament```.

### **_Santa's Binary Christmas Tree Requirements_**

A valid Binary Christmas Tree will meet the following requirements:

- Root node has a 'star' ornament
- Nodes with zero children (excluding the root node) have a 'blue' colored ornament
- Nodes with one or two children (excluding the root node) have a 'red' colored ornament

### **_Examples_**

```
isValidTree({
  ornament: 'star',
  color: 'yellow'
});

returns => true
___________________________

isValidTree({
  ornament: 'star',
  color: 'yellow',
  left: {
    ornament: 'candy cane',
    color: 'blue'
  }
});

returns => true
___________________________

isValidTree({
  ornament: 'star',
  color: 'yellow',
  right: {
    ornament: 'stocking',
    color: 'red'
  }
});

returns => false
```

#

<br />

# Challenge 121 Only One Gift Per Child

My solution -> *[121OnlyOneGiftPerChild](121OnlyOneGiftPerChild.js)*

## **_Task condition:_**

Santa is handing out gifts in the kindergarten. Many toddlers are around there and everyone should have the opportunity to have a seat on Santa's lap. But there's Peter, a 5 year old boy, who is a bit naughty. He tries to get two gifts. After he got the first one, he lines up again in the queue of children.

But fortunately Santa is not alone. His elves keep a list with the names of the children, which already were on Santa's lap. We know, that each child name is unique. If a child tries to get a second gift, the elves will tell Santa.

OK, let's help Santa and his elves with a simple function ```handOutGift()``` which takes the name of the next child. If this child already got a gift, it must throw an error in order to remind Santa.

### **_Examples_**

```
handOutGift("Peter");
handOutGift("Alison");
handOutGift("John");
handOutGift("Maria");
handOutGift("Peter"); => must throw an error
```

#

<br />

# Challenge 122 Milk And Cookies For Santa

My solution -> *[122MilkAndCookiesForSanta](122MilkAndCookiesForSanta.js)*

## **_Task condition:_**

It's almost Christmas Eve, so we need to prepare some milk and cookies for Santa! Wait... when exactly do we need to do that?

### **_Time for Milk and Cookies_**

Complete the function that accepts a Date object, and returns true if it's Christmas Eve (December 24th), false otherwise.

Keep in mind Javascript's Date month is 0 based!

### **_Examples_**

```
timeForMilkAndCookies(new Date(2013, 11, 24)) // true
timeForMilkAndCookies(new Date(2013, 0, 23))  // false
timeForMilkAndCookies(new Date(3000, 11, 24)) // true
```

#

<br />

# Challenge 123 A Gift Well Spent

My solution -> *[123AGiftWellSpent](123AGiftWellSpent.js)*

## **_Task condition:_**

You got a gift card for your local store. It has some credit you can use to buy things, but it may be used only for up to two items, and any credit you don't use is lost. You want something for a friend and yourself. Therefore, you want to buy two items which add up the entire gift card value.

You will get the value of the gift card ```c``` and a finite list of item values. You should return a pair of indices that correspond to values that add up to ```c```.

The indices start at 0. The first index should always be smaller than the second index. If there are multiple solutions, return the minimum (lexicographically).

### **_Examples_**

```
Input: buy(2,[1,1]) => Output: [0,1]

Input: buy(3,[1,1]) => Output: null

Input: buy(5,[5,2,3,4,5]) => Output: [1,2]

Input: buy(5,[1,2,3,4,5]) => Output: [0,3] - the values at [1,2] also adds up to five, but [0,3] < [1,2]
```

#

<br />

# Challenge 124 Santa's Missing Gift List

My solution -> *[124SantasMissingGiftList](124SantasMissingGiftList.js)*

## **_Task condition:_**

Santa has misplaced his list of gift to all the children, he has however a condensed version lying around.

In this condensed verison, instead of a list of gifts for each child, each one has an integer.

He also have a list of gifts corresponding to each integer. His list is as follows:

```
GIFTS = {
    1 => 'Toy Soldier',
    2 => 'Wooden Train',
    4 => 'Hoop',
    8 => 'Chess Board',
   16 => 'Horse',
   32 => 'Teddy',
   64 => 'Lego',
  128 => 'Football',
  256 => 'Doll',
  512 => "Rubik's Cube"
}
```

This list is made available to you, as ```GIFTS```.

The integer for each child is such that the child should get the highest toy lower than or equal to that integer, and then, if there's more left, also get the highest toy lower than the rest and so on. Know that Santa never gives the same gift twice.

For example, by Timmy's name is ```160```. This means that Timmy should get both a football and a teddy, because ```128 + 32 = 160```.

You should help Santa by decoding his own list and recreate the missing list for him. Santa's elf wants the list sorted alphabetically by the toys, so you should help them as well and list the toys in a sorted order.

### **_Examples_**

```
Input: 1    => Output: ['Toy Soldier']

Input: 2    => Output: ['Wooden Train']

Input: 3    => Output: ['Toy Soldier', 'Wooden Train']

Input: 22   => Output: ['Hoop', 'Horse', 'Wooden Train']

Input: 160  => Output: ['Football', 'Teddy']
```

#

<br />

# Challenge 125 Santa's Naughty List

My solution -> *[125SantasNaughtyList](125SantasNaughtyList.js)*

## **_Task condition:_**

Christmas is coming, and Santa has a long list to go through, to find who deserves presents for the big day. Go through a list of children, and return a list containing every child who appeared on Santa's list. Do not add any child more than once. Output should be sorted.

Comparison should be case sensitive and the returned list should contain only one copy of each name: ```"Sam"``` and ```"sam"``` are different, but ```"sAm"``` and ```"sAm"``` are not.

### **_Examples_**

```
Input:  ['Jason', 'Jackson', 'Jordan', 'Johnny'], ['Jason', 'Jordan', 'Jennifer']
Output: ['Jason', 'Jordan']

Input:  ['jASon', 'JAsoN', 'JaSON', 'jasON'], ['JasoN', 'jASOn', 'JAsoN', 'jASon', 'JASON']
Output: ['JAsoN', 'jASon']

Input:  ['Jason', 'James', 'Johnson'], ['Jason', 'James', 'JJ']
Output: ['James', 'Jason']
```

#

<br />

# Challenge 126 Christmas Mission: Distribute Gifts #7

My solution -> *[126ChristmasMissionDistributeGiftsN7](126ChristmasMissionDistributeGiftsN7.js)*

## **_Task condition:_**

Christmas is coming soon. Santa Claus is ready for the gift, he will give the gifts to the children.

Santa Claus is naughty, and he always distributes gifts according to the size of the children's sock.

First he chose the smallest sock and put in the largest gift. Then he chose the largest sock and put in the smallest gift. And so on.. Until no gifts, or every child got a gift.

Can you calculate the final distribution?

#### **Inputs**

- ```gifts```: An integer array that represents the volume of each gift.

- ```socks```: An integer array that represents the volume of each child's sock. It is guaranteed that there is no duplicate number.

#### **Output**

- An integer array that represents each child's gift. According to the order of ```socks```.

### **_Examples_**

```
Input: gifts = [1,2,3]    socks = [1,2,3] => Output: [3,2,1]

Input: gifts = [1,2]      socks = [1,2,3] => Output: [2,0,1]

Input: gifts = [1,2,3,4]  socks = [1,2,3] => Output: [4,3,1]
```

#

<br />

# Challenge 127 Shopping Calculation

My solution -> *[127ShoppingCalculation](127ShoppingCalculation.js)*

## **_Task condition:_**

The task is about shopping calculation. There are products, product's prices, customers and customer's total money.

Create function that takes as parameter List of strings, and this list contains statements which give information about product name, product price, customer name and customer budget.

```
These statements can have 3 basic form like; (is, has, buys)
  'Apple is $5.'
  'Alice has $26.'
  'Alice buys 2 apples.'
```

The function must calculate the result which is ```[(string,string,string)]``` and holds ```[(Customer Name, Customer Total Money, Bought Products)]```.

```
  "is" statement gives info about product name and its price.
  "has" statement gives info about customer name and his/her money.
  "buys" statement gives info about customer name, bought product name and bought product count.
```

You need to split bought products by comma and space(", ") like ```'2 apples, 5 oranges, 1 grape'```

The order of statements is not guaranteed. As an example: you could receive a buy statement before knowing the cost of the product.

### **_Examples_**

```
Input:
[
	'Apple is $5.',
	'Banana is $7.',
	'Orange is $2.',
	'Alice has $26.',
	'John has $41.',
	'Alice buys 2 apples.',
	'John buys 1 banana.',
	'Alice buys 5 oranges.'
]

Output: 
[
  [ 'Alice', '$6', '2 apples, 5 oranges' ],
  [ 'John', '$34', '1 banana' ]
]

Input:
[
  'John has $41.',
  'Apple is $5.',
  'Alice buys 2 apples.',
  'Alice has $26.',
  'John buys 1 banana.',
  'Alice buys 5 oranges.',
  'Banana is $7.',
  'Orange is $2.'
]

Output:
[
  [ 'John', '$34', '1 banana' ],
  [ 'Alice', '$6', '2 apples, 5 oranges' ]
]

```

**_NOTES:_**

- Currency is always preceded by the ```$``` symbol.
- Output must be ordered by the placement of customers in the input list.
- Products must be ordered by the order in which they were bought by that customer.
- All input statements will be valid. No need to check for invalid statements.
- Customers will always have enough money for their purchases. No need to validate for negative balances.
- Inputs guarantee that the same customer will not perform multiple purchases for the same product.
- Just use ```-s``` as plural suffix.

#

<br />

# Challenge 128 List Filtering

My solution -> *[128ListFiltering](128ListFiltering.js)*

## **_Task condition:_**

You have to create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

### **_Examples_**

```
Input: [1, 2, 'a', 'b'] => Output: [1, 2]

Input: [1, 'a', 'b', 0, 15] => Output: [1, 0, 15]

Input: [1, 2, 'aasf', '1', '123', 123] => Output: [1, 2, 123]
```

#

<br />

# Challenge 129 Equal Sides Of An Array

My solution -> *[129EqualSidesOfAnArray](129EqualSidesOfAnArray.js)*

## **_Task condition:_**

You are going to be given an array of integers. Your job is to take that array and find an index ```N``` where the sum of the integers to the left of ```N``` is equal to the sum of the integers to the right of ```N```.

If there is no index that would make this happen, return ```-1```.

### **_Examples_**

```
Input: [1, 2, 3, 4, 3, 2, 1] => Output: 3

Еxplanation: at the 3rd position of the array, the sum of left side of the index ([1, 2, 3]) and the sum of the right side of the index ([3, 2, 1]) both equal 6.

Input: [1, 100, 50, -51, 1, 1] => Output: 1

Еxplanation: at the 1st position of the array, the sum of left side of the index ([1]) and the sum of the right side of the index ([50, -51, 1, 1]) both equal 1.

Input: [20, 10, -80, 10, 10, 15, 35] => Output: 0

Еxplanation: at index 0 the left side is ([]), the right side is ([10, -80, 10, 10, 15, 35]), they both are equal to 0 when added.

(Empty arrays are equal to 0 in this problem)
```

**_NOTES:_**

- Input: An integer array of length ```0 < arr < 1000```. The numbers in the array can be any integer positive or negative.
- Output: The lowest index N where the side to the left of ```N``` is equal to the side to the right of ```N```. If you do not find an index that fits these rules, then you will return ```-1```.
- If you are given an array with multiple answers, return the lowest correct index. 
- The index of an array starts at ```0```.

#

<br />

# Challenge 130 Christmas Mission: Programmer's Christmas #3

My solution -> *[130ChristmasMissionProgrammersChristmasN3](130ChristmasMissionProgrammersChristmasN3.js)*

## **_Task condition:_**

Christmas is coming soon. As a programmer, you need to complete a series of tasks to welcome the arrival of Christmas. This time your task is:

Given a string ```s```. You need to count how many pairs of two words "Merry" and "Christmas" appear in ```s```, return the maximum possible numbers of pair(not the numbers of single word).

### **_Examples_**

```
Input: 'MerryChristmas' => Output: 1

Input: 'ChristmasMerry' => Output: 1

Input: 'yrreMsamtsirhC' => Output: 1

Input: 'MerryMerry' => Output: 0

Input: 'ChristmasChristmas' => Output: 0

Input: 'MMeerrrryyCChhrriissttmmaass' => Output: 2

Input: 'MMmmeerrrrrryyCChhiissssttaa' => Output: 2

Input: 'MMmmeerrrryyCChhiissssssttaa' => Output: 1
```

**_NOTES:_**

- Letters should be case sensitive. "M" and "m" are different.
- You don't need to consider the order, the characters are disorganized.

#

<br />

# Challenge 131 Christmas Present Calculator

My solution -> *[131ChristmasPresentCalculator](131ChristmasPresentCalculator.js)*

## **_Task condition:_**

Santa's little helper aren't sick anymore. They are ready to give away presents again. But some of them are still weak. This leads to more productive elves than others.

How many presents can Santa distribute this christmas?

You will get two inputs. One dictionary with the producitivity of each elf like the following:

```
{'Santa': 1, 'elf_1': 1, 'elf_2': 1, 'elf_3': 2, 'elf_4': 3}
```

and a string array with the time needed for each present like the following:

```'hh:mm:ss'```

The productivity describes the workload an elf can do each day:

```
//productivity 1 = 24 hours each day
//productivity 2 = 48 hours each day
...
```

**Return the number of present they can distribute at maximum.**

### **_Examples_**

```
countPresents(prod, presents);

Input:  prod = { 'Santa': 1, 'elf_1': 1, 'elf_2': 2 };
        presents = ['01:00:00', '06:00:00', '12:00:00', '18:00:00', '24:00:00', '36:00:00'];

Output: 5
```

**_NOTES:_**

- They have only 24 hours.
- They try to give out as much as presents as possible (the ones with less time first).
- All the elves can work on multiple tasks. You can count it as one work capacity.

#

<br />

# Challenge 132 Chocolate Celebration

My solution -> *[132ChocolateCelebration](132ChocolateCelebration.js)*

## **_Task condition:_**

Tell me, is there enough chocolate?

You will be given two variables: people, and bars.

There are ```16``` pieces in each chocolate bar.

The people are divided into the following groups:

- ```group A```: 20% of the people in the group will not want any chocolate
- ```group B```: 10% of the people may want to have a piece, but only after everyone who wanted at least one piece had it.
- ```group C```: 5% of the group will take one piece to start with, but happily take up to 20 pieces of chocolate in total if there are any left over after everyone else has had one piece
- ```group D```: everyone else will only want a single piece of chocolate

If the group size is defined with a %, round group sizes to the nearest integer (default solution relies on use of ```Math.round```). If there aren't enough chocolate pieces for everyone, chocolate gets distributed on the first come, first served basis.

#### OUTPUT

- Return an array with [0] number of people who had at least one piece, ```[1]``` number of pieces left after everyone has had all they want.
- If there wasn't enough chocolate to satisfy basic requirements (ie groups ```C``` and ```D```), add to the array ```[2]``` "You should buy more chocolate next time", and ```[3]``` suggested total number of bars to satisfy basic requirements of this group. Round to the nearest integer. Add one bar for a good measure.
- If there were more than ```16``` pieces left at the end, add to the array ```[2]``` "That was too much chocolate!", and ```[3]``` suggested total number of bars to satisfy groups ```B```, ```C```, and ```D```. Round to the nearest integer. Add one bar for a good measure.
- If either people or bars are not a numbers, return "Error. We need numbers.".
- If there is noone in the group, return "Nobody here. Skedaddle.".

### **_Examples_**

```
Input: 100, 10 => Output: [80, 0]

Input: 1000, 10 => Output: [160, 0, 'You should buy more chocolate next time', 45]

Input: 8, 10 => Output: [6, 154, 'That was too much chocolate!', 1]

Input: 0, 10 => Output: 'Nobody here. Skedaddle.'

Input: 'blue', 10 => Output: 'Error. We need numbers.'

Input: 8, [8, 7] => Output: 'Error. We need numbers.'
```

#

<br />

# Challenge 133 Roasting Chicken

My solution -> *[133RoastingChicken](133RoastingChicken.js)*

## **_Task condition:_**

Oliver likes to roast a chicken on a Sunday Afternoon.

He knows that in order to get it just how he wants it, he should roast it for ```20 minutes``` for every ```450g``` of uncooked weight plus an additional ```20 minutes```.

You are given a weight of a uncooked chicken in ```kg```, return for how long it needs to be roasted - in hours and minutes, rounding up to the nearest five minutes.

If the chicken is to be roasted for more than ```2``` hours then write ```hrs```, otherwise write ```hr```.

If the chicken is to be roasted for less than an hour, only give the number of minutes.

If the uncooked weight is ```0```, return "There is no chicken!".

An example time is ```2 hrs 45 mins```.

### **_Examples_**

```
Input: 1 => Output: 1 hr 5 mins

Input: 2.2 => Output: 2 hrs

Input: 0.3 => Output: 35 mins
```

#

<br />

# Challenge 134 Printer Errors

My solution -> *[134PrinterErrors](134PrinterErrors.js)*

## **_Task condition:_**

In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from ```a to m```.

The colors used by the printer are recorded in a control string. For example a "good" control string would be ```aaabbbbhaijjjm``` meaning that the printer used three times color ```a```, four times color ```b```, one time color ```h``` then one time color ```a```...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. ```aaaxbbbbyyhwawiwjjjwwm``` with letters not from ```a to m```.

You have to write a function ```printerError(s)``` which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ```a to z```.

### **_Examples_**

```
Input: 'aaabbbbhaijjjm' => Output: 0/14

Input: 'aaaxbbbbyyhwawiwjjjwwm' => Output: 8/22

Input: 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz' => Output: 3/56
```

#

<br />

# Challenge 135 Count The Smiley Faces!

My solution -> *[135CountTheSmileyFaces](135CountTheSmileyFaces.js)*

## **_Task condition:_**

Given an array ```(arr)``` as an argument complete the function ```countSmileys()``` that should return the total number of smiling faces.

Rules for a smiling face:

- Each smiley face must contain a valid pair of eyes. Eyes can be marked as ```:``` or ```;```
- A smiley face can have a nose but it does not have to. Valid characters for a nose are ```-``` or ```~```
- Every smiling face must have a smiling mouth that should be marked with either ```)``` or ```D```

No additional characters are allowed except for those mentioned.

**Valid smiley face examples:** ```:) :D ;-D :~)```  
**Invalid smiley faces:** ```;( :> :} :]```

### **_Examples_**

```
Input: [':)', ';(', ';}', ':-D'] => Output: 2

Input: [';D', ':-(', ':-)', ';~)'] => Output: 3

Input: [';]', ':[', ';*', ':$', ';-D'] => Output: 1
```

**_NOTES:_**

- In case of an empty array return ```0```. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

#

<br />

# Challenge 136 ROT13

My solution -> *[136ROT13](136ROT13.js)*

## **_Task condition:_**

```ROT13``` is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the Latin alphabet.

Applying ROT13 to a piece of text requires examining its alphabetic characters and replacing each one by the letter 13 places further along in the alphabet, wrapping back to the beginning if necessary.

To encode message: ```A``` becomes ```N```, ```B``` becomes ```O```, and so on up to ```M```, which becomes ```Z```, then the sequence continues at the beginning of the alphabet: ```N``` becomes ```A```, ```O``` becomes ```B```, and so on to ```Z```, which becomes ```M```. To decode a message, You apply the same substitution rules, but this time on the ROT13 encrypted text. (Any other character, for example numbers, symbols, punctuation or whitespace, are left unchanged.) 

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

### **_Examples_**

```
Input: 'EBG13 rknzcyr.' => Output: 'ROT13 example.'

Input: 'This is my first ROT13 excercise!' => Output: 'Guvf vf zl svefg EBG13 rkprepvfr!'
```

#

<br />

# Challenge 137 Unique In Order

My solution -> *[137UniqueInOrder](137UniqueInOrder.js)*

## **_Task condition:_**

Implement the function ```uniqueInOrder(iterable)``` which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

### **_Examples_**

```
Input: 'AAAABBBCCDAABBB' => Output: ['A', 'B', 'C', 'D', 'A', 'B']

Input: 'ABBCcAD' => Output: ['A', 'B', 'C', 'c', 'A', 'D']

Input: [1,2,2,3,3] => Output: [1,2,3]
```

#

<br />

# Challenge 138 Find The Odd Int

My solution -> *[138FindTheOddInt](138FindTheOddInt.js)*

## **_Task condition:_**

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

### **_Examples_**

```
Input: [7] => Output: 7 - because it occurs 1 time (which is odd)

Input: [0] => Output: 0 - because it occurs 1 time (which is odd)

Input: [1,1,2] => Output: 2 - because it occurs 1 time (which is odd)

Input: [0,1,0,1,0] => Output: 0 - because it occurs 3 times (which is odd)

Input: [1,2,2,3,3,3,4,3,3,3,2,2,1] => Output: 4 - because it appears 1 time (which is odd)
```

#

<br />

# Challenge 139 Are They The "Same"?

My solution -> *[139AreTheyTheSame](139AreTheyTheSame.js)*

## **_Task condition:_**

Given two arrays ```a``` and ```b``` write a function ```comp(a, b)``` (or ```compSame(a, b)```) that checks whether the two arrays have the "same" elements, with the same _multiplicities_ (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in ```b``` are the elements in ```a``` squared, regardless of the order.

### **_Examples_**

**Valid arrays**

```
a = [121, 144, 19, 161, 19, 144, 19, 11],
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
```

```comp(a, b)``` returns ```true``` because in ```b``` 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write ```b's``` elements in terms of squares:

```
a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
```

**Invalid arrays**

If, for example, we change the first number of ```b``` to something else, ```comp``` is not returning ```true``` anymore:

```
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
```

```comp(a,b)``` returns ```false``` because in b 132 is not the square of any number of a.

```
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
```

```comp(a,b)``` returns false because in ```b``` 36100 is not the square of any number of ```a```.


**_NOTES:_**

- ```a``` or ```b``` might be ```[]``` or ```{}```.
- ```a``` or ```b``` might be ```null``` or empty.
- If ```a``` or ```b``` are ```null``` or ```empty```, the problem doesn't make sense so return false.

#

<br />

# Challenge 140 The Supermarket Queue

My solution -> *[140TheSupermarketQueue](140TheSupermarketQueue.js)*

## **_Task condition:_**

There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

**input**

- ```customers```: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
- ```n```: a positive integer, the number of checkout tills.

**output**

The function should return an integer, the total time required.

### **_Examples_**

```
queueTime([5, 3, 4], 1)
// should return 12
// because when there is 1 till, the total time is just the sum of the times

queueTime([10, 2, 3, 3], 2)
// should return 10
// because here n=2 and the 2nd, 3rd, and 4th people in the 
// queue finish before the 1st person has finished.

queueTime([2, 3, 10], 2)
// should return 12
```

```
Input: ([], 1) => Output: 0

Input: ([1, 2, 3, 4], 1) => Output: 10

Input: ([2, 2, 3, 3, 4, 4], 2) => Output: 9

Input: ([1, 2, 3, 4, 5], 100) => Output: 5

Input: ([2, 3, 10, 2], 2) => Output: 12
```

**_NOTES:_**

- There is only ONE queue serving many tills, and
- The order of the queue NEVER changes, and
- The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
- You should assume that all the test input will be valid, as specified above.

#

<br />

# Challenge 141 Find The Unique Number

My solution -> *[141FindTheUniqueNumber](141FindTheUniqueNumber.js)*

## **_Task condition:_**

There is an array with some numbers. All numbers are equal except for one. Try to find it!

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

### **_Examples_**

```
Input: [1, 1, 1, 2, 1, 1] => Output: 2

Input: [0, 0, 0.55, 0, 0] => Output: 0.55
```

#

<br />

# Challenge 142 Bouncing Balls

My solution -> *[142BouncingBalls](142BouncingBalls.js)*

## **_Task condition:_**

A child is playing with a ball on the n-th floor of a tall building. The height of this floor above ground level, ```h```, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of ```0.66```).

His mother looks out of a window ```1.5``` meters from the ground.

**How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing)?**

Three conditions must be met for a valid experiment:

1. Float parameter "h" in meters must be greater than 0.
2. Float parameter "bounce" must be greater than 0 and less than 1.
3. Float parameter "window" must be less than h.

If all three conditions above are fulfilled, return a positive integer, otherwise return ```-1```.

### **_Examples_**

```
Input: h = 3, bounce = 0.66, window = 1.5 => Output: 3

Input: h = 3, bounce = 1, window = 1.5 => Output: -1 // (Condition 2) not fulfilled
```

**_NOTES:_**

- The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

#

<br />

# Challenge 143 Consecutive strings

My solution -> *[143ConsecutiveStrings](143ConsecutiveStrings.js)*

## **_Task condition:_**

You are given an array(list) ```strarr``` of strings and an integer ```k```. Your task is to return the first longest string consisting of ```k consecutive``` strings taken in the array.

### **_Examples_**

```
strarr = ['tree', 'foling', 'trashy', 'blue', 'abcdef', 'uvwxyz'], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling    (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy  ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue    ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef    ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz  ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(['zone', 'abigail', 'theta', 'form', 'libe', 'zas', 'theta', 'abigail'], 2) --> "abigailtheta"
```

**_NOTES:_**

- ```n``` being the length of the string array, if ```n = 0``` or ```k > n``` or ```k <= 0``` return "".
- Consecutive strings : follow one after another without an interruption

#

<br />

# Challenge 144 Sudoku Board Validator

My solution -> *[144SudokuBoardValidator](144SudokuBoardValidator.js)*

## **_Task condition:_**

Sudoku is a game played on a ```9x9``` grid. The goal of the game is to fill all cells of the grid with digits from ```1``` to ```9```, so that each column, each row, and each of the nine ```3x3``` sub-grids (also known as blocks) contain all of the digits from ```1``` to ```9```.

Write a function that accepts a Sudoku board, and returns ```true``` if it is a valid Sudoku solution, or ```false``` otherwise. The cells of the input Sudoku board may also contain ```0's```, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

### **_Examples_**

```
Valid board:

    5 3 4|6 7 8|9 1 2
    6 7 2|1 9 5|3 4 8
    1 9 8|3 4 2|5 6 7
    -----+-----+-----
    8 5 9|7 6 1|4 2 3
    4 2 6|8 5 3|7 9 1
    7 1 3|9 2 4|8 5 6
    -----+-----+-----
    9 6 1|5 3 7|2 8 4
    2 8 7|4 1 9|6 3 5
    3 4 5|2 8 6|1 7 9
```
```
Invalid board:
                
              This column has two 3's
                        v
This cell has a 0 > 0 3 4|6 7 8|9 1 2
                    6 7 2|1 9 5|3 4 8
                    1 9 8|3 4 2|5 6 7
                    -----+-----+-----
                    8 5 9|7 6 1|4 2 3
                    4 2 6|8 5 3|7 9 1
                    7 1 3|9 2 4|8 5 6
                    -----+-----+-----
    This box has   /9 6 1|5 3 7|2 8 4
         two 3's >| 2 8 3|4 1 9|6 3 5 < This row has two 3's
                   \3 4 5|2 8 6|1 7 9
```

**_NOTES:_**

- All inputs are guaranteed to be ```2D``` boards of size ```9x9``` with possible values in range ```0-9```.
- Rows, columns and blocks (```3x3``` small squares) must contain each number from range ```1-9``` exactly once.
- User solution must not modify input boards.

#

<br />

# Challenge 145 Find The Missing Letter

My solution -> *[145FindTheMissingLetter](145FindTheMissingLetter.js)*

## **_Task condition:_**

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2. The array will always contain letters in only one case.

### **_Examples_**

```
Input: ['a', 'b', 'c', 'd', 'f'] => Output: 'e'

Input: ['O', 'Q', 'R', 'S'] => Output: 'P'
```

**_NOTES:_**

- Use the English alphabet with 26 letters!

#

<br />

# Challenge 146 Bit Counting

My solution -> *[146BitCounting](146BitCounting.js)*

## **_Task condition:_**

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

### **_Examples_**

```
Input: 1234 => Output: 5 // The binary representation of 1234 is 10011010010, so the function should return 5 in this case

Input: 0 => Output: 0

Input: 4 => Output: 1

Input: 7 => Output: 3

Input: 9 => Output: 2

Input: 10 => Output: 2
```

#

<br />

# Challenge 147 Valid Braces

My solution -> *[147ValidBraces](147ValidBraces.js)*

## **_Task condition:_**

Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return ```true``` if the string is valid, and ```false``` if it's invalid.

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ```()[]{}```.

**What is considered Valid?**

A string of braces is considered valid if all braces are matched with the correct brace.

### **_Examples_**

```
Input: '(){}[]'   => Output: true

Input: '([{}])'   => Output: true

Input: '(}'       => Output: false

Input: '[(])'     => Output: false

Input: '[({})](]' => Output: false
```

#

<br />

# Challenge 148 Roman Numerals Encoder

My solution -> *[148RomanNumeralsEncoder](148RomanNumeralsEncoder.js)*

## **_Task condition:_**

Create a function taking a positive integer between `1` and `3999` (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.

**In Roman numerals:**

- `1990` is rendered: `1000 = M + 900 = CM + 90 = XC` resulting in `MCMXC`.
- `2008` is written as `2000 = MM, 8 = VIII` or `MMVIII`.
- `1666` uses each Roman symbol in descending order: `MDCLXVI`.

```
    Symbol    Value
    ------    -----
      I         1
      V         5
      X         10
      L         50
      C         100
      D         500
      M         1000
```

### **_Examples_**

```
Input:     1 => Output:  'I'

Input:  1000 => Output:  'M'

Input:  1666 => Output:  'MDCLXVI'
```

#

<br />

# Challenge 149 Range Extraction

My solution -> *[149RangeExtraction](149RangeExtraction.js)*

## **_Task condition:_**

A format for expressing an ordered list of integers is to use a comma separated list of either

- individual integers
- or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, `'-'`. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least `3` numbers. For example `"12,13,15-17"`

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format. 

### **_Examples_**

```
Input: [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
Output: '-10--8,-6,-3-1,3-5,7-11,14,15,17-20'

Input: [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
Output: '-6,-3-1,3-5,7-11,14,15,17-20'
```

#

<br />

# Challenge 150 Array Plus Array

My solution -> *[150ArrayPlusArray](150ArrayPlusArray.js)*

## **_Task condition:_**

Write a function that calculates sum of two arrays. Actually the sum of all their elements.

Each array includes only integer numbers. Output is a number too.

### **_Examples_**

```
Input: [1, 2, 3], [4, 5, 6] => Output: 21

Input: [-1, -2, -3], [-4, -5, -6] => Output: -21

Input: [0, 0, 0], [4, 5, 6] => Output: 15

Input: [100, 200, 300], [400, 500, 600] => Output: 2100
```

#

<br />

# Challenge 151 Find The Parity Outlier

My solution -> *[151FindTheParityOutlier](151FindTheParityOutlier.js)*

## **_Task condition:_**

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

### **_Examples_**

```
Input: [2, 4, 0, 100, 4, 11, 2602, 36] => Output: 11 (the only odd number)

Input: [160, 3, 1719, 19, 11, 13, -21] => Output: 160 (the only even number)
```

#

<br />

# Challenge 152 Is Integer Array?

My solution -> *[152IsIntegerArray](152IsIntegerArray.js)*

## **_Task condition:_**

Write a function that:

- returns `true  / True` if every element in an array is an integer or a float with no decimals.
- returns `true  / True` if array is empty.
- returns `false / False` for every other input.

### **_Examples_**

```
Input: [] => Output: true

Input: [1, 2, 3, 4] => true

Input: [-11, -12, -13, -14] => Output: true

Input: [1.0, 2.0, 3.0] => Output: true

Input: [1.0, 2.0, 3.0001] => Output: false

Input: [1, 2, NaN] => Output: false

Input: '' => Output: false
```

#

<br />

# Challenge 153 Help The bookseller!

My solution -> *[153HelpTheBookseller](153HelpTheBookseller.js)*

## **_Task condition:_**

A bookseller has lots of books classified in `26 categories` labeled `A, B, C, ..., Z`. Each book has a code of `at least 3 characters`. The `1st` character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code is followed by a space and by a positive integer, which indicates the quantity of books of this code in stock.

You will receive the bookseller's stocklist and a list of categories. Your task is to find the total number of books in the bookseller's stocklist, with the category codes in the list of categories.

Return the result as a string described in the example below.

If any of the input lists is empty, return an empty string.

### **_Examples_**

```
# the bookseller's stocklist:
'ABART 20', 'CDXEF 50', 'BKWRK 25', 'BTSQZ 89', 'DRTYM 60'

# list of categories: 
'A', 'B', 'C', 'W'

# result:
'(A : 20) - (B : 114) - (C : 50) - (W : 0)'

#Explanation:
category A: 20 books (ABART)
category B: 114 books = 25 (BKWRK) + 89 (BTSQZ)
category C: 50 books (CDXEF)
category W: 0 books
```

**_NOTES:_**

- The codes are in the same order in both lists.

#

<br />

# Challenge 154 Decode The Morse Code

My solution -> *[154DecodeTheMorseCode](154DecodeTheMorseCode.js)*

## **_Task condition:_**

You have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.

The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter `A` is coded as `·−`, letter `Q` is coded as `−−·−`, and digit `1` is coded as `·−−−−`. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a `single space` is used to separate the character codes and `3 spaces` are used to separate words. For example, the message `HEY JUDE` in Morse code is `···· · −·−−   ·−−− ··− −·· ·`.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal `SOS` (that was first issued by Titanic), that is coded as `···−−−···`. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

### **_Examples_**

```
Input: '.... . -.--   .--- ..- -.. .' => Output: 'HEY JUDE'

Input: '   .... . -.--   ' => 'HEY'
```

**_NOTES:_**

- Extra spaces before or after the code have no meaning and should be ignored.
- For coding purposes you have to use `ASCII` characters `.` and `-`, not `Unicode` characters.
- The Morse code table is preloaded for you as a dictionary, feel free to use it - `MORSE_CODE['.--']`.

#

<br />

# Challenge 155 Message Validator

My solution -> *[155MessageValidator](155MessageValidator.js)*

## **_Task condition:_**

You have an input string and you should check whether it is a valid message. To decide that, you need to split the string by the numbers, and then compare the numbers with the number of characters in the following substring.

### **_Examples_**

For example `"3hey5hello2hi"` should be split into `3`, `hey`, `5`, `hello`, `2`, `hi` and the function should return `true`, because `"hey"` is `3` characters, `"hello"` is `5`, and `"hi"` is `2`, as the numbers and the character counts match, the result is `true`.

```
Input: '4code13hellocodewars' => Output: true

Input: '3hey5hello2hi5'       => Output: false

Input: 'code4hello5'          => Output: false

Input: '1a2bb3ccc4dddd5eeeee' => Output: true

Input: ''                     => Output: true
```

#

**_NOTES:_**

- Messages are composed of only letters and digits.
- Numbers may have multiple digits: e.g. `"4code13hellocodewars"` is a valid message.
- Every number must match the number of character in the following substring, otherwise the message is invalid: e.g. `"hello5"` and `"2hi2"` are invalid.
- If the message is an empty string, you should return `true`.

<br />

# Challenge 156 Reversing A Process

My solution -> *[156ReversingAProcess](156ReversingAProcess.js)*

## **_Task condition:_**

Suppose we know the process by which a string `s` was encoded to a string `r`. Our goal is to decode this string `r` to get back the original string `s`.

### **_Explanation of the encoding process:_**

- **input:** a string `s` composed of lowercase letters from `"a" to "z"`, and a positive integer `num`
- we know there is a correspondence between `abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...`
- if `c` is a character of `s` whose corresponding number is `x`, apply to `x` the function `f: x-> f(x) = num * x % 26`, then find `ch` the corresponding character of `f(x)`
- Accumulate all these `ch` in a string `r`
- concatenate `num` and `r` and return the result

**For example:**

```
encode("mer", 6015)  -->  "6015ekx"

m --> 12,   12 * 6015 % 26 = 4,     4 --> e
e --> 4,     4 * 6015 % 26 = 10,   10 --> k
r --> 17,   17 * 6015 % 26 = 23,   23 --> x

So we get "ekx", hence the output is "6015ekx"
```

**Task**

A string `s` was encoded to string `r` by the above process. complete the function to get back `s` whenever it is possible.

Indeed it can happen that the decoding is impossible for strings composed of whatever letters from "a" to "z" when positive integer num has not been correctly chosen. In that case return `"Impossible to decode"`.

### **_Examples_**

```
Input: decode('6015ekx') => Output: 'mer'

Input: decode('5057aan') => Output: 'Impossible to decode'
```

#

<br />

# Challenge 157 Making Change

My solution -> *[157MakingChange](157MakingChange.js)*

## **_Task condition:_**

Complete the method that will determine the minimum number of coins needed to make change for a given amount in American currency.

Coins used will be half-dollars, quarters, dimes, nickels, and pennies, worth `50¢`, `25¢`, `10¢`, `5¢` and `1¢`, respectively. They'll be represented by the symbols `H`, `Q`, `D`, `N` and `P`.

The argument passed in will be an integer representing the value in cents. The return value should be a hash/dictionary/object with the symbols as keys, and the numbers of coins as values. Coins that are not used should not be included in the hash. If the argument passed in is 0, then the method should return an empty hash.

### **_Examples_**

```
Input: makeChange(0) => Output: {}

Input: makeChange(1) => Output: {'P':1}

Input: makeChange(43) => Output: {'Q': 1, 'D': 1, 'N': 1, 'P': 3}

Input: makeChange(91) => Output: {'H': 1, 'Q': 1, 'D': 1, 'N': 1, 'P': 1}
```

#

<br />

# Challenge 158 Take A Ten Minutes Walk

My solution -> *[158TakeATenMinutesWalk](158TakeATenMinutesWalk.js)*

## **_Task condition:_**

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. `['n', 's', 'w', 'e']`). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

### **_Examples_**

```
Input: ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] => Output: true

Input: ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'] => Output: false

Input: ['w'] => Output: false

Input: ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'] => Output: false
```

**_NOTES:_**

- You will always receive a valid array containing a random assortment of direction letters `('n', 's', 'e', or 'w' only)`. It will never give you an empty array (that's not a walk, that's standing still!).

#

<br />

# Challenge 159 Does My Number Look Big In This?

My solution -> *[159DoesMyNumberLookBigInThis](159DoesMyNumberLookBigInThis.js)*

## **_Task condition:_**

A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this task, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

```
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```

and 1652 (4 digits), which isn't:

```
1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
```

**The Challenge:**

Your code must return `true` or `false` (not `'true'` and `'false'`) depending upon whether the given number is a `Narcissistic number in base 10`.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function. 

### **_Examples_**

```
Input: 7 => Output: true

Input: 153 => Output: true

Input: 122 => Output: false

Input: 487 => Output: false
```

#

<br />

# Challenge 160 Sum The Nums, Sum The Sums And Sum The Nums Up To That Sum

My solution -> *[160SumTheNumsSumTheSumsAndSumTheNumsUpToThatSum](160SumTheNumsSumTheSumsAndSumTheNumsUpToThatSum.js)*

## **_Task condition:_**

Let's define two functions:

```
S(N) — sum of all positive numbers not more than N
S(N) = 1 + 2 + 3 + ... + N

Z(N) — sum of all S(i), where 1 <= i <= N
Z(N) = S(1) + S(2) + S(3) + ... + S(N)
```

You will be given an integer `N` as input; your task is to return the value of `S(Z(N))`.

For example, let `N = 3`:

```
Z(3n) = 1n + 3n + 6n = 10n
S(Z(3n)) = S(10n) = 55n
```

The input range is `1 <= N <= 10^9` and there are `80 (40 in LC)` test cases, of which most are random.

### **_Examples_**

```
Input: 3 => Output: 55n

Input: 5 => Output: 630n

Input: 100 => Output: 14740530850n
```

#

<br />

# Challenge 161 Land Perimeter

My solution -> *[161LandPerimeter](161LandPerimeter.js)*

## **_Task condition:_**

Given an array `arr` of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with `'X'` while the water fields are represented as `'O'`. Consider each tile being a perfect `1 x 1` piece of land.

### **_Examples_**

```
['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']

should return: "Total land perimeter: 24"
```

```
['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']

should return: "Total land perimeter: 18"
```

#

<br />

# Challenge 162 Is A Number Prime?

My solution -> *[162IsANumberPrime](162IsANumberPrime.js)*

## **_Task condition:_**

Define a function that takes an integer argument and returns a logical value `true` or `false` depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than `1` that has no positive divisors other than `1` and itself.

**Requirements**

- You can assume you will be given an integer input.
- You can not assume that the integer will be only positive. You may be given negative numbers as well (or `0`).
- NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to `2^31` ( or similar, depending on language ). Looping all the way up to `n`, or `n/2`, will be too slow.

### **_Examples_**

```
Input: is_prime(1)  => Output: false

Input: is_prime(2)  => Output: true

Input: is_prime(-1) => Output: false
```

#

<br />

# Challenge 163 Name To Matrix

My solution -> *[163NameToMatrix](163NameToMatrix.js)*

## **_Task condition:_**

Given a name, turn that name into a perfect square matrix (nested array with the amount of arrays equivalent to the length of each array).

You will need to add periods `(.)` to the end of the name if necessary, to turn it into a matrix.

If the name has a length of 0, return `'name must be at least one letter'`.

### **_Examples_**

```
'Bill' =>
  [
    ['B', 'i'],
    ['l', 'l']
  ]

'Frank' =>
  [ 
    ['F', 'r', 'a'],
    ['n', 'k', '.'],
    ['.', '.', '.']
  ]
```

#

<br />

# Challenge 164 What The Biggest Search Keys?

My solution -> *[164WhatTheBiggestSearchKeys](164WhatTheBiggestSearchKeys.js)*

## **_Task condition:_**

You're a programmer in a SEO company. The SEO specialist of your company gets the list of all project keywords everyday, then he looks for the longest keys to analyze them.

You will get the list with keywords and must write a simple function that returns the biggest search keywords and sorts them in lexicographical order.

### **_Examples_**

```
Input: theBiggestSearchKeys('key1', 'key2', 'key3', 'key n', 'bigkey2', 'bigkey1')
Output: 'bigkey1', 'bigkey2'

Input: theBiggestSearchKeys('key1', 'key22', 'key333')
Output: 'key333'

Input: theBiggestSearchKeys('coding', 'sorting', 'tryruby')
Output: 'sorting', 'tryruby'

Input: theBiggestSearchKeys('small keyword', 'how to coding?', 'very nice kata', 'a lot of keys', 'I like Ruby!!!')
Output: 'I like Ruby!!!', 'how to coding?', 'very nice kata'

Input: theBiggestSearchKeys('pippi')
Output: 'pippi'

Input: theBiggestSearchKeys()
Output: ''
```

#

<br />

# Challenge 165 A String Of Sorts

My solution -> *[165AStringOfSorts](165AStringOfSorts.js)*

## **_Task condition:_**

Define a method that accepts 2 strings as parameters. The method returns the first string sorted by the second.

To elaborate, the second string defines the ordering. It is possible that in the second string characters repeat, so you should remove repeating characters, leaving only the first occurrence.

Any character in the first string that does not appear in the second string should be sorted to the end of the result in original order.

### **_Examples_**

```
Input: 'foos', 'of' => Output: 'oofs'

Input: 'string', 'gnirts' => Output: 'gnirts'

Input: 'banana', 'abn' => Output: 'aaabnn'
```

#

<br />

# Challenge 166 Int32 To IPv4

My solution -> *[166Int32ToIPv4](166Int32ToIPv4.js)*

## **_Task condition:_**

Take the following IPv4 address: `128.32.10.1`

- 1st octet `128` has the binary representation: `10000000`
- 2nd octet `32` has the binary representation: `00100000`
- 3rd octet `10` has the binary representation: `00001010`
- 4th octet `1` has the binary representation: `00000001`

So `128.32.10.1` == `10000000.00100000.00001010.00000001`

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: `2149583361`

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

### **_Examples_**

```
Input: 2149583361  => Output: '128.32.10.1'

Input: 32          => Output: '0.0.0.32'

Input: 0           => Output: '0.0.0.0'
```

#

<br />

# Challenge 167 Interleaving Arrays

My solution -> *[167InterleavingArrays](167InterleavingArrays.js)*

## **_Task condition:_**

Create a function, that accepts an arbitrary number of arrays and returns a single array generated by alternately appending elements from the passed in arguments. If one of them is shorter than the others, the result should be padded with empty elements.

### **_Examples_**

```
Input: [1, 2, 3], ['c', 'd', 'e'] => Output: [1, 'c', 2, 'd', 3, 'e']

Input: [1, 2, 3], [4, 5] => [1, 4, 2, 5, 3, null]

Input: [1, 2, 3], [4, 5, 6], [7, 8, 9] => [1, 4, 7, 2, 5, 8, 3, 6, 9]

Input: [] => []
```

#

<br />

# Challenge 168 Grouped By Commas

My solution -> *[168GroupedByCommas](168GroupedByCommas.js)*

## **_Task condition:_**

Finish the solution so that it takes an input `n` (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.

Assume: `0 <= n <= 2147483647`

### **_Examples_**

```
       1  ->           '1'
      10  ->          '10'
     100  ->         '100'
    1000  ->       '1,000'
   10000  ->      '10,000'
  100000  ->     '100,000'
 1000000  ->   '1,000,000'
35235235  ->  '35,235,235'
```

#

<br />

# Challenge 169 ISBN-10 Validation

My solution -> *[169ISBN10Validation](169ISBN10Validation.js)*

## **_Task condition:_**

ISBN-10 identifiers are ten digits long. The first nine characters are digits `0-9`. The last digit can be `0-9` or `X`, to indicate a value of `10`.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:

```
ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
```

This is a valid ISBN, because:

```
(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
```

### **_Examples_**

```
Input: 1112223339   => Output: true

Input: 111222333    => Output: false

Input: 1112223339X  => Output: false

Input: 1234554321   => Output: true

Input: 1234512345   => Output: false

Input: 048665088X   => Output: true

Input: X123456788   => Output: false
```

#

<br />

# Challenge 170 Two Sets Of Equal Sum

My solution -> *[170TwoSetsOfEqualSum](170TwoSetsOfEqualSum.js)*

## **_Task condition:_**

If possible, divide the integers `1,2,…,n` into two sets of equal sum.

**Input**

A positive integer `n <= 1,000,000`.

**Output**

If it's not possible, return `[]`;

If it's possible, return two disjoint sets. Each integer from `1` to `n` must be in one of them. The integers in the first set must sum up to the same value as the integers in the second set. The sets must be returned in tuple.

### **_Examples_**

```
Input: n = 8 => Output: [[1, 3, 6, 8], [2, 4, 5, 7]] or [[8, 1, 3, 2, 4], [5, 7, 6]] or [[7, 8, 3], [6, 1, 5, 4, 2]] or others

Input: n = 9 => Output: [] -> it is not possible
```

#

<br />

# Challenge 171 Are We Alternate?

My solution -> *[171AreWeAlternate](171AreWeAlternate.js)*

## **_Task condition:_**

Create a function that accepts a string as an argument and validates whether the vowels `(a, e, i, o, u)` and consonants are in alternate order.

### **_Examples_**

```
Input: "amazon" => Output: true

Input: "apple" => Output: false

Input: "banana" => Output: true
```

**_NOTES:_**

- Arguments consist of only lowercase letters.

#

<br />

# Challenge 172 Greed Is Good

My solution -> *[172GreedIsGood](172GreedIsGood.js)*

## **_Task condition:_**

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

```
Three 1's => 1000 points
Three 6's =>  600 points
Three 5's =>  500 points
Three 4's =>  400 points
Three 3's =>  300 points
Three 2's =>  200 points
One   1   =>  100 points
One   5   =>   50 point
```

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

### **_Examples_**

```
Input: [5, 1, 3, 4, 1] => Output: 250 (50 (for the 5) + 2 * 100 (for the 1s))

Input: [1, 1, 1, 3, 1] => Output: 1100 (1000 (for three 1s) + 100 (for the other 1))

Input: [2, 4, 4, 5, 4] => Output: 450 (400 (for three 4s) + 50 (for the 5))
```

**_NOTES:_**

- Solution must not modify the input array.

#

<br />

# Challenge 173 Inverted Ranges

My solution -> *[173InvertedRanges](173InvertedRanges.js)*

## **_Task condition:_**

A range of numbers is represented as a tuple of two numbers, for example `[0, 10]` would indicate a range between `0` and `10` inclusively.

The inverse of a range between some bounds are the ranges from the lower bound, to the lowest part of the range and the upper part of the range to the upper bound.

**For example:**

- Given the range `[25, 75]`
- And the lower bound `0`
- And the upper bound `100`

The inverse ranges would be `[[0, 24], [76, 100]]`.

Write a function `invertedRanges` which when given a list of ranges, returns the inverse of those ranges with a lower bound of `0` and an upper bound of `100`.

All ranges will be between `0` and `100`, they will be given in order and will not overlap.

### **_Examples_**

```
An empty list of ranges would return a list with a single range between 0 and 100:

Input: invertedRanges([]) => Output: [[0, 100]]

A list of ranges which cover numbers between 0 and 100 would return an empty list:

Input: invertedRanges([[0, 100]]) => Output: []
Input: invertedRanges([[0, 50], [51, 100]]) => Output: []

A list of ranges which cover some numbers between 0 and 100 must return the ranges that aren't covered:

Input: invertedRanges([[0, 25], [51, 75]]) => Output: [[26, 50], [76, 100]]
```

#

<br />

# Challenge 174 Binary Coded Decimal

My solution -> *[174BinaryCodedDecimal](174BinaryCodedDecimal.js)*

## **_Task condition:_**

Convert a number to a binary coded decimal `(BCD)`.

You can assume input will always be an integer. If it is a negative number then simply place a minus sign in front of the output string. Output will be a string with each digit of the input represented as `4` bits (`0` padded) with a space between each set of `4` bits.

### **_Examples_**

```
Input: 10 => Output: '0001 0000'

Input: -10 => Output: '-0001 0000'
```

#

<br />

# Challenge 175 Data Reverse

My solution -> *[175DataReverse](175DataReverse.js)*

## **_Task condition:_**

A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

```
11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
```

should become:

```
10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
```

The total number of bits will always be a multiple of 8.

The data is given in an array as such:

```
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
```

### **_Examples_**

```
Input: [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
Output: [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

Input: [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
Output: [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
```

#

<br />

# Challenge 176 Valid Phone Number

My solution -> *[176ValidPhoneNumber](176ValidPhoneNumber.js)*

## **_Task condition:_**

Write a function that accepts a string, and returns true if it is in the form of a phone number.

Assume that any integer from `0-9` in any of the spots will produce a valid phone number.

Only worry about the following format: `(123) 456-7890` (don't forget the space after the close parentheses).

### **_Examples_**

```
Input: '(123) 456-7890' => Output: true

Input: '(1111)555 2345' => Output: false

Input: '(098) 123 4567' => Output: false
```

#

<br />

# Challenge 177 Make The Deadfish Swim

My solution -> *[177MakeTheDeadFishSwim](177MakeTheDeadFishSwim.js)*

## **_Task condition:_**

Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to `0`.

It uses four single-character commands:
- `i`: Increment the value
- `d`: Decrement the value
- `s`: Square the value
- `o`: Output the value to a result array

All other instructions are no-ops and have no effect.

### **_Examples_**

```
Input: 'iiisdoso' => Output: [8, 64]

Input: 'iiisdosodddddiso' => Output: [8, 64, 3600]
```

#

<br />

# Challenge 178 Alex & Snooker: Points Earned

My solution -> *[178AlexAndSnookerPointsEarned](178AlexAndSnookerPointsEarned.js)*

## **_Task condition:_**

Alex is a great fan of snooker and he likes recording the results of his favourite players by recording the balls that fall into the pockets of the table. He asks you to help him with a program that calculates the points a player scored in a given set using his notes. Unfortunately, his notes are quite a mess... Sometimes Alex forgets that he already wrote down a color and records it multiple times.

Given his short hand notation as string, calculate the points a player scored in a set.

He codes the ball colors with letters:

```
- R  = red     -->  1 point
- Y  = yellow  -->  2 points
- G  = green   -->  3 points
- Bn = brown   -->  4 points
- Be = blue    -->  5 points
- P  = pink    -->  6 points
- Bk = black   -->  7 points
- W  = white   -->  no points because it's a foul
```

The color may be followed by a number, e.g. R12 would stand for 12 red balls pocketed. If there is no number given, the ball was pocketed once.

**_Notes:_**

- If the string includes the white ball, return `'Foul'`.
- If the total score is more than `147`, return `'invalid data'`.

For your convenience the points for each color are provided as hash / dictionary with the name `blz`.

### **_Examples_**

```
Input: 'R15P3G1Bk4Y1Bn1Be3'         => Output: 85

Input: 'R13Bk14YRGBnBkRBePBk1'      => Output: 147

Input: 'G9G11P9Bn2Bn1Be10G7WBn10G3' => Output: 'Foul'

Input: 'Bn14Bn14Bn8P9'              => Output: 'invalid data'
```

#

<br />

# Challenge 179 Name Array Capping

My solution -> *[179NameArrayCapping](179NameArrayCapping.js)*

## **_Task condition:_**

Create a function that accepts an array of names, and returns an array of each name with its first letter capitalized and the remainder in lowercase.

### **_Examples_**

```
Input: ['jo', 'nelson', 'jurie'] => Output: ['Jo', 'Nelson', 'Jurie']

Input: ['KARLY', 'DANIEL', 'KELSEY'] => Output: ['Karly', 'Daniel', 'Kelsey']
```

#

<br />

# Challenge 180 Build A Pile Of Cubes

My solution -> *[180BuildAPileOfCubes](180BuildAPileOfCubes.js)*

## **_Task condition:_**

Your task is to construct a building which will be a pile of **_n_** cubes. The cube at the bottom will have a volume of **_n<sup>3</sup>_**, the cube above will have volume of **_(n−1)<sup>3</sup>_** and so on until the top which will have a volume of **_1<sup>3</sup>_**.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb will be an integer **_m_** and you have to return the integer **_n_** such as **_n<sup>3</sup> + (n−1)<sup>3</sup> + (n−2)<sup>3</sup> + ... + 1<sup>3</sup> = m_** if such a **_n_** exists or **_-1_** if there is no such **_n_**.

### **_Examples_**

```
Input: 1071225 => Output: 45

Input: 91716553919377 => Output: -1
```

#

<br />

# Challenge 181 IP Validation

My solution -> *[181IPValidation](181IPValidation.js)*

## **_Task condition:_**

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between `0` and `255`, inclusive.

### **_Examples_**

```
Input: 1.2.3.4 => Output: true

Input: 123.45.67.89 => Output: true

Input: 1.2.3 => Output: false

Input: 1.2.3.4.5 => Output: false

Input: 123.456.78.90 => Output: false

Input: 123.045.067.089 => Output: false
```

**_NOTES:_**

- Leading zeros (e.g. `01.02.03.04`) are considered invalid
- Inputs are guaranteed to be a single string

#

<br />