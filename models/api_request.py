import requests
import json
from alchemize import JsonTransmuter, JsonMappedModel, Attr

endpoint = ''
data = {'username': '', 'password': ''}

r = requests.post(endpoint, data=data, verify=False)
token = json.loads(r.text)['authorization']


class Meta(JsonMappedModel):
    __mapping__ = {
        'scope': Attr('scope', str),
        'uri': Attr('uri', str),
    }


class IDIdentity(JsonMappedModel):
    __mapping__ = {
        'id': Attr('id', int),
        'identity': Attr('user', str),
        'metadata': Attr('metadata', Meta),
    }


class Login(JsonMappedModel):
    __mapping__ = {
        'authorization': Attr('authorization', str),
        'user': Attr('user', IDIdentity),
    }


result_model = JsonTransmuter.transmute_from(r.text, Login)

abc = 1
