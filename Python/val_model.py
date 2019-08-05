def cm(y_test, y_pred, model_name=None, print_parameters=False, print_time=False):

    print('Accuracy', model_name, ':', '{percent:.4%}'.format(percent=round(metrics.accuracy_score(y_test, y_pred),4)), '\n')
          
    for a, b in sklearn.metrics.confusion_matrix(y_test, y_pred):
        print(a, '	({:.0%})'.format(round(a /(a+b), 2)), ' ', b, '	({:.0%})'.format(round(b/(a+b), 2)))
        
    if print_parameters==True:    
        print('\n')
        for i in data.columns: print(i)
            
    if print_time==True:
        print('\n')
        print(time.ctime(time.time()), '\n')
