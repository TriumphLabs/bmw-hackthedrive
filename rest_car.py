import requests
import json
evt_base_url = "http://data.api.hackthedrive.com:80/v1/Events"
vehicle_base_url = "http://data.api.hackthedrive.com:80/v1/Vehicles"
user="pwnrao"
pwd="welcomePA1"
MojioId="307630a0-5490-4def-9a0b-4bd42b83e52a"

car_ids = [996880,996881,996882,996883,996884,996885,996886,996887,996888,996889,996890,996891,996892,996893,996894,996895,996896,996897,996898,996899,996900,996901,996902,996903,996904]
car_type = [2,1,1,1,2,2,1,1,2,2,2,2,1,1,2,2,2,1,1,2,2,2,1,1,2]
car_rate = [2,1,2,2,2,2,1,2,1,2,2,2,1,1,2,2,2,1,1,1,2,2,2,1,1]
lat_long_parking = [[-122.41856552660467, 37.775226388320405], [-122.41667725145817, 37.776515380561385], [-122.41579011082649, 37.76847577247014], [-122.41457439959048, 37.77872018361018], [-122.41324402391909, 37.77329285782031], [-122.41272903978825, 37.77933073282808], [-122.41149857640265, 37.7754638359482], [-122.41141274571417, 37.766983090790866], [-122.40912415087222, 37.777532990139655], [-122.40892365574835, 37.78007695280165], [-122.40755036473273, 37.773089325352494], [-122.4014563858509, 37.7743105117552] ,[-122.42122627794744, 37.77332677984383], [-122.41839386522769, 37.78000911493352], [-122.41556145250797, 37.77777043035903], [-122.41526104509832, 37.77488717610065], [-122.41433098912239, 37.78156937014928], [-122.41380192339419, 37.77732946934459], [-122.41307236254214, 37.7754638359482], [-122.41217114031315, 37.78061965350541], [-122.41122700273989, 37.78129802378191], [-122.41028286516666, 37.77790611014198], [-122.41023994982243, 37.78197638783258], [-122.40766502916813, 37.776752824049225], [-122.40680672228336, 37.776074412060694], [-122.4061770737171, 37.7662367386528], [-122.40394547581673, 37.77973776283843], [-122.40385964512825, 37.774785412131216]]
names =['Brain Burling','Jutta Sheckler','Felisha Spring','Elvira Boston','Richie Yeaton','Page Alberty','Gracia Flewelling','Elizbeth Strouth','Hung Puff','Maryalice Walls','Salome Welsch','Wonda Wilborn','Serina Atkison','Robbyn Paschall','Amalia Laidlaw','Lavera Lowder','Laurel Rimer','Shawn Decicco','Lorene Vicario','Melodee Willbanks','Yahaira Koran','Lon Demyan','Geri Lamotte','Donnell Mumma','Lani Garbutt']
plates =['7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','63SN851']

def create_vehicle (index, json_str):
  data = json.loads(json_str)
  data['Type'] = 'Vehicle'
  data['Name'] = names[index]
  data['VIN'] = str(car_ids[index])
  data['LicensePlate'] = plates[index]
  if car_type[index] == 1 :
    data['EngineType'] = 'Electric'
  else :
    data['EngineType'] = 'Gas'
  temp = json.dumps(data)
  resp = requests.post(vehicle_base_url, data=temp, headers={'content-type':'application/json','MojioAPIToken':'b3655bdb-ca50-4476-986c-b39c65dab8d4'})
  print resp.text

if __name__ == "__main__":

  json_data = open('sample1.json').read()

  index = 0
  for index in range(0,25) :
     create_vehicle(index, json_data)

