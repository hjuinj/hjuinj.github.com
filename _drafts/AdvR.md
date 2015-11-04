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