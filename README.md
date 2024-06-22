**Crypto Trading Engineering: Scalable Backtesting Infrastructure**
===========================================================

**Overview**
--------

This project aims to design and build a reliable, large-scale trading data pipeline for a startup called Mela, which wants to make it simple for everyone to enter the world of cryptocurrencies. The pipeline will enable investors to run backtests that simulate current and past particular situations as well as their trend over time.

**Business Need**
-------------

The startup wants to provide a reliable source of investment while lowering the risk associated with trading cryptocurrencies. To achieve this, a robust data pipeline is needed to run various backtests and store useful artifacts in a robust data warehouse system.

**Data**
-----

The project will use candlestick data from Yahoo Finance and Binance. Candlestick data is a type of financial data that represents the price action of a security over time.

**Expected Outcomes**
------------------

* A robust data pipeline that can run various backtests
* Storage of useful artifacts in a robust data warehouse system
* Skills in technical analysis, backtesting, trading, and data engineering
* Knowledge of financial prediction, movement prediction, and enterprise-grade data engineering

**Technical Requirements**
-------------------------

* Apache Airflow
* Apache Kafka
* MLflow
* CML
* Structured Streaming
* Data modeling techniques (Kimbal, DataVault, Immon data models, database normal forms (1NF, 2NF, 3NF, 4NF, 5NF))

**Tasks**
------

### Task 1: Backtesting

* Plan the flow of work and assign tasks
* Understand the difference between fundamental and technical analysis
* Run multiple backtests using different technical indicators and assets
* Generate important metrics from backtests (return, number of trades, winning trades, losing trades, max drawdown, Sharpe ratio)
* Create a dynamic scene that automates the run of backtests

### Task 2: Build Backend for Processing Requests

* Design SQL table schema to store scenes and backtests
* Create a Flask, FastAPI, or Node.js application to take in scenes and run backtests
* Create a module to check if backtest results for a specific range exist
* Create authentication handling backend for users to login

### Task 3: Integrate MLOps Tools into Your Workflow

* Use Kafka to receive scenes that contain hyperparameters of backtests
* Publish backtest results to Kafka
* Automate backtest runs using Airflow
* Integrate MLflow using the provided database as a remote store
* Integrate CML to run various backtests on algorithmic changes
* Use GitHub actions to run test cases on code change

### Task 4: Build Frontend for Running Backtests

* Build a frontend application for logged-in users to specify scene parameters and get backtest results

**Contributors**
------

- [Yohanes Teshome kebede](https://github.com/Yohanes213)
- [Eyerusalem Admassu](https://github.com/jadmassu)
- [Getachew Abebe](https://github.com/GetachewAbebe)
- [Mistir Nigusse](https://github.com/mistir-nigusse)
- [Abdelrhman Yasir](https://github.com/AB-y1)
