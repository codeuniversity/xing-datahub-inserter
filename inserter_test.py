import unittest
import json
import requests
import subprocess
import os
import time
import hive_handler
import hdfs_helpers
from build import protocol_pb2
from confluent_kafka import Producer

class EndpointTestCase(unittest.TestCase):
  def test_insertion(self):
    producer = Producer({'bootstrap.servers': 'localhost:9092'})
    local_path = 'datahub-data/'
    remote_path = '/datahub-data/inserter_test/'
    filename = 'inserter_test'
    try:
      os.makedirs(local_path)
    except FileExistsError:
      print('Path already exists')
    f = open(local_path + filename , mode='w')
    f.write('42;\n65;')
    f.close()
    hdfs_helpers.put_in_hdfs(remote_path+filename, local_path+filename)
    info = protocol_pb2.WrittenCSVInfo()
    info.filepath = remote_path + filename
    info.filename = filename
    info.recordType = 'target_users'
    msg = info.SerializeToString()
    producer.produce('written_files', msg)
    time.sleep(30)
    hash_arr = hive_handler.fetch_target_users()
    self.assertEqual(len(hash_arr),2)
    self.assertDictEqual(hash_arr[0], {'user_id':42})
    self.assertDictEqual(hash_arr[1], {'user_id':65})
time.sleep(3)
unittest.main()
