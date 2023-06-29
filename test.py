from CourtScraper import CourtScraper

scrap = CourtScraper()

""" Get max 500 files - year param between 2005 to 2023 """
data = scrap.get_by_year(year=2019,limit=1)


print("The keys from file:")
print(data[0].keys())

print("Link:")
print(data[0]['link'])

print("Who is the judge ? ")
print(data[0]['לפני'].replace("  ","").replace("\n",""))

print("Verdict:")
print(data[0]['פסק-דין'].replace("  ","").replace("\n\n",""))