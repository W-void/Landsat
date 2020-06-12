import numpy as np 


def npy2tex(arr):
    # arr = np.load(path)
    arr = arr[:8]
    arr = arr.T
    l = []
    l.append([a for a in arr[1]/arr[0]] + [arr[1].sum()/arr[0].sum()]) #acc
    l.append(np.array([a for a in arr[2]/arr[3]] + [arr[2].sum()/arr[3].sum()])) #rec.
    l.append([a for a in arr[2]/arr[4]] + [arr[2].sum()/arr[4].sum()]) #prec.
    l.append(a for a in 2*l[1]*l[2]/(l[1]+l[2])) #f1    
    name = ['Acc  ', 'Rec. ', 'Prec.', 'F1   ']
    for i, eval in enumerate(l):
        print('&%s'%name[i], end=' ')
        for e in eval:
            print('&%.2f'%(e*100), end=' ')
        print("\\\\")


if __name__ == '__main__':
    arr = np.load('./log/qaEvalArray_region.npy')
    npy2tex(arr)