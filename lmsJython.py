from javax.swing import *
from javax.swing.table import DefaultTableModel

from com.ziclix.python.sql import zxJDBC
import os
import sys
from java.util import Properties
sys.path.append('/root/Desktop/mysql-connector-java-5.1.42.jar')
import com.mysql.jdbc.Driver as Driver
props=Properties()
props.put('user','root')
props.put('password','redhat')
mysqlConn=zxJDBC.connect(Driver().connect('jdbc:mysql://localhost/library',props))
cursor=mysqlConn.cursor()

#Home Screen
homeframe = JFrame("Home")
homeframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
homeframe.setLocation(550,200)
homeframe.setSize(700,500)
homepanel = JPanel()
homepanel.setLayout(None)
homeframe.add(homepanel)


def checkUserLogin(uname,pswd):
	sql="SELECT * FROM user WHERE uname = '"+uname+"' and pswd = '"+pswd+"'"
	cursor.execute(sql)
	data = cursor.fetchall()
	return data



def aoptions(aframe):
	#admin options frame
	aoframe = JFrame("Library Management System")
	aoframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	aoframe.setLocation(550,200)
	aoframe.setSize(700,500)
	aopanel = JPanel()
	aopanel.setLayout(None)
	aoframe.add(aopanel)
		
	def addbook():
		addbookframe = JFrame("Library Management System")
		addbookframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		addbookframe.setLocation(550,200)
		addbookframe.setSize(700,500)
		panel = JPanel()
		panel.setLayout(None)
		addbookframe.add(panel)
		def OnClick(event):
			sql="INSERT INTO books (name,author) VALUES ('"+txtn.getText()+"','"+txta.getText()+"')"
			try:
				cursor.execute(sql)
				mysqlConn.commit()
				print "addbook"
			except:
				mysqlConn.rollback()
		lbltitle = JLabel("Fill Book Details")
		lbltitle.setBounds(270,40,500,50)
		lbln = JLabel("Book Name: ")
		lbln.setBounds(200,150,100,30)
		txtn = JTextField(10)
		txtn.setBounds(350,150,100,30)
		lbla = JLabel("Author: ")
		lbla.setBounds(200,200,100,30)
		txta = JTextField(10)
		txta.setBounds(350,200,100,30)
		btn = JButton("Add Book",actionPerformed=OnClick)
		btn.setBounds(220,250,200,40)
		def OnClickBack(event):
			aoframe.setVisible(True)
			addbookframe.setVisible(False)
		btnback = JButton("Back",actionPerformed=OnClickBack)
		btnback.setBounds(220,300,200,40)
		panel.add(btnback)
		panel.add(lbltitle)
		panel.add(lbln)
		panel.add(txtn)
		panel.add(lbla)
		panel.add(txta)
		panel.add(btn)
		aoframe.setVisible(False)
		addbookframe.setVisible(True)
	
	def bookdetails():
		bdframe = JFrame("Library Management System")
		bdframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		bdframe.setLocation(550,200)
		bdframe.setSize(800,500)
		panel = JPanel()
		panel.setLayout(None)
		bdframe.add(panel)
		def OnClick(event):
			sql="SELECT name,author FROM books WHERE name = '"+txtn.getText()+"'"
			try:
				cursor.execute(sql)
				tableData = cursor.fetchall()
				if len(tableData) != 0:
					print tableData
					colNames = ('User Name','Book Issued','Date of Issue','Mobile No.','Email Id','Address','Date of Joining')
					dataModel = DefaultTableModel(tableData, colNames)
					table = JTable(dataModel)
					#table.setBounds(20,200,700,100)
					scrollPane = JScrollPane()
					scrollPane.setPreferredSize(Dimension(700,100))
					scrollPane.getViewport().setView((table))
					panel.add(scrollPane)
					print "bookd"
			except:
				mysqlConn.rollback()
		lbltitle = JLabel("BOOK DETAILS")
		lbltitle.setBounds(300,50,500,50)
		lbln = JLabel("User Name: ")
		lbln.setBounds(230,100,100,30)
		txtn = JTextField(10)
		txtn.setBounds(380,100,100,30)
		btn = JButton("Book Details",actionPerformed=OnClick)
		btn.setBounds(250,150,200,40)
		def OnClickBack(event):
			aoframe.setVisible(True)
			bdframe.setVisible(False)
		btnback = JButton("Back",actionPerformed=OnClickBack)
		btnback.setBounds(250,200,200,40)
		panel.add(btnback)
		panel.add(lbltitle)
		panel.add(lbln)
		panel.add(txtn)
		panel.add(btn)
		aoframe.setVisible(False)
		bdframe.setVisible(True)
	
	def removebook():
		rmvbookframe = JFrame("Library Management System")
		rmvbookframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		rmvbookframe.setLocation(550,200)
		rmvbookframe.setSize(700,500)
		panel = JPanel()
		panel.setLayout(None)
		rmvbookframe.add(panel)
		def OnClick(event):
			sql="DELETE FROM books WHERE name = '"+txtn.getText()+"' and author = '"+txta.getText()+"'"
			try:
				cursor.execute(sql)
				mysqlConn.commit()
				print "rmvbook"
			except:
				mysqlConn.rollback()
		lbltitle = JLabel("Fill Book Details")
		lbltitle.setBounds(270,40,500,50)
		lbln = JLabel("Book Name: ")
		lbln.setBounds(200,150,100,30)
		txtn = JTextField(10)
		txtn.setBounds(350,150,100,30)
		lbla = JLabel("Author: ")
		lbla.setBounds(200,200,100,30)
		txta = JTextField(10)
		txta.setBounds(350,200,100,30)
		btn = JButton("Remove Book",actionPerformed=OnClick)
		btn.setBounds(220,250,200,40)
		def OnClickBack(event):
			aoframe.setVisible(True)
			rmvbookframe.setVisible(False)
		btnback = JButton("Back",actionPerformed=OnClickBack)
		btnback.setBounds(220,300,200,40)
		panel.add(btnback)
		panel.add(lbltitle)
		panel.add(lbln)
		panel.add(txtn)
		panel.add(lbla)
		panel.add(txta)
		panel.add(btn)
		aoframe.setVisible(False)
		rmvbookframe.setVisible(True)
	
	def adduser():
		
		adduserframe = JFrame("Library Management System")
		adduserframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		adduserframe.setLocation(550,200)
		adduserframe.setSize(700,500)
		panel = JPanel()
		panel.setLayout(None)
		adduserframe.add(panel)
		def OnClick(event):
			sql="INSERT INTO user (uname,pswd,mobno,emailid,address,doj) VALUES ('"+txtu.getText()+"','"+txtp.getText()+"','"+txtmn.getText()+"','"+txteid.getText()+"','"+txtaddr.getText()+"','"+txtdoj.getText()+"')"
			try:
				cursor.execute(sql)
				mysqlConn.commit()
				print "adduser"
			except:
				mysqlConn.rollback()
		lbltitle = JLabel("ADD NEW STUDENT")
		lbltitle.setBounds(270,40,500,50)
		lblu = JLabel("User Name: ")
		lblu.setBounds(200,100,100,30)
		txtu = JTextField(10)
		txtu.setBounds(350,100,100,30)
		lblp = JLabel("Password: ")
		lblp.setBounds(200,150,100,30)
		txtp = JTextField(10)
		txtp.setBounds(350,150,100,30)
		lblmn = JLabel("Mobile No.: ")
		lblmn.setBounds(200,200,100,30)
		txtmn = JTextField(10)
		txtmn.setBounds(350,200,100,30)
		lbleid = JLabel("Email Id: ")
		lbleid.setBounds(200,250,100,30)
		txteid = JTextField(10)
		txteid.setBounds(350,250,100,30)
		lbladdr = JLabel("Address: ")
		lbladdr.setBounds(200,300,100,30)
		txtaddr = JTextField(10)
		txtaddr.setBounds(350,300,100,30)
		lbldoj = JLabel("Date of Joining: ")
		lbldoj.setBounds(200,350,150,30)
		txtdoj = JTextField(10)
		txtdoj.setBounds(350,350,100,30)
		btn = JButton("Add Student",actionPerformed=OnClick)
		btn.setBounds(220,400,200,40)
		def OnClickBack(event):
			aoframe.setVisible(True)
			adduserframe.setVisible(False)
		btnback = JButton("Back",actionPerformed=OnClickBack)
		btnback.setBounds(220,450,200,40)
		panel.add(btnback)
		panel.add(lbltitle)
		panel.add(lblu)
		panel.add(txtu)
		panel.add(lblp)
		panel.add(txtp)
		panel.add(lblmn)
		panel.add(txtmn)
		panel.add(lbleid)
		panel.add(txteid)
		panel.add(lbladdr)
		panel.add(txtaddr)
		panel.add(lbldoj)
		panel.add(txtdoj)
		panel.add(btn)
		aoframe.setVisible(False)
		adduserframe.setVisible(True)
	
	def removeuser():
		rmvuserframe = JFrame("Library Management System")
		rmvuserframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		rmvuserframe.setLocation(550,200)
		rmvuserframe.setSize(700,500)
		panel = JPanel()
		panel.setLayout(None)
		rmvuserframe.add(panel)
		def OnClick(event):
			sql="DELETE FROM user WHERE uname = '"+txtu.getText()+"'"
			try:
				cursor.execute(sql)
				mysqlConn.commit()
				print "rmvuser"
			except:
				mysqlConn.rollback()
		lbltitle = JLabel("REMOVE STUDENT")
		lbltitle.setBounds(270,50,500,50)
		lblu = JLabel("User Name: ")
		lblu.setBounds(200,150,100,30)
		txtu = JTextField(10)
		txtu.setBounds(350,150,100,30)
		btn = JButton("Remove Student",actionPerformed=OnClick)
		btn.setBounds(220,250,200,40)
		def OnClickBack(event):
			aoframe.setVisible(True)
			rmvuserframe.setVisible(False)
		btnback = JButton("Back",actionPerformed=OnClickBack)
		btnback.setBounds(220,300,200,40)
		panel.add(btnback)
		panel.add(lbltitle)
		panel.add(lblu)
		panel.add(txtu)
		panel.add(btn)
		aoframe.setVisible(False)
		rmvuserframe.setVisible(True)
	
	def userdetails():
		udframe = JFrame("Library Management System")
		udframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		udframe.setLocation(550,200)
		udframe.setSize(800,500)
		panel = JPanel()
		panel.setLayout(None)
		udframe.add(panel)
		def OnClick(event):
			aoframe.setVisible(False)
			sql="SELECT uname,bissued,dissue,mobno,emailid,address,doj FROM user WHERE uname = '"+txtu.getText()+"'"
			try:
				cursor.execute(sql)
				tableData = cursor.fetchall()
				if len(tableData) != 0:
					print tableData
					colNames = ('User Name','Book Issued','Date of Issue','Mobile No.','Email Id','Address','Date of Joining')
					dataModel = DefaultTableModel(tableData, colNames)
					table = JTable(dataModel)
					#table.setBounds(20,200,700,100)
					scrollPane = JScrollPane()
					scrollPane.setPreferredSize(Dimension(700,100))
					scrollPane.getViewport().setView((table))
					panel.add(scrollPane)
					print "userd"
			except:
				mysqlConn.rollback()
		lbltitle = JLabel("STUDENT DETAILS")
		lbltitle.setBounds(300,50,500,50)
		lblu = JLabel("User Name: ")
		lblu.setBounds(230,100,100,30)
		txtu = JTextField(10)
		txtu.setBounds(380,100,100,30)
		btn = JButton("Student Details",actionPerformed=OnClick)
		btn.setBounds(250,150,200,40)
		def OnClickBack(event):
			aoframe.setVisible(True)
			udframe.setVisible(False)
		btnback = JButton("Back",actionPerformed=OnClickBack)
		btnback.setBounds(250,200,200,40)
		panel.add(btnback)
		panel.add(lbltitle)
		panel.add(lblu)
		panel.add(txtu)
		panel.add(btn)
		udframe.setVisible(True)
		
	
	def OnCheck(event):
		if rb1.isSelected():
			addbook()
		elif rb2.isSelected():
			bookdetails()
		elif rb3.isSelected():
			removebook()
		elif rb4.isSelected():
			adduser()
		elif rb5.isSelected():
			removeuser()
		else:
			userdetails()
	aolbltitle = JLabel("ADMIN PANEL")
	aolbltitle.setBounds(270,40,500,50)
	rb1 = JRadioButton("Add New Books", actionPerformed = OnCheck)
	rb1.setBounds(200,100,400,20)
	rb2 = JRadioButton("Books Details", actionPerformed = OnCheck)
	rb2.setBounds(200,130,400,20)
	rb3 = JRadioButton("Remove Books", actionPerformed = OnCheck)
	rb3.setBounds(200,160,400,20)
	rb4 = JRadioButton("Add User", actionPerformed = OnCheck)
	rb4.setBounds(200,190,400,20)
	rb5 = JRadioButton("Remove User", actionPerformed = OnCheck)
	rb5.setBounds(200,220,400,20)
	rb6 = JRadioButton("User Details", actionPerformed = OnCheck)
	rb6.setBounds(200,250,400,20)
	def OnClickBack(event):
		homeframe.setVisible(True)
		aoframe.setVisible(False)
	btnback = JButton("Logout",actionPerformed=OnClickBack)
	btnback.setBounds(200,300,200,40)
	aopanel.add(btnback)
	grp = ButtonGroup()
	grp.add(rb1)
	grp.add(rb2)
	grp.add(rb3)
	grp.add(rb4)
	grp.add(rb5)
	grp.add(rb6)
	aopanel.add(aolbltitle)
	aopanel.add(rb1)
	aopanel.add(rb2)
	aopanel.add(rb3)
	aopanel.add(rb4)
	aopanel.add(rb5)
	aopanel.add(rb6)
	aframe.setVisible(False)
	aoframe.setVisible(True)



def soptions(sframe,uname):
	#student options frame
	soframe = JFrame("Library Management System")
	soframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	soframe.setLocation(550,200)
	soframe.setSize(700,500)
	sopanel = JPanel()
	sopanel.setLayout(None)
	soframe.add(sopanel)
	
	def borrowbook():
		bframe = JFrame("Library Management System")
		bframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		bframe.setLocation(550,200)
		bframe.setSize(800,500)
		panel = JPanel()
		panel.setLayout(None)
		bframe.add(panel)
		def OnClick(event):
			sql1="SELECT * FROM books WHERE name = '"+txtn.getText()+"'"
			cursor.execute(sql1)
			book = cursor.fetchall()
			if len(book)!=0:
				sql2="UPDATE user SET bissued='"+txtn.getText()+"', dissue='"+txtd.getText()+"' WHERE uname ='"+uname+"'"
				try:
					cursor.execute(sql2)
					mysqlConn.commit()
					print "borrowbook"
				except:
					mysqlConn.rollback()
		lbltitle = JLabel("BORROW A BOOK")
		lbltitle.setBounds(270,40,500,50)
		lbln = JLabel("Book Name: ")
		lbln.setBounds(200,100,100,30)
		txtn = JTextField(10)
		txtn.setBounds(350,100,100,30)
		lbla = JLabel("Author: ")
		lbla.setBounds(200,150,100,30)
		txta = JTextField(10)
		txta.setBounds(350,150,100,30)
		lbld = JLabel("Date of Issue: ")
		lbld.setBounds(200,200,100,30)
		txtd = JTextField(10)
		txtd.setBounds(350,200,100,30)
		btn = JButton("Borrow Book",actionPerformed=OnClick)
		btn.setBounds(220,250,200,40)
		def OnClickBack(event):
			soframe.setVisible(True)
			bframe.setVisible(False)
		btnback = JButton("Back",actionPerformed=OnClickBack)
		btnback.setBounds(220,300,200,40)
		panel.add(btnback)
		panel.add(lbltitle)
		panel.add(lbln)
		panel.add(txtn)
		panel.add(lbla)
		panel.add(txta)
		panel.add(lbld)
		panel.add(txtd)
		panel.add(btn)
		soframe.setVisible(False)
		bframe.setVisible(True)
	
	def returnbook():
		rframe = JFrame("Library Management System")
		rframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		rframe.setLocation(550,200)
		rframe.setSize(800,500)
		panel = JPanel()
		panel.setLayout(None)
		rframe.add(panel)
		def OnClick(event):
			sql1="SELECT * FROM books WHERE name = '"+txtn.getText()+"'"
			cursor.execute(sql1)
			book = cursor.fetchall()
			if len(book)!=0:
				bn=None
				di=None
				sql2="UPDATE user SET bissued='"+str(bn)+"', dissue='"+str(di)+"' WHERE uname ='"+uname+"'"
				try:
					cursor.execute(sql2)
					mysqlConn.commit()
					print "rtnbook"
				except:
					mysqlConn.rollback()
		lbltitle = JLabel("RETURN A BOOK")
		lbltitle.setBounds(270,50,500,50)
		lbln = JLabel("Book Name: ")
		lbln.setBounds(200,150,100,30)
		txtn = JTextField(10)
		txtn.setBounds(350,150,100,30)
		lbla = JLabel("Author: ")
		lbla.setBounds(200,200,100,30)
		txta = JTextField(10)
		txta.setBounds(350,200,100,30)
		btn = JButton("Return Book",actionPerformed=OnClick)
		btn.setBounds(220,250,200,40)
		def OnClickBack(event):
			soframe.setVisible(True)
			rframe.setVisible(False)
		btnback = JButton("Back",actionPerformed=OnClickBack)
		btnback.setBounds(220,300,200,40)
		panel.add(btnback)
		panel.add(lbltitle)
		panel.add(lbln)
		panel.add(txtn)
		panel.add(lbla)
		panel.add(txta)
		panel.add(btn)
		soframe.setVisible(False)
		rframe.setVisible(True)
		
	
	def OnCheck(event):
		if rb1.isSelected():
			borrowbook()
		else:
			returnbook()
	solbltitle = JLabel("STUDENT PANEL")
	solbltitle.setBounds(270,40,500,50)
	rb1 = JRadioButton("Borrow Book", actionPerformed = OnCheck)
	rb1.setBounds(200,150,400,20)
	rb2 = JRadioButton("Return Book", actionPerformed = OnCheck)
	rb2.setBounds(200,250,400,20)
	def OnClickBack(event):
		homeframe.setVisible(True)
		soframe.setVisible(False)
	btnback = JButton("Logout",actionPerformed=OnClickBack)
	btnback.setBounds(220,300,200,40)
	sopanel.add(btnback)
	grp = ButtonGroup()
	grp.add(rb1)
	grp.add(rb2)
	sopanel.add(solbltitle)
	sopanel.add(rb1)
	sopanel.add(rb2)
	sframe.setVisible(False)
	soframe.setVisible(True)


def clickhb1(event):
	#adminlogin
	aframe = JFrame("Library Management System")
	aframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	aframe.setLocation(550,200)
	aframe.setSize(700,500)
	apanel = JPanel()
	apanel.setLayout(None)
	aframe.add(apanel)
	def admin(event):
		uname = atxtu.getText()
		pswd = atxtp.getText()
		if uname=="admin" and pswd=="admin":
			aoptions(aframe)
	albltitle = JLabel("ADMIN LOGIN")
	albltitle.setBounds(270,40,500,50)
	alblu = JLabel("User Name: ")
	alblu.setBounds(200,100,100,40)
	atxtu = JTextField(10)
	atxtu.setBounds(350,100,100,40)
	alblp = JLabel("Password: ")
	alblp.setBounds(200,200,100,40)
	atxtp = JTextField(10)
	atxtp.setBounds(350,200,100,40)
	abtnl = JButton("Log in",actionPerformed=admin)
	abtnl.setBounds(220,300,200,40)
	apanel.add(alblu)
	apanel.add(atxtu)
	apanel.add(alblp)
	apanel.add(atxtp)
	apanel.add(abtnl)
	apanel.add(albltitle)
	aframe.setVisible(True)
	homeframe.setVisible(False)

def clickhb2(event):
	#studentlogin
	sframe = JFrame("Library Management System")
	sframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	sframe.setLocation(550,200)
	sframe.setSize(700,500)
	spanel = JPanel()
	spanel.setLayout(None)
	sframe.add(spanel)
	def student(event):
		suname = stxtu.getText()
		spswd = stxtp.getText()
		data = checkUserLogin(suname,spswd)
		if len(data) != 0:
			soptions(sframe,suname)
	slbltitle = JLabel("STUDENT LOGIN")
	slbltitle.setBounds(270,40,500,50)
	slblu = JLabel("User Name: ")
	slblu.setBounds(200,100,100,40)
	stxtu = JTextField(10)
	stxtu.setBounds(350,100,100,40)
	slblp = JLabel("Password: ")
	slblp.setBounds(200,200,100,40)
	stxtp = JTextField(10)
	stxtp.setBounds(350,200,100,40)
	sbtnl = JButton("Log in",actionPerformed=student)
	sbtnl.setBounds(220,300,200,40)
	spanel.add(slblu)
	spanel.add(stxtu)
	spanel.add(slblp)
	spanel.add(stxtp)
	spanel.add(sbtnl)
	spanel.add(slbltitle)
	sframe.setVisible(True)
	homeframe.setVisible(False)


hlbltitle = JLabel("WELCOME TO LIBRARY MANAGEMENT SYSTEM")
hlbltitle.setBounds(180,50,500,50)
hb1 = JButton("Admin Login",actionPerformed=clickhb1)
hb1.setBounds(100,200,200,40)
hb2 = JButton("Student Login",actionPerformed=clickhb2)
hb2.setBounds(400,200,200,40)
homepanel.add(hb1)
homepanel.add(hb2)
homepanel.add(hlbltitle)

homeframe.setVisible(True)
