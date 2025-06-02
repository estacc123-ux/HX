import requests

user_list_url = "https://adm.heatherx.site/api/user-list"
delete_user_url = "https://adm.heatherx.site/api/delete-user"
add_to_blacklist_url = "https://adm.heatherx.site/api/add-to-blacklist"
remove_from_blacklist_url = "https://adm.heatherx.site/api/remove-from-blacklist"

cookies = {
    "auth": "authenticated",
}

headers = {
    # "X-CSRF-Token": "",  # <-- Will Add later
    "Referer": "https://adm.heatherx.site/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
}

def get_user_list():
    print("Fetching current HWID list...")
    response = requests.get(user_list_url, cookies=cookies, headers=headers)
    if response.ok:
        return response.json().get("valid", {})
    else:
        print("[Error] Failed to fetch user list:", response.status_code, response.reason)
        return {}

def delete_hwid(hwid):
    payload = {"hwid": hwid}
    response = requests.post(delete_user_url, json=payload, cookies=cookies, headers=headers)
    if response.ok:
        print(f"HWID {hwid} deleted successfully.")
    else:
        print(f"[Error] Failed to delete HWID {hwid}: {response.status_code} - {response.reason}")

def add_to_blacklist(hwid):
    payload = {"hwid": hwid}
    response = requests.post(add_to_blacklist_url, json=payload, cookies=cookies, headers=headers)
    if response.ok:
        print(f"HWID {hwid} added to blacklist successfully.")
    else:
        print(f"[Error] Failed to add HWID {hwid} to blacklist: {response.status_code} - {response.reason}")

def remove_from_blacklist(hwid):
    payload = {"hwid": hwid}
    response = requests.post(remove_from_blacklist_url, json=payload, cookies=cookies, headers=headers)
    if response.ok:
        print(f"HWID {hwid} removed from blacklist successfully.")
    else:
        print(f"[Error] Failed to remove HWID {hwid} from blacklist: {response.status_code} - {response.reason}")

if __name__ == "__main__":
    hwid = input("Enter the HWID: ").strip()
    action = input("Choose action (delete / add_blacklist / remove_blacklist): ").strip().lower()
    user_list = get_user_list()

    if hwid not in user_list:
        print("HWID not found in the user list.")
    else:
        if action == "delete":
            delete_hwid(hwid)
        elif action == "add_blacklist":
            add_to_blacklist(hwid)
        elif action == "remove_blacklist":
            remove_from_blacklist(hwid)
        else:
            print("Unknown action.")
