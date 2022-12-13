import os

from micloud import MiCloud

from dotenv import load_dotenv

load_dotenv()

mc = MiCloud(
    os.environ.get('MI_CLOUD_USERNAME'),
    os.environ.get('MI_CLOUD_PASSWORD')
)
mc.login()
token = mc.get_token()
device_list = mc.get_devices(save=True, file="devices.json")
