import qiniu
import uuid


def upload(pat):
    from maotai.config import global_config
    key = uuid.uuid4()
    access_key = global_config.getRaw('upload', 'access_key')
    secret_key = global_config.getRaw('upload', 'secret_key')
    bucket_name = global_config.getRaw('upload', 'bucket_name')
    q = qiniu.Auth(access_key, secret_key)
    key = '%s.png' % key
    token = q.upload_token(bucket_name, key)
    ret, info = qiniu.put_file(token, key, pat)

    bucket_domain = 'file.clickear.top'
    base_url = 'https://%s/%s' % (bucket_domain, key)
    if ret is not None:
        return base_url
