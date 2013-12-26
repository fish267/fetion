#!/usr/bin/python
#coding:utf-8

from Tkinter import *
import fetion
# 写界面呀写界面

root = Tk()
root.bind('<Control-q>', sys.exit)
Label(root, text = 'Sender:').grid(row = 0, column = 0)
Label(root, text = 'Password:').grid(row = 0, column = 1)
Label(root, text = 'Receiver:').grid(row = 0, column = 2)
# initial sender, password, receiver
sender = StringVar()
sender.set('******')
password = StringVar()
password.set('a******')
receiver = StringVar()
receiver.set('15******0')
# add some components
sender_entry = Entry(root, textvariable = sender)
sender_entry.grid(row = 1, column = 0)
password_entry = Entry(root, textvariable = password)
password_entry.grid(row = 1, column = 1)
receiver_entry = Entry(root, textvariable = receiver)
receiver_entry.grid(row = 1, column = 2)
# 这个让密码栏显示的是*
password_entry['show'] = '*'

Label(root, text = 'Content').grid(row = 2, column = 0, columnspan = 2)
content_text = Text(root, height = 10, width = 60)
content_text.grid(row = 3, column = 0, columnspan = 2, rowspan = 3)
# 两个按键，发送按键，另一个是发送天气预报的按键
weather_button = Button(root, text = 'Weather Info')
weather_button.grid(row = 3, column = 2)
send_button = Button(root, text = 'Send Message')
send_button.grid(row = 4, column = 2)
# 一个message，当状态栏吧

state = StringVar()
state.set('Welcome!')
fetion_state = Message(root, textvariable = state, width = 70)
fetion_state.grid(row = 5, column = 2)
# 发送信息
def send_message(evnet):
	f = fetion.Fetion()
	f.set_account(sender_entry.get(), password_entry.get())
	msg = u'%s' %content_text.get(1.0, END)
	print msg
	global state
	if len(msg) == 1:
		state.set('Are you kidding!')
	else:
		while f.send_msg(receiver_entry.get(), msg.encode('utf-8')) != 0:
			state.set('Sending.... Please wait')
			print 'sending..'
		state.set('Success!')
# 定义发送button的绑定行为
send_button.bind('<Button-1>', send_message)
root.mainloop()
