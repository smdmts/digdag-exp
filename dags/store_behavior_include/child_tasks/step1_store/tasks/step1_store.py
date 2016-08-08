import digdag

class Step1Store(object):
  def call_store(self):
    digdag.env.store({"parameter":"step_1_parameter"})
