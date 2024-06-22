import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_backend_request(start_date, end_date, strategy, params, start_cash, comm):
    message = {
        'start_date': start_date,
        'end_date': end_date,
        'strategy': strategy,
        'params': params,
        'start_cash': start_cash,
        'comm': comm
    }
    producer.send('backend_requests', value=message)
    producer.flush()

def send_backtest_results(metrics):
    message = {
        #'backtest_id': backtest_id,
        'metrics': metrics
    }
    producer.send('backtest_results', value=message)
    producer.flush()
