class ReleaseMemory:
 def __init__(self):self.events=[]
 def add(self,event):self.events.append(event)
 def snapshot(self):return list(self.events)
