from starlette.testclient import TestClient

from app import fast_app
from app.util.fibonacci import Fibonacci
from core.config import config


class TestAPIFib:
    API_TEST_CLIENT = TestClient(fast_app)

    def test_normal_integer_input(self):
        response = self.API_TEST_CLIENT.get("/fibonacci?fib_position=8")
        assert response.status_code == 200
        assert response.json() == {'fibonacci_sequence': [0, 1, 1, 2, 3, 5, 8, 13]}

    def test_not_integer_input(self):
        response = self.API_TEST_CLIENT.get("/fibonacci?fib_position=aaaa")
        assert response.status_code == 422
        assert response.json() == {'detail': [
            {'loc': ['query', 'fib_position'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]
        }

    def test_special_character_input(self):
        response = self.API_TEST_CLIENT.get("/fibonacci?fib_position=##$@!@$")
        assert response.status_code == 422
        assert response.json() == {'detail': [
            {'loc': ['query', 'fib_position'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]
        }

    def test_gt_max_input(self):
        response = self.API_TEST_CLIENT.get("/fibonacci?fib_position=1001")
        assert response.status_code == 422
        assert response.json() == {'detail': [
            {'loc': ['query', 'fib_position'], 'msg': f'ensure this value is less than {config.FIB_SEQ_MAX}',
             'type': 'value_error.number.not_lt', 'ctx': {'limit_value': config.FIB_SEQ_MAX}}]
        }

    def test_lt_min_input(self):
        response = self.API_TEST_CLIENT.get("/fibonacci?fib_position=-1")
        assert response.status_code == 422
        assert response.json() == {'detail': [
            {'loc': ['query', 'fib_position'], 'msg': f'ensure this value is greater than {config.FIB_SEQ_MIN}',
             'type': 'value_error.number.not_gt', 'ctx': {'limit_value': config.FIB_SEQ_MIN}}]
        }


def test_fib_performance():
    # Since iterator need a loop to run
    # This testcase make sure cache mechanism work well
    fib_instance = Fibonacci(100)
    for _ in fib_instance:
        continue
    assert len(fib_instance.CACHE) == 100
    assert fib_instance.CACHE == {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55, 11: 89,
                                  12: 144, 13: 233, 14: 377, 15: 610, 16: 987, 17: 1597, 18: 2584, 19: 4181, 20: 6765,
                                  21: 10946, 22: 17711, 23: 28657, 24: 46368, 25: 75025, 26: 121393, 27: 196418,
                                  28: 317811, 29: 514229, 30: 832040, 31: 1346269, 32: 2178309, 33: 3524578,
                                  34: 5702887, 35: 9227465, 36: 14930352, 37: 24157817, 38: 39088169, 39: 63245986,
                                  40: 102334155, 41: 165580141, 42: 267914296, 43: 433494437, 44: 701408733,
                                  45: 1134903170, 46: 1836311903, 47: 2971215073, 48: 4807526976, 49: 7778742049,
                                  50: 12586269025, 51: 20365011074, 52: 32951280099, 53: 53316291173, 54: 86267571272,
                                  55: 139583862445, 56: 225851433717, 57: 365435296162, 58: 591286729879,
                                  59: 956722026041, 60: 1548008755920, 61: 2504730781961, 62: 4052739537881,
                                  63: 6557470319842, 64: 10610209857723, 65: 17167680177565, 66: 27777890035288,
                                  67: 44945570212853, 68: 72723460248141, 69: 117669030460994, 70: 190392490709135,
                                  71: 308061521170129, 72: 498454011879264, 73: 806515533049393, 74: 1304969544928657,
                                  75: 2111485077978050, 76: 3416454622906707, 77: 5527939700884757,
                                  78: 8944394323791464, 79: 14472334024676221, 80: 23416728348467685,
                                  81: 37889062373143906, 82: 61305790721611591, 83: 99194853094755497,
                                  84: 160500643816367088, 85: 259695496911122585, 86: 420196140727489673,
                                  87: 679891637638612258, 88: 1100087778366101931, 89: 1779979416004714189,
                                  90: 2880067194370816120, 91: 4660046610375530309, 92: 7540113804746346429,
                                  93: 12200160415121876738, 94: 19740274219868223167, 95: 31940434634990099905,
                                  96: 51680708854858323072, 97: 83621143489848422977, 98: 135301852344706746049,
                                  99: 218922995834555169026}
