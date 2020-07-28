
import time

def sleep(n_secs):
    time.sleep(n_secs)

def get_timestamp():
    return str(int(time.time() * 10))

def get_base_url(env_type="prod"):
    if env_type == "prod":
        return "http://10.23.190.107/zhgd_mms"  
    else:
        return "http://test.com/zhgd_mms"