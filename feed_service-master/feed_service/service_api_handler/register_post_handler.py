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
            Year="";Jan="";Feb="";Mar="";Apr="";May="";Jun="";Jul="";Aug="";Sep="";Oct="";Nov="";Dec="";Win="";Spr="";Sum="";Aut="";Ann="";
            for i in value.split(' '):
                if i:
                    count1 = count1 + 1
                    if count1 == 1:
                        Year=i
                    if count1 == 2:
                        Jan=i
                    if count1 == 3:
                        Feb=i
                    if count1 == 4:
                        Mar=i
                    if count1 == 5:
                        Apr=i
                    if count1 == 6:
                        May=i
                    if count1 == 7:
                        Jun=i
                    if count1 == 8:
                        Jul=i
                    if count1 == 9:
                        Aug=i
                    if count1 == 10:
                        Sep=i
                    if count1 == 11:
                        Oct=i
                    if count1 == 12:
                        Nov=i
                    if count1 == 13:
                        Dec=i
                    if count1 == 14:
                        Win=i
                    if count1 == 15:
                        Spr=i
                    if count1 == 16:
                        Sum=i
                    if count1 == 17:
                        Aut=i
                    if count1 == 18:
                        Ann=i
                else:
                    continue
            register_object=Climate.objects.create(Region=Region,Climate_type=Climate_type,Year=Year,Jan=Jan,Feb=Feb,Mar=Mar,Apr=Apr,May=May,Jun=Jun,Jul=Jul,Aug=Aug,Sep=Sep,Oct=Oct,Nov=Nov,Dec=Dec,Win=Win,Spr=Spr,Sum=Sum,Aut=Aut,Ann=Ann)
    return register_object

