msg='啊'
byte_msg=msg.encode()
print('--default:[%s]'%byte_msg)
new_msg=byte_msg.decode()
print('--default:[%s]'%new_msg)

byte_msg=msg.encode('utf-8')
print('--utf-8:[%s]'%byte_msg)
new_msg=byte_msg.decode('utf-8')
print('--utf-8:[%s]'%new_msg)

byte_msg=msg.encode('gbk')
print('--gbk:[%s]'%byte_msg)
new_msg=byte_msg.decode('gbk')
print('--gbk:[%s]'%new_msg)

byte_msg=msg.encode('gb2312')
print('--gb2312:[%s]'%byte_msg)
new_msg=byte_msg.decode('gb2312')
print('--b2312:[%s]'%new_msg)
