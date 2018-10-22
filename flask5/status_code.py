# Filename  : status_code.py
# Date  : 2018/10/15

USER_REGISTER_MOBILE_INVALID = {'code': 1000, 'msg': '请输入正确的手机号'}

USER_REGISTER_MOBILE_EXSIST = {'code': 1001, 'msg': '该手机号已注册，请登录'}

USER_REGISTER_PASSWORD_LESS = {'code': 1002, 'msg': '密码不少于6个字符'}

USER_LOGIN_PASSWORD_ERROR = {'code': 1004, 'msg': '密码错误'}

USER_LOGIN_INFO_VALID = {'code': 1005, 'msg': '请填写完整信息'}

USER_LOGIN_MOBILE_INVALID = {'code': 1006, 'msg': '该手机未注册'}

USER_AUTH_ID_ERRRE = {'code': 1008, 'msg': '请输入正确的身份证'}

SUCCESS = {'code': 200, 'msg': '请求成功'}