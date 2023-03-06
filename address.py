import os
import requests

key = os.environ['KEY']



ENDPOINT = "http://164.92.218.36:8080/api"


def created_address_id():
    payload = """<?xml version="1.0" encoding="UTF-8"?>
    <prestashop
        xmlns:xlink="http://www.w3.org/1999/xlink">
        <address>
            <id_customer></id_customer>
            <active>1</active>
            <id_manufacturer></id_manufacturer>
            <id_supplier></id_supplier>
            <id_warehouse></id_warehouse>
            <id_country>1</id_country>
            <id_state></id_state>
            <alias>Alina</alias>
            <company></company>
            <lastname>Gladkaya</lastname>
            <firstname>Alina</firstname>
            <vat_number></vat_number>
            <address1>Pushkinskaya str</address1>
            <address2></address2>
            <postcode>61000</postcode>
            <city>Kharkov</city>
            <other></other>
            <phone></phone>
            <phone_mobile>09999999</phone_mobile>
            <dni></dni>
            <deleted></deleted>
            <date_add></date_add>
            <date_upd></date_upd>
        </address>
    </prestashop>"""
    response = requests.post(ENDPOINT+"/addresses", data=payload,
                             headers={'Content-Type': 'application/xml'},
                             auth=(key, ""))
    assert response.status_code == 201
    print(response.text)
    id_xml = response.text.split("id")[1][slice(10, -5)]
    return id_xml



def test_can_call_endpoint():
    response_call = requests.get(ENDPOINT, auth=(key,""))
    assert response_call.status_code == 200
    print(response_call)



def test_can_create():
    payload = """<?xml version="1.0" encoding="UTF-8"?>
    <prestashop
        xmlns:xlink="http://www.w3.org/1999/xlink">
        <address>
            <id_customer></id_customer>
            <active>1</active>
            <id_manufacturer></id_manufacturer>
            <id_supplier></id_supplier>
            <id_warehouse></id_warehouse>
            <id_country>1</id_country>
            <id_state></id_state>
            <alias>Alina</alias>
            <company></company>
            <lastname>Gladkaya</lastname>
            <firstname>Alina</firstname>
            <vat_number></vat_number>
            <address1>Pushkinskaya str</address1>
            <address2></address2>
            <postcode>61000</postcode>
            <city>Kharkov</city>
            <other></other>
            <phone></phone>
            <phone_mobile>09999999</phone_mobile>
            <dni></dni>
            <deleted></deleted>
            <date_add></date_add>
            <date_upd></date_upd>
        </address>
    </prestashop>"""
    response = requests.post(ENDPOINT+"/addresses", data=payload,
                             headers={'Content-Type': 'application/xml'},
                             auth=(key, ""))
    assert response.status_code == 201
    print(response.text)
    id_xml = response.text.split("id")[1][slice(10, -5)]
    print(id_xml)
    assert id_xml.isdigit(), "returned id was not correct"




def test_get_url():
    response_get = requests.get(ENDPOINT+"/addresses/"+created_address_id(), auth=(key,""))
    print(response_get.url)
    print(response_get.text)


def test_can_update():
    payload = f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop
    xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id>{created_address_id()}</id>
        <active></active>
        <id_manufacturer></id_manufacturer>
        <id_supplier></id_supplier>
        <id_warehouse></id_warehouse>
        <id_country>1</id_country>
        <id_state></id_state>
        <alias>Alina</alias>
        <company></company>
        <lastname>Gladkaya</lastname>
        <firstname>Alina</firstname>
        <vat_number></vat_number>
        <address1>Svobody str</address1>
        <address2></address2>
        <postcode></postcode>
        <city>Kiev</city>
        <other></other>
        <phone></phone>
        <phone_mobile>0661446544</phone_mobile>
        <dni></dni>
        <deleted></deleted>
        <date_add></date_add>
        <date_upd></date_upd>
    </address>
</prestashop>"""
    response = requests.put(ENDPOINT+"/addresses", data=payload,
                               headers={'Content-Type': 'application/xml'}, auth=(key,""))
    print(response.text)




def test_can_delete():
    response = requests.delete(ENDPOINT+"/addresses/"+created_address_id(),
                               headers={'Content-Type': 'application/xml'}, auth=(key,""))
    assert response.status_code == 200
    print(response.text)












