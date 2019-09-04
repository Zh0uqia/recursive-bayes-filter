import bayes_filter
import visualize
import numpy as np
import change_state

TRUE_X=5.  # the true state value
PRIOR_MEAN=0.
PRIOR_STD=0.05 # sigma^2=25
EPS_MEAN=0.
EPS_STD=1.   # s^2=1
N=50.


np.random.seed(42)

def main():
    p=1./(PRIOR_STD**2)
    q=1./(EPS_STD**2)

    eps=np.random.normal(int(EPS_MEAN), int(EPS_STD), int(N))
    # x1=np.random.normal(int(PRIOR_MEAN), int(PRIOR_STD), 1)

    y=TRUE_X+eps

    y=np.array(y)

    idx=0
    mean_lst, mean_t=bayes_filter.bayes_filter(idx, y, TRUE_X, PRIOR_MEAN, p, EPS_MEAN, q, N)
    print('\n')

    y_kalman=[]
    y_kalman.append(TRUE_X+eps[0])
    x_kalman=[]
    x_kalman.append(TRUE_X)
    y_list, mean_kalman_lst, mean_kalman_t=change_state.kalman_filter(x_kalman, idx, y_kalman, PRIOR_MEAN, p, EPS_MEAN, q, N, eps)

    print("The final bayes mean is: {}".format(mean_t))
    print(mean_lst)
    print('\n')
    print("The final kalman mean is: {}".format(mean_kalman_t))
    print(mean_kalman_lst)
    visualize.plot_bayes_filter(TRUE_X, y, mean_lst)
    visualize.plot_kalman_filter(TRUE_X, y_list, mean_kalman_lst)


if __name__=="__main__":
    main()