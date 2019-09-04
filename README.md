# Recursive Bayes Filter
This is a simple example of estimating state x given observations y1, y2, ..., yn and a prior estimate u of state x in computer vision.

```
bayes_filter.py 
```
is to compute the mean value of the posterior combining all of the observations with the prior.

```
change_state.py 
```
is to change the above simulation so that x is no longer constant, but instead is a value that
changes as a function of time.

- testing:
```
main.py
```
Plot the value of the mean value of the posterior over time.
