race <- function (v1, v2, g) {
  time = g/(v2-v1)
  if(time <0){return(NULL)}
  else{return(c(floor(time), floor((time*60) %% 60), floor((time * 3600) %% 60)))}
}
