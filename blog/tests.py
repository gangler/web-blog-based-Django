from django.test import TestCase
from django.test.client import Client

class TestOne(TestCase):
    c = Client(HTTP_USER_AGENT='Mozilla/5.0')

    response = c.get('/post/new', data=None, follow=False, secure=False,
                     SECRET_KEY = '4-u4o0y1rqv0fc4925(2tpsx98^hz**e51ql7_!#$42bl-(@^&')
    # print(response)

t = TestOne()

# print("request:" + request)
# print("request body:" + request.body)
# print("request POST" + request.POST)
