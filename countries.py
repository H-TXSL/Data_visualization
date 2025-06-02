from pygal_maps_world.i18n import COUNTRIES
# 字典COUNTRIES包含两个字母的国别码及其对应的国家名称
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])