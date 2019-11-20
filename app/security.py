from flask_appbuilder.security.sqla.manager import SecurityManager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_appbuilder.const import LOGMSG_WAR_SEC_LOGIN_FAILED

import logging

log = logging.getLogger(__name__)

class CustomSecurityManager(SecurityManager):

  def __init__(self, appbuilder):
    super(CustomSecurityManager, self).__init__(appbuilder)

  def auth_user_db(self, username, password):
    log.info('login intercept')
    """
        Method for authenticating user, auth db style
        :param username:
            The username or registered email address
        :param password:
            The password, will be tested against hashed password on db
    """
    if username is None or username == "":
      return None

    if not customFindUser(username):
      log.info(LOGMSG_WAR_SEC_LOGIN_FAILED.format(username))
      return None
    
    user = self.find_user(username=username)
    if customLoginAuth(username, password):
      if user is None:
        user = self.add_user(username=username, first_name='', last_name=username,
                             email=username+'@test.com',
                             role=self.find_role(self.auth_user_registration_role))
      self.update_user_auth_stat(user, True)
      return user
    else:
      if user is not None:
        self.update_user_auth_stat(user, False)
      log.info(LOGMSG_WAR_SEC_LOGIN_FAILED.format(username))
      return None

users = [
  {"username":"admin","password":"admin1234"},
  {"username":"user1","password":"1234"},
  {"username":"user2","password":"1234"},
  {"username":"user3","password":"1234"},
  {"username":"user4","password":"1234"}
]

def customFindUser(username):
  if any(user["username"] == username for user in users):
    return True
  return False

def customLoginAuth(username, password):
  user = next((user for user in users if user["username"] == username), None)
  return customPasswordCheck(user["password"], password)

def customPasswordCheck(password, inputPassword):
  return password == inputPassword