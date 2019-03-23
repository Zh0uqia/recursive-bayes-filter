from __future__ import division



MEAN_LIST=[]

def bayes_filter(idx, y, true_x, prior_mean, p, eps_mean, q, n):
    i=idx
    return cal_mean(i, y, true_x, prior_mean, p, eps_mean, q, n)

def cal_mean(i, y, true_x, prior_mean, p, eps_mean, q, n):
    MEAN_LIST.append(prior_mean)
    cur_i=i
    y_i=y[cur_i]
    precision=p+q
    mean=(p*prior_mean+q*y_i)/precision

    if cur_i==n-1:
        return MEAN_LIST, mean

    print("bayes step {}:".format(i), "mean = {}".format(mean))
    cur_i+=1
    mean_list, mean_new=cal_mean(cur_i, y, true_x, mean, precision, eps_mean, q, n)

    return mean_list, mean_new



