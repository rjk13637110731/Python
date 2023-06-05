team1 = [
    {
        'name': '乔丹',
        'height': 198
    },
    {
        'name': '姚明',
        'height': 223
    }
]

import json
team2 = json.loads(json.dumps(team1))

team2[0]['name']='麦迪'
print(team1[0]['name'])
