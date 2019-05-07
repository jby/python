import json
import csv

username_by_email={}

with open ("ad-users.csv", "r") as AD_users:
    ad_users = csv.reader(AD_users, delimiter=',')
    for ad_user in ad_users:
        username_by_email[ad_user[2]] = ad_user[1]

with open ("users.json", "r") as HC_users:
    hc_users = json.load(HC_users)
    for hc_user in hc_users:
        if hc_user["User"]["is_deleted"] == False:
            try:
                hc_user["User"]["mention_name"]=username_by_email[hc_user["User"]["email"]]
            except KeyError:
                pass

with open ("users_modified.json", "w") as f:
    f.write(json.dumps(hc_users, indent=4))