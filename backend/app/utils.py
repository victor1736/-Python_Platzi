def get_population(country_dict):
    population_dic = {
        '2022':country_dict['2022 Population'],
        '2022':country_dict['2020 Population'],
        '2015':country_dict['2015 Population'],
        '2010':country_dict['2010 Population'],
        '2000':country_dict['2000 Population'],
        '1990':country_dict['1990 Population'],
        '1980':country_dict['1980 Population'],
        '1970':country_dict['1970 Population']
    }
    labels = population_dic.keys()
    values = population_dic.values()
    
    return labels,values

def population_by_country(data,country):
    result = list(filter(lambda item:item['country']==country,data))
    return result