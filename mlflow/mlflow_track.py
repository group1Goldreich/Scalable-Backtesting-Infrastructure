import mlflow
import mlflow.pyfunc

mlflow.set_tracking_uri("http://localhost:5001")


def track(strategy, start_date, end_date, start_cash, commission, params, drawdown):

        with mlflow.start_run():
            mlflow.log_param('Strategy', strategy)
            mlflow.log_param('Start date', start_date)
            mlflow.log_param('End date', end_date)
            mlflow.log_param('Start cash', start_cash)
            mlflow.log_param('Commission', commission)
            
            for key, value in params.items():
                mlflow.log_param(f'param_{key}', value)
            
            mlflow.log_metric('max_draw_down', drawdown.max.drawdown)