import hydra
from omegaconf import DictConfig
from data_preparation import get_data
from optimization import bayesian_optimization
from report import generate_report


@hydra.main(config_path="conf/config.yaml")
def run(cfg: DictConfig)-> None:
     
    # Getting data
    data = get_data(dataname=cfg.stock.name,period=cfg.grain.period)
    
    # Run optimization
    dct = bayesian_optimization(data,cfg)
    
    # Generate report 
    generate_report(dct,cfg)

if __name__ == "__main__":
    run()
    

    
