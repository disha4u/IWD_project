# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:51:08 2018

@author: Disha Agarwal
"""

import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QMessageBox
from PyQt5.QtWidgets import QLineEdit,QPushButton,QGridLayout
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout
from time import sleep
from speechfn import tts,stt 
from selenium import webdriver

class login(QWidget):
    def __init__(self):
        super(login, self).__init__()
        self.make()
    def closee(self):
        text=self.URL.text()
        self.name.setText(text)
        '''url='https://goo.gl/forms/j6nLOdAKunpqva2n1'
        url2='https://docs.google.com/forms/d/e/1FAIpQLSey4s7_e4Dzcjl54u1dX8m2wdQelwmohvFccgEWevzxpfn8_Q/viewform'
        url_temp="https://docs.google.com/forms/d/e/1FAIpQLSfVnxAfzy1KMqzoFinX1FcFymXz-ZjoxQtcyed2ThEID9jkGA/viewform?usp=pp_url&entry.1904454057=Sebanti&entry.783816675=skjdsk@gmail.com"
        url_ask="https://docs.google.com/forms/d/1XDERTa2siKhTrz1L4p0epIYc0j91EOaLFYbkJRF9Aos/viewform?usp=pp_url&entry.1904454057=Sebanti&entry.783816675=hjhjdf"'''
        url_filled="https://docs.google.com/forms/d/e/1FAIpQLScJuIVSlCWV8nxmEJg0ZiwIG2nNIPL96ROlAZx56uLivM5JIQ/viewform?usp=pp_url&entry.1124689223=Sebanti&entry.239059333=Column+1&entry.686868202=Option+1"
        br=webdriver.Chrome()
        try: 
            
            br.get(text)
        except:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Check WIFI connection")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            
        x=br.execute_script("return FB_PUBLIC_LOAD_DATA_")
        br.close()
        qs=[]
        self.ques_read=[]
        self.quess=[]
        self.anss=[]
        self.anss_edit=[]
        for l in x[1][1]:
            y=[]
            y.append(l[1])
            str=""
            if len(l[4][0])>5:
                y.append(l[4][0][1])
                '''str=y[0]
                if len(y)>1:
                    str=y[0]
                    for i in range(0,len(y)):
                        str=str+":"+y[1][i][0]'''
            qs.append(y)
        #self.ques.setText(qs[0][0])
        #print(y)
        #print(qs)
        for i in qs:
            str=i[0]+" : "
            if(len(i)>1):
                #str=""
                for j in range(0,len(i)):
                    str=str+"\n"+i[1][j][0]

            lab=QLabel(str)
            self.ques_read.append(str)
            edit=QLineEdit()
            self.anss_edit.append(edit)
            hbox=QHBoxLayout()
            hbox.addWidget(lab)
            hbox.addWidget(edit)
            self.quess.append(hbox)

        print(self.ques)
        for i in self.quess:
            self.vbox.addLayout(i)
        sleep(5)
        ans=[]
        for index,i in enumerate(self.ques_read):
        
            tts(i)
            sleep(1)
            try:
                ans.append(stt())
            except:
                msg=QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Speech cannot be recognized")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            sleep(5)
            print(ans[-1])
            self.anss_edit[index].setText(ans[-1])
            
            
        '''for i in range(len(self.quess)):
            tts(qs[i][0])
            if len(qs[i]>1):
                for l in qs[1]:
                    tts(l[0])'''
                    
        self.submitres=QPushButton("SUBMIT")
        hbox=QHBoxLayout()
        hbox.addWidget(QLabel(""))
        hbox.addWidget(self.submitres)
        self.vbox.addLayout(hbox)
        self.submitres.clicked.connect(lambda:self.temp())
        #print self.name_e.text()'''
    def temp(self):
        for i in self.anss_edit:
            self.anss.append(i.text())
        get_filled_url(self.URL.text(),self.anss)

    def make(self):

        self.lab=QLabel("Enter URL : ")
        self.name=QLabel("")
        self.URL=QLineEdit()
        self.URL.setPlaceholderText("Enter URL")
        self.submit=QPushButton("SUBMIT")
        self.ques=QLabel("")
        self.ans=QLineEdit("")
        #self.grid=QGridLayout()
        self.vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        hbox.addWidget(self.lab)
        hbox.addWidget(self.URL)
        '''w=QWidget(hbox)'''
        self.vbox.addLayout(hbox)
        hbox=QHBoxLayout()

        label=QLabel("")
        hbox.addWidget(label)
        hbox.addWidget(self.submit)
        '''w=QWidget(hbox)'''
        self.vbox.addLayout(hbox,5)
        hbox=QHBoxLayout()

        self.resize(500,500)
        '''
        hbox.addWidget(self.ques)
        hbox.addWidget(self.ans)'''
        '''w=QWidget(hbox)'''
        self.vbox.addLayout(hbox)
        self.setLayout(self.vbox)
        
        #self.submit.setSizePolicy(19,15)
        self.submit.clicked.connect(lambda:self.closee())
        self.move(300, 150)
        self.show()

    '''def text_fill(self,self.quess,self.anss_edit):
        s=""
        for i in self.quess:
            read()
            ct=1
            s=hear()
            while(s=="" and ct<5):
                s=hear()
                time.sleep(20)
                ct+=1
    '''


def get_filled_url(url,ans):
    print("url is : ",url)
    print("Dictionary is : ",ans)
    br=webdriver.Chrome()
    br.get(url)
    x=br.execute_script("return FB_PUBLIC_LOAD_DATA_")
    br.close()
    url=url.replace('edit_requested=true','usp=pp_url&')
    gc=[]
    for l in x[1][1]:
        gc.append('entry.'+str(l[4][0][0]))
    form_dict={}
    for i in range(len(gc)):
        #if not "+" in ans[i]:
        #    form_dict[gc[i]]=ans[i]
        #else:
            l=ans[i].split("dashcolondash")
            form_dict[gc[i]]=l

    print(form_dict)
    seq=[]
    for k in form_dict:
        ct=0
        for i in form_dict[k]:
            ct+=1
            seq.append(k+"="+i)
            '''if ct==len(form_dict):
                seq.append(k+"="+i)
            else:
                seq.append(k+"="+i)#+"&")
            '''
    dstr=("&").join(seq)
    furl=url+dstr
    print("url is : ",furl)
    br=webdriver.Chrome()
    br.get(furl)
    return furl


def main():
    global app
    app = QApplication(sys.argv)
    ex = login()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

