# recursive-bayes-filter
This is a simple example of estimating state x given observations y1, y2, ..., yN and a prior estimate u.

bayes_filter.py is to compute the mean value of the posterior combining all of the observations with the prior.

kalman_filter.py is to change the above simulation so that x is no longer constant, but instead is a value that
changes as a function of time.

By running main.py, you will see the plots of the mean value of the posterior.
