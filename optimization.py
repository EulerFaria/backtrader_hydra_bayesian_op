import backtrader as bt
import datetime
import json
import logging 
import os

from bayes_opt import BayesianOptimization
from backtrader_plotting.schemes import Tradimo
from backtrader_plotting import Bokeh
from omegaconf import OmegaConf
from sma import SmaCross


logger = logging.getLogger(__name__)

tframes = dict(minute=bt.TimeFrame.Minutes,daily=bt.TimeFrame.Days, weekly=bt.TimeFrame.Weeks,
              monthly=bt.TimeFrame.Months)

_data = None
_cash = 10000
_commission =0.03
_replay_period= None
_strategy = None


def run_strat(**kwargs):
    # Instantiate Cerebro
    cerebro = bt.Cerebro()

    # Add data original timestamp 
    cerebro.adddata(_data)
    
    # Upsampling in case of need just uncomment the next line 
    cerebro.replaydata(_data,timeframe=tframes[_replay_period])    

    # Add strateg 
    cerebro.addstrategy(_strategy,**kwargs)

    # Set our desired cash start
    cerebro.broker.setcash(_cash)

    # Set the commission
    cerebro.broker.setcommission(commission=_commission)

    cerebro.run()

    return cerebro.broker.getvalue()


def save_plot(**kwargs):
    # Instantiate Cerebro
    cerebro = bt.Cerebro()

    # Add data original timestamp 
    cerebro.adddata(_data)
    
    # Upsampling in case of need just uncomment the next line 
    cerebro.replaydata(_data,timeframe=tframes[_replay_period])   

    # Add strateg 
    cerebro.addstrategy(_strategy,**kwargs)

    # Set our desired cash start
    cerebro.broker.setcash(_cash)

    # Set the commission
    cerebro.broker.setcommission(commission=_commission)

    cerebro.run()

    # Plot the result
    b = Bokeh(style='bar',scheme=Tradimo(),output_mode='save',filename='./best_iteration.html')
    cerebro.plot(b)

def bayesian_optimization(data,cfg):

    logger.info("Parameters optimization:")

    global _data 
    global _replay_period
    global _strategy 


    _data= data
    _replay_period= cfg.grain.replay

    stg_name=cfg.strategy.pop('name', None)
    
    if stg_name == 'sma':        
        params = OmegaConf.to_container(cfg.strategy,resolve=True) 
        _strategy = SmaCross 

    elif cfg.strategy.name =='ichimoku':
        # Implement your strateg in a separated file and then add
        # the option here 
        pass

    logger.info(f"Search space for optmization: {params}")
    
    st = datetime.datetime.now()
    
    optimizer = BayesianOptimization(
        f=run_strat,
        pbounds=params,
        random_state=1,
    )
    # The init_points and n_iter were randonmly chosen just for demonstration purposes
    # you should adjust it according with your needs. 
    # checkout the documentation (https://github.com/fmfn/BayesianOptimization)
    optimizer.maximize(
        init_points=3, 
        n_iter=6,
    )

    dt = (datetime.datetime.now() - st).total_seconds()//60 

    logger.info(f"Optmization finished in : {dt:.2f} seconds")

    # Dumping best parameters found
    with open(f"./{stg_name}.json", 'w') as fp:
        json.dump(optimizer.max, fp)

    # Logging out best result
    logger.info(f"Final Portfolio Value:{optimizer.max['target']:.2f}")

    res = {**optimizer.max,**{"strategy":stg_name}}
    
    # Saving bokeh html of best iteration
    save_plot(**optimizer.max['params'])

    return res
    