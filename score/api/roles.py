from score.api.serializers import PersonSerializer
import requests
import json

def request_query_cpf(cpf, scale):
    body = json.dumps({u"cpf": cpf})
    query_scale = scale
    url = u"https://onkm73wqfd.execute-api.sa-east-1.amazonaws.com/prd/score"

    request = requests.post(url, data=body)
    result = request.json()
    try:
        result = float(result[55:-2])
        return calculating_score(result, query_scale)
    except:
        return 'error'

    
def calculating_score(scoring, scale):
    if scale == 1:
        response = scoring / 100
    elif scale == 10:
        response = scoring / 10
    elif scale == 100:
        response = scoring
    elif scale == 1000:
        response = scoring * 10
    else:
        return 'error'

    return round(float(response), 2)


def verify_validation(data):
    serializer = PersonSerializer(data=data)
    if serializer.is_valid():
        return True
