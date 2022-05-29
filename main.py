from imports import *

def main():

    ARGS = len(sys.argv)

    if ARGS < 2: 
        print("\n[-] Usage: python scan.py <http(s)://domain.com/> <port>\n[i] Port defaults to 80\n[i] SSL is automatically set \n[+] Must include full URL")
        sys.exit()
    elif ARGS < 3:
        PORT = str('80')
        print("\n[+] No port defined, defaulting to 80")
    else:
        PORT = sys.argv[2]

    def separator():
        print(" -" * len(URL))

    try:

        URL = sys.argv[1]

        if 'https://' or 'http://' not in URL:
            print("[-] Must be full URL, example: https://domain.com/\n")
            sys.exit()

        if 'https' in URL:
            SSL = True
            print("[+] SSL certificate verification set to True")
        else:
            SSL = False
            print("[+] SSL set to False")

        separator()
        print("[+] Requesting " + URL + " ...")
        GET = requests.get(URL, timeout=10, verify=SSL)
        GET.raise_for_status()  

        ENCODING = GET.encoding
        COOKIES = GET.cookies
        TIME = GET.elapsed
        CONTENT = GET.content
        HEADERS = GET.headers
        REDIRECTED = GET.is_redirect
        REASON = GET.reason

        status_code = GET.status_code
        if status_code != 200:
            print("[-] : " + status_code)
        else:
            print("[+] Response took " + str(TIME) + " seconds")
            print("[+] Response status code: 200")
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
        
    except ConnectionError:
        print ("[-] Connection error, host might be down")
    except Timeout:
        print ("[-] Host is taking too long to respond")
    except HTTPError:
        print ("[-] HTTPError: " + status_code)

if __name__ == "__main__":
        main()
        

