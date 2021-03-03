# import requests
# import json
# from alchemize import JsonTransmuter, JsonMappedModel, Attr
#
# endpoint = ''
# data = {'username': '', 'password': ''}
#
# r = requests.post(endpoint, data=data, verify=False)
# token = json.loads(r.text)['authorization']
#
#
# class Meta(JsonMappedModel):
#     __mapping__ = {
#         'scope': Attr('scope', str),
#         'uri': Attr('uri', str),
#     }
#
#
# class IDIdentity(JsonMappedModel):
#     __mapping__ = {
#         'id': Attr('id', int),
#         'identity': Attr('user', str),
#         'metadata': Attr('metadata', Meta),
#     }
#
#
# class Login(JsonMappedModel):
#     __mapping__ = {
#         'authorization': Attr('authorization', str),
#         'user': Attr('user', IDIdentity),
#     }
#
#
# result_model = JsonTransmuter.transmute_from(r.text, Login)
#
# abc = 1

import requests


endpoint = 'https://api.thecatapi.com/v1/votes'
data = {
    "image_id": "asf10",
    "sub_id": "my-user-12341",
    "value": 1,
}

headers = {
    'x-api-key': 'dae034ac-1aa2-4a5c-abe5-041dba3a0c86',
}

r = requests.post(endpoint, json=data, headers=headers)
abc = 1




# endpoint = 'https://api.thecatapi.com/v1/votes'
# headers = {
#     'x-api-key': 'dae034ac-1aa2-4a5c-abe5-041dba3a0c86',
# }
#
# r = requests.get(endpoint, headers=headers)
# abc = 1