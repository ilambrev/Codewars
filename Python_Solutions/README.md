# Challenge 001 Convert A Boolean To A String

My solution -> *[001_convert_a_boolean_to_a_string](001_convert_a_boolean_to_a_string.py)*

## **_Task condition:_**

Implement a function which convert the given boolean value into its string representation.

### **_Examples_**

```
Input: boolean_to_string(True) => Output: "True"

Input: boolean_to_string(False) => Output: "False"
```

**_NOTES:_**

- Only valid inputs will be given.

#

<br />

# Challenge 002 Hello, Name Or World!

My solution -> *[002_hello_name_or_world](002_hello_name_or_world.py)*

## **_Task condition:_**

Define a method `hello` that `returns "Hello, Name!"` to a given `name`, or says `Hello, World!` if `name` is not given (or passed as an empty String).

Assuming that `name` is a `String` and it checks for user typos to return a name with a first capital letter (Xxxx).

### **_Examples_**

```
Input: "John" => Output: "Hello, John!"

Input: "aLIce" => Output: "Hello, Alice!"

Input: "" => Output: "Hello, World!"
```

#

<br />

# Challenge 003 Parse Float

My solution -> *[003_parse_float](003_parse_float.py)*

## **_Task condition:_**

Write function `parse_float` which takes a string/list and returns a `number` or `None` if conversion is not possible.

### **_Examples_**

```
Input: "1.0" => Output: 1.0

Input: "a" => Output: None

Input: "234.0234" => Output: 234.0234
```

#

<br />

# Challenge 004 Remove Exclamation Marks

My solution -> *[004_remove_exclamation_marks](004_remove_exclamation_marks.py)*

## **_Task condition:_**

Write function `remove_exclamation_marks(s)` which removes all exclamation marks from a given string.

### **_Examples_**

```
Input: "Hello World!" => Output: "Hello World"

Input: "Hello World!!!" => Output: "Hello World"

Input: "Hi! Hello!" => Output: "Hi Hello"

Input: "" => Output: ""

Input: "Oh, no!!!" => Output: "Oh, no"
```

#

<br />

# Challenge 005 Is It A Palindrome?

My solution -> *[005_is_it_a_palindrome](005_is_it_a_palindrome.py)*

## **_Task condition:_**

Write a function that checks if a given string (case insensitive) is a `palindrome`.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as `madam` or `racecar`.

### **_Examples_**

```
Input: "a" => Output: True

Input: "aba" => Output: True

Input: "Abba" => Output: True

Input: "malam" => Output: True

Input: "walter" => Output: False

Input: "kodok" => Output: True

Input: "Kasue" => Output: False
```

#

<br />

# Challenge 006 Third Angle Of A Triangle

My solution -> *[006_third_angle_of_a_triangle](006_third_angle_of_a_triangle.py)*

## **_Task condition:_**

You are given two interior angles (in degrees) of a triangle.

Write a function `other_angl(first_angle, second_angle)` to return the 3rd.

### **_Examples_**

```
Input: other_angle(30, 60) => Output: 90

Input: other_angle(60, 60) => Output: 60

Input: other_angle(43, 78) => Output: 59

Input: other_angle(10, 20) => Output: 150
```

**_NOTES:_**

- Only positive integers will be tested.

#

<br />

# Challenge 007 Invert Values

My solution -> *[007_invert_values](007_invert_values.py)*

## **_Task condition:_**

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

### **_Examples_**

```
Input: [1, 2, 3, 4, 5] => Output: [-1, -2, -3, -4, -5]

Input: [1, -2, 3, -4, 5] => Output: [-1, 2, -3, 4, -5]

Input: [] => Output: []
```

**_NOTES:_**

- You can assume that all values are integers.
- Do not mutate the input array.

#

<br />

# Challenge 008 Find Numbers Which Are Divisible By Given Number

My solution -> *[008_find_numbers_which_are_divisible_by_given_number](008_find_numbers_which_are_divisible_by_given_number.py)*

## **_Task condition:_**

Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of `numbers` and the second is the `divisor`.

### **_Examples_**

```
Input: divisible_by([1,2,3,4,5,6], 2) => Output: [2,4,6]

Input: divisible_by([1,2,3,4,5,6], 3) => Output: [3,6]

Input: divisible_by([0,1,2,3,4,5,6], 4) => Output: [0,4]

Input: divisible_by([0], 4) => Output: [0]

Input: divisible_by([1,3,5], 2) => Output: []

Input: divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1) => Output: [0,1,2,3,4,5,6,7,8,9,10]
```

#

<br />

# Challenge 009 What Is Between?

My solution -> *[009_what_is_between](009_what_is_between.py)*

## **_Task condition:_**

Complete the function that takes two integers (`a, b`, where `a < b`) and return an array of all integers between the input parameters, including them.

### **_Examples_**

```
Input: between(1, 4) => Output: [1, 2, 3, 4]

Input: between(-2, 2) => Output: [-2, -1, 0, 1, 2]
```

#

<br />

# Challenge 010 Correct The Mistakes Of The Character Recognition Software

My solution -> *[010_correct_the_mistakes_of_the_character_recognition_software](010_correct_the_mistakes_of_the_character_recognition_software.py)*

## **_Task condition:_**

Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

- `S` is misinterpreted as `5`
- `O` is misinterpreted as `0`
- `I` is misinterpreted as `1`

The test cases contain numbers only by mistake.

### **_Examples_**

```
Input: correct("L0ND0N") => Output: "LONDON"

Input: correct("DUBL1N") => Output: "DUBLIN"

Input: correct("51NGAP0RE") => Output: "SINGAPORE"

Input: correct("BUDAPE5T") => Output: "BUDAPEST"

Input: correct("PAR15") => Output: "PARIS"
```

#

<br />

# Challenge 011 Count The Monkeys!

My solution -> *[011_count_the_monkeys](011_count_the_monkeys.py)*

## **_Task condition:_**

You take your son to the forest to see the monkeys. You know that there are a certain number there `(n)`, but your son is too young to just appreciate the full number, he has to start counting them from `1`.

As a good parent, you will sit and count with him. Given the number `(n)`, populate an array with all numbers up to and including that number, but excluding zero.

### **_Examples_**

```
Input: monkey_count(5) => Output: [1, 2, 3, 4, 5]

Input: monkey_count(3) => Output: [1, 2, 3]

Input: monkey_count(9) => Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Input: monkey_count(10) => Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Input: monkey_count(20) => Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```

#

<br />

# Challenge 012 Digits Explosion

My solution -> *[012_digits_explosion](012_digits_explosion.py)*

## **_Task condition:_**

Given a string made of digits `[0-9]`, return a string where each digit is repeated a number of times equals to its value. 

### **_Examples_**

```
Input: explode("312") => Output: "333122"

Input: explode("102269") => Output: "12222666666999999999"

Input: explode("0") => Output: ""

Input: explode("000") => Output: ""

Input: explode("123") => Output: "122333"
```

#

<br />

# Challenge 013 Sliding Windows

My solution -> *[013_sliding_windows](013_sliding_windows.py)*

## **_Task condition:_**

Given a `length`, an `offset`, and a `list`, slide a window of that length, moving by that offset every step, over the list, returning a list of lists.

The windows may overlap each other, or skip certain elements. All windows should be of the given length; if insufficient elements remain after a certain offset, end the list of lists. It is possible to take `0` elements from an empty list, so take care to handle `window(0, offset, list)` correctly.

The length will always be non-negative; the offset will always be strictly positive.

### **_Examples_**

```
Input: window(2, 1, [0,1,2,3,4]) => Output: [[0,1], [1,2], [2,3], [3,4]]

Input: window(2, 2, [0,1,2,3,4]) => Output: [[0,1], [2,3]]

Input: window(2, 3, [0,1,2,3,4]) => Output: [[0,1], [3,4]]
```

#

<br />

# Challenge 014 esrever esreveR!

My solution -> *[014_reverse_reverse](014_reverse_reverse.py)*

## **_Task condition:_**

You must take an input string, reverse the order of the words, and reverse the order of the letters within the words.

But, as a bonus, every test input will end with a punctuation mark (! ? .) and the output should be returned with the mark at the end.

### **_Examples_**

```
Input: esrever("hello world.") => Output: "dlrow olleh."

Input: esrever("Much l33t?") => Output: "t33l hcuM?"

Input: esrever("tacocat!") => Output: "tacocat!"
```

**_NOTES:_**

- A string will always be passed in (though it may be empty) so no need for error-checking other types.

#

<br />

# Challenge 015 Find The Nth Occurrence Of A Word In A String!

My solution -> *[015_find_the_nth_occurrence_of_a_wordIn_a_string](015_find_the_nth_occurrence_of_a_wordIn_a_string.py)*

## **_Task condition:_**

You are required to implement a function that returns the index of the `nth` occurrence of a `substring` within a `string` (considering that those substring could overlap each other). If there are less than `n` occurrences of the substring, return `-1`.

### **_Examples_**

```
substring = "example"
string = "This is an example. Return the nth occurrence of example in this example string."

Input: find_nth_occurrence(substring, string, 1) => Output: 11
Input: find_nth_occurrence(substring, string, 2) => Output: 49
Input: find_nth_occurrence(substring, string, 3) => Output: 65
Input: find_nth_occurrence(substring, string, 4) => Output: -1

---------------------------
substring = "TestTest"
string = "TestTestTestTest"

Input: find_nth_occurrence(substring, string, 1) => Output: 0
Input: find_nth_occurrence(substring, string, 2) => Output: 4
Input: find_nth_occurrence(substring, string, 3) => Output: 8
Input: find_nth_occurrence(substring, string, 4) => Output: -1
```

**_NOTES:_**

- Multiple occurrences of a substring are allowed to overlap.

#

<br />

# Challenge 016 Exclamation Marks Series #5: Remove All Exclamation Marks From The End Of Words

My solution -> *[016_remove_all_exclamation_marks_from_the_end_of_words](016_remove_all_exclamation_marks_from_the_end_of_words.py)*

## **_Task condition:_**

Remove all exclamation marks from the end of words. Words are separated by a single space. There are no exclamation marks within a word.

### **_Examples_**

```
Input: remove('Hi!') => Output: 'Hi'

Input: remove('Hi!!!') => Output: 'Hi'

Input: remove('!Hi') => Output: '!Hi'

Input: remove('!Hi!') => Output: '!Hi'

Input: remove('Hi! Hi!') => Output: 'Hi Hi'

Input: remove('!!!Hi !!hi!!! !hi') => Output: '!!!Hi !!hi !hi'
```

#

<br />

# Challenge 017 Blowing Birthday Candles

My solution -> *[017_blowing_birthday_candles](017_blowing_birthday_candles.py)*

## **_Task condition:_**

Today is the special day you've been waiting for - it's your birthday! It's 8 AM and you're setting up your birthday cake for the party. It's time to put the candles on top.

You take out all the candles you've bought. As you are about to put them on the cake, you just realize that there are numbers on each candles. What are these numbers?! After searching about it on the internet, turns out these are special candles. These candles need to be blown a certain number of times before they're finally extinguished, and those numbers on the candles are the required times to blow them.

Being one who plans meticulously, you want to determine the total number of blows you need to extinguish all the candles once you've put them on the cake.

Remove all exclamation marks from the end of words. Words are separated by a single space. There are no exclamation marks within a word.

**_Task_**

Given a string containing digits (representing the strength of the candles), calculate the number of blows you need to extinguish all the candles.

Starting at the beginning of the string, each blow can only reach `3` candles, reducing their strength by one each. You can only reach more candles once those directly in front of you are extinguished.

### **_Examples_**

```
Input: '1321' => Output: 3

Input: '0323456' => Output: 9

Input: '2113' => Output: 5
```

#

<br />

# Challenge 018 Selective Fear Of Numbers

My solution -> *[018_selective_fear_of_numbers](018_selective_fear_of_numbers.py)*

## **_Task condition:_**

I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated: The number I'm afraid of depends on which day of the week it is... This is a concrete description of my mental illness:

```
Monday      => 12

Tuesday     => numbers greater than 95

Wednesday   => 34

Thursday    => 0

Friday      => numbers divisible by 2

Saturday    => 56

Sunday      => 666 or -666
```

Write a function which takes a string (day of the week) and an integer (number to be tested) so it tells the doctor if I'm afraid or not. (return a boolean)

### **_Examples_**

```
Input: am_i_afraid('Monday', 13) => Output: False

Input: am_i_afraid('Sunday', -666) => Output: True

Input: am_i_afraid('Tuesday', 2) => Output: False

Input: am_i_afraid('Tuesday', 965) => Output: True

Input: am_i_afraid('Friday', 2) => Output: True
```

#

<br />

# Challenge 019 Area Of An Arrow

My solution -> *[019_area_of_an_arrow](019_area_of_an_arrow.py)*

## **_Task condition:_**

An arrow is formed in a rectangle with sides a and b by joining the bottom corners to the midpoint of the top edge and the centre of the rectangle.

```
 ____________
|            | 
|            | 
|            | 
|            |
|            |
|     /\     |
|    /  \    | b
|   /    \   |
|  /      \  |
| /  arrow \ |
|/__________\|
     a
```

`a` and `b` are integers and > `0`.

Write a function which returns the area of the arrow.

### **_Examples_**

```
Input: arrow_area(4,2) => Output: 2

Input: arrow_area(7,6) => Output: 10.5

Input: arrow_area(25,25) => Output: 156.25
```

#

<br />

# Challenge 020 Jenny The Youngest Detective

My solution -> *[020_jenny_the_youngest_detective](020_jenny_the_youngest_detective.py)*

## **_Task condition:_**

Jenny is 9 years old. She is the youngest detective in North America. Jenny is a 3rd grader student, so when a new mission comes up, she gets a code to decipher in a form of a sticker (with numbers) in her math notebook and a comment (a sentence) in her writing notebook. All she needs to do is to figure out one word, from there she already knows what to do. And here comes your role - you can help Jenny find out what the word is!

In order to find out what the word is, you should use the sticker (`array of 3 numbers`) to retrive `3 letters` from the comment (`string`) that create the word.

- Each of the numbers in the array refers to the position of a letter in the string, in increasing order.
- Spaces are not places, you need the actual letters. No spaces.
- The returned word should be all lowercase letters.
- if you can't find one of the letters using the index numbers, return `"No mission today"`. Jenny would be very sad, but that's life... :(

### **_Examples_**

```
Input: missing([0, 3, 5], 'I love you') => Output: "ivy"

Input: missing([29, 31, 8], 'The quick brown fox jumps over the lazy dog') => Output: "bay"

Input: missing([12, 4, 6], 'Good Morning') => Output: "No mission today"
```

#

<br />

# Challenge 021 String Scramble

My solution -> *[021_string_scramble](021_string_scramble.py)*

## **_Task condition:_**

Given a string and an array of indices, rearrange the characters of the string so that each character is placed at the position specified by the corresponding index in the array.

### **_Explanation_**

```
input: "abcd", [0, 3, 1, 2]
output: "acdb"

- The character 'a' is placed at index 0.
- The character 'b' is placed at index 3.
- The character 'c' is placed at index 1.
- The character 'd' is placed at index 2.
```

### **_Examples_**

```
Input: scramble('abcd', [0, 3, 1, 2]) => Output: 'acdb'

Input: scramble('sc301s', [4,0,3,1,5,2]) => Output: 'c0s3s1'

Input: scramble('bskl5', [2,1,4,3,0]) => Output: '5sblk'
```

**_NOTES:_**

- The string and the array will be of equal length.
- The string will contain valid characters `(A-Z, a-z, or 0-9)`.
- The array will contain valid indices.

#

<br />

# Challenge 022 Return The First M Multiples Of N

My solution -> *[022_return_the_first_m_multiples_of_n](022_return_the_first_m_multiples_of_n.py)*

## **_Task condition:_**

Implement a function that takes two numbers `m` and `n` and returns an array of the first `m` multiples of the real number `n`. Assume that `m` is a positive integer.

### **_Examples_**

```
Input: multiples(3, 5) => Output: [5, 10, 15]
```

#

<br />

# Challenge 023 EAN Validation

My solution -> *[023_ean_validation](023_ean_validation.py)*

## **_Task condition:_**

A lot of goods have an International Article Number (formerly known as "European Article Number") abbreviated "EAN". EAN is a 13-digit barcode consisting of 12 digits followed by a single-digit checksum.

The single-digit checksum is calculated as follows (based upon the first 12 digits):
- The digits at the first, third, fifth, etc. positions (i.e. at the odd positions) are multiplied by `1`.
- The digits at the second, fourth, sixth, etc. positions (i.e. at the even positions) are multiplied by `3`.
- Sum these results.

If this sum is divisible by `10`, the checksum is `0`. Otherwise the checksum has the following formula:

_`checksum = 10 - (sum mod 10)`_

For example, calculate the checksum for `400330101839` (12 digits):

_`4 * 1 + 0 * 3 + 0 * 1 + 3 * 3 + 3 * 1 + 0 * 3 + 1 * 1 + 0 * 3 + 1 * 1 + 8 * 3 + 3 * 1 + 9 * 3 = 4 + 0 + 0 + 9 + 3 + 0 + 1 + 0 + 1 + 24 + 3 + 27 = 72`_

_`10 - (72 mod 10) = 8 => Checksum: 8`_

Thus, the `EAN-Code` is `4003301018398` (12 digits followed by single-digit checksum).

Validate a given `EAN-Code`. Return `True` if the given `EAN-Code` is valid, otherwise `False`.

### **_Examples_**

```
Input: validate_ean('4003301018398') => Output: True

Input: validate_ean('9783815820865') => Output: True

Input: validate_ean('9783815820864') => Output: False

Input: validate_ean('9783827317100') => Output: True
```

**_NOTES:_**

- You can assume the given code is syntactically valid, i.e. it only consists of numbers and it exactly has a length of `13` characters.

#

<br />

# Challenge 024 Pairs Of Integers From 0 To N

My solution -> *[024_pairs_of_integers_from_0_to_n](024_pairs_of_integers_from_0_to_n.py)*

## **_Task condition:_**

Write a function that accepts an integer argument `n` and generates an array containing the pairs of integers `[a, b]` that satisfy the condition

_`0 <= a <= b <= n`_

The pairs should be sorted by increasing values of `a`, then by increasing values of `b`.

### **_Examples_**

```
Input: generate_pairs(2) => Output: [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]]

Input: generate_pairs(0) => Output: [[0, 0]]
```

#

<br />

# Challenge 025 Simple Letter Removal

My solution -> *[025_simple_letter_removal](025_simple_letter_removal.py)*

## **_Task condition:_**

You will be given a lower case string and your task will be to remove `k` characters from that string using the following rule:

- first remove all letter 'a', followed by letter 'b', then 'c', etc...
- remove the leftmost character first.

### **_Examples_**

```
Input: solve('abracadabra', 1) => Output: 'bracadabra'

Input: solve('abracadabra', 2) => Output: 'brcadabra'

Input: solve('abracadabra', 6) => Output: 'rcdbr'

Input: solve('abracadabra', 8) => Output: 'rdr'

Input: solve('abracadabra',50) => Output: ''
```

#

<br />

# Challenge 026 Pull Your Words Together, Man!

My solution -> *[026_pull_your_words_together_man](026_pull_your_words_together_man.py)*

## **_Task condition:_**

Your friend Robbie has successfully created an AI that is capable of communicating in English!

Robbie's almost done with the project, however the machine's output isn't working as expected. Here's a sample of a sentence that it outputs:

```
["this","is","a","sentence"]
```

Every time that it tries to say a sentence, instead of formatting it in normal English orthography, it just outputs a list of words.

Robbie has pulled multiple all-nighters to get this project finished, and he needs some beauty sleep. So, he wants you to write the last part of his code, a `sentencify` function, which takes the output that the machine gives, and formats it into proper English orthography.

Your function should:

1. Capitalise the first letter of the first word.
2. Add a period (`.`) to the end of the sentence.
3. Join the words into a complete string, with spaces.
4. Do no other manipulation on the words.

### **_Examples_**

```
Input: sentencify(["i", "am", "an", "AI"]) => Output: "I am an AI."

Input: sentencify(["yes"]) => Output: "Yes."

Input: sentencify(["FIELDS", "of", "CORN", "are", "to", "be", "sown"]) => Output: "FIELDS of CORN are to be sown."

Input: sentencify(["i'm", "afraid", "I", "can't", "let", "you", "do", "that"]) => Output: "I'm afraid I can't let you do that."
```

#

<br />

# Challenge 027 Likes Vs Dislikes

My solution -> *[027_likes_vs_dislikes](027_likes_vs_dislikes.py)*

## **_Task condition:_**

YouTube had a like and a dislike button, which allowed users to express their opinions about particular content. It was set up in such a way that you cannot like and dislike a video at the same time. There are two other interesting rules to be noted about the interface: Pressing a button, which is already active, will undo your press. If you press the like button after pressing the dislike button, the like button overwrites the previous "Dislike" state. The same is true for the other way round.

Create a function that takes in a list of button inputs and returns the final state.

### **_Examples_**

```
Input: like_or_dislike([Dislike]) => Output: Dislike

Input: like_or_dislike([Like, Like]) => Output: Nothing

Input: like_or_dislike([Dislike, Like]) => Output: Like

Input: like_or_dislike([Like, Dislike, Dislike]) => Output: Nothing
```

**_NOTES:_**

- If no button is currently active, return `Nothing`.
- If the list is empty, return `Nothing`.

#

<br />

# Challenge 028 Initialize My Name

My solution -> *[028_Initialize_my_name](028_Initialize_my_name.py)*

## **_Task condition:_**

Some people just have a first name; some people have first and last names and some people have first, middle and last names.

You task is to initialize the middle names (if there is any).

### **_Examples_**

```
Input: initialize_names('Jack Ryan') => Output: 'Jack Ryan'

Input: initialize_names('Lois Mary Lane') => Output: 'Lois M. Lane'

Input: initialize_names('Dimitri') => Output: 'Dimitri'

Input: initialize_names('Alice Betty Catherine Davis') => Output: 'Alice B. C. Davis'
```

#

<br />

# Challenge 029 Find The Divisors!

My solution -> *[029_find_the_divisors](029_find_the_divisors.py)*

## **_Task condition:_**

Create a function named `divisors` that takes an integer `n > 1` and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string `'(integer) is prime'`.

### **_Examples_**

```
Input: divisors(12) => Output: [2, 3, 4, 6]

Input: divisors(25) => Output: [5]

Input: divisors(13) => Output: '13 is prime'
```

#

<br />

# Challenge 030 Add Commas To A Number

My solution -> *[030_add_commas_to_a_number](030_add_commas_to_a_number.py)*

## **_Task condition:_**

Your task is to convert a given number into a string with commas added for easier readability. The number should be rounded to 3 decimal places and the commas should be added at intervals of three digits before the decimal point. There does not need to be a comma at the end of the number.

You will receive both positive and negative numbers.

### **_Examples_**

```
Input: commas(1) => Output: "1"

Input: commas(1000) => Output: "1,000"

Input: commas(100.2346) => Output: "100.235"

Input: commas(1000000000.23) => Output: "1,000,000,000.23"

Input: commas(-1) => Output: "-1"

Input: commas(-1000000.123) => Output: "-1,000,000.123"
```

#

<br />

# Challenge 031 Even Odd Pattern #1

My solution -> *[031_even_odd_pattern_1](031_even_odd_pattern_1.py)*

## **_Task condition:_**

Write a function that takes an `list` of numbers and returns a number.

See the examples and try to guess the pattern.

### **_Examples_**

```
Input: even_odd([1, 2, 6, 1, 6, 3, 1, 9, 6]) => Output: 393

Input: even_odd([1, 2, 3]) => Output: 5

Input: even_odd([0, 2, 3]) => Output: 3

Input: even_odd([1, 0, 3]) => Output: 3

Input: even_odd([3, 2]) => Output: 6
```

#

<br />

# Challenge 032 World Bits War

My solution -> *[032_world_bits_war](032_world_bits_war.py)*

## **_Task condition:_**

The war has expanded and become dirtier and meaner; both even and odd numbers will fight with their pointy `1s`. And negative integers are coming into play as well, with, `"ça va sans dire"`, a negative contribution (think of them as spies or saboteurs).

A number's strength is determined by the number of set bits (`1s`) in its binary representation. Negative integers work against their own side so their strength is negative. For example `-5 = -101` has strength `-2` and `+5 = +101` has strength `+2`.

The side with the largest cumulated strength wins.

Again, three possible outcomes: `odds win`, `evens win` and `tie`.

### **_Examples_**

```
Input: bits_war([1, 5, 12]) => Output: "odds win" // 1 + 101 vs 1100, 3 vs 2

Input: bits_war([7, -3, 20]) => Output: "evens win" // 111 - 11  vs 10100, 3 - 2 vs 2

Input: bits_war([7, -3, -2, 6]) => Output: "tie" // 111 - 11  vs -1 + 110, 3 - 2 vs -1 + 2
```

#

<br />

# Challenge 033 Check If Two Words Are Isomorphic To Each Other

My solution -> *[033_check_if_two_words_are_isomorphic_to_each_other](033_check_if_two_words_are_isomorphic_to_each_other.py)*

## **_Task condition:_**

Two strings `a` and `b` are called isomorphic if there is a one to one mapping possible for every character of `a` to every character of `b`. And all occurrences of every character in `a` map to same character in `b`.

You will create a function that return `True` if two given strings are isomorphic to each other, and `False` otherwise. Remember that order is important.

Your solution must be able to handle words with more than 10 characters.

### **_Examples_**

```
Input: isomorph("CBAABC", "DEFFED") => Output: True

Input: isomorph("XXX", "YYY") => Output: True

Input: isomorph("RAMBUNCTIOUSLY", "THERMODYNAMICS") => Output: True

Input: isomorph("AB", "CC") => Output: False

Input: isomorph("XXY", "XYY") => Output: False

Input: isomorph("ABAB", "CD") => Output: False
```

#

<br />

# Challenge 034 Separating Strings

My solution -> *[034_separating_strings](034_separating_strings.py)*

## **_Task condition:_**

Create a function that takes a string and separates it into a sequence of letters.

The array will be formatted as so:

```
[['J','L','L','M'],
 ['u','i','i','a'],
 ['s','v','f','n'],
 ['t','e','e','']]
```

The function should separate each word into individual letters, with the first word in the sentence having its letters in the 0th index of each 2nd dimension array, and so on.

Shorter words will have an empty string in the place once the word has already been mapped out. (See the last element in the last part of the array.)

### **_Examples_**

```
Input: sep_str("Just Live Life Man")

Output:

    [['J','L','L','M'],
     ['u','i','i','a'],
     ['s','v','f','n'],
     ['t','e','e','']]

-----------------------------

Input: sep_str("The Mitochondria is the powerhouse of the cell")

Output:

    [[ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
     [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
     [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
     [ '', 'o', '', '', 'e', '', '', 'l' ],
     [ '', 'c', '', '', 'r', '', '', '' ],
     [ '', 'h', '', '', 'h', '', '', '' ],
     [ '', 'o', '', '', 'o', '', '', '' ],
     [ '', 'n', '', '', 'u', '', '', '' ],
     [ '', 'd', '', '', 's', '', '', '' ],
     [ '', 'r', '', '', 'e', '', '', '' ],
     [ '', 'i', '', '', '', '', '', '' ],
     [ '', 'a', '', '', '', '', '', '' ]]
```
#

<br />

# Challenge 035 The Queen On The Chessboard

My solution -> *[035_the_queen_on_the_chessboard](035_the_queen_on_the_chessboard.py)*

## **_Task condition:_**

In chess, the `queen` can be moved across any number of unoccupied squares in a straight line vertically, horizontally, or diagonally, thus combining the moves of the rook and bishop.

Given the square of a queen on a chessboard, your function must output an array of the squares the queen can move to. Squares are represented as strings using chess algebraic notation.

### Input

- A valid input position is a string of one letter from `A` to `H` followed by a digit from `1` to `8`, for example `"A1"`, `"C8"`, `"B3"`.
- If the input is anything else (e.g. not a string, or an invalid position such as `A10` or `H0`), return an empty array.

### Output

An array of positions (strings). It should be sorted in lexicographical order and should not include the starting square of the queen.

### **_Examples_**

```
Input: available_moves("A1")

Output: ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "C1", "C3", "D1", "D4", "E1", "E5", "F1", "F6", "G1", "G7", "H1", "H8"]

     A   B   C   D   E   F   G   H
   + - + - + - + - + - + - + - + - +
1  | Q | x | x | x | x | x | x | x |
   + - + - + - + - + - + - + - + - +
2  | x | x |   |   |   |   |   |   |
   + - + - + - + - + - + - + - + - +
3  | x |   | x |   |   |   |   |   |
   + - + - + - + - + - + - + - + - +
4  | x |   |   | x |   |   |   |   |
   + - + - + - + - + - + - + - + - +
5  | x |   |   |   | x |   |   |   |
   + - + - + - + - + - + - + - + - +
6  | x |   |   |   |   | x |   |   |
   + - + - + - + - + - + - + - + - +
7  | x |   |   |   |   |   | x |   |
   + - + - + - + - + - + - + - + - +
8  | x |   |   |   |   |   |   | x |
   + - + - + - + - + - + - + - + - +
   
Q = queen
x = available move
```

#

<br />

# Challenge 036 Ping-Pong Service Problem

My solution -> *[036_ping_pong_service_problem](036_ping_pong_service_problem.py)*

## **_Task condition:_**

Playing ping-pong can be really fun!

Unfortunately, after a long and exciting play, you can forget whose service turn it is. Let's do something about that!

Write a function that takes as its parameter the current score as a string separated by `:`, and returns `"first"` or `"second"` depending on whose service turn it is.

We're playing old-school, so the rule is that players take turns after every five services. That is until the score is `20:20` - from that moment each player serves twice, in turn.

There's no need to check if the passed parameter is valid - the score will be always provided in correct syntax and you don't need to check if one of the players has already won - that won't be the case.

The game ends when one of the players reaches `21` points with a minimum `2` point lead.

After a score of `20:20`, the winner will be the first player to reach a `2` point lead.

### **_Examples_**

```
Input: print(service('0:0')) => Output: 'first'

Input: print(service('3:2')) => Output: 'second'

Input: print(service('21:20')) => Output: 'first'

Input: print(service('21:22')) => Output: 'second'
```

#

<br />

# Challenge 037 X Marks The Spot!

My solution -> *[037_x_marks_the_spot](037_x_marks_the_spot.py)*

## **_Task condition:_**

Write a function that takes in a positive integer `n` and returns an `n x n` matrix with an `X` in the middle. The `X` will be represented by `1's` and the rest will be `0's`.

### **_Examples_**

```
Input: 5

[[1, 0, 0, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 1, 0, 0],
 [0, 1, 0, 1, 0],
 [1, 0, 0, 0, 1]]

--------------------

Input: 6

[[1, 0, 0, 0, 0, 1],
 [0, 1, 0, 0, 1, 0],
 [0, 0, 1, 1, 0, 0],
 [0, 0, 1, 1, 0, 0],
 [0, 1, 0, 0, 1, 0],
 [1, 0, 0, 0, 0, 1]]
```

#

<br />

# Challenge 038 Chess Piece Values

My solution -> *[038_chess_piece_values](038_chess_piece_values.py)*

## **_Task condition:_**

Complete the function that accepts two arguments, an 8x8 array representing a chess board and a string. Depending on the value of the string which can be either `"white"` or `"black"`, calculate the value of the pieces on the table for the corresponding player (white or black).

Empty fields will be marked as a space, while the fields with pieces look like this:

```
"w-king"    - white king
"b-bishop"  - black bishop
"w-pawn"    - white pawn
```

...and so on. There is an object available for you holding the value of each piece:

```
values = {
    "queen": 9,
    "rook": 5,
    "bishop": 3,
    "knight": 3,
    "pawn": 1,
}
```

This is a rough estimation and the real piece value depends on other factors in game as well, such as the game being a closed or open one, which can favor either knights or bishops. But for our purposes we will use the mentioned values.

### **_Examples_**

```
board = [
   [" ", " ", " ", " ", " ", " ", " ", " "],
   [" ", " ", "b-queen", " ", " ", " ", " ", "w-queen"],
   [" ", "b-king", " ", " ", "w-rook", " ", " ", " "],
   [" ", " ", " ", " ", " ", " ", " ", " "],
   [" ", " ", " ", " ", " ", " ", " ", " "],
   ["w-king", " ", " ", " ", " ", " ", " ", " "],
   [" ", " ", " ", " ", " ", " ", " ", " "],
   [" ", " ", " ", " ", " ", " ", " ", " "]
]

Input: pieces_value(board, 'white') => Output: 14 (queen, rook)

Input: pieces_value(board, 'black') => Output: 9 (queen)

-------------------------------------------------

board = [
   [" ", " ", " ", " ", " ", " ", " ", " "],
   [" ", " ", "b-queen", " ", " ", " ", " ", "w-queen"],
   [" ", "b-king", " ", "b-pawn", "w-rook", " ", " ", " "],
   [" ", " ", " ", " ", "w-pawn", " ", " ", " "],
   [" ", " ", " ", " ", " ", "w-bishop", " ", " "],
   ["w-king", " ", " ", " ", " ", " ", " ", " "],
   [" ", " ", " ", "b-pawn", " ", " ", " ", " "],
   [" ", " ", " ", " ", " ", " ", " ", " "]
]

Input: pieces_value(board, 'white') => Output: 18 (queen, rook, pawn, bishop)

Input: pieces_value(board, 'black') => Output: 11 (queen, 2 pawns)
```

**_NOTES:_**

- The value of a king cannot be estimated because without it the game would be over, so DO NOT take into consideration the value of the king. You will not be tested for invalid input.

#

<br />

# Challenge 039 Mr. Safety's Treasures

My solution -> *[039_mr_safetys_treasures](039_mr_safetys_treasures.py)*

## **_Task condition:_**

Mr. Safety loves numeric locks and his Nokia 3310. He locked almost everything in his house. He is so smart and he doesn't need to remember the combinations. He has an algorithm to generate new passcodes on his Nokia cell phone.

Can you crack his numeric locks? Mr. Safety's treasures wait for you. Write an algorithm to open his numeric locks. Can you do it without his Nokia 3310?

**_Input_**

The `message` input string consists of lowercase and upercase characters. It's a real object that you want to unlock.

**_Output_**

Return a string that only consists of digits. 

### **_Examples_**

```
Input: unlock("Nokia") => Output: "66542"

Input: unlock("Valut") => Output: "82588"

Input: unlock("toilet") => Output: "864538"
```

#

<br />

# Challenge 040 Card Game

My solution -> *[040_card_game](040_card_game.py)*

## **_Task condition:_**

Lеt's create function to play cards. You receive 3 arguments: `card1` and `card2` are cards from a single deck; `trump` is the main suit, which beats all others.

You have a preloaded `deck` (in case you need it):

```
deck = ["joker","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♣",
                "2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦","A♦",
                "2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♥",
                "2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♠"]
```

**_Game rules_**

- If both cards have the same suit, the higher one wins
- If both cards have trump, the higher one wins
- If the cards have different suits and no one has trump, return `"Let us play again."`
- If one card has trump, but not the other, the one with the trump wins
- If there is a winner, return `"The first/second card won."`
- If the two cards are the same, return `"Someone cheats."`
- The joker always wins

### **_Examples_**

```
Input: card_game("3♣", "Q♣", "♦") => Output: "The second card won."

Input: card_game("5♥", "A♣", "♦") => Output: "Let us play again."

Input: card_game("8♠", "8♠", "♣") => Output: "Someone cheats."

Input: card_game("2♦", "A♠", "♦") => Output: "The first card won."

Input: card_game("joker", "joker", "♦") => Output: "Someone cheats."
```

#

<br />

# Challenge 041 Consecutive Count

My solution -> *[041_consecutive_count](041_consecutive_count.py)*

## **_Task condition:_**

I want to know the size of the longest consecutive elements of `X` in `Y`. You will receive two arguments: `items` and `key`. Return the length of the longest segment of consecutive `keys` in the given `items`.

### **_Examples_**

```
Input: get_consective_items(90000, 0) => Output: 4

Input: get_consective_items("abcdaaadse", "a") => Output: 3

Input: get_consective_items("abcdaaadse", "z") => Output: 0
```

**_NOTES:_**

- The items and the key will be either an integer or a string (consisting of letters only)
- If the key does not appear in the items, return `0`

#

<br />

# Challenge 042 Simple String Indices

My solution -> *[042_simple_string_indices](042_simple_string_indices.py)*

## **_Task condition:_**

You will be given a `string with brackets` and an `index of an opening bracket` and your task will be to `return the index of the matching closing bracket`. Both the input and returned index are 0-based. An opening brace will always have a closing brace. Return `-1` if there is no answer.

### **_Examples_**

```
Input: solve("((1)23(45))(aB)", 0) => Output: 10 -- the opening brace at index 0 matches the closing brace at index 10

Input: solve("((1)23(45))(aB)", 1) => Output: 3

Input: solve("((1)23(45))(aB)", 2) => Output: -1 -- there is no opening bracket at index 2, so return -1

Input: solve("((1)23(45))(aB)", 6) => Output: 9

Input: solve("((1)23(45))(aB)", 11) => Output: 14

Input: solve("((>)|?(*'))(yZ)", 11) => Output: 14
```

**_NOTES:_**

- Input will consist of letters, numbers and special characters, but no spaces. The only brackets will be `(` and `)`. 

#

<br />

# Challenge 043 Prime Reduction

My solution -> *[043_prime_reduction](043_prime_reduction.py)*

## **_Task condition:_**

Consider the prime number `23`. If we sum the square of its digits we get: `2^2 + 3^2 = 13`, then for `13: 1^2 + 3^2 = 10`, and finally for `10: 1^2 + 0^2 = 1`.

Similarly, if we start with prime number `7`, the sequence is: `7 -> 49 -> 97 -> 130 -> 10 -> 1`.

Given a range, how many primes within that range will eventually end up being `1`?

The upperbound for the range is `50,000`. A range of `(2,25)` means that: `2 <= n < 25`.

### **_Examples_**

```
Input: solve(1, 25) => Output: 4

Input: solve(100, 1000) => Output: 28

Input: solve(100, 2000) => Output: 47

Input: solve(100, 3000) => Output: 65

Input: solve(100, 4000) => Output: 95
```

#

<br />

# Challenge 044 Find Cracker

My solution -> *[044_find_cracker](044_find_cracker.py)*

## **_Task condition:_**

Someone was hacking the score. Each student's record is given as an array The objects in the array are given again as an array of scores for each name and total score.

For example:

```
arr = [
  ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
  ["name2", 110, ["B", "A", "A", "A"]],
  ["name3", 200, ["B", "A", "A", "C"]],
  ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
]
```

The scores for each grade is:

- A: 30 points
- B: 20 points
- C: 10 points
- D: 5 points
- Everything else: 0 points

If there are `5` or more courses and all courses has a grade of `B` or above, additional `20` points are awarded. After all the calculations, the total score should be capped at `200` points.

Returns the name of the hacked name as an array when scoring with this rule. 

### **_Examples_**

```
arr = [
  ["name1", 445, ["B", "A", "A", "C", "A", "A"]],     # name1 total point is over 200 => hacked
  ["name2", 110, ["B", "A", "A", "A"]],               # name2 point is right
  ["name3", 200, ["B", "A", "A", "C"]],               # name3 point is 200 but real point is 90 => hacked
  ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]] # name4 point is right
]

Input: find_hack(arr) => Output: ["name1", "name3"]
```

#

<br />

# Challenge 045 Countdown - Longest Word

My solution -> *[045_countdown_longest_word](045_countdown_longest_word.py)*

## **_Task condition:_**

Countdown is a British game show with number and word puzzles. The letters round consists of the contestant picking 9 shuffled letters - either picking from the vowel pile or the consonant pile. The contestants are given 30 seconds to try to come up with the longest English word they can think of with the available letters - letters can not be used more than once unless there is another of the same character.

Given an uppercase `9 letter` string, `letters`, find the longest word that can be made with some or all of the letters. The preloaded array `words` contains a bunch of uppercase words that you will have to loop through. Only return the longest word; if there is more than one, return the words of the same lengths in alphabetical order. If there are no words that can be made from the letters given, return `None`.

### **_Examples_**

```
Input: longest_word("ZZZZZZZZZ") => Output: None

Input: longest_word("POVMERKIA") => Output: ["VAMPIRE"]

Input: longest_word("DVAVPALEM") => Output: ["PALMED", "VALVED", "VAMPED"]
```

#

<br />

# Challenge 046 Custom FizzBuzz Array

My solution -> *[046_custom_fizz_buzz_array](046_custom_fizz_buzz_array.py)*

## **_Task condition:_**

Write a function that returns a (custom) FizzBuzz sequence of the numbers `1 to 100`.

The function should be able to take up to 4 arguments:

- The 1st and 2nd arguments are strings, `"Fizz"` and `"Buzz"` by default;
- The 3rd and 4th arguments are integers, `3` and `5` by default.

Thus, when the function is called without arguments, it will return the classic FizzBuzz sequence up to 100:

```
fizz_buzz_custom() --> [ 1, 2, "Fizz", 4, "Buzz", "Fizz", 7, ... 14, "FizzBuzz", 16, 17, ... 98, "Fizz", "Buzz" ]
```

When the function is called with (up to 4) arguments, it should return a custom FizzBuzz sequence, for example:

```
fizz_buzz_custom('Hey', 'There')      -->  [ 1, 2, "Hey", 4, "There", "Hey", ... ]

fizz_buzz_custom('Foo', 'Bar', 2, 3)  -->  [ 1, "Foo", "Bar", "Foo", 5, "FooBar", 7, ... ]
```

### **_Examples_**

```
Input: fizz_buzz_custom()[15] => Output: 16

Input: fizz_buzz_custom()[44] => Output: "FizzBuzz" (45 is divisible by 3 and 5)

Input: fizz_buzz_custom('Hey', 'There')[25] => Output: 26

Input: fizz_buzz_custom('Hey', 'There')[11] => Output: "Hey" (12 is divisible by 3)

Input: fizz_buzz_custom("What's ", "up?", 3, 7)[80] => Output: "What's " (81 is divisible by 3)
```

**_NOTES:_**

- The function must return the sequence as a `list`. 

#

<br />

# Challenge 047 Disgruntled Employee

My solution -> *[047_disgruntled_employee](047_disgruntled_employee.py)*

## **_Task condition:_**

Sir Bobsworth is a custodian at a local data center. As he suspected, Bobsworth recently found out he is to be fired on his birthday after years of pouring his soul into maintaining the facility.

Bobsworth, however, has other plans.

Bobsworth knows there are `1` to `n` switches in the breaker box of the data center. Moving from switch `1` to `n`, Bob first flips every switch off. Beginning from the first switch again, Bob then flips `every 2nd` switch. Once again starting from the first switch, Bob then flips `every 3rd` switch. Bob continues this pattern until he flips every `nth` switch & makes `n` passes.

At the end of Bobsworth's mayhem, how many switches are turned off?

Create the function `off(n)`, that receives the `nth` switch as argument `n`. The function should return an ascending array containing all of the switch numbers that remain off after Bob completes his revenge.

### **_Examples_**

```
Input: off(1) => Output: [1]

Input: off(2) => Output: [1]

Input: off(4) => Output: [1, 4]
```

**_NOTES:_**

- The parameter `n` will always be a `number >= 1`.

#

<br />

# Challenge 048 FizzBuzz Backwards

My solution -> *[048_fizz_buzz_backwards](048_fizz_buzz_backwards.py)*

## **_Task condition:_**

Traditionally in `FizzBuzz`, multiples of `3` are replaced by `"Fizz"` and multiples of `5` are replaced by `"Buzz"`. But we could also play `FizzBuzz` with any other integer pair `[n, m]` whose multiples are replaced with `Fizz` and `Buzz`.

For a sequence of numbers, `Fizzes`, `Buzzes` and `FizzBuzzes`, find the numbers whose multiples are being replaced by `Fizz` and `Buzz`. Return them as an array `[n, m]`.

The `Fizz` and `Buzz` numbers will always be integers between `1` and `50`, and the sequence will have a maximum length of `100`. The `Fizz` and `Buzz` numbers might be equal, and might be equal to `1`.

### **_Examples_**

```
Classic FizzBuzz; multiples of 3 are replaced by Fizz, multiples of 5 are replaced by Buzz:

Input: reverse_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 6]) => Output: [3, 5]


Multiples of 2 are replaced by Fizz, multiples of 3 are replaced by Buzz:

Input: reverse_fizz_buzz([1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]) => Output: [2, 3]


Multiples of 2 are replaced by Fizz and Buzz:

Input: reverse_fizz_buzz([1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]) => Output: [2, 2]


Fizz = 1, Buzz = 6:

Input: reverse_fizz_buzz(["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]) => Output: [1, 6]
```

#

<br />

# Challenge 049 Surrounding Primes For A Value

My solution -> *[049_surrounding_primes_for_a_value](049_surrounding_primes_for_a_value.py)*

## **_Task condition:_**

We need a `function prime_bef_aft()` that gives the `largest prime` below a certain given value `n`, `bef_prime` and the smallest prime larger than this value, `aft_prime`.

The result should be output in a list like the following:

```
prime_bef_aft(n) => [befPrime, aftPrime]
```

If `n` is a prime number it will give two primes, n will not be included in the result.

### **_Examples_**

```
Input: prime_bef_aft(100) => Output: [97, 101]

Input: prime_bef_aft(97) => Output: [89, 101]

Input: prime_bef_aft(101) => Output: [97, 103]
```

**_NOTES:_**

- Range for the random tests: `1000 <= n <= 200000`.
- The extreme and special case `n = 2` will not be considered for the tests.

#

<br />

# Challenge 050 Closest And Smallest

My solution -> *[050_closest_and_smallest](050_closest_and_smallest.py)*

## **_Task condition:_**

Create a function `closest(strng)`. Input is a string `strng` of `n` positive numbers `(n = 0 or n >= 2)`. Let us call `weight` of a number the sum of its digits. For example `99` will have `"weight" 18`, `100` will have `"weight" 1`. Two numbers are `"close"` if the difference of their weights is small.

For each number in strng calculate its `"weight"` and then find two numbers of strng that have:

- the smallest difference of weights ie that are the closest;
- with the smallest weights;
- and with the smallest indices (or ranks, numbered from 0) in strng;

Function should return an array of two arrays, each subarray in the following format:

```
[number-weight, index in strng of the corresponding number, original corresponding number in strng]
```

The two subarrays are sorted in `ascending` order by their number weights if these weights are different, by their indexes in the string if they have the same weights.

### **_Examples_**

```
Input: closest("103 123 4444 99 2000") => Output: [[2, 4, 2000], [4, 0, 103]]

The weights are 4, 6, 16, 18, 2 (ie 2, 4, 6, 16, 18) closest() should return [[2, 4, 2000], [4, 0, 103]], because 2000 and 103 have for weight 2 and 4, their indexes in strng are 4 and 0. The smallest difference is 2. 4 (for 103) and 6 (for 123) have a difference of 2 too but they are not 
the smallest ones with a difference of 2 between their weights.

....................

Input: closest("80 71 62 53") => Output: [[8, 0, 80], [8, 1, 71]]

All the weights are 8. closest() should return [[8, 0, 80], [8, 1, 71]]
71 and 62 have also:
- the smallest weights (which is 8 for all)
- the smallest difference of weights (which is 0 for all pairs)
- but not the smallest indices in strng.

....................

Input: closest("444 2000 445 544") => Output: [[13, 2, 445], [13, 3, 544]]

The weights are 12, 2, 13, 13. closest() should return [[13, 2, 445], [13, 3, 544]] 
444 and 2000 have the smallest weights (12 and 2) but not the smallest difference of weights - they are not the closest.
Here the smallest difference is 0 and in the result the indexes are in ascending order.

...................

Input: closest("444 2000 445 644 2001 1002") => Output: [[3, 4, 2001], [3, 5, 1002]]

Here the smallest difference is 0 and in the result the indexes are in ascending order.
...................

Input: closest("239382 162 254765 182 485944 468751 49780 108 54") => Output: [[9, 1, 162], [9, 7, 108]]

The weights are: 27, 9, 29, 11, 34, 31, 28, 9, 9. closest() should return  [[9, 1, 162], [9, 7, 108]].
108 and 54 have the smallest difference of weights too, they also have the smallest weights but they don't have the smallest ranks in the original string.
..................

Input: closest("54 239382 162 254765 182 485944 468751 49780 108") => Output: [[9, 0, 54], [9, 2, 162]]

```

**_NOTES:_**

-  If `n == 0 closest("")` should return `[]`.

#

<br />

# Challenge 051 Rot13

My solution -> *[051_rot13](051_rot13.py)*

## **_Task condition:_**

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

### **_Examples_**

```
Input: rot13('test') => Output: 'grfg'

Input: rot13('Test') => Output: 'Grfg'

Input: rot13('aA bB zZ 1234 *!?%') => Output: 'nN oO mM 1234 *!?%'
```

**_NOTES:_**

- Please note that using `encode` is considered cheating.

#

<br />

# Challenge 052 The Road-Kill Detective

My solution -> *[052_the_road_kill_detective](052_the_road_kill_detective.py)*

## **_Task condition:_**

My name is State Trooper Mark ("skidmark" ) McDingle. My job is maintaining 117 miles of the Interstate, keeping it clean and clear of dead varmints. It is a serious job and I take my job seriously.

I am the **Road-Kill Detective**

Every time I find some dead critter I scrape it up and record what type it was in my dead-critter notebook. Mostly I just cruise up and down the interstate and only find a few racoons or the occasional squirrel... But recently the road-kill has become much more exotic. There must be some illegal private zoo back in the woods with a major security problem. But that's none of my business... Anything beyond the fog-line is out of my jurisdiction.

### **_Evidence_**

Here are some photos of what I came across last week:

- There was a thing that looked like a **_hyena_** `==========h===yyyyyy===eeee=n==a========`
- a long black and white smudge that probably once was a **_penguin_** `======pe====nnnnnn=======================n=n=ng====u==iiii=iii==nn========================n=`
- and an unlucky **_bear_** that was hit going the other direction `=====r=rrr=rra=====eee======bb====b=======`

### **_Task_**

Even for a professional like me, the identification of flattened exotic animals is not always easy!

If it ever happens that I can't find all of the remains, or if there are gaps or other parts that I don't recognise, then I record it as `??` in my dead-critter notebook.

What I really need is a program that I can scan my photos into which can give back the correct answer straight away.

Something like this:

Input: photo (not null)
Output: the detected animal name, or `??` if unknown


### **_Examples_**

```
Input: road_kill("====l===e===r=======riuqs=====") => Output: "squirrel"

Input: road_kill("===g=eccc==kkkooBo=") => Output: "??"

Input: road_kill("==gggg=iiiiirrrr===aaaaaff==fffeee") => Output: "giraffe"
```

**_NOTES:_**

- An list of all `"known"` animals is preloaded in a variable called `ANIMALS`.

#

<br />

# Challenge 053 Count IP Addresses

My solution -> *[053_count_ip_addresses](053_count_ip_addresses.py)*

## **_Task condition:_**

Implement a function that receives two `IPv4` addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid `IPv4` addresses in the form of strings. The last address will always be greater than the first one.

### **_Examples_**

```
Input: ips_between("150.0.0.0", "150.0.0.1") => Output: 1

Input: ips_between("10.0.0.0", "10.0.0.50") => Output: 50

Input: ips_between("20.0.0.10", "20.0.1.0") => Output: 246

Input: ips_between("10.11.12.13", "10.11.13.0") => Output: 243

Input: ips_between("160.0.0.0", "160.0.1.0") => Output: 256

Input: ips_between("10.0.0.0", "10.0.1.0") => Output: 256

Input: ips_between("94.95.217.20", "240.137.22.216") => Output: 2452176324

Input: ips_between("236.4.19.226", "236.9.54.139") => Output: 336553
```

#

<br />

# Challenge 054 Integers: Recreation One

My solution -> *[054_integers_recreation_one](054_integers_recreation_one.py)*

## **_Task condition:_**

Find all integers between `m` and `n` (`m` and `n` are integers with `1 <= m <= n`) such that the `sum` of their squared divisors is itself a square.

We will return an array of subarrays.

The subarrays will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

`1, 246, 2, 123, 3, 82, 6, 41` are the divisors of number `246`.

Squaring these divisors we get: `1, 60516, 4, 15129, 9, 6724, 36, 1681`.

The `sum` of these squares is `84100` which is `290 * 290`.

### **_Examples_**

```
Input: list_squared(1, 250) => Output: [[1, 1], [42, 2500], [246, 84100]]

Input: list_squared(42, 250) => Output: [[42, 2500], [246, 84100]]

Input: list_squared(250, 500) => Output: [[287, 84100]]
```

#

<br />

# Challenge 055 Mystery Function #1

My solution -> *[055_mystery_function_1](055_mystery_function_1.py)*

## **_Task condition:_**

There's a mystery function which is already available to use. It's a simple function called `mystery`. It accepts a string as a parameter and outputs a string. The exercise depends on guessing what this function actually does.

You can call the mystery function like this:

```
my_output = mystery("my_input")
```

Using your own test cases, try to call the mystery function with different input strings and try to analyze its output in order to guess what is does. You are free to call the mystery function in your own test cases however you want.

When you think you've understood how my mystery function works, prove it by reimplementing its logic in a function that you should call `'solved(x)'`. To validate your code, your function `'solved'` should return the same output as my function `'mystery'` given the same inputs.

### **_Examples_**

```
Input: solved("Hello World") => Output: "HWdellloor"

Input: solved("foobar") => Output: "abfoor"

Input: solved("I see what you did there!") => Output: "     !Iaddeeeehhirsttuwy"

Input: solved("") => Output: ""

Input: solved("abcd") => Output: "abcd"

Input: solved("abcde") => Output: "abde"
```

#

<br />

# Challenge 056 Feynman's Square Question

My solution -> *[056_feynmans_square_question](056_feynmans_square_question.py)*

## **_Task condition:_**

Richard Phillips Feynman was a well-known American physicist and a recipient of the Nobel Prize in Physics. He worked in theoretical physics and pioneered the field of quantum computing.

Recently, an old farmer found some papers and notes that are believed to have belonged to Feynman. Among notes about mesons and electromagnetism, there was a napkin where he wrote a simple puzzle: "how many different squares are there in a grid of `NxN` squares?".

For example, when `N=2`, the answer is `5`: the `2x2` square itself, plus the four `1x1` squares in its corners.

Complete the function that solves Feynman's question in general. The input to your function will always be a positive integer.

### **_Examples_**

```
Input: count_squares(1) => Output: 1

Input: count_squares(2) => Output: 5

Input: count_squares(3) => Output: 14

Input: count_squares(5) => Output: 55

Input: count_squares(8) => Output: 204

Input: count_squares(15) => Output: 1240
```

#

<br />

# Challenge 057 Part 1: Evil Programming Government Restrictions

My solution -> *[057_part_1_evil_programming_government_restrictions](057_part_1_evil_programming_government_restrictions.py)*

## **_Task condition:_**

The evil programming government has banned the use of numbers. Your task, if you choose to accept it is to return numbers, without using numbers.

Problems:

- You can't use number literals in your source code.
- You can't use the length property directly in your code.

Goal:

- You have to return `"I can write numbers like, 1, 2, 3.'"`.

### **_Examples_**

```
Input: print(anarchy()) => Output: "I can write numbers like, 1, 2, 3."
```

#

<br />

# Challenge 058 Find The Word Pair!

My solution -> *[058_find_the_word_pair.py](058_find_the_word_pair.py)*

## **_Task condition:_**

Given an array of `words` and a `target` compound word, your objective is to find the two words which combine into the target word, returning both words in the order they appear in the array, and their respective indices in the order they combine to form the target word. Words in the array you are given may repeat, but there will only be one unique pair that makes the target compound word. If there is no match found, return `None`.

### **_Examples_**

```
arr1 = ['super','bow','bowl','tar','get','book','let']
arr2 = ['bow','crystal','organic','ally','rain','line']
arr3 = ['top','main','tree','ally','fin','line']
arr4 = ['bel', 'bed', 'low', 'grab', 'be', 'knight']

Input: compound_match(arr1, 'superbowl') => Output: ['super','bowl', [0,2]]

Input: compound_match(arr2, 'crystalline') => Output: ['crystal','line', [1,5]]

Input: compound_match(arr2, 'rainbow') => Output: ['bow','rain', [4,0]]

Input: compound_match(arr2, 'organically') => Output: ['organic','ally', [2,3]]

Input: compound_match(arr3, 'mainline') => Output: ['main','line', [1,5]]

Input: compound_match(arr3, 'treetop') => Output: ['top','tree', [2,0]]

Input: compound_match(arr3, 'finally') => Output: ['ally','fin', [4,3]]

Input: compound_match(arr3, 'treefinally') => Output: None

Input: compound_match(arr4, 'below') => Output: ['low','be', [4,2]]

Input: compound_match(arr4, 'bellow') => Output: ['bel','low',[0,2]]

Input: compound_match(arr4, 'beknight') => Output: ['be','knight',[4,5]]
```

**_NOTES:_**

- Some arrays will be very long and may include duplicates, so keep an eye on efficiency.

#

<br />

# Challenge 059 If you can read this...

My solution -> *[059_if_you_can_read_this](059_if_you_can_read_this.py)*

## **_Task condition:_**

You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

```
NATO = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu",
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
```

```
"IF YOU CAN READ THIS IM NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN NEVER GONNA RUN AROUND AND DESERT YOU"

India Foxtrot Yankee Oscar Uniform Charlie Alpha
November Romeo Echo Alpha Delta Tango Hotel
India Sierra India Mike November Echo Victor Echo
Romeo Golf Oscar November November Alpha
Golf India Victor Echo Yankee Oscar Uniform
Uniform Papa November Echo Victor Echo Romeo
Golf Oscar November November Alpha Lima Echo
Tango Yankee Oscar Uniform Delta Oscar
Whiskey November November Echo Victor Echo
Romeo Golf Oscar November November Alpha
Romeo Uniform November Alpha Romeo Oscar Uniform
November Delta Alpha November Delta Delta Echo
Sierra Echo Romeo Tango Yankee Oscar Uniform
```

### Input:

`If, you can read?`

### Output:

`India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?`

### **_Examples_**

```
Input: print(to_nato('If you can read')) => Output: "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta"

Input: print(to_nato('Did not see that coming')) => Output: "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf"

Input: print(to_nato('.d?d!')) => Output: ". Delta ? Delta !"
```

**_NOTES:_**

- There is a preloaded dictionary that you can use, named `NATO`. It uses uppercase keys, e.g. `NATO['A']` is `"Alfa"`.
- The set of used punctuation is `,.!?`.
- Punctuation should be kept in your return string, but spaces should not.
- `Xray` should not have a dash within.
- Every word and punctuation mark should be seperated by a space `' '`.
- There should be no trailing whitespace.

#

<br />

# Challenge 060 Factorial decomposition

My solution -> *[060_factorial_decomposition](060_factorial_decomposition.py)*

## **_Task condition:_**

The aim of the task is to decompose `n!` (factorial n) into its prime factors.

```
n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.

n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"

n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
```

Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.

### **_Examples_**

```
Input: decomp(5) => Output: "2^3 * 3 * 5"

Input: decomp(14) => Output: "2^11 * 3^5 * 5^2 * 7^2 * 11 * 13"

Input: decomp(17) => Output: "2^15 * 3^6 * 5^3 * 7^2 * 11 * 13 * 17"

Input: decomp(22) => Output: "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"

Input: decomp(25) => Output: "2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23"

Input: decomp(79) => Output: "2^74 * 3^36 * 5^18 * 7^12 * 11^7 * 13^6 * 17^4 * 19^4 * 23^3 * 29^2 * 31^2 * 37^2 * 41 * 43 * 47 * 53 * 59 * 61 * 67 * 71 * 73 * 79"

Input: decomp(98) => Output: "2^95 * 3^46 * 5^22 * 7^16 * 11^8 * 13^7 * 17^5 * 19^5 * 23^4 * 29^3 * 31^3 * 37^2 * 41^2 * 43^2 * 47^2 * 53 * 59 * 61 * 67 * 71 * 73 * 79 * 83 * 89 * 97"

Input: decomp(3988) => Output: "2^3981 * 3^1990 * 5^994 * 7^662 * 11^396 * 13^330 * 17^247 * 19^220 * 23^180 * 29^141 * 31^132 * 37^109 * 41^99 * 43^94 * 47^85 * 53^76 * 59^68 * 61^66 * 67^59 * 71^56 * 73^54 * 79^50 * 83^48 * 89^44 * 97^41 * 101^39 * 103^38 * 107^37 * 109^36 * 113^35 * 127^31 * 131^30 * 137^29 * 139^28 * 149^26 * 151^26 * 157^25 * 163^24 * 167^23 * 173^23 * 179^22 * 181^22 * 191^20 * 193^20 * 197^20 * 199^20 * 211^18 * 223^17 * 227^17 * 229^17 * 233^17 * 239^16 * 241^16 * 251^15 * 257^15 * 263^15 * 269^14 * 271^14 * 277^14 * 281^14 * 283^14 * 293^13 * 307^12 * 311^12 * 313^12 * 317^12 * 331^12 * 337^11 * 347^11 * 349^11 * 353^11 * 359^11 * 367^10 * 373^10 * 379^10 * 383^10 * 389^10 * 397^10 * 401^9 * 409^9 * 419^9 * 421^9 * 431^9 * 433^9 * 439^9 * 443^9 * 449^8 * 457^8 * 461^8 * 463^8 * 467^8 * 479^8 * 487^8 * 491^8 * 499^7 * 503^7 * 509^7 * 521^7 * 523^7 * 541^7 * 547^7 * 557^7 * 563^7 * 569^7 * 571^6 * 577^6 * 587^6 * 593^6 * 599^6 * 601^6 * 607^6 * 613^6 * 617^6 * 619^6 * 631^6 * 641^6 * 643^6 * 647^6 * 653^6 * 659^6 * 661^6 * 673^5 * 677^5 * 683^5 * 691^5 * 701^5 * 709^5 * 719^5 * 727^5 * 733^5 * 739^5 * 743^5 * 751^5 * 757^5 * 761^5 * 769^5 * 773^5 * 787^5 * 797^5 * 809^4 * 811^4 * 821^4 * 823^4 * 827^4 * 829^4 * 839^4 * 853^4 * 857^4 * 859^4 * 863^4 * 877^4 * 881^4 * 883^4 * 887^4 * 907^4 * 911^4 * 919^4 * 929^4 * 937^4 * 941^4 * 947^4 * 953^4 * 967^4 * 971^4 * 977^4 * 983^4 * 991^4 * 997^4 * 1009^3 * 1013^3 * 1019^3 * 1021^3 * 1031^3 * 1033^3 * 1039^3 * 1049^3 * 1051^3 * 1061^3 * 1063^3 * 1069^3 * 1087^3 * 1091^3 * 1093^3 * 1097^3 * 1103^3 * 1109^3 * 1117^3 * 1123^3 * 1129^3 * 1151^3 * 1153^3 * 1163^3 * 1171^3 * 1181^3 * 1187^3 * 1193^3 * 1201^3 * 1213^3 * 1217^3 * 1223^3 * 1229^3 * 1231^3 * 1237^3 * 1249^3 * 1259^3 * 1277^3 * 1279^3 * 1283^3 * 1289^3 * 1291^3 * 1297^3 * 1301^3 * 1303^3 * 1307^3 * 1319^3 * 1321^3 * 1327^3 * 1361^2 * 1367^2 * 1373^2 * 1381^2 * 1399^2 * 1409^2 * 1423^2 * 1427^2 * 1429^2 * 1433^2 * 1439^2 * 1447^2 * 1451^2 * 1453^2 * 1459^2 * 1471^2 * 1481^2 * 1483^2 * 1487^2 * 1489^2 * 1493^2 * 1499^2 * 1511^2 * 1523^2 * 1531^2 * 1543^2 * 1549^2 * 1553^2 * 1559^2 * 1567^2 * 1571^2 * 1579^2 * 1583^2 * 1597^2 * 1601^2 * 1607^2 * 1609^2 * 1613^2 * 1619^2 * 1621^2 * 1627^2 * 1637^2 * 1657^2 * 1663^2 * 1667^2 * 1669^2 * 1693^2 * 1697^2 * 1699^2 * 1709^2 * 1721^2 * 1723^2 * 1733^2 * 1741^2 * 1747^2 * 1753^2 * 1759^2 * 1777^2 * 1783^2 * 1787^2 * 1789^2 * 1801^2 * 1811^2 * 1823^2 * 1831^2 * 1847^2 * 1861^2 * 1867^2 * 1871^2 * 1873^2 * 1877^2 * 1879^2 * 1889^2 * 1901^2 * 1907^2 * 1913^2 * 1931^2 * 1933^2 * 1949^2 * 1951^2 * 1973^2 * 1979^2 * 1987^2 * 1993^2 * 1997 * 1999 * 2003 * 2011 * 2017 * 2027 * 2029 * 2039 * 2053 * 2063 * 2069 * 2081 * 2083 * 2087 * 2089 * 2099 * 2111 * 2113 * 2129 * 2131 * 2137 * 2141 * 2143 * 2153 * 2161 * 2179 * 2203 * 2207 * 2213 * 2221 * 2237 * 2239 * 2243 * 2251 * 2267 * 2269 * 2273 * 2281 * 2287 * 2293 * 2297 * 2309 * 2311 * 2333 * 2339 * 2341 * 2347 * 2351 * 2357 * 2371 * 2377 * 2381 * 2383 * 2389 * 2393 * 2399 * 2411 * 2417 * 2423 * 2437 * 2441 * 2447 * 2459 * 2467 * 2473 * 2477 * 2503 * 2521 * 2531 * 2539 * 2543 * 2549 * 2551 * 2557 * 2579 * 2591 * 2593 * 2609 * 2617 * 2621 * 2633 * 2647 * 2657 * 2659 * 2663 * 2671 * 2677 * 2683 * 2687 * 2689 * 2693 * 2699 * 2707 * 2711 * 2713 * 2719 * 2729 * 2731 * 2741 * 2749 * 2753 * 2767 * 2777 * 2789 * 2791 * 2797 * 2801 * 2803 * 2819 * 2833 * 2837 * 2843 * 2851 * 2857 * 2861 * 2879 * 2887 * 2897 * 2903 * 2909 * 2917 * 2927 * 2939 * 2953 * 2957 * 2963 * 2969 * 2971 * 2999 * 3001 * 3011 * 3019 * 3023 * 3037 * 3041 * 3049 * 3061 * 3067 * 3079 * 3083 * 3089 * 3109 * 3119 * 3121 * 3137 * 3163 * 3167 * 3169 * 3181 * 3187 * 3191 * 3203 * 3209 * 3217 * 3221 * 3229 * 3251 * 3253 * 3257 * 3259 * 3271 * 3299 * 3301 * 3307 * 3313 * 3319 * 3323 * 3329 * 3331 * 3343 * 3347 * 3359 * 3361 * 3371 * 3373 * 3389 * 3391 * 3407 * 3413 * 3433 * 3449 * 3457 * 3461 * 3463 * 3467 * 3469 * 3491 * 3499 * 3511 * 3517 * 3527 * 3529 * 3533 * 3539 * 3541 * 3547 * 3557 * 3559 * 3571 * 3581 * 3583 * 3593 * 3607 * 3613 * 3617 * 3623 * 3631 * 3637 * 3643 * 3659 * 3671 * 3673 * 3677 * 3691 * 3697 * 3701 * 3709 * 3719 * 3727 * 3733 * 3739 * 3761 * 3767 * 3769 * 3779 * 3793 * 3797 * 3803 * 3821 * 3823 * 3833 * 3847 * 3851 * 3853 * 3863 * 3877 * 3881 * 3889 * 3907 * 3911 * 3917 * 3919 * 3923 * 3929 * 3931 * 3943 * 3947 * 3967"

Input: decomp(3989) => Output: "2^3981 * 3^1990 * 5^994 * 7^662 * 11^396 * 13^330 * 17^247 * 19^220 * 23^180 * 29^141 * 31^132 * 37^109 * 41^99 * 43^94 * 47^85 * 53^76 * 59^68 * 61^66 * 67^59 * 71^56 * 73^54 * 79^50 * 83^48 * 89^44 * 97^41 * 101^39 * 103^38 * 107^37 * 109^36 * 113^35 * 127^31 * 131^30 * 137^29 * 139^28 * 149^26 * 151^26 * 157^25 * 163^24 * 167^23 * 173^23 * 179^22 * 181^22 * 191^20 * 193^20 * 197^20 * 199^20 * 211^18 * 223^17 * 227^17 * 229^17 * 233^17 * 239^16 * 241^16 * 251^15 * 257^15 * 263^15 * 269^14 * 271^14 * 277^14 * 281^14 * 283^14 * 293^13 * 307^12 * 311^12 * 313^12 * 317^12 * 331^12 * 337^11 * 347^11 * 349^11 * 353^11 * 359^11 * 367^10 * 373^10 * 379^10 * 383^10 * 389^10 * 397^10 * 401^9 * 409^9 * 419^9 * 421^9 * 431^9 * 433^9 * 439^9 * 443^9 * 449^8 * 457^8 * 461^8 * 463^8 * 467^8 * 479^8 * 487^8 * 491^8 * 499^7 * 503^7 * 509^7 * 521^7 * 523^7 * 541^7 * 547^7 * 557^7 * 563^7 * 569^7 * 571^6 * 577^6 * 587^6 * 593^6 * 599^6 * 601^6 * 607^6 * 613^6 * 617^6 * 619^6 * 631^6 * 641^6 * 643^6 * 647^6 * 653^6 * 659^6 * 661^6 * 673^5 * 677^5 * 683^5 * 691^5 * 701^5 * 709^5 * 719^5 * 727^5 * 733^5 * 739^5 * 743^5 * 751^5 * 757^5 * 761^5 * 769^5 * 773^5 * 787^5 * 797^5 * 809^4 * 811^4 * 821^4 * 823^4 * 827^4 * 829^4 * 839^4 * 853^4 * 857^4 * 859^4 * 863^4 * 877^4 * 881^4 * 883^4 * 887^4 * 907^4 * 911^4 * 919^4 * 929^4 * 937^4 * 941^4 * 947^4 * 953^4 * 967^4 * 971^4 * 977^4 * 983^4 * 991^4 * 997^4 * 1009^3 * 1013^3 * 1019^3 * 1021^3 * 1031^3 * 1033^3 * 1039^3 * 1049^3 * 1051^3 * 1061^3 * 1063^3 * 1069^3 * 1087^3 * 1091^3 * 1093^3 * 1097^3 * 1103^3 * 1109^3 * 1117^3 * 1123^3 * 1129^3 * 1151^3 * 1153^3 * 1163^3 * 1171^3 * 1181^3 * 1187^3 * 1193^3 * 1201^3 * 1213^3 * 1217^3 * 1223^3 * 1229^3 * 1231^3 * 1237^3 * 1249^3 * 1259^3 * 1277^3 * 1279^3 * 1283^3 * 1289^3 * 1291^3 * 1297^3 * 1301^3 * 1303^3 * 1307^3 * 1319^3 * 1321^3 * 1327^3 * 1361^2 * 1367^2 * 1373^2 * 1381^2 * 1399^2 * 1409^2 * 1423^2 * 1427^2 * 1429^2 * 1433^2 * 1439^2 * 1447^2 * 1451^2 * 1453^2 * 1459^2 * 1471^2 * 1481^2 * 1483^2 * 1487^2 * 1489^2 * 1493^2 * 1499^2 * 1511^2 * 1523^2 * 1531^2 * 1543^2 * 1549^2 * 1553^2 * 1559^2 * 1567^2 * 1571^2 * 1579^2 * 1583^2 * 1597^2 * 1601^2 * 1607^2 * 1609^2 * 1613^2 * 1619^2 * 1621^2 * 1627^2 * 1637^2 * 1657^2 * 1663^2 * 1667^2 * 1669^2 * 1693^2 * 1697^2 * 1699^2 * 1709^2 * 1721^2 * 1723^2 * 1733^2 * 1741^2 * 1747^2 * 1753^2 * 1759^2 * 1777^2 * 1783^2 * 1787^2 * 1789^2 * 1801^2 * 1811^2 * 1823^2 * 1831^2 * 1847^2 * 1861^2 * 1867^2 * 1871^2 * 1873^2 * 1877^2 * 1879^2 * 1889^2 * 1901^2 * 1907^2 * 1913^2 * 1931^2 * 1933^2 * 1949^2 * 1951^2 * 1973^2 * 1979^2 * 1987^2 * 1993^2 * 1997 * 1999 * 2003 * 2011 * 2017 * 2027 * 2029 * 2039 * 2053 * 2063 * 2069 * 2081 * 2083 * 2087 * 2089 * 2099 * 2111 * 2113 * 2129 * 2131 * 2137 * 2141 * 2143 * 2153 * 2161 * 2179 * 2203 * 2207 * 2213 * 2221 * 2237 * 2239 * 2243 * 2251 * 2267 * 2269 * 2273 * 2281 * 2287 * 2293 * 2297 * 2309 * 2311 * 2333 * 2339 * 2341 * 2347 * 2351 * 2357 * 2371 * 2377 * 2381 * 2383 * 2389 * 2393 * 2399 * 2411 * 2417 * 2423 * 2437 * 2441 * 2447 * 2459 * 2467 * 2473 * 2477 * 2503 * 2521 * 2531 * 2539 * 2543 * 2549 * 2551 * 2557 * 2579 * 2591 * 2593 * 2609 * 2617 * 2621 * 2633 * 2647 * 2657 * 2659 * 2663 * 2671 * 2677 * 2683 * 2687 * 2689 * 2693 * 2699 * 2707 * 2711 * 2713 * 2719 * 2729 * 2731 * 2741 * 2749 * 2753 * 2767 * 2777 * 2789 * 2791 * 2797 * 2801 * 2803 * 2819 * 2833 * 2837 * 2843 * 2851 * 2857 * 2861 * 2879 * 2887 * 2897 * 2903 * 2909 * 2917 * 2927 * 2939 * 2953 * 2957 * 2963 * 2969 * 2971 * 2999 * 3001 * 3011 * 3019 * 3023 * 3037 * 3041 * 3049 * 3061 * 3067 * 3079 * 3083 * 3089 * 3109 * 3119 * 3121 * 3137 * 3163 * 3167 * 3169 * 3181 * 3187 * 3191 * 3203 * 3209 * 3217 * 3221 * 3229 * 3251 * 3253 * 3257 * 3259 * 3271 * 3299 * 3301 * 3307 * 3313 * 3319 * 3323 * 3329 * 3331 * 3343 * 3347 * 3359 * 3361 * 3371 * 3373 * 3389 * 3391 * 3407 * 3413 * 3433 * 3449 * 3457 * 3461 * 3463 * 3467 * 3469 * 3491 * 3499 * 3511 * 3517 * 3527 * 3529 * 3533 * 3539 * 3541 * 3547 * 3557 * 3559 * 3571 * 3581 * 3583 * 3593 * 3607 * 3613 * 3617 * 3623 * 3631 * 3637 * 3643 * 3659 * 3671 * 3673 * 3677 * 3691 * 3697 * 3701 * 3709 * 3719 * 3727 * 3733 * 3739 * 3761 * 3767 * 3769 * 3779 * 3793 * 3797 * 3803 * 3821 * 3823 * 3833 * 3847 * 3851 * 3853 * 3863 * 3877 * 3881 * 3889 * 3907 * 3911 * 3917 * 3919 * 3923 * 3929 * 3931 * 3943 * 3947 * 3967 * 3989"

Input: decomp(3990) => Output: "2^3982 * 3^1991 * 5^995 * 7^663 * 11^396 * 13^330 * 17^247 * 19^221 * 23^180 * 29^141 * 31^132 * 37^109 * 41^99 * 43^94 * 47^85 * 53^76 * 59^68 * 61^66 * 67^59 * 71^56 * 73^54 * 79^50 * 83^48 * 89^44 * 97^41 * 101^39 * 103^38 * 107^37 * 109^36 * 113^35 * 127^31 * 131^30 * 137^29 * 139^28 * 149^26 * 151^26 * 157^25 * 163^24 * 167^23 * 173^23 * 179^22 * 181^22 * 191^20 * 193^20 * 197^20 * 199^20 * 211^18 * 223^17 * 227^17 * 229^17 * 233^17 * 239^16 * 241^16 * 251^15 * 257^15 * 263^15 * 269^14 * 271^14 * 277^14 * 281^14 * 283^14 * 293^13 * 307^12 * 311^12 * 313^12 * 317^12 * 331^12 * 337^11 * 347^11 * 349^11 * 353^11 * 359^11 * 367^10 * 373^10 * 379^10 * 383^10 * 389^10 * 397^10 * 401^9 * 409^9 * 419^9 * 421^9 * 431^9 * 433^9 * 439^9 * 443^9 * 449^8 * 457^8 * 461^8 * 463^8 * 467^8 * 479^8 * 487^8 * 491^8 * 499^7 * 503^7 * 509^7 * 521^7 * 523^7 * 541^7 * 547^7 * 557^7 * 563^7 * 569^7 * 571^6 * 577^6 * 587^6 * 593^6 * 599^6 * 601^6 * 607^6 * 613^6 * 617^6 * 619^6 * 631^6 * 641^6 * 643^6 * 647^6 * 653^6 * 659^6 * 661^6 * 673^5 * 677^5 * 683^5 * 691^5 * 701^5 * 709^5 * 719^5 * 727^5 * 733^5 * 739^5 * 743^5 * 751^5 * 757^5 * 761^5 * 769^5 * 773^5 * 787^5 * 797^5 * 809^4 * 811^4 * 821^4 * 823^4 * 827^4 * 829^4 * 839^4 * 853^4 * 857^4 * 859^4 * 863^4 * 877^4 * 881^4 * 883^4 * 887^4 * 907^4 * 911^4 * 919^4 * 929^4 * 937^4 * 941^4 * 947^4 * 953^4 * 967^4 * 971^4 * 977^4 * 983^4 * 991^4 * 997^4 * 1009^3 * 1013^3 * 1019^3 * 1021^3 * 1031^3 * 1033^3 * 1039^3 * 1049^3 * 1051^3 * 1061^3 * 1063^3 * 1069^3 * 1087^3 * 1091^3 * 1093^3 * 1097^3 * 1103^3 * 1109^3 * 1117^3 * 1123^3 * 1129^3 * 1151^3 * 1153^3 * 1163^3 * 1171^3 * 1181^3 * 1187^3 * 1193^3 * 1201^3 * 1213^3 * 1217^3 * 1223^3 * 1229^3 * 1231^3 * 1237^3 * 1249^3 * 1259^3 * 1277^3 * 1279^3 * 1283^3 * 1289^3 * 1291^3 * 1297^3 * 1301^3 * 1303^3 * 1307^3 * 1319^3 * 1321^3 * 1327^3 * 1361^2 * 1367^2 * 1373^2 * 1381^2 * 1399^2 * 1409^2 * 1423^2 * 1427^2 * 1429^2 * 1433^2 * 1439^2 * 1447^2 * 1451^2 * 1453^2 * 1459^2 * 1471^2 * 1481^2 * 1483^2 * 1487^2 * 1489^2 * 1493^2 * 1499^2 * 1511^2 * 1523^2 * 1531^2 * 1543^2 * 1549^2 * 1553^2 * 1559^2 * 1567^2 * 1571^2 * 1579^2 * 1583^2 * 1597^2 * 1601^2 * 1607^2 * 1609^2 * 1613^2 * 1619^2 * 1621^2 * 1627^2 * 1637^2 * 1657^2 * 1663^2 * 1667^2 * 1669^2 * 1693^2 * 1697^2 * 1699^2 * 1709^2 * 1721^2 * 1723^2 * 1733^2 * 1741^2 * 1747^2 * 1753^2 * 1759^2 * 1777^2 * 1783^2 * 1787^2 * 1789^2 * 1801^2 * 1811^2 * 1823^2 * 1831^2 * 1847^2 * 1861^2 * 1867^2 * 1871^2 * 1873^2 * 1877^2 * 1879^2 * 1889^2 * 1901^2 * 1907^2 * 1913^2 * 1931^2 * 1933^2 * 1949^2 * 1951^2 * 1973^2 * 1979^2 * 1987^2 * 1993^2 * 1997 * 1999 * 2003 * 2011 * 2017 * 2027 * 2029 * 2039 * 2053 * 2063 * 2069 * 2081 * 2083 * 2087 * 2089 * 2099 * 2111 * 2113 * 2129 * 2131 * 2137 * 2141 * 2143 * 2153 * 2161 * 2179 * 2203 * 2207 * 2213 * 2221 * 2237 * 2239 * 2243 * 2251 * 2267 * 2269 * 2273 * 2281 * 2287 * 2293 * 2297 * 2309 * 2311 * 2333 * 2339 * 2341 * 2347 * 2351 * 2357 * 2371 * 2377 * 2381 * 2383 * 2389 * 2393 * 2399 * 2411 * 2417 * 2423 * 2437 * 2441 * 2447 * 2459 * 2467 * 2473 * 2477 * 2503 * 2521 * 2531 * 2539 * 2543 * 2549 * 2551 * 2557 * 2579 * 2591 * 2593 * 2609 * 2617 * 2621 * 2633 * 2647 * 2657 * 2659 * 2663 * 2671 * 2677 * 2683 * 2687 * 2689 * 2693 * 2699 * 2707 * 2711 * 2713 * 2719 * 2729 * 2731 * 2741 * 2749 * 2753 * 2767 * 2777 * 2789 * 2791 * 2797 * 2801 * 2803 * 2819 * 2833 * 2837 * 2843 * 2851 * 2857 * 2861 * 2879 * 2887 * 2897 * 2903 * 2909 * 2917 * 2927 * 2939 * 2953 * 2957 * 2963 * 2969 * 2971 * 2999 * 3001 * 3011 * 3019 * 3023 * 3037 * 3041 * 3049 * 3061 * 3067 * 3079 * 3083 * 3089 * 3109 * 3119 * 3121 * 3137 * 3163 * 3167 * 3169 * 3181 * 3187 * 3191 * 3203 * 3209 * 3217 * 3221 * 3229 * 3251 * 3253 * 3257 * 3259 * 3271 * 3299 * 3301 * 3307 * 3313 * 3319 * 3323 * 3329 * 3331 * 3343 * 3347 * 3359 * 3361 * 3371 * 3373 * 3389 * 3391 * 3407 * 3413 * 3433 * 3449 * 3457 * 3461 * 3463 * 3467 * 3469 * 3491 * 3499 * 3511 * 3517 * 3527 * 3529 * 3533 * 3539 * 3541 * 3547 * 3557 * 3559 * 3571 * 3581 * 3583 * 3593 * 3607 * 3613 * 3617 * 3623 * 3631 * 3637 * 3643 * 3659 * 3671 * 3673 * 3677 * 3691 * 3697 * 3701 * 3709 * 3719 * 3727 * 3733 * 3739 * 3761 * 3767 * 3769 * 3779 * 3793 * 3797 * 3803 * 3821 * 3823 * 3833 * 3847 * 3851 * 3853 * 3863 * 3877 * 3881 * 3889 * 3907 * 3911 * 3917 * 3919 * 3923 * 3929 * 3931 * 3943 * 3947 * 3967 * 3989"
```

**_NOTES:_**

- the function is `decomp(n)` and should return the decomposition of `n!` into its prime factors in increasing order of the primes, as a string.
- factorial can be a very big number (`4000!` has `12674` digits, `n` can go from `300` to `4000`).

#

<br />

# Challenge 061 John and Ann sign up for Codewars

My solution -> *[061_john_and_ann_sign_up_for_codewars](061_john_and_ann_sign_up_for_codewars.py)*

## **_Task condition:_**

John and his wife Ann have decided to go to Codewars. On the first day Ann will do `one` kata and John - he wants to know how it is working - `0` kata.

Let us call `a(n)` - and `j(n)` - the number of katas done by Ann - and John - at day `n`. We have `a(0) = 1` and in the same manner `j(0) = 0`.

They have chosen the following rules:

- On day n the number of katas done by Ann should be `n` minus the number of katas done by John at day `t`, `t` being equal to the number of katas done by Ann herself at day `n - 1`
- On day `n` the number of katas done by John should be `n` minus the number of katas done by Ann at day `t`, `t` being equal to the number of katas done by John himself at day `n - 1`

Whoops! I think they need to lay out a little clearer exactly what there're getting themselves into!

Could you write:

- functions `ann(n)` and `john(n)` that return the list of the number of katas Ann/John does on the first `n` days;
- functions `sum_ann(n)` and `sum_john(n)` that return the total number of katas done by Ann/John on the first `n` days

### **_Examples_**

```
Input: john(11) => Output: [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]

Input: ann(6) => Output: [1, 1, 2, 2, 3, 3]

Input: sum_john(75) => Output: 1720

Input: sum_ann(115) => Output: 4070
```

**_NOTES:_**

- Keep an eye on performance.

#

<br />

# Challenge 062 Drunk friend

My solution -> *[062_drunk_friend](062_drunk_friend.py)*

## **_Task condition:_**

You're hanging out with your friends in a bar, when suddenly one of them is so drunk, that he can't speak, and when he wants to say something, he writes it down on a paper. However, none of the words he writes make sense to you. He wants to help you, so he points at a `beer` and writes `"yvvi"`. You start to understand what he's trying to say, and you write a script, that decodes his words.

Keep in mind that numbers, as well as other characters, can be part of the input, and you should keep them like they are. You should also test if the input is a string. If it is not, return `"Input is not a string"`.

### **_Examples_**

```
Input: decode("yvvi") => Output: "beer"

Input: decode("Blf zoivzwb szw 10 yvvih") => Output: "You already had 10 beers"

Input: decode("Ovg'h hdrn rm gsv ulfmgzrm!") => Output: "Let's swim in the fountain!"

Input: decode({"brand": "Starobrno" }) => Output: "Input is not a string"

Input: decode("Tl slnv, blf'iv wifmp") => Output: "Go home, you're drunk"

Input: decode("Hfiv r xzm wzmxv lm xlk'h xzi, slow nb yvvi") => Output: "Sure i can dance on cop's car, hold my beer"

Input: decode(True) => Output: "Input is not a string"

Input: decode("Hvv? R'n mlg gszg wifmp, rAn orderly trail of ants is marching across the park picnic area.

It looks something like this:

..ant..ant.ant...ant.ant..ant.ant....ant..ant.ant.ant...ant..

But suddenly there is a rumour that a dropped chicken sandwich has been spotted on the ground ahead. The ants surge forward! Oh No, it's an ant stampede!!

Some of the slower ants are trampled, and their poor little ant bodies are broken up into scattered bits.

The resulting carnage looks like this:

...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t

Can you find how many ants have died? xzm hgroo gzpv nb xolgsvh luu") => Output: "See? I'm not that drunk, i can still take my clothes off"

Input: decode(123) => Output: "Input is not a string"

Input: decode(["Beer"]) => Output: "Input is not a string"
```

#

<br />

# Challenge 063 Dead Ants

My solution -> *[063_dead_ants](063_dead_ants.py)*

## **_Task condition:_**

An orderly trail of ants is marching across the park picnic area.

It looks something like this:

```
..ant..ant.ant...ant.ant..ant.ant....ant..ant.ant.ant...ant..
```

But suddenly there is a rumour that a dropped chicken sandwich has been spotted on the ground ahead. The ants surge forward! Oh No, it's an ant stampede!!

Some of the slower ants are trampled, and their poor little ant bodies are broken up into scattered bits.

The resulting carnage looks like this:

```
...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t
```

Can you find how many ants have died?

### **_Examples_**

```
Input: dead_ant_count("ant ant ant ant") => Output: 0

Input: dead_ant_count("") => Output: 0

Input: dead_ant_count(" ") => Output: 0

Input: dead_ant_count("ant anantt aantnt") => Output: 2

Input: dead_ant_count("ant ant .... a nt") => Output: 1

Input: dead_ant_count("ant ant ant ant") => Output: 0

Input: dead_ant_count("") => Output: 0

Input: dead_ant_count(" ") => Output: 0

Input: dead_ant_count("ant anantt aantnt") => Output: 2

Input: dead_ant_count("ant ant .... a nt") => Output: 1

Input: dead_ant_count("antatn ant ant") => Output: 1

Input: dead_ant_count("ant a ant anatttt") => Output: 4

Input: dead_ant_count("antantantan") => Output: 1

Input: dead_ant_count("aaaaannnntttt") => Output: 5

Input: dead_ant_count("aaaannnnntttt") => Output: 5

Input: dead_ant_count("aaaannnnttttt") => Output: 5

Input: dead_ant_count("a n t") => Output: 1

Input: dead_ant_count("... .. ...") => Output: 0

Input: dead_ant_count("$$$ant..a") => Output: 1

Input: dead_ant_count(".n..tt.n.nt..t.ntant..aaaaa..tn.na.aaat..n..tn.ntan.t") => Output: 10

Input: dead_ant_count("ant ant .... a nt") => Output: 1
```

**_NOTES:_**

- When in doubt, assume that the scattered bits are from the same ant. e.g. 2 heads and 1 body = 2 dead ants, not 3.

#

<br />

# Challenge 064 Data compression using run-length encoding

My solution -> *[064_data_compression_using_run_length_encoding](064_data_compression_using_run_length_encoding.py)*

## **_Task condition:_**

`Run-length encoding` (`RLE`) is a very simple form of lossless data compression in which runs of data are stored as a single data value and count.

A simple form of `RLE` would encode the string `"AAABBBCCCD"` as `"3A3B3C1D"` meaning, first there are `3 A`, then `3 B`, then `3 C` and last there is `1 D`.

Your task is to write a `RLE` encoder and decoder using this technique. The texts to encode will always consist of only uppercase characters, no numbers.

### **_Examples_**

```
Input: encode("A") => Output: "1A"

Input: encode("AAA") => Output: "3A"

Input: encode("AB") => Output: "1A1B"

Input: encode("AAABBBCCCA") => Output: "3A3B3C1A"


Input: decode("1A") => Output: "A"

Input: decode("3A") => Output: "AAA"

Input: decode("1A1B") => Output: "AB"

Input: decode("3A3B3C1A") => Output: "AAABBBCCCA"


Input: encode(decode("10A1B")) => Output: "10A1B"

Input: encode(decode("1A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z")) => Output: "1A1B1C1D1E1F1G1H1I1J1K1L1M1N1O1P1Q1R1S1T1U1V1W1X1Y1Z"

Input: decode(encode("AAAAAAAAAAB")) => Output: "AAAAAAAAAAB"

Input: decode(encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) => Output: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

#

<br />

# Challenge 065 Coding 3min: Trypophobia

My solution -> *[065_coding_3min_trypophobia](065_coding_3min_trypophobia.py)*

## **_Task condition:_**

Unfortunately, you have trypophobia, You always want to clear up some of the things that have occurred many times.

Give you a number array(2D array) `arr`, remove the most common number in each subarray from that array.

If more than one numbers have same repeat times, remove all of them.

```
For a = [[3,3,3,3,3,3,3,3,3]], the output should be [[]]

Because 3 is the most common number.

For a = [[3,4,5],[4,4,4]], the output should be [[3,5],[]]

Because 4 is the most common number. Remove all 4 from each subarray.

For a = [[3,4,5],[3,4,5]], the output should be [[],[]]

Because 3,4,5 is the most common numbers, they all repeated 2 times. Remove all of them from each subarray.
```

### **_Examples_**

```
Input: sc([[3,3,3,3,3,3,3,3,3]]) => Output: [[]]

Input: sc([[3,3,3,3,3,3,3,3,3,4,5]]) => Output: [[4,5]]

Input: sc([[3,4,5]]) => Output: [[]]

Input: sc([[3,4,5],[3,4,5]]) => Output: [[],[]]

Input: sc([[3,4,5],[4,4,4]]) => Output: [[3,5],[]]

Input: sc([[3,4,4,5],[3,4,4,5],[3,4,4,5],[3,4,4,5]]) => Output: [[3,5],[3,5],[3,5],[3,5]]

Input: sc([[]]) => Output: [[]]

Input: sc([]) => Output: []
```

#

<br />