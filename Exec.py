import json
import hashlib
import requests
#import random

# host地址
host = "https://app-home.viomi.com.cn"
host_test = "https://app-home-test.viomi.com.cn"
host_iot = "https://viot.viomi.com.cn"
host_admin = "https://admin-home.viomi.com.cn"
host_ms = "https://ms.viomi.com.cn"

uri_scene_list = "/api/scene/manage/list/aggregationV2"
uri_device_scene_list = "/home/v4/methods"
uri_device_list = "/api/smarthome/web/user/device/list"
uri_device_list_old = "/api/smarthome/web/multi/family/device/list/aggregation"

uri_family = "/api/smarthome/web/homemap/wholehouse/life/solutions"
uri_family_water = "/api/smarthome/web/homemap/wholehouse/life/waterpurifier/v1/module/info"

uri_card_list = "/api/smarthome/web/family/screen/homepadplus/shortcut_device/list"
uri_mesh_list = "/api/device/open-api/v1/inner/mesh/listMeshConfig/v2"
uri_card_v1 = "/api/plugins/model/findCardText"
uri_card_v2 = "/api/plugins/model/findCardTextV2"

uri_login = "/user-web/services/login/withPwd.json"
uri_register = "/user-web/services/login/regAndLogin.json"

uri_mp_family_list = "/api/smarthome/web/mp/family/list"

uri_voice_family_list = "/ai/speechandlanguage/voiceprint/familylist"

uri_device_info = "/api/smarthome/web/family/device/info"
uri_device_helpful = "/api/smarthome/web/multi/family/device/feature/list"
uri_device_control = "/api/smarthome/web/multi/family/device/feature/control"


def MD5(en_data):
    m = hashlib.md5()
    m.update(en_data.encode('utf-8'))
    return m.hexdigest().upper()


def login(uri, dataDict):
    response = requests.get(url=host_ms + uri, params=dataDict)
    return json.loads(response.text)['mobBaseRes']['result']['token']


def register(uri, dataDict):
    response = requests.post(url=host_ms + uri, headers=headers, params=dataDict)
    print(response.json())
    return response.json()


def getRequest(getHost, uri, dataDict=None):
    resp = requests.get(url=getHost + uri, headers=headers, params=dataDict)
    print(resp.text)
    return resp.json()


def postRequest(postHost, uri, dataDict=None):
    resp = requests.post(url=postHost + uri, headers=headers, data=json.dumps(dataDict))
    print(resp.json())
    return resp.json()


if __name__ == "__main__":
    login_account = "12152957"
    login_passwd = "a12345"
    data_login = {"account": login_account, "pwd": MD5(login_passwd)}
    data_account = {"mobile": "13424134969", "authCode": "", "sourceChannel": 3, "pwdMD5": MD5("a12345")}
    # print(data_account)

    token = login(uri_login, data_login)
    # token = "Fr2w8sds1PZ1sNaE"

    headers = {
        "accpet": "*/*",
        "DOSIGNORE": "1",
        "content-Type": "application/json",
        "charset": "UTF-8",
        "token": token,
        "Authorization_v1": token}

    data_family = {"familyId": "2777434",
                   "screenDid": "1003089048",
                   "appKey": "9A274e84C985d7Db",
                   "shareDevice": "1"}

    data_device = {"channel": "viot",
                   "type": "viot.switch.w5",
                   "did": "1003531620"}

    data_familyId = {"familyId": "2777434"}

    data_card = {"sdkLevel": "2.0.0",
                 "status": "1,3",
                 "models": ""}

    data_control_v1 = {"controlKey": "FUNCTION_CLOSE",
                       "familyId": 2777434,
                       "deviceInfo": {"did": "1003351917",
                                      "model": "viot.heater.v1",
                                      "protocolCode": 9}}

    data_control_y109 = {"controlKey": "CLOSE_DEGRADE_HCHO",
                         "familyId": 2777434,
                         "deviceInfo": {"did": "1003317806",
                                        "model": "viot.aircondition.y109",
                                        "protocolCode": 9}}

    # register
    # register(uri_register, data_account)

    # homeMapPage
    # getRequest(host, uri_family, data_family)

    # deviceList
    getRequest(host, uri_device_list)

    # deviceListOld
    # getRequest(host, uri_device_list_old, data_family)

    # sceneList
    # getRequest(host, uri_scene_list, data_family)

    # deviceSceneList
    # getRequest(host_iot, uri_device_scene_list, data_device)

    # familyWater
    # getRequest(host, uri_family_water, data_family)

    # cardList
    # getRequest(host, uri_card_list, data_family)

    # meshList
    # getRequest(host, uri_mesh_list, data_familyId)

    # voiceFamilyList
    # getRequest(host, uri_voice_family_list, data_familyId)

    # deviceCard
    # getRequest(host_admin, uri_card_v1, data_card)
    # getRequest(host_admin, uri_card_v2, data_card)

    # deviceHelpful
    # dataControl = getRequest(host, uri_device_helpful, data_familyId)

    """
    # deviceControl
    newData = dataControl["result"]
    if len(newData) > 0:
        for data in newData:
            featureList = data["featureList"][0]
            did = data["did"]
            deviceDid = {"did": did}
            model = getRequest(host, uri_device_info, deviceDid)["result"]["model"]
            data_control = {"controlKey": featureList["controlKey"], "familyId": 2777434, "deviceInfo": {"did": did, "model": model,"protocolCode": 9}}
            postRequest(host, uri_device_control, data_control)
    # postRequest(host, uri_device_control, data_control_v1)
    """