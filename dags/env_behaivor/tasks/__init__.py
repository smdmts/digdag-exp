# -*- coding: utf-8 -*-
import digdag
import sys

class MyWorkflow(object):
  def step1(self):
    print(digdag.env.params)
