import requests
from enum import Enum

class ApiEndpoint(Enum):
    HELLO = "hello"
    TIME = "time"
    STATS = "stats"
    LOG = "log"
    START = "start"
    STOP = "stop"
    RESTART = "restart"
    MY_LINK = "my-link"
    MY_SFTP = "my-sftp"
    MY_HASH = "my-hash"
    MY_HASH_SFTP = "my-hash-sftp"
    LIST_PLAYERS = "list-players"
    WEBSITE = "website"
    MAP = "map"
    BAN = "ban"
    UNBAN = "unban"
    SAY = "say"
    TELL = "tell"
    CONSOLE = "console"
    GIVE = "give"
    INSTALL = "install"
    UNINSTALL = "uninstall"
    SEARCH = "search"
    MOD_LIST = "mod-list"

class MyMcPy:
    BASE_URL = "https://api.my-mc.link/"
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    def __init__(self, token: str):
        self.token = token
        resp = self._get(ApiEndpoint.HELLO)
        if not resp.get("success", False):
            raise RuntimeError(resp.get("message", "Token verification failed."))

    def _request(self, method: str, endpoint: ApiEndpoint, data: dict = None):
        url = self.BASE_URL + endpoint.value
        headers = {**self.HEADERS, "x-my-mc-auth": self.token}
        try:
            resp = requests.request(method, url, headers=headers, json=data)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            raise RuntimeError(f"API {method} request failed: {e}")

    def _get(self, endpoint: ApiEndpoint):
        return self._request("GET", endpoint)

    def _post(self, endpoint: ApiEndpoint, data: dict):
        return self._request("POST", endpoint, data)

    def _delete(self, endpoint: ApiEndpoint):
        return self._request("DELETE", endpoint)

    # API methods
    def get_time(self): return self._get(ApiEndpoint.TIME)
    def get_stats(self): return self._get(ApiEndpoint.STATS)
    def get_log(self): return self._get(ApiEndpoint.LOG)
    def start_server(self): return self._get(ApiEndpoint.START)
    def stop_server(self): return self._get(ApiEndpoint.STOP)
    def restart_server(self): return self._get(ApiEndpoint.RESTART)
    def create_my_link(self): return self._get(ApiEndpoint.MY_LINK)
    def delete_my_link(self): return self._delete(ApiEndpoint.MY_LINK)
    def create_link_sftp(self): return self._get(ApiEndpoint.MY_SFTP)
    def delete_link_sftp(self): return self._delete(ApiEndpoint.MY_SFTP)
    def get_connection_hash(self): return self._get(ApiEndpoint.MY_HASH)
    def get_connection_hash_sftp(self): return self._get(ApiEndpoint.MY_HASH_SFTP)
    def get_online_players(self): return self._get(ApiEndpoint.LIST_PLAYERS)
    def get_website_url(self): return self._get(ApiEndpoint.WEBSITE)
    def get_map_url(self): return self._get(ApiEndpoint.MAP)
    def post_ban(self, username): return self._post(ApiEndpoint.BAN, {"username": username})
    def post_unban(self, username): return self._post(ApiEndpoint.UNBAN, {"username": username})
    def post_say(self, message): return self._post(ApiEndpoint.SAY, {"message": message})
    def post_tell(self, username, message): return self._post(ApiEndpoint.TELL, {"username": username, "message": message})
    def post_console(self, command): return self._post(ApiEndpoint.CONSOLE, {"message": command})
    def post_give(self, username, item, amount): return self._post(ApiEndpoint.GIVE, {"username": username, "item": item, "amount": amount})
    def install_mod(self, mod_id): return self._post(ApiEndpoint.INSTALL, {"mod": mod_id})
    def uninstall_mod(self, mod_id): return self._post(ApiEndpoint.UNINSTALL, {"mod": mod_id})
    def get_installed_mods(self): return self._get(ApiEndpoint.MOD_LIST)
