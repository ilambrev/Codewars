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