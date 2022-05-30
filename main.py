from imports import *

def main():

    ARGS = len(sys.argv)

    if ARGS < 2: 
        print("\n[-] Usage: python main.py <http(s)://domain.com/> <port>\n[i] Port defaults to 80\n[i] SSL is automatically set \n[+] Must include full URL")
        sys.exit()
    elif ARGS < 3:
        PORT = str('80')
        print("\n[+] No port defined, defaulting to 80")
    else:
        PORT = sys.argv[2]

    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    def separator():
        print(" -" * len(URL))

    try:

        URL = sys.argv[1]

        if not re.match(regex, (URL)) is not None:
            print("[-] Invalid URL")
            sys.exit()

        if 'https' in URL:
            SSL = True
            print("[+] SSL certificate verification set to True")
        else:
            SSL = False
            print("[+] SSL set to False")

        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }

        separator()

        print("[+] Requesting " + URL + " ...")

        GET = requests.get(URL, timeout=10, verify=SSL, headers=HEADERS)
        GET.raise_for_status()  

        ENCODING = GET.encoding
        COOKIES = GET.cookies
        TIME = GET.elapsed
        CONTENT = GET.content
        HEADERS = GET.headers
        REDIRECTED = GET.is_redirect
        REASON = GET.reason
        STATUS_CODE = GET.status_code

        if Response:
            print("[+] Response took " + str(TIME) + " seconds")
            print("[+] Response status code: " + str(STATUS_CODE))
            print("[+] Status code reason: " + str(REASON)) 
            print("[+] Encoding: " + str(ENCODING))
            print("[+] Cookies: " + str(COOKIES))

            if REDIRECTED == True:
                print("[+] Request was redirected")
        
            if path.exists("headers.txt"):
                print ("[+] headers.txt already exists, overwriting")
                header_file = open('headers.txt', 'w')
                header_file.write(str(HEADERS))
                header_file.close   
            else:
                print ("[+] Created headers.txt")
                header_file = open('headers.txt', 'x')
                header_file.write(str(HEADERS))
                header_file.close

            print ("[+] Saved headers in headers.txt")

            if path.exists("content.txt"):
                print ("[+] content.txt already exists, overwriting")
                content_file = open('content.txt', 'w')
                content_file.write(str(CONTENT))
                content_file.close   
            else:
                print ("[+] Created content.txt")
                content_file = open('content.txt', 'x')
                content_file.write(str(CONTENT))
                content_file.close

            print ("[+] Saved content in content.txt")

            separator()
            print("[+] Request for " + URL + " finished\n")
        else:
            print("[-] Error occured. " + str(STATUS_CODE))
            sys.exit()
        
    except ConnectionError:
        print ("[-] A connection error occured. Host might be down.")
    except Timeout:
        print ("[-] The request timed out.")
    except HTTPError:
        print ("[-] An HTTP error occured. " + STATUS_CODE)

if __name__ == "__main__":
        main()
        