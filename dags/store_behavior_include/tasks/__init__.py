# -*- coding: utf-8 -*-
import digdag
import sys

path = [
  "child_tasks/step1_store/tasks"
]

sys.path.extend(path)

from step1_store import *

def load_env():
  digdag.env.store({
    "RDS_USER": "ABC",
    "RDS_PASSWORD": "EFG"
  })
