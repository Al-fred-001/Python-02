import requests
from requests import Response


"""
To do: 
    format the output and display in the console. (It's not neat -_- )
    add some additional formatting to the output.
    separate the concern of the check_website func.
"""

def normalize_url(url:str) -> str:
    return url if url.startswith(("http://", "https://") ) else f"https://{url}"


def check_website(url: str, timeout:int = 10) -> None:
    url = normalize_url(url)

    print(f"\t\t-- Analyzing website: {url} -- ")
    print("")
    try: 
        response: Response = requests.get(url, timeout=timeout)
    except Exception as e:
        print(f"Error: {e}")
        return
    

    status_code :int = response.status_code
    elapsed_time :float = response.elapsed.total_seconds()
    reason : str = response.reason
    content_type :str = response.headers.get("Content-Type", "")
    encoding: str|None = response.encoding
    headers: dict[str, str] = dict(response.headers)
    print("---------------------------------------------------------")
    print(f"""
    Status Code: {status_code} ({reason})
    Elapsed Time: {elapsed_time}
    Content-Type: {content_type}
    Encoding : {encoding or "N/A"}
    """)
    print("---------------------------------------------------------")

    print("Headers:")
    for key, value in headers.items():
        print(f"\t• {key}: {value}")
    print("---------------------------------------------------------")


def test()->None:
    print("\n\t\t-- Website Analyser --\n")
    get_url = input("Url of website to analyse: ")
    check_website(get_url)

if __name__ == "__main__":
    test()


    
