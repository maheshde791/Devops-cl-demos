from ansible.module_utils.basic import *

def is_user_exist(username):
  try:
    import pwd
    return ( username in [entry.pw_name for entry in pwd.getpwall()])
  except:
    module.fail_json(msg="Module pwd not found")
def main():

  module = AnsibleModule(argument_spec = dict(username = dict(required=True)))
  username = module.params.get("username")

  exists = is_user_exist(username)
  if exists:
    msg = "{0} is found".format(username)
  else:
    msg = "{0} is not present".format(username)

  module.exit_json(change=True, msg="User not found")



main()
