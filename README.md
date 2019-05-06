# python
Misc python scripts

* normalize_hc_username.py - convert stupid HipChat mention_names to proper usernames from AD, using an AD-export of users in CSV-format

  Make an export of all data in your HipChat server, decrypt and unpack the export locally, make a CSV-file of AD users containing (Full Name, username (sAMAccountName), email address), put the AD exported CSV-file in the same dir as users.json from HipChat export, run this and you'll get a users_modified.json that could be used instead of users.json when importing into for instance Rocket.chat or Mattermost with AD/LDAP authentication enabled.
  
