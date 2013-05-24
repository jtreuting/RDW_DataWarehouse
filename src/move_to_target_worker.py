from udl2.W_move_to_target import explode_to_dims, explode_to_fact
from celery import chain
import argparse


def main():
    parser = argparse.ArgumentParser(description='Move to Target Worker')
    parser.add_argument("-b", "--batch_id", type=int, default=1369321935, help="Batch id")
    args = parser.parse_args()

    batch = {'batch_id': args.batch_id}

    result_uuid = chain(explode_to_dims.s(batch), explode_to_fact.s())()
    result_value = result_uuid.get()
    print(result_value)

if __name__ == '__main__':
    main()
