import digdag

class Step1Store(object):
  def call_store():
    digdag.env.store({"parameter":"step_1_parameter"})
