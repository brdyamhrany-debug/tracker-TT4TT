import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_location():
    # Welcome message
    print(Fore.BLUE + "\n" + "="*0)
    print(Fore.BLUE + "terack ip")
    print(Fore.BLUE + "="*0 + "\n")

    ip = input(Fore.CYAN + " Target IP > " + Style.RESET_ALL).strip()

    if not ip:
        print(Fore.RED + "Error: No IP address provided!")
        return

    print(Fore.YELLOW + f"[*] Fetching data for {ip}...")

    try:
        # Using API to get location information
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,lat,lon,query")
        data = response.json()

        if data['status'] == 'success':
            print(Fore.GREEN + "\n[+] Information Found:")
            print(Fore.WHITE + f"----------------------------")
            print(Fore.WHITE + f"IP Address: {data['query']}")
            print(Fore.WHITE + f"Country:    {data['country']}")
            print(Fore.WHITE + f"Region:     {data['regionName']}")
            print(Fore.WHITE + f"City:       {data['city']}")
            print(Fore.WHITE + f"Latitude:   {data['lat']}")
            print(Fore.WHITE + f"Longitude:  {data['lon']}")
            print(Fore.WHITE + f"----------------------------")

            # Creating Google Maps link
            google_maps_link = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
            print(Fore.BLUE + f"\n[!] Google Maps Link: {google_maps_link}")
            
        else:
            print(Fore.RED + f"[-] Error: {data.get('message', 'Invalid IP address')}")

    except Exception as e:
        print(Fore.RED + f"[-] An error occurred: {e}")

if __name__ == "__main__":
    get_location()
