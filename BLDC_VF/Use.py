#***************************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (UAntwerpen) <Bert.VanAcker@uantwerpen.be>
# *
# * This file is part of the vfWorks project.
# *
# * vfWorks can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **************************************************************************************
import time
import random
import serial
from vfworks.metamodels.validity_frame import *
from vfworks.utils.data.dataLoader import *
from vfworks.utils.model.modelLoader import *
#-------------------------LOAD EXISTING VF------------------------------------------------
VF = ValidityFrame(name="BLDC_VF", description="Populate BLDC_VF package",config="config.yaml",loadExistingVF=True,VFPackage="")

# 1 . Select model structure used for training
VF.setActiveModelStructure(name="anomalyDetector_2D")

#2. load the data to perform anomaly detection
_data_loader = DataLoader(name="VF_data_loader",validityframe=VF)
data_test = _data_loader.loadData(experimentLabel="anomaly",prefix="",type="numpy",shuffle=False)

#3. load the model
_model_loader = ModelLoader(name="VF_model_loader",validityFrame=VF)
_model_loader.loadModel(type="torch")
model = _model_loader.model

#4. use the model for single datapoint predictions + send to wio terminal for visualization
#ser = serial.Serial('COM6', 115200)
velocity_command = 100
model.n_features_in_ = 2
for datapoint in data_test:
    _input = [datapoint]
    prediction = model.predict(_input)
    anomaly_score = model.decision_function(_input)  # Higher = normal, Lower = anomaly
    label = "Anomaly" if prediction[0] == -1 else "Normal"
    print("Power usage:"+datapoint.__str__()+" prediction:"+label+" score: "+anomaly_score.__str__())  # (1 = anomaly, 0 = normal)

    anomaly = 1 if prediction[0] == -1 else 0
    certainty = 0.5 + random.random() * 0.5 # generate random certainty for monitoring purposes
    print("velCommand: " + str(velocity_command) + " Certainty: " + str(certainty))
    for monitor in VF.runtime_monitors:
        monitor.validate_point(certainty, "Certainty")
        monitor.validate_point(velocity_command, "velocityCommand")
        if monitor.status == StatusType.INVALID:
            print("WARNING: " + monitor.observes[0].feature + " is out of range")
    time.sleep(1)


