import os
import time
from generate import unreliably_generate_data


def check_env_vars():
    print("Checking env vars")
    env_vars = [
        'OUTPUT_BUCKET'
    ]

    for item in env_vars:
        if item not in os.environ:
            raise Exception("Required environment variable missing: {env_var}"
                            .format(env_var=item))


if __name__ == "__main__":
    check_env_vars()
    while True:
        time.sleep(3)
        unreliably_generate_data()
