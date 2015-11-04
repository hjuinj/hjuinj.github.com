---
title: "Building R Package"
author: "hjuinj"
date: "29 October 2015"
output: html_document
---

The material is based on the book (available online) ***[R packages](http://r-pkgs.had.co.nz/)*** by Hadley Wickham.

# /R
All R code files are stored in this sub-dirctory. You cannot creat further sub-dirctories to store files for different purpose.

The difference between R scripts and a R package is that:

- In a script, code is run when it is loaded. In a package, code is run when it is built. This means your package code should only create objects, the vast majority of which will be functions.


- Functions in your package will be used in situations that you didn’t imagine. This means your functions need to be thoughtful in the way that they interact with the outside world.
If the behaviour of other functions differs before and after running your function, you’ve modified the landscape

### Coding convention to follow:
Use camel case for both function and variable names 