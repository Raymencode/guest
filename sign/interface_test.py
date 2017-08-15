# -*- coding: utf-8 -*-

import requests
import unittest


class GetEventListTest(unittest.TestCase):

#查询发布会接口
    def setUp(self):
       self.url = "http://127.0.0.1:8000/api/get_event_list"

    def test_get_event_null(self):
        #发布会id为空

        r = requests.get(self.url,params={'eid':''})
        result = r.json()
        print (result)
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")

    def test_get_event_success(self):
        #发布会id为1查询成功
        r = requests.get(self.url,params={'eid': '1'})
        result = r.json()
        print (result)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "success")
        self.assertEqual(result['data']['name'],"小米5发布会".decode('utf-8'))
        self.assertEqual(result['data']['address'],"上海中心" .decode('utf-8'))
        self.assertEqual(result['data']['limit'],1000)
        self.assertEqual(result['data']['start_time'], "2017-07-31T06:00:00")
        self.assertTrue(result['data']['status'])



class GetGuestListTest(unittest.TestCase):
    ''' 获得嘉宾列表 '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/get_guest_list/"

    def tearDown(self):
        print(self.result)

    def test_get_guest_list_eid_null(self):
        ''' eid 参数为空 '''
        r = requests.get(self.base_url, params={'eid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'eid cannot be empty')

    def test_get_event_list_eid_error(self):
        ''' 根据 eid 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid':901})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid':1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data'][0]['realname'],'jack')
        self.assertEqual(self.result['data'][0]['phone'],'13600000001')

    def test_get_event_list_eid_phone_null(self):
        ''' 根据 eid 和phone 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid':1,'phone':'10000000000'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_phone_success(self):
        ''' 根据 eid 和phone 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid':1,'phone':'13600000001'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['realname'],'jack')
        self.assertEqual(self.result['data']['phone'],'13600000001')


if __name__ == '__main__':
   # test_data.init_data() # 初始化接口测试数据
    unittest.main()
