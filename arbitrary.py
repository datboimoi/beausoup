# The beginning of this Lab (Task 1: First Commit)
change = "My small contribution"

# Copy of Postman python request code (Task 2: Python Request)
import requests

url = "https://www.indeed.com/jobs?q=Software Developer&l=Charlotte"

payload={}
headers = {
  'Cookie': 'CTK=1g9id1hcmi6gi802; __cf_bm=sP50_76LmVBHIcHFJja3Y4dZuX5skJ6MFGOjyuPvdb0-1659548780-0-Aciq9Aj2TIeepLn82CVFaT11vxxg4N53X74ESdNTJ4KMDu/W6iwF+Ky7tAFEMGK/EJzpOeygwR9mL0mso3qBau0=; _cfuvid=FPwJ3bX9MYfSpZwjK38bsXEZGpf88oFAbY6s8X8aspI-1659548780071-0-604800000; INDEED_CSRF_TOKEN=zGcilpDfKzlhWuic2Cjrh7Tpmhh18adL; JSESSIONID=FB49E73DC577AE20515C5E93C96EFE71; PREF="TM=1659548779935:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1659548779960"; UD="LA=1659548779:CV=1659548779:TS=1659548779:SG=7ba0eb7ce4a8288c15e07cb403001010"; ctkgen=1; indeed_rcc=""; jaSerpCount=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)