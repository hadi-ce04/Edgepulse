import random, time

class Device:
    def __init__(self, device_id, name, location):
        self.id=device_id; self.name=name; self.location=location
        self.temperature=random.uniform(30,45); self.vibration=random.uniform(.5,2)
        self.cpu=random.uniform(20,55); self.memory=random.uniform(30,65)
        self.latency=random.uniform(18,60); self.battery=random.uniform(70,100)
        self.status="online"; self.anomaly=False; self.alert=""; self.last_seen=time.time()

    def tick(self, fault=False):
        if fault:
            self.temperature+=random.uniform(2,5); self.vibration+=random.uniform(.4,1)
            self.cpu+=random.uniform(5,12); self.memory+=random.uniform(2,7)
            self.latency+=random.uniform(20,55); self.battery-=random.uniform(.4,1.5)
        else:
            self.temperature+=random.uniform(-1.2,1.2); self.vibration+=random.uniform(-.18,.18)
            self.cpu+=random.uniform(-5,5); self.memory+=random.uniform(-3,3)
            self.latency+=random.uniform(-8,8); self.battery-=random.uniform(.02,.12)
        self.temperature=max(15,min(100,self.temperature)); self.vibration=max(.1,min(12,self.vibration))
        self.cpu=max(5,min(100,self.cpu)); self.memory=max(10,min(100,self.memory))
        self.latency=max(5,min(300,self.latency)); self.battery=max(0,min(100,self.battery))
        self.last_seen=time.time()

    def as_dict(self):
        return {"id":self.id,"name":self.name,"location":self.location,
                "temperature":round(self.temperature,1),"vibration":round(self.vibration,2),
                "cpu":round(self.cpu,1),"memory":round(self.memory,1),
                "latency":round(self.latency,1),"battery":round(self.battery,1),
                "status":self.status,"anomaly":self.anomaly,"alert":self.alert}

class DeviceFleet:
    def __init__(self):
        self.devices=[
            Device("edge-001","Vision Node","Paris"),
            Device("edge-002","Robotics Node","Lyon"),
            Device("edge-003","Sensor Gateway","Grenoble"),
            Device("edge-004","Factory Node","Lille"),
            Device("edge-005","Autonomous Node","Toulouse"),
            Device("edge-006","Telemetry Node","Bordeaux")]
        self.fault_device=None

    def tick(self):
        for d in self.devices: d.tick(d.id==self.fault_device)
        return self.snapshot()

    def snapshot(self):
        return {"timestamp":time.time(),"devices":[d.as_dict() for d in self.devices]}
