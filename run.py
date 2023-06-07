import uvicorn

from app.endpoint.main import fast_app

if __name__ == '__main__':
    uvicorn.run(fast_app, port=1111, host='127.0.0.1')

# class A:
#     HIHI = []
#
#
# a = A()
# a.HIHI.append(1)
# b = A()
# print(b.HIHI)