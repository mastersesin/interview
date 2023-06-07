import sqlalchemy
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from app.db.model.transaction import Transaction


class TransactionOperation:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_transactions(self) -> [Transaction]:
        query = select(Transaction)
        result = await self.db_session.execute(query)
        return [x[0].jsonify() for x in result.fetchall()]

    async def get_transactions_sum_group_by_user_id(self):
        query = select(
            Transaction.customer_id,
            sqlalchemy.func.sum(Transaction.amount)
        ).group_by(
            Transaction.customer_id
        )
        result = await self.db_session.execute(query)
        return [{'customer_id': x[0], 'amount': x[1]} for x in result.fetchall()]
