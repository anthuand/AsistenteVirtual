from wit import Wit


def witai(comando):
    access_token = "Aquiva el toke de Wit_ai"
    client = Wit(access_token=access_token)
    response = client.message(comando)
    # print(response)
    for x in response['intents']:
        if x['confidence'] > 0.5:
            nombre = (x['name'])
            print(nombre)
            if 'wit$message_body:message_body' in response["entities"]:
                values = response['entities']['wit$message_body:message_body']
                print(values[0]['body'])
                return nombre, values[0]['body']
            else:
                values = 'no hay valores del body'
                return nombre, values
    print("la respuesta devueltano es confiable")
    return 'nohay','nohay'

