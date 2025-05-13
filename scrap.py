# import requests
# url = "https://www.imdb.com/chart/toptv/"
# payload = {}
# headers = {
#   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
#   'accept-language': 'en-US,en;q=0.8',
#   'priority': 'u=0, i',
#   'sec-ch-ua': '"Chromium";v="136", "Brave";v="136", "Not.A/Brand";v="99"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'document',
#   'sec-fetch-mode': 'navigate',
#   'sec-fetch-site': 'none',
#   'sec-fetch-user': '?1',
#   'sec-gpc': '1',
#   'upgrade-insecure-requests': '1',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
#   'Cookie': 'session-id=147-1834452-7506408; ubid-main=131-2173481-4189038; at-main=Atza|IwEBILjLmNDGqqixIBjtUOvKhX0pIw_wEB4tV1JZMRGt4hx8PZL2oaQr9Q22XoJUxTpm8dYORxanlliQKCpOIIXE4ofiIMr8CKNvTafScxwORub2NH0BrqVDNNb4Et69h4umb2QTQqkDxS6sJ2jVJKaXeZ1lSDXqy88S84VGYjQuR0YV_omdfTDlpMNVF0C8HekI2usedXYRPSt89yuCZYX9qgczyjWUmmXNc1qOgVKs8Uip1c2LRLp2WCUAV4yGkIp1hI9uFfu3yABxg5sCY3TNQQjf; sess-at-main="qG3xnmix/Mw5yUz7tkj9geR8wfNV6Rn3ySRhzMgGDPs="; uu=eyJpZCI6InV1ZjljODVhNzdiMTgyNDc3NWE3YzAiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfSwidWMiOiJ1cjE1MDYxNTUzNSJ9; session-id-time=2082787201l; ad-oo=16; gpc-cache=1; ci=eyJpc0dkcHIiOmZhbHNlfQ; session-token=nRt2SQ9KAqq/QtsncVjTokwgxmoDr0v4hW08W6sWU7ziJrBn33ezSSRwQj3FGPf3OSQi/MKvZlLZAtBPMhAUy0FGcO4ZVh27YGZRaEobE/6Fb27AHgD5gJ+lvA00mfj83Kj/YHnwW5cahTlX9qnTt001LuuWP9lpiAwylx0p55MTqHP4sptK/zsw1UkcoC9ZFFqLp1nzLpp6nnKtcy3yLEvkI+edfN8Pxg4csM8isMHwiXxS1VAtZtH0KWlNp+j9oH/N8LdoxmmNXpD0VX82RM1X18ee2B2Mbil9M/9V2YzbNJs79Uxo1SKjs3mrtXeI+7qDWiwwKnITP6imotClax3uclw7NJhr; csm-hit=adb:adblk_yes&t:1747041256695&tb:s-FRTBTJWM65WKXNAYJ1D6|1747041256381; session-id=147-1834452-7506408; session-id-time=2082787201l; session-token=YccQHs+c+/jabwBQW4AmEs6Dijb59qSNY/RqHDxCMhRVtur2hMYDKQqp3/LmU64DtnsVO+86V7h+BmtWBUZBxu0fcy25GHaXZSdu67UrWm0JvH3QDNwBOYuHNSDxNpNgIKDMccw9X5se0bNdX5XTbF9J+RXQMfsZbjXaLkAU7VUfXyychpKCc6eXXQTEHf+k2piHItHYIRRqDUzSxfuG28GkMAoKGIlFrrTa/TrIa0gsIQ2BmUcUneu6erXWDmPg0Tb9ONSaml7PMGL2g/PVHh8Kwuuz2ZBCsa+iPsRQ+vg5j0ImXtfXejnIEeqdxYI6MTI+FBc7+RcWiJH7M5hOYG1siiqmMAy7'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
# print(response.txt)

# playwrite library

""" import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/"
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="136", "Brave";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Cookie': 'session-id=147-1834452-7506408; ubid-main=131-2173481-4189038; at-main=Atza|IwEBILjLmNDGqqixIBjtUOvKhX0pIw_wEB4tV1JZMRGt4hx8PZL2oaQr9Q22XoJUxTpm8dYORxanlliQKCpOIIXE4ofiIMr8CKNvTafScxwORub2NH0BrqVDNNb4Et69h4umb2QTQqkDxS6sJ2jVJKaXeZ1lSDXqy88S84VGYjQuR0YV_omdfTDlpMNVF0C8HekI2usedXYRPSt89yuCZYX9qgczyjWUmmXNc1qOgVKs8Uip1c2LRLp2WCUAV4yGkIp1hI9uFfu3yABxg5sCY3TNQQjf; ...'  # Shortened for readability
}

r = requests.get(url, headers=headers)

# Check the status code before parsing
if r.status_code != 200:
    raise Exception(f"Request failed with status code {r.status_code}")

# Parse the response with BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

imdb_list =soup.find_all("li",{"class":"ipc-metadata-list-summary-item"})
# print(imdb_list)

imdb_list_data=[]
for i in imdb_list:
    title=i.find("div",{"class":"ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-d6dda2a0-2 bwOaNw cli-title with-margin"}).text.strip()
    ratings=i.find("span",{"class":"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"}).text.strip()
    time_period=i.find("span",{"class":"sc-4b408797-8 iurwGb cli-title-metadata-item"}).text.strip()
    img_tag = i.find("img", {"class": "ipc-image"})
    image = img_tag['src']
    imdb_list_data.append({
        "title":title,
        "time_period":time_period,
        "ratings":ratings,
        "image":image
    })
    
print(imdb_list)

csv_file = "imdb_top_tv.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "ratings", "time_period", "image"])
    writer.writeheader()
    writer.writerows(imdb_list_data)

print(f"✅ Data saved to '{csv_file}' successfully.") """

