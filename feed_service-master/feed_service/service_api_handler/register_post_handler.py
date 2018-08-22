from feed_service.db.climate_models.models import Climate
import requests

from feed_service.service_api_handler.Climate_type import climate_generator


def create_register(request_data):
    Region = request_data['Region']
    Climate_type = request_data['Climate_type']
    climate_object=climate_generator(Climate_type)
    link ="https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/"+climate_object+"/date/"+Region+".txt"
    f = requests.get(link)
    data = f.text
    count = 0
    for value in data.split("\n"):
        count = count + 1
        if count >= 9:
            count1 = 0
            climate_list=[]
            for i in value.split(' '):
                if i:
                    count1 = count1 + 1
                    climate_list.append(i)
                else:
                    continue
            if len(climate_list)==18:
                Climate.objects.get_or_create(Region=Region,Climate_type=Climate_type,Year=climate_list[0],Jan=climate_list[1],Feb=climate_list[2],Mar=climate_list[3],Apr=climate_list[4],May=climate_list[5],Jun=climate_list[6],Jul=climate_list[7],Aug=climate_list[8],Sep=climate_list[9],Oct=climate_list[10],Nov=climate_list[11],Dec=climate_list[12],Win=climate_list[13],Spr=climate_list[14],Sum=climate_list[15],Aut=climate_list[16],Ann=climate_list[17])
    return True

