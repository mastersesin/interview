from fastapi import Query
from fastapi_pagination import Page, paginate

from app import fast_app, async_session
from app.db.op.transaction import TransactionOperation
from app.endpoint.model.transaction import GetTransactionOutput, GetTransactionSumGroupByOutput
from app.util.fibonacci import Fibonacci
from core.config import config


@fast_app.get("/fibonacci")
# Input validation built-in with fastapi
async def fibonacci(fib_position: int = Query(..., gt=config.FIB_SEQ_MIN, lt=config.FIB_SEQ_MAX)):
    """

    Method that handle fibonacci endpoint. Gt and lt stand for greater than less than it just a validation
    that make sure our users not go above our resource limit

    Args:
        fib_position (int): Minimum 0 Maximum 1000.

    Returns:
        json_response: Return a response contain fib sequence for our user.

    API Docs at : http://your_app_address:your_port/docs

    """
    fibo_instance_worker = Fibonacci(fib_position)
    return {"fibonacci_sequence": [x for x in fibo_instance_worker]}


@fast_app.get("/transactions", response_model=Page[GetTransactionOutput])
# Input validation built-in with fastapi
async def transactions():
    # TODO: We already implement pagination by adding page and size but still can
    #  make it better by provide next_page_token so client dont have to manually
    #  process queue
    """
    Method that handle a pagination of all transactions

    Args:
        page (int): Which page of a pagination result you want to view
        size (int): Size of each page

    Returns:
        json_response: Return a response contain fib sequence for our user.

    API Docs at : http://your_app_address:your_port/docs

    """
    async with async_session() as session:
        async with session.begin():
            transaction_instance = TransactionOperation(session)
            return paginate(await transaction_instance.get_transactions())


@fast_app.get("/transaction/amount", response_model=Page[GetTransactionSumGroupByOutput])
# Input validation built-in with fastapi
async def transaction_amount():
    # TODO: We already implement pagination by adding page and size but still can
    #  make it better by provide next_page_token so client dont have to manually
    #  process queue
    """
    Method that handle a sum group by that show us total amount of each user by their user_id

    Args:
        page (int): Which page of a pagination result you want to view
        size (int): Size of each page

    Returns:
        json_response: Return a response contain customer_id and mount their spend.

    API Docs at : http://your_app_address:your_port/docs

    """
    async with async_session() as session:
        async with session.begin():
            transaction_instance = TransactionOperation(session)
            return await transaction_instance.get_transactions_sum_group_by_user_id()
