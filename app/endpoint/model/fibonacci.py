from pydantic import BaseModel


class GetFibOutput(BaseModel):
    fibonacci_sequence: list
