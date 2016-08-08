# -*- coding: utf-8 -*-
import digdag
import sys

path = [
  "child_tasks/step1_store/tasks",
  "child_tasks/step2_modify/tasks",
  "child_tasks/step3_check/tasks"
]

sys.path.extend(path)

from step1_store import *
from step2_modify import *
from step3_check import *

def load_env():
  digdag.env.store({
    "RDS_USER": "ABC",
    "RDS_PASSWORD": "EFG"
  })
