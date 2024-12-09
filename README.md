# SudoLang
## A language for absolute beginners

Sudo is a language based off pseudocode, to help enforce basic programming concepts like assignment, conditionals, and repetition.

The language is structured off a [simple language](https://augustine.myusa.cloud/perugini/AveMaria/teaching/courses/csci151/LectureNotes/pseudocodeLanguage.html) designed by [Dr. Saverio Perugini](https://saverio.carrd.co/) to teach these concepts to introductory students.


The reader may well say, "Just use Python, bro?"

Well, bro, there a number of reasons why a student's learning experience could be tainted by a language like Python. The primary reason is that Python is a "hodgepodge of a language" and tries to be too many things at once. Students often will miss the entire point of an assignment designed to help them think algorithmically, focusing instead on some shiny and obscure "syntactic sugar", of which Python is chock-full. For instance, Sudo limits arithmetic operations to those between the same type, avoiding weird expressions like `"Hello" * 100` (This excludes of course floats and ints).

Sudo removes this dangerous pitfall by providing a language stripped of any juicy language features, leaving a simple set of instructions to help new students formulate their ideas in to mechanical procedures.

# Basic Syntax

If you're already familar with programming, you might find Sudo mildly infuriating. There are no loops, no functions, and only primitive data types. The whole language can be broken down into five basic rules.

## 1. Let Statements

The Let Statement allows you to assign the output of an expression to a particular mneumonic representation of the expression. 


Syntax -> `let <mneumonic> be <expression>`

Examples:

```
let x be 5
let interest_rate be 0.14
let x be x + 1
let ratio be (x + 5 / interest_rate)
ratio
```

## 2. If Statements

The If Statement allows you to conditionally execute a line of code. The body of the statement will only execute if the expression evaluates to True.


Syntax -> `if <comparison expression>, then <statement(s)`

Examples:

```
let a be 1

if a + 6 > 7, then
    let limit be "not too far"

if a - 6 <= 7, then let limit be 2.17

limit
```

## 3. If-Else Statements

The If-Else Statement simply provides alternative execution case for when the condition from an If statement evaluates False. 


Syntax -> `If <comparison expression>, then <statements(s)> else <statement(s)>`

Examples:
```
let a be "not too far"
let speed be 60
let score be 73

if limit != "not too far", then
    if speed == 60, then
        let score be 7009.56
else
    let answer be score - 75

score
answer
```


## 4. Return Statement

Return statements are used to simply return the value of a statement or expression.


Syntax -> `return <mneumonic`

Examples:
```
let wrong be 3
let right be 7

if wrong + wrong == right, then 
    return True
else
    return False
```

## 5. Goto Statements

TBD

