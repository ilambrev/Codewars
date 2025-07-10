# Challenge 001 Convert A Boolean To A String

My solution -> *[001ConvertABooleanToAString](001ConvertABooleanToAString.py)*

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

My solution -> *[002HelloNameOrWorld](002HelloNameOrWorld.py)*

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

My solution -> *[003ParseFloat](003ParseFloat.py)*

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

My solution -> *[004RemoveExclamationMarks](004RemoveExclamationMarks.py)*

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

My solution -> *[005IsItAPalindrome](005IsItAPalindrome.py)*

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

My solution -> *[006ThirdAngleOfATriangle](006ThirdAngleOfATriangle.py)*

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

My solution -> *[007InvertValues](007InvertValues.py)*

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

My solution -> *[008FindNumbersWhichAreDivisibleByGivenNumber](008FindNumbersWhichAreDivisibleByGivenNumber.py)*

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