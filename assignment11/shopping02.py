import time
import asyncio
from asyncio import Queue


class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    customers_processed = 0  # Counter to track the number of customers processed by the cashier
    total_checkout_time = 0  # Tracker for the total checkout time of all customers for this cashier

    while not queue.empty():
        customer: Customer = await queue.get()
        customers_processed += 1
        customer_start_time = time.perf_counter()
        print(f'The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}')

        # Track the total checkout time for each customer
        customer_checkout_time = 0
        for product in customer.products:
            print(f'The Cashier_{cashier_number} will checkout Customer_{customer.customer_id} '
                  f'Product_{product.product_name} in {product.checkout_time} secs')
            await asyncio.sleep(product.checkout_time)
            customer_checkout_time += product.checkout_time

        total_checkout_time += customer_checkout_time
        print(f'The Cashier_{cashier_number} finished checkout Customer_{customer.customer_id} '
              f'in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs')

        queue.task_done()

    # Print the total number of customers processed and total time taken by this cashier
    print(f"Cashier_{cashier_number} processed {customers_processed} customers.")
    print(f"Cashier_{cashier_number} total checkout time: {round(total_checkout_time, 2)} secs.")


def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)


async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id) for the_id in range(customer_count, customer_count + customers)]
        for customer in customers:
            print(f"Waiting to put customer_{customer.customer_id} in line...")
            await queue.put(customer)
            print(f"Customer_{customer.customer_id} put in line...")
        customer_count += len(customers)
        await asyncio.sleep(.001)
        return customer_count


async def main():
    customer_queue = Queue(5)
    customer_start_time = time.perf_counter()
    customer_producer = asyncio.create_task(customer_generation(customer_queue, 20))

    cashiers = [checkout_customer(customer_queue, i) for i in range(5)]

    await asyncio.gather(customer_producer, *cashiers)
    print('---------------------------------')
    print(f'The supermarket process finished {customer_producer.result()} customers '
          f'in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs')


if __name__ == "__main__":
    asyncio.run(main())
