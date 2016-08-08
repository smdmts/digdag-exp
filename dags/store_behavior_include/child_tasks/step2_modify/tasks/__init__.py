class Step2Store(object):
  def modify(self):
    digdag.env.store({"parameter":"step_2_modify"})
