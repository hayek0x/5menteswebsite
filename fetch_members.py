import requests

str4nx_socket = requests.get(
            'https://api.147.wtf/user?id=930806366212354078'
            )
hayek_socket = requests.get(
            'https://api.147.wtf/user?id=973588723809783928'
            )
mardok_socket = requests.get(
    'https://api.147.wtf/user?id=499456208596369438'
            )

nevask_socket = requests.get(
    'https://api.147.wtf/user?id=986781168529719346'
            )
    
hayek_socket_json = hayek_socket.json()
str4nx_socket_json = str4nx_socket.json()
mardok_socket_json = mardok_socket.json()
nevask_socket_json = nevask_socket.json()

hayek = hayek_socket_json['user']['username']
str4nx = str4nx_socket_json['user']['username']
mardok = mardok_socket_json['user']['username']
nevask = nevask_socket_json['user']['username']

str4nx_avatar = str4nx_socket_json['user']['avatarURL']
hayek_avatar = hayek_socket_json['user']['avatarURL']
mardok_avatar = mardok_socket_json['user']['avatarURL']
nevask_avatar = nevask_socket_json['user']['avatarURL']