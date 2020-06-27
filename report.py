import os
import pandas as pd 

_file_path = os.path.dirname(os.path.abspath(__file__))

def generate_report(dct,cfg):
    
    if os.path.exists(_file_path +"/results.csv"):
        current_csv =pd.read_csv(_file_path +"/results.csv")
    
        tmp= pd.DataFrame({"stock":[cfg.stock.name],
                            "period":[cfg.grain.period],
                            "strategy":[dct['strategy']],
                            "params":[str(dct['params'])],
                            "target":[dct['target']]
                            })

        pd.concat([current_csv,tmp],ignore_index=True).to_csv(_file_path +"/results.csv",index=False)

    else:
        tmp= pd.DataFrame({"stock":[cfg.stock.name],
                    "period":[cfg.grain.period],
                    "strategy":[dct['strategy']],
                    "params":[str(dct['params'])],
                    "target":[dct['target']]
                    })

        tmp.to_csv(_file_path +"/results.csv",index=False)