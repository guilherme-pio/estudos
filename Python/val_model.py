import time
import sklearn

def val_model(y_true, y_pred, model_name=None, print_parameters=False, print_time=False):
    """
    Traz algumas métricas principais de validação de um modelo de ML.
    
    Parameters
    ----------
    
    y_true : array, shape = [n_samples]
    Valores verdade do modelo.

    y_pred : array, shape = [n_samples]
    Valores estimados retornados pelo modelo.
    
    model_name : str
    Nome do modelo que retornará no print.
    
    print_parameters : boolean
    Se True, printa os parâmetros que compõem o modelo.
    
    print_time : boolean
    Se True, printa a hora em que a função foi rodada.
    """

    print('Accuracy', model_name, ':', '{percent:.4%}'.format(percent=round(sklearn.metrics.accuracy_score(y_true, y_pred),4)), '\n')
          
    for a, b in sklearn.metrics.confusion_matrix(y_true, y_pred):
        print(a, '	({:.0%})'.format(round(a /(a+b), 2)), ' ', b, '	({:.0%})'.format(round(b/(a+b), 2)))
        
    if print_parameters==True:    
        print('\n')
        for i in data.columns: print(i)
            
    if print_time==True:
        print('\n')
        print(time.ctime(time.time()), '\n')
