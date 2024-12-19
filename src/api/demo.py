from . import api, api_return, need_login, login_user, logout_user


@api.get("")
def hello():
    """
    #group  基础
    #name   hello
    #desc   测试接口
    #return code    <str>   验证码，只有测服会返回
    #output_example
    {
        "code": 0,
        "msg": "成功",
        "data": "Hello, World!"
    }
    """
    return api_return("OK", "Hello, World!")
