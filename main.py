import os
import time
import schedule
import threading


def check_env_vars():
    print("Checking env vars")
    env_vars = [
        'OUTPUT_BUCKET'
    ]

    for item in env_vars:
        if item not in os.environ:
            raise Exception("Required environment variable missing: {env_var}".format(env_var=item))


def job():
    print("I'm running on thread %s" % threading.current_thread())


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(5).seconds.do(run_threaded, job)

if __name__ == "__main__":
    check_env_vars()
    while True:
        schedule.run_pending()
        time.sleep(1)
