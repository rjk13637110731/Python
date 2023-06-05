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

team2 = []

for one in team1:
    team2.append({'name': one['name'], 'height': one['height']})


team2[0]['name']='麦迪'
print(team1[0]['name'])
