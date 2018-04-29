from yx import dm
from mail import send_mail

yxdm = dm()
dm_list = yxdm.get_dm_lists()
# print(dm_list)

output_message = '\n'.join(
    ['{}，{}，{}， 密码：{}'.format(name, series_name, pan_url, pan_password) for name, series_name, pan_url, pan_password in
     yxdm.get_detail(dm_list) if name is not None])

# 发送邮件
my_mail_fyx = send_mail(output_message, yxdm.addresses)