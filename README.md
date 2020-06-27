# A framework for optimizing trading strategies with Bayesian Optimization

![MKT](https://img.shields.io/badge/language-Python-orange.svg)

# Description

This repository contains a framework for optimiziging the possible parameters of a given trading strategy using Bayesian optimization.

It was used mainly three libraries:

- [backtrader](https://www.backtrader.com/): A feature-rich Python framework for backtesting and trading; 

- [Hydra](https://hydra.cc/docs/intro): The key feature used in this project is the ability to dynamically create a hierarchical configuration by composition and override it through config files and the command line.

- [Bayesian Optimization](https://github.com/fmfn/BayesianOptimization): This is a constrained global optimization package built upon bayesian inference and gaussian process, that attempts to find the maximum value of an unknown function in as few iterations as possible

- [backtrader_plotting](https://github.com/verybadsoldier/backtrader_plotting): Library to add extended plotting capabilities to backtrader. Currently the only available backend is [Bokeh](https://bokeh.org/).


The `SMACross` strategy was taken from backtrader examples documentation and slightly modified to demonstrate the capability of adding replay data using this framework.

# Features

- Reproducibility of experiments;
- Config management;
- Basic Logging;
- Simple and effective Performance Report;
- Parameters optimization through Bayesian Optimization;
- Interactive graphs using backtrader_plotting with Bokeh

# Environment configuration

The packages used to develop the project are listed in the `environment.yml` file. To reproduce the results and functionalities of the project you should install [Anaconda](https://anaconda.org) and set up the environment as explained in what follows. However, if you prefer you can also create your enviroment using `pip env` and install the required libraries listed on the file.

## Conda env

Once you have installed Anaconda and download/cloned the repository, open a terminal and go to the directory of the project.

```
$ cd .../backtrader_hydra_bayesian_op

```

After that run the following command to create the conda environment with the required packages.

```
$ conda env create -f environment.yml

```

Then activate your new environment using the following command :

```
$ conda activate bt_hydra_byo

```


# Running the example

Once you have installed and activated the conda env, just run the following command in the terminal for running an experiment with the default parameters described in `conf/config.yaml`.

```
$ python main.py

```
For this cenario, the results will be saved in folder `./outputs/..` . 

The second and more exciting option is to use the `multirun` feature of Hydra, in this case try using the following command:

```
$ python main.py --multirun stock=vale,bbdc grain=daily,hour

```

The above comand will optimize the strategy parameters for VALE3.sa,BBDC4.sa stocks considering two sets of multiframes for trading and evaluation of parameters: hour-daily, daily-weekly. The results of each iteration will be automatically saved in the directories in folder `./multirun/..`.

The important part is the concepts behind the framework, you can take the main idea of this example and adjust it according with your needs.

# Next Steps

- Implementing walking forward analysis;


Every feedback is welcomed.
