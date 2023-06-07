from starlette.testclient import TestClient

from app import fast_app


class TestAPITransaction:
    API_TEST_CLIENT = TestClient(fast_app)

    def test_normal_integer_input(self):
        response = self.API_TEST_CLIENT.get("/transactions")
        assert response.status_code == 200

    #TODO: Test pagniation method

    #TODO: Test pagniation method wrong input validation

    #TODO: Test sum group by method

