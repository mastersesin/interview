from pydantic import BaseModel


class GetTransactionOutput(BaseModel):
    transaction_id: int
    customer_id: int
    amount: float


class GetTransactionSumGroupByOutput(BaseModel):
    customer_id: int
    amount: float
