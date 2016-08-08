import digdag

class Step2Modify(object):
  def modify(self):
    digdag.env.store({"parameter":"step_2_modify"})
