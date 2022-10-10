from pathlib import Path 
from functools import reduce 
import pandas as pd 
import csv 

# %cd /app 
def fullpath(*path):
  root = Path(".")
  full = reduce(lambda a, b: Path(a) / Path(b), path, root)
  return full.resolve().absolute()
def ensure_dir(*path):
  dirname = fullpath(*path)
  dirname.mkdir(parents=True, exist_ok=True)
  return dirname 

class dotdict(dict):
  def __getattr__(self, name):
    return self.get(name)
  def __setattr__(self, name, value):
    self[name] = value 
  def dict(self):
    return dict(self)
  def __dict__(self):
    return dict(self)

def save_csv(df, filename, encoding="utf-8_sig", index=False, **kwargs):
  return df.to_csv(filename, encoding=encoding, index=index, **kwargs)

def load_csv(filename, encoding="utf-8_sig", **kwargs):
  filename = fullpath(filename)
  df.to_csv(filename, encoding=encoding, **kwargs)
  return df

"""
filename = ensure_dir("csv") / "test.csv"
kwargs = dict()
df = pd.DataFrame([dotdict(id=x, name=f"name of {x: >5}").dict() for x in range(100)])
save_csv(df, filename)
load_csv(filename)
"""