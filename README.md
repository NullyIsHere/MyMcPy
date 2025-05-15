# MyMcPy

A simple Python library for interacting with the my-mc.link API.

> Thanks to [MiTask](https://github.com/MrMasrozYTLIVE) for creating [MyMC-Java-Lib](https://github.com/MrMasrozYTLIVE/MyMC-Java-Lib) from where i got the info of the api endpoints, and inspired me to create this.

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPLv3).  
See the [LICENSE](LICENSE) file for details.

## Installation

Install via pip (after publishing to PyPI):

```
pip install MyMcPy
```

Or install directly from source:

```
pip install .
```

## Basic Usage

```
from mymcpy import MyMcPy

# Initialize with your API token
client = MyMcPy("your_token_here")

# Get server stats
stats = client.get_stats()
print(stats)

# Ban a player
result = client.post_ban("Steve")
print(result)

# List online players
players = client.get_online_players()
print(players)
```

## API Overview

- `get_stats()` - Get server statistics
- `get_online_players()` - List online players
- `post_ban(username)` - Ban a player by username
- `post_unban(username)` - Unban a player
- `post_say(message)` - Send a chat message
- `post_tell(username, message)` - Send a private message
- `post_console(command)` - Execute a console command
- `install_mod(mod_id)` - Install a mod by ID
- `uninstall_mod(mod_id)` - Uninstall a mod by ID
- ...and more!

See the source code for the full list of available methods.

## Contributing

Contributions are welcome! Please open issues or pull requests.

