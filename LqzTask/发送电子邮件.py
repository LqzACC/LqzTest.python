import smtplib,imapclient,pprint,pyzmail,imaplib,openpyxl,sys
imaplib._MAXLINE = 10000000


"""
#发送邮件
email=smtplib.SMTP('smtp.qq.com',587)
email.ehlo()#250表示成功
email.starttls()#220表示系统就绪
email.login('1506947494@qq.com',
            'oaiihtxylztpjgid'
            )
#235系统认证成功,邮箱授权码设置为密码
email.sendmail('1506947494@qq.com',
               input('请输入收件人邮箱:'),
               'Subject:'+input('右键标题:')+'\n'+input('请输入邮件内容:')+' '*4
               )
email.quit()
"""

"""
#第三方登陆邮件
pullemail=imapclient.IMAPClient('smtp.qq.com',ssl=True)
pullemail.login('1506947494@qq.com',
                'oaiihtxylztpjgid'
                )
pprint.pprint(pullemail.list_folders())
pullemail.select_folder('INBOX',readonly=False)
pu=pullemail.search(['ON 02-Jul-2021'])
rawmessage=pullemail.fetch(pu,['BODY[]'])
pprint.pprint(rawmessage)
message=pyzmail.PyzMessage.factory(rawmessage[7][b'BODY[]'])
print(message.get_addresses('from')+message.get_addresses('to'))#用'+'生成一个元组列表,用','生成两个元组列表
print(message.text_part!=None)#False是html文件，True是text文件
print(message.html_part!=None)#False是text文件，True是html文件
text=open('D:\\代码\\python块包\\pagehtml.html','wb')#'w'是写入,'wb'是二进制写入，后续需要对待写入字符串进行encode()及decode()操作
a=message.html_part.get_payload().decode(message.html_part.charset)
a=a.encode()#open中的参数为'wb'时，需要对字符串进行.encode()编码操作
#print(message.text_part.get_payload().decode(message.text_part.charset))
text.write(a)
text.close()
pullemail.delete_messages(pu)
#pullemail.expunge()
pullemail.logout()
"""

"""
#导入发送邮件
vip=openpyxl.load_workbook('D:\\代码\\python块包\\automate_online-materials\\duesRecords.xlsx')
vsheet=vip.get_sheet_by_name('Sheet1')
lastcol=vsheet.max_column
maxrow=vsheet.max_row
#get_highest_row()和get_highest_column()在最新版的openpyxl模块中已经被删除了，取而代之的是max_row和max_column两个方法。
memberdict={}
for i in range(2,maxrow+1):
    lastmonth=vsheet.cell(row=i,column=lastcol).value
    if vsheet.cell(row=i,column=lastcol).value=='paid':
        print(vsheet.cell(row=i,column=1).value+'paid')
    else:
        print(type(vsheet.cell(row=i,column=1).value))
        name=vsheet.cell(row=i,column=1).value
        email=vsheet.cell(row=i,column=2).value
        memberdict[name]=email
pprint.pprint(memberdict)

for name,email in memberdict.items():
    email=smtplib.SMTP('smtp.qq.com',587)
    email.ehlo()#250表示成功
    email.starttls()#220表示系统就绪
    email.login('1506947494@qq.com',
                'oaiihtxylztpjgid'
                )
                #235系统认证成功,邮箱授权码设置为密码
    try:
        email.sendmail('1506947494@qq.com',
                       email,
                       'Subject:'+input('右键标题:')+'\n'+input('请输入邮件内容:')+' '*4
                       )
    except BaseException as err:
        print(email+'send err')
    else:
        print('send success')
email.quit()
"""