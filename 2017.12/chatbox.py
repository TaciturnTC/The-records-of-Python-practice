import wx,time

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"Tracy'Chat",size=(520,510))
		panel = wx.Panel(self)
		
		labelAll = wx.StaticText(panel,-1,'All Contents')
		self.textAll = wx.TextCtrl(panel,-1,size=(480,210),style=wx.TE_MULTILINE | wx.TE_READONLY)

		lebelIn = wx.StaticText(panel,-1,'My Chat')
		self.textIn = wx.TextCtrl(panel,-1,size=(480,140),style=wx.TE_MULTILINE)

		self.btnSend = wx.Button(panel,-1,'Send',size=(60,25))
		self.btnClear = wx.Button(panel,-1,'Clear',size=(60,25))

		self.Bind(wx.EVT_BUTTON,self.OnButtonSend,self.btnSend)
		self.Bind(wx.EVT_BUTTON,self.OnButtonClear,self.btnClear)

		btnSizer = wx.BoxSizer()
		btnSizer.Add(self.btnSend,proportion=0)
		btnSizer.Add(self.btnClear,proportion=0)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(labelAll,proportion=0,flag=wx.ALIGN_CENTER)
		mainSizer.Add(self.textAll,proportion=1,flag=wx.EXPAND)
		mainSizer.Add(lebelIn,proportion=0,flag=wx.ALIGN_CENTER)
		mainSizer.Add(self.textIn,proportion=1,flag=wx.EXPAND)
		mainSizer.Add(btnSizer,proportion=0,flag=wx.ALIGN_CENTER)

		panel.SetSizer(mainSizer)




	def OnButtonSend(self,event):
		userinput = self.textIn.GetValue()
		self.textIn.Clear()
		nowtime = time.ctime()
		inmsg = 'Tracy (%s):\n %s\n' %(nowtime,userinput)
		self.textAll.Append(inmsg)

	def OnButtonClear(self,event):
		self.textIn.Clear()


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
