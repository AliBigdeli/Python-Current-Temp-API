from current_temp_api.api import OpenMeteo,OpenWeather

open_meteo_obj = OpenMeteo(35.69,51.42)
print(open_meteo_obj.get_current_temperature())


open_weather_obj = OpenWeather(35.69,51.42,api_token="aff45d1d01b53551610ea16cddd34457")
print(open_weather_obj.get_current_temperature())
    