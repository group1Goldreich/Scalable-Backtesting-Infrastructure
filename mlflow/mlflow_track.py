import mlflow
import mlflow.pyfunc

mlflow.set_tracking_uri("http://localhost:5001")


def track(name, strategy, start_date, end_date, start_cash, commission, params, metrics):

        with mlflow.start_run():
            mlflow.log_param('Coin Name', name)
            mlflow.log_param('Strategy', strategy)
            mlflow.log_param('Start date', start_date)
            mlflow.log_param('End date', end_date)
            mlflow.log_param('Start cash', start_cash)
            mlflow.log_param('Commission', commission)
            
            for key, value in params.items():
                mlflow.log_param(f'param_{key}', value)
            
            for key, value in metrics.items():
                 mlflow.log_metric(f'metric_ {key}', value)