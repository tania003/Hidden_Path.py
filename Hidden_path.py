import requests

target_url = "website_name"


def request(url):
    try:
      return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
      pass

with open("/home/kali/Downloads/common.txt","r") as wordlist_file:
 for line in wordlist_file:
  word = line.strip()
  test_url = target_url + "/" + word
  response = request(test_url)
  if response:
    print("[+] Discovered URL ---->" + test_url)
