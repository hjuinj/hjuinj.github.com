---
title: "Advanced R Notes"
author: "hjuinj"
date: "29 October 2015"
output: html_document
---

#Data Structures
Additional attributes can be defined such as follows. But all these add-on attributes are lost after manipulating the object. 
The only unchanged attr are name, type and dimension.
```{r}

structure(1:10, attributes = "this is a vector")

```


Arrays are high dimensional 'matrices'
```{r}
a <- array(data = 1:12, dim = c(2,3,2))

aperm(a) #generalised transpose of array

# supress automatic turning of strings into factors
df <- data.frame(
  x = 1:3,
  y = c("a", "b", "c"),
  stringsAsFactors = FALSE)
str(df)

dfl <- data.frame(x = 1:3, y = I(list(1:2, 1:3, 1:4)))
str(dfl)

```


#Subsetting
There are preserving and simplifying way of subsetting. The former returns an object of the same type as the input.
The latter returns different output depending on input.

Factor: drops any unused levels.
```{r]}
z <- factor(c("a", "b"))
z[1]
#> [1] a
#> Levels: a b
z[1, drop = TRUE]
#> [1] a
#> Levels: a
```

Matrix or array: if any of the dimensions has length 1, drops that dimension.
```{r]}
a <- matrix(1:4, nrow = 2)
a[1, , drop = FALSE]
#>      [,1] [,2]
#> [1,]    1    3
a[1, ]
#> [1] 1 3
```

Data frame: if output is a single column, returns a vector instead of a data frame.
```{r}
df <- data.frame(a = 1:2, b = 1:2)
str(df[1])
#> 'data.frame':    2 obs. of  1 variable:
#>  $ a: int  1 2
str(df[[1]])
#>  int [1:2] 1 2
str(df[, "a", drop = FALSE])
#> 'data.frame':    2 obs. of  1 variable:
#>  $ a: int  1 2
str(df[, "a"])
#>  int [1:2] 1 2
```

A lot more subsetting with dataframe at the **Applications** section which might come in handy


# Functions
the `body(FUN)` functions prints the body of the function, `formal()` and `enviroment()` work similarly
> Lexical scoping looks up symbol values based on how functions were nested when they were created, not how they are nested when they are called.

Each function call is completely independent to its past calls, `codetools::findGlobals(FUN)` finds all the variables and functions the particular function FUN relies on in the global environment

All operators are masked/overloaded functions, for example:
```{r}
x <- 10; y <- 5
x + y
#> [1] 15
`+`(x, y)
#> [1] 15

for (i in 1:2) print(i)
#> [1] 1
#> [1] 2
`for`(i, 1:2, print(i))
#> [1] 1
#> [1] 2

if (i == 1) print("yes!") else print("no.")
#> [1] "no."
`if`(i == 1, print("yes!"), print("no."))
#> [1] "no."

x[3]
#> [1] NA
`[`(x, 3)
#> [1] NA

{ print(1); print(2); print(3) }
#> [1] 1
#> [1] 2
#> [1] 3
`{`(print(1), print(2), print(3))
#> [1] 1
#> [1] 2
#> [1] 3
```

All user defined infix functions must be wrapped by '%'

> Replacement functions act like they modify their arguments in place, and have the special name xxx<-. They typically have two arguments (x and value), although they can have more, and they must return the modified object. For example, the following function allows you to modify the second element of a vector:

```{r]}
`second<-` <- function(x, value) {
  x[2] <- value
  x
}
x <- 1:10
second(x) <- 5L
x
#>  [1]  1  5  3  4  5  6  7  8  9 10
```
This creats a new copy that replaces the old object.
`library(pryr)`'s `address` function shows memory address



# OOP


#FP

```{r}
summary <- function(x) {
  funs <- c(mean, median, sd, mad, IQR)
  lapply(funs, function(f) f(x, na.rm = TRUE))
}
```
### closures
functions made by other functions. Closures are described in the next section.
> “An object is data with functions. A closure is a function with data.”

Closures get their name because they enclose the environment of the parent function and can access all its variables. This is useful because it allows us to have two levels of
parameters: a parent level that controls operation and a child level that does the work.

```{r}
power <- function(exponent) {
  function(x) {
    x ^ exponent
  }
}

square <- power(2)
square(2)
#> [1] 4
square(4)
#> [1] 16

cube <- power(3)
cube(2)
#> [1] 8
cube(4)
#> [1] 64


simple_tag <- function(tag) {
  force(tag)
  function(...) {
    paste0("<", tag, ">", paste0(...), "</", tag, ">")
  }
}
tags <- c("p", "b", "i")
html <- lapply(setNames(tags, tags), simple_tag)
```
I’ve put the functions in a list because I don’t want them to be available all the time. The risk of a conflict between an existing R function and an HTML tag is high. But keeping them in a list makes code more verbose:
```{r}
html$p("This is ", html$b("bold"), " text.")
#> [1] "<p>This is <b>bold</b> text.</p>"
```
Depending on how long we want the effect to last, you have three options to eliminate the use of html$:

For a very temporary effect, you can use with():

```{r}
with(html, p("This is ", b("bold"), " text."))
#> [1] "<p>This is <b>bold</b> text.</p>"
```
For a longer effect, you can attach() the functions to the search path, then detach() when you’re done:

```{r}
attach(html)
p("This is ", b("bold"), " text.")
#> [1] "<p>This is <b>bold</b> text.</p>"
detach(html)
```
Finally, you could copy the functions to the global environment with list2env(). You can undo this by deleting the functions after you’re done.

```{r}
list2env(html, environment())
#> <environment: R_GlobalEnv>
p("This is ", b("bold"), " text.")
#> [1] "<p>This is <b>bold</b> text.</p>"
rm(list = names(html), envir = environment())
```


sapply() is a thin wrapper around lapply() that transforms a list into a vector in the final step. vapply() is an implementation of lapply() that assigns results to a vector (or matrix) of appropriate type instead of as a list. 