from ansible.module_utils.basic import *

def user_shell_print(username):
  try:
    import pwd
    return [entry.pw_shell for entry in pwd.getpwall() if entry.pw_name==username][0]
  except:
    module.fail_json(msg="Module pwd not found")


def main():

  module = AnsibleModule(argument_spec = dict(username = dict(required=True)))
  username = module.params.get("username")

  usr_shell = user_shell_print(username)
  if usr_shell:
    msg = "{0} is found".format(username)
    msg = "{} is users shell".format(usr_shell)
  else:
    msg = "{0} is not present".format(username)

  module.exit_json(change=True, msg="User not found")



main()
