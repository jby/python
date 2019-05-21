import json
import csv

username_by_email={}

with open ("ad-users.csv", "r") as AD_users:
    ad_users = csv.reader(AD_users, delimiter=',')
    for ad_user in ad_users:
        username_by_email[ad_user[3]] = ad_user[0]

with open ("users.json", "r") as HC_users:
    hc_users = json.load(HC_users)
    for hc_user in hc_users:
        user=hc_user['User']
        if ('is_deleted' in user and user["is_deleted"] == True):
            continue
        if user['email'] not in username_by_email:
            continue
        user["mention_name"]=username_by_email[user["email"]]
        print('User: %24s"\t"Mention Name: %s' % (user['name'],user['mention_name']))

with open ("users_modified.json", "w") as f:
    f.write(json.dumps(hc_users, indent=4))