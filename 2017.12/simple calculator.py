import wx

class MyCalculator(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,
						size = (337,460),
						pos = (800,300))
		panel = wx.Panel(frame,-1)

		#add textbox to show result

		self.textResult = wx.TextCtrl(panel,-1,'0',size=(320,70),pos=(0,0),style=wx.TE_READONLY)

		#add number's button

		self.btnNumber7 = wx.Button(panel,-1,'7',size=(80,70),pos=(0,70))
		self.btnNumber8 = wx.Button(panel,-1,'8',size=(80,70),pos=(80,70))
		self.btnNumber9 = wx.Button(panel,-1,'9',size=(80,70),pos=(160,70))
		self.btnNumber4 = wx.Button(panel,-1,'4',size=(80,70),pos=(0,140))
		self.btnNumber5 = wx.Button(panel,-1,'5',size=(80,70),pos=(80,140))
		self.btnNumber6 = wx.Button(panel,-1,'6',size=(80,70),pos=(160,140))
		self.btnNumber1 = wx.Button(panel,-1,'1',size=(80,70),pos=(0,210))
		self.btnNumber2 = wx.Button(panel,-1,'2',size=(80,70),pos=(80,210))
		self.btnNumber3 = wx.Button(panel,-1,'3',size=(80,70),pos=(160,210))
		self.btnNumber0 = wx.Button(panel,-1,'0',size=(160,70),pos=(0,280))

		#add compute sign's button

		self.btnSignDot = wx.Button(panel,-1,'.',size=(80,70),pos=(160,280))
		self.btnSignDiv = wx.Button(panel,-1,'÷',size=(80,70),pos=(240,70))
		self.btnSignMul = wx.Button(panel,-1,'×',size=(80,70),pos=(240,140))
		self.btnSignMin = wx.Button(panel,-1,'-',size=(80,70),pos=(240,210))
		self.btnSignPlu = wx.Button(panel,-1,'+',size=(80,70),pos=(240,280))
		self.btnSignEq = wx.Button(panel,-1,'=',size=(160,70),pos=(160,350))

		#add function button

		self.btnClear = wx.Button(panel,-1,'C',size=(160,70),pos=(0,350))

		#bind button's events

		self.Bind(wx.EVT_BUTTON,self.OnBtnN0,self.btnNumber0)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN1,self.btnNumber1)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN2,self.btnNumber2)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN3,self.btnNumber3)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN4,self.btnNumber4)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN5,self.btnNumber5)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN6,self.btnNumber6)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN7,self.btnNumber7)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN8,self.btnNumber8)
		self.Bind(wx.EVT_BUTTON,self.OnBtnN9,self.btnNumber9)

		self.Bind(wx.EVT_BUTTON,self.OnBtnSdot,self.btnSignDot)
		self.Bind(wx.EVT_BUTTON,self.OnBtnSd,self.btnSignDiv)
		self.Bind(wx.EVT_BUTTON,self.OnBtnSmul,self.btnSignMul)
		self.Bind(wx.EVT_BUTTON,self.OnBtnSmin,self.btnSignMin)
		self.Bind(wx.EVT_BUTTON,self.OnBtnSplu,self.btnSignPlu)
		self.Bind(wx.EVT_BUTTON,self.OnBtnSeq,self.btnSignEq)

		self.Bind(wx.EVT_BUTTON,self.OnBtnClear,self.btnClear)

		frame.Show()
		return True


	#definit the button event
	
	var1 = '0'
	var2 = '0'
	judge = ''

	def OnBtnClear(self,event):
		self.textResult.SetValue('0')

	def OnBtnSdot(self,event):
		var = self.textResult.GetValue()
		self.textResult.Value =var+'.'

	def OnBtnN0(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('0')
		else:
			self.textResult.SetValue(var + '0')

	def OnBtnN1(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('1')
		else:
			self.textResult.SetValue(var + '1')

	def OnBtnN2(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('2')
		else:
			self.textResult.SetValue(var + '2')

	def OnBtnN3(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('3')
		else:
			self.textResult.SetValue(var + '3')

	def OnBtnN4(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('4')
		else:
			self.textResult.SetValue(var + '4')

	def OnBtnN5(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('5')
		else:
			self.textResult.SetValue(var + '5')

	def OnBtnN6(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('6')
		else:
			self.textResult.SetValue(var + '6')

	def OnBtnN7(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('7')
		else:
			self.textResult.SetValue(var + '7')

	def OnBtnN8(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('8')
		else:
			self.textResult.SetValue(var + '8')

	def OnBtnN9(self,event):
		var = self.textResult.GetValue()
		if var == '0':
			self.textResult.SetValue('9')
		else:
			self.textResult.SetValue(var + '9')


	def OnBtnSplu(self,event):
		self.var1 = float(self.textResult.GetValue())
		self.judge='+'
		self.textResult.Value = '0'

	def OnBtnSmin(self,event):
		self.var1 = float(self.textResult.GetValue())
		self.judge='-'
		self.textResult.Value ='0'
	
	def OnBtnSmul(self,event):
		self.var1 = float(self.textResult.GetValue())
		self.judge='*'
		self.textResult.Value ='0'

	def OnBtnSd(self,event):
		self.var1 = float(self.textResult.GetValue())
		self.judge='/'
		self.textResult.Value ='0'

	def OnBtnSeq(self,event):
		self.var2 = float(self.textResult.GetValue())
		if self.judge =='+':
			self.textResult.Value = str(self.var1+self.var2)
		elif self.judge =='-':
			self.textResult.Value = str(self.var1-self.var2)
		elif self.judge =='*':
			self.textResult.Value = str(self.var1*self.var2)
		elif self.judge =='/':
			self.textResult.Value = str(self.var1/self.var2)
	


if __name__ == '__main__':
	calculator = MyCalculator()
	calculator.MainLoop()
