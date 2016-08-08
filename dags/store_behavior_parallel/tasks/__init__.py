import digdag

def prepare():
  digdag.env.store({"parameter": ["a","b","c"]})

def overwrite():
  digdag.env.store({"parameter": ["x","y","z"]})

def make_parameter(parameter , i):
  digdag.env.store({"parameter_in_method" : parameter[i] + "_" + str(i)})
