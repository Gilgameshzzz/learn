### 请求地址
        POST /user/register

### 请求参数

- mobile str '手机号'
- imagecode str '验证码'
- passwd str '密码1'
- passwd2 str '确认密码2'

### 响应结果

- 失败响应
    {'code':1000, 'msg': '验证码错误'}
    {'code':1001, 'msg': '请填写完整的注册信息'}
    {'code':1002, 'msg': '手机格式不正确'}
    {'code':1003, 'msg': '两次密码不一致'}
    {'code':1004, 'msg': '密码错误'}
    {'code':1005, 'msg': '请填写完整登录信息'}
    {'code': 1006, 'msg': '该手机未注册'}
    
- 成功响应
    {'code':200, 'msg':'请求成功'}
   
### 响应参数
- msg str '响应信息'
- code int '状态码'
