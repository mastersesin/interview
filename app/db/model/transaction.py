import json

from sqlalchemy import Column, Integer, Float

from app import Base


# Implement class base transaction for ORM method
class Transaction(Base):
    __tablename__ = 'Transaction'

    transaction_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    amount = Column(Float)

    def __repr__(self):
        return "Transaction<{}>".format(self.transaction_id)

    def jsonify(self):
        return {
            'transaction_id': self.transaction_id,
            'customer_id': self.customer_id,
            'amount': self.amount
        }

    def jsonify_sum_group_by(self):
        return {
            'customer_id': self.customer_id,
            'amount': self.amount
        }

    def json_string(self):
        return json.dumps(self.jsonify())
