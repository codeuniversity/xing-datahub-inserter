from hdfs import InsecureClient


def put_in_hdfs(hdfs_path, local_path):
    print('uploading...')
    client = InsecureClient('http://quickstart.cloudera:50070', user='cloudera')
    client.upload(hdfs_path=hdfs_path,
                  local_path=local_path,
                  progress=lambda x, y: print(x, y),
                  overwrite=True,
                  temp_dir='/tmp/{}'.format(local_path))
    print('done!')


def test():
    put_in_hdfs('/users/test', 'data/users.csv')
