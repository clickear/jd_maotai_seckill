
from maotai.config import  *

from helper.jd_helper import *
from upload.qiniu import *

if __name__ == "__main__":
    send_qr_image("他说他")
    # url = upload('logo','../qr_code.png')
    # print(url)