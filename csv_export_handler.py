import hdfs_helpers
import hive_handler
import os
import hive_handler

class ExportHandler(object):
  def __init__(self, name = 'users', schema_string = hive_handler.user_schema_string):
    self.name = name
    self.schema_string = schema_string

  def commit(self, filepath, filename):
    try:
      remote_location = self.name + "/{}b/data".format(filename)
      hdfs_helpers.put_in_hdfs(remote_location, filepath)
      self._handle_tables(filename)
      # TODO: remove csv file from hdfs too
      os.remove(filepath)
    except Exception as err:
      print(err)

  def _handle_tables(self, filename):
    hive_handler.create_csv_table(filename, self.name, self.schema_string)
    hive_handler.insert_from_table(self.name, filename)
    hive_handler.drop_table(filename)

