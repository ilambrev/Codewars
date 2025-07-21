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

My solution -> *[014ReverseReverse](014ReverseReverse.py)*

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

My solution -> *[015FindTheNthOccurrenceOfAWordInAString](015FindTheNthOccurrenceOfAWordInAString.py)*

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

My solution -> *[016RemoveAllExclamationMarksFromTheEndOfWords](016RemoveAllExclamationMarksFromTheEndOfWords.py)*

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