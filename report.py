
import pandas as pd 


def generate_report(dct,cfg):

    tmp=pd.read_csv('D:/Documents/Projetos/bot-dos-brother/results.csv')
    
    tmp1= pd.DataFrame({"stock":[cfg.stock.name],
                        "period":[cfg.grain.period],
                        "strategy":[dct['strategy']],
                        "params":[str(dct['params'])],
                        "target":[dct['target']]
                         })

    pd.concat([tmp,tmp1],ignore_index=True).to_csv('D:/Documents/Projetos/bot-dos-brother/results.csv',index=False)