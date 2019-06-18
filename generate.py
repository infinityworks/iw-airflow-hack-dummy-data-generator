import csv
import json
import boto3
import os
import random
import string
import datetime as dt
import numpy as np


def unreliably_generate_data():
    rand = np.random.randint(low=1, high=100)

    if rand <= 15:
        generate_dummy_data()
    else:
        generate_garbage_data()


def generate_garbage_data():
    with open("garbage.json", 'w+') as file:
        letters = string.ascii_lowercase
        file.write(''.join(random.choice(letters) for i in range(3000)))

    s3_client = boto3.client('s3')
    bucket_name = os.getenv("OUTPUT_BUCKET")
    s3_client.Bucket(bucket_name)\
        .upload_file("garbage.json", str(dt.datetime.now()))

    os.remove("garbage.json")


def generate_dummy_data():
    num_transactions = np.random.randint(low=1, high=50)

    with open("file.json", 'w+') as file:
        for i in range(num_transactions):
            transaction = json.dumps(generate_dummy_customer_transaction_data())
            file.write(transaction)

    s3_client = boto3.client('s3')
    bucket_name = os.getenv("OUTPUT_BUCKET")
    s3_client.Bucket(bucket_name)\
        .upload_file("file.json", str(dt.datetime.now()))

    os.remove("file.json")


def generate_dummy_customer_transaction_data():
    products = read_products_data()

    dummy_transaction = {
        "customer_id": "",
        "basket": []
    }

    customer_id = "C{cust_id}".format(cust_id=np.random.randint(low=1, high=300))
    dummy_transaction["customer_id"] = customer_id

    num_products_bought = np.random.randint(low=1, high=10)

    for i in range(num_products_bought):
        random_product_index = np.random.randint(low=1, high=64)
        product = products[random_product_index]
        dummy_transaction["basket"].append(product)

    return dummy_transaction


def read_products_data():
    with open('products.csv') as file:
        reader = csv.DictReader(file)
        products = list(reader)
        return products


if __name__ == "__main__":
    generate_dummy_data()
