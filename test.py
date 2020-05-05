from sklearn.ensemble import RandomForestClassifier
import numpy as np
domainlist = []
class Domain:
  def __init__(self,_name,_label,_min,_max,_numip,_ipset);
  self.name = _name
  self.label = _label
  self.ttlmin = _min
  self.ttlmax = _max
  self.numip = _numip
  self.ipset = _ipset
  
  def returnData(self):
    return [self.ttlmin,self.ttlmax,self.numip]
  
  def returnLabel(self):
    if self.label == "good":
      return 0
    else:
      return 1
    
def initData(filename):
  
