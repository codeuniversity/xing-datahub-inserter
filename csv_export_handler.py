import hdfs_helpers
import hive_handler
import os

class ExportHandler(object):
  def __init__(self, name = 'users', schema_string = hive_handler.user_schema_string):
    self.name = name
    self.schema_string = schema_string

  def commit(self, filepath, filename):
    try:
      self._handle_tables(filename, filepath)
    except Exception as err:
      print(err)

  def _handle_tables(self, filename, path):
    only_path_components = path.split('/')[:-1]
    only_path = '/'.join(only_path_components)
    hive_handler.create_csv_table(filename, only_path, self.schema_string)
    hive_handler.insert_from_table(self.name, filename)
    hive_handler.drop_table(filename)

