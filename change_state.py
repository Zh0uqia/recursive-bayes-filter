from __future__ import division

MEAN_KALMAN_LIST=[]
def kalman_filter(x_kalman, idx, y_kalman, prior_mean, p, eps_mean, q, n, eps):
    i=idx
    return cal_kalman_mean(x_kalman, i, y_kalman, prior_mean, p, eps_mean, q, n, eps)

def cal_kalman_mean(x_kalman, i, y_kalman, prior_mean, p, eps_mean, q, n, eps):

    MEAN_KALMAN_LIST.append(prior_mean)

    cur_i=i
    y_kalman_i=y_kalman[cur_i]


    precision=p+q
    mean=(p*prior_mean+q*y_kalman_i)/precision

    y_update=x_kalman[cur_i]+eps[cur_i]
    y_kalman_list = y_kalman
    y_kalman_list.append(y_update)
    x_kalman_list = x_kalman
    x_kalman_list.append(x_kalman[cur_i] + 1)

    if cur_i==n-1:
        return y_kalman_list[0:int(n)], MEAN_KALMAN_LIST, mean

    print("kalman step {}:".format(i), "kalman mean = {}".format(mean))
    cur_i+=1

    y_list, mean_list, mean_new=cal_kalman_mean(x_kalman_list, cur_i, y_kalman_list, mean, precision, eps_mean, q, n, eps)

    return y_list, mean_list, mean_new