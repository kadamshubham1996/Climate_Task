
def climate_generator(climate_data):
    climate_object="";
    if climate_data=="Max Temp":
        climate_object="Tmax"
    elif climate_data=="Min Temp":
        climate_object="Tmin"
    elif climate_data == "Mean Temp":
        climate_object="Tmean"
    elif climate_data == "Sunshine":
        climate_object="Sunshine"
    elif climate_data == "Rainfall":
        climate_object="Rainfall"
    elif climate_data == "Raindays":
        climate_object="Raindays1mm"
    elif climate_data == "Days of Air frost":
        climate_object="AirFrost"
    return climate_object
