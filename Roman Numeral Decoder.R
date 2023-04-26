library("tidyverse")

solution <- function(roman){
  # complete the solution by transforming the roman numeral into an integer
  # steps,  1) convert string to a series of numbers.
  # 2) evaluate subtraction rule
  # 3) sum across numbers

  Symbol <- c("I", "V", "X", "L", "C", "D", "M")
  Value <- c(1,5,10,50,100,500,1000)
  
  Tbl <- as.data.frame(cbind(Symbol, Value))
  Tbl$Value <- as.numeric(Tbl$Value)
  
  ROMANS <- unlist(strsplit(roman,""))
  
  ROMANS <- Tbl$Value[match(ROMANS, Tbl$Symbol)]
  
  a <- c(ROMANS, NA)
  b <- c(NA, ROMANS)
  c <- ifelse(a-b > 0, a-b, NA)
  d <- c(c[-1], NA)
  
  sol <- ifelse(is.na(c)*is.na(d), a, c)
  
  return(sum(sol, na.rm = TRUE))
}