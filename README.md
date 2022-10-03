# CrawlData
## Download all city 3D model from internet to local
> Step to do 
  - Clone this code 
  - Check all ID of model need download in object_id.txt
  - Check libraries must install i requirments.txt
  - Run code comandline: python main.py
  - With default code, we will create data folder to save all file downloaded through id object
  - Logs of project will save in logs.json with format:
        - "DONE__object_id": success to download
        - "ERROR__object_id": faild to download

> Data Folder Structure:
All data will save in data/ folder
-  With each object ID we will save 3 files - .obj, .json, .png
-  .obj save shape model
-  .json save all static information of model
-  .png save all texture