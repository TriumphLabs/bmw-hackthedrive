from keen.client import KeenClient
import time
import requests

KEEN_WR_KEY = "05113afcc9cf7a26d442ea480f8c07c12ed594ec57e65b653f6baffcb4e0cee95b7384c18a67031a8d1d81f508d9aefd305493f2cf60bb854860b9619c7012563025ad9a878f16f466d41a5871ed253c9d3edcf392ac3d0b404dce7710fc81ce5dd0422c7a766ea012e162b11efda22a"
KEEN_RD_KEY = "e82a057e6db0420eae3f8731c8b3e6ab2495d4896820d94d916c513a1ef3bcc082bd2840c2b1155ef172676519c6b4b2b663eae703c89ace55ccd1b8af35fd4a75908e323e52a7fe9a5bb57983386d8d870e2bf71ac9062c2dc8fb3ba0b063479d7c64399d0168d893148a5fc8cedb5f"
KEEN_PROJ_ID = "54b1af4a2fd4b13c34583e3c"
KEEN_MASTER_API_KEY = "A6AF6AD7E04BC5FFFD9B5C63C54797B8"

evt_base_url = "http://data.api.hackthedrive.com:80/v1/Events"
user="pwnrao"
pwd="welcomePA1"
MojioId="307630a0-5490-4def-9a0b-4bd42b83e52a"


car_ids = [996880,996881,996882,996883,996884,996885,996886,996887,996888,996889,996890,996891,996892,996893,996894,996895,996896,996897,996898,996899,996900,996901,996902,996903,996904]
car_type = [2,1,1,1,2,2,1,1,2,2,2,2,1,1,2,2,2,1,1,2,2,2,1,1,2]
car_rate = [2,1,2,2,2,2,1,2,1,2,2,2,1,1,2,2,2,1,1,1,2,2,2,1,1]
lat_long_parking = [[-122.41856552660467, 37.775226388320405], [-122.41667725145817, 37.776515380561385], [-122.41579011082649, 37.76847577247014], [-122.41457439959048, 37.77872018361018], [-122.41324402391909, 37.77329285782031], [-122.41272903978825, 37.77933073282808], [-122.41149857640265, 37.7754638359482], [-122.41141274571417, 37.766983090790866], [-122.40912415087222, 37.777532990139655], [-122.40892365574835, 37.78007695280165], [-122.40755036473273, 37.773089325352494], [-122.4014563858509, 37.7743105117552] ,[-122.42122627794744, 37.77332677984383], [-122.41839386522769, 37.78000911493352], [-122.41556145250797, 37.77777043035903], [-122.41526104509832, 37.77488717610065], [-122.41433098912239, 37.78156937014928], [-122.41380192339419, 37.77732946934459], [-122.41307236254214, 37.7754638359482], [-122.41217114031315, 37.78061965350541], [-122.41122700273989, 37.78129802378191], [-122.41028286516666, 37.77790611014198], [-122.41023994982243, 37.78197638783258], [-122.40766502916813, 37.776752824049225], [-122.40680672228336, 37.776074412060694], [-122.4061770737171, 37.7662367386528], [-122.40394547581673, 37.77973776283843], [-122.40385964512825, 37.774785412131216]]
names =['Brain Burling','Jutta Sheckler','Felisha Spring','Elvira Boston','Richie Yeaton','Page Alberty','Gracia Flewelling','Elizbeth Strouth','Hung Puff','Maryalice Walls','Salome Welsch','Wonda Wilborn','Serina Atkison','Robbyn Paschall','Amalia Laidlaw','Lavera Lowder','Laurel Rimer','Shawn Decicco','Lorene Vicario','Melodee Willbanks','Yahaira Koran','Lon Demyan','Geri Lamotte','Donnell Mumma','Lani Garbutt']
plates =['7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','7BSN851','7BSN852','6BSN851','63SN851']
vehicle_ids = ["9ef8572d-7cc8-4279-8410-fb64f46ab359","e55e6f41-dc06-435f-b389-caacb4fdc29c","1acf3045-5021-44d5-8d19-dba0889c3863","f32c4958-6220-4364-b7ea-7a8faa627657","73ad18f9-ef7d-43f1-b8ca-ce1f7aa56d4c","9d8d0087-44ba-4528-abe8-e8ddeb288016","1dc91031-0660-4d1a-bc04-2346b8f81816","731f05d7-1c5d-4bbe-8f2a-44a37e73be69","0bb70e21-e49b-4ee6-ae64-84b6e359b7bb","ebcaef3e-d561-4d3e-93d5-9b7ad993deed","0350436d-f4ed-4da9-aee6-fa78243230f1","1af0b5a7-e996-4c00-ae1e-655b8586fc49","7aa0eb42-abe6-45f2-9b8b-60cc5d69acb3","61d44f36-31ab-49a2-b505-4fd4c0c0f8ca","1e25a15b-84b2-4e01-bafb-c992e3ba874c","688ab09f-18a8-4a0f-b622-355e477145ff","97399cd2-0f26-48e9-b97a-a3958de0b15d","1507b118-21f9-45be-894d-c339b9ec17be","cb0171b2-7e93-4735-8d42-a6d6b559a257","c97de837-409d-4cf7-8084-ba7981523e84","29ca4a0a-6b31-4e92-9bea-c83660541d5d","7e41ea9e-fbc6-4f50-ac8f-42d761c6a8cc","3da92dfd-ad0f-4293-a695-80cb85810876","5855a2d0-984f-4562-85ce-d2c3f77b7abb","b276db13-01d9-462e-8f04-533222e968db"]




if __name__ == "__main__":

   client = KeenClient(project_id=KEEN_PROJ_ID,write_key=KEEN_WR_KEY,read_key=KEEN_RD_KEY)

   event_data = requests.get('http://data.api.hackthedrive.com:80/v1/Events?limit=25&offset=0&sortBy=Time&desc=true&criteria=',headers={'MojioAPIToken':'b3655bdb-ca50-4476-986c-b39c65dab8d4'}).json()
   
   index = 0
   for event in event_data['Data']:
     timeStamp = int(time.time())
     if event['EventType'] == 'IgnitionOff':
       print "Account for parking"
       billing_rate = 2.00 + 3.00 * car_type[index] + 3.00 * car_rate[index]
       client.add_events({
       "parking_v4": [
           { "Index":index , "VIN":car_ids[index],"Name":names[index],"Plates":plates[index], "time": timeStamp, "keen": { "location": { "coordinates": [lat_long_parking[index][0],lat_long_parking[index][1]] } },"bill_amt":billing_rate, "occupied":"yes"}
         ]
       })
     else :
       client.add_events({
       "parking_v4": [
           { "Index":index, "VIN":car_ids[index],"Name":names[index],"Plates":plates[index], "time": timeStamp, "keen": { "location": { "coordinates": [lat_long_parking[index][0],lat_long_parking[index][1]] } }, "bill_amt":0, "occupied":"no"}
         ]
     }) 
     index = index + 1