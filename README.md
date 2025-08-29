# VFworks-demo

This repository contains the reference implementation and demonstration of **Validity Frames (VF)** for managing machine learning model lifecycle validity.
It includes the source code of the VFworks backend, a BLDC motor use case dataset, Docker setup for reproducibility, and example workflows used in the paper:
The `BLDC_VF` folder contains a complete validity frame for the BLDC motor use case as well as the workflows used to build the frame. The `vfworks` folder 
contains the Python implementation of the metamodels. 

---
## Getting started
### Requirements
1.  [Python3.11+](https://www.python.org/downloads/)
2.  [Docker](https://docs.docker.com/get-docker/)
3. [Docker Compose](https://docs.docker.com/compose/install/)
### Installation
Clone the repository and install dependencies
```bash
git clone https://github.com/Jan-Gladine/vfworks-demo.git
cd vfworks-demo
pip install -r requirements.txt
  ```
---
## Usage
### initialization
To initialize the validity frame, run
```bash
python BLDC_VF/populatePackage.py
```
This will populate the folder structure with the validity frame information concerning the model definition.
It can also retrieve training data from the Redis database and place it in the `BLDC_VF/Experiments` folder.
### Training
To train a model, run
```bash
python BLDC_VF/processes/train.py
```
This will open the model training GUI. Starting the workflow will execute the training process for the anomaly detection model.
In this example, the specifications are made in a way such that the workflow will return a warning of an incomplete dataset.
This can be changed in the specifications part of `BLDC_VF/populatePackage`.

### Deployment
Both `Use.py` and `deployed_use.py` allow to run the model alongside the validity frame. `deployed_use.py` requires a BLDC
setup to run correctly as it will use actual runtime data to operate. `Use.py` loads a known dataset and evaluate each point
using the model. Both will generate runtime monitors from the VF to show how this works.

---
## License

This project is licensed under the Apache License – see the [LICENSE](LICENSE) file for details.

---
## Future Work

* Extension to other ML tasks (classification, regression, deep learning).
* Add model evaluation
* Integration with benchmark datasets.

