from celery import Celery
import time

app = Celery("tasks", backend="redis://localhost", broker="redis://localhost")


@app.task()
def task():
    """
    This is Asyncio task
    :return: None
    """
    print("Started some work ......")
    time.sleep(4)
    print("Task Complete")