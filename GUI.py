import sys
from PyQt5 import QtWidgets, QtCore,QtGui,Qt
from PyQt5.QtGui import QIcon
import qtawesome

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout()
        self.addLeftWidget()
        self.addRightWidget()
        self.addMidWidget()
        self.show()
        

    def layout(self):
        '''Init whole mainwinodws \n
        There is three widgets in mainwidghts which are left,middle,right widgets\n
        '''
        '''set main widghts'''
        self.setGeometry(400,250,1000,600)
        self.mainWidget=QtWidgets.QWidget()
        self.mainLayout=QtWidgets.QGridLayout()
        self.mainWidget.setLayout(self.mainLayout)

        self.leftWidget=QtWidgets.QWidget()
        self.leftWidget.setObjectName('left widget')
        self.leftLayout=QtWidgets.QGridLayout()
        self.leftWidget.setLayout(self.leftLayout)

        self.midWidget=QtWidgets.QWidget()
        self.midWidget.setObjectName('middle widget')
        self.midLayout=QtWidgets.QVBoxLayout()
        self.midWidget.setLayout(self.midLayout)

        self.rightWidget=QtWidgets.QWidget()
        self.rightWidget.setObjectName('right widget')
        self.rightLayout=QtWidgets.QVBoxLayout()
        self.rightWidget.setLayout(self.rightLayout)

        self.mainLayout.addWidget(self.leftWidget,0,0,12,3)
        self.mainLayout.addWidget(self.midWidget,0,3,12,5)
        self.mainLayout.addWidget(self.rightWidget,0,8,12,1)

        self.status=QtWidgets.QStatusBar()
        self.setCentralWidget(self.mainWidget)
        self.setStatusBar(self.status)
        self.status.showMessage('Ready')
        self.setWindowTitle('Teaching Tool')

    def addLeftWidget(self):
        '''Left windgets contain toggle box and button showing which component's failure mode'''
        self.leftClose=QtWidgets.QPushButton("")
        self.leftVisit=QtWidgets.QPushButton("")
        self.leftMini=QtWidgets.QPushButton("")

        self.compression=QtWidgets.QPushButton("Compression")
        self.tension=QtWidgets.QPushButton('Tension')
        self.smallPartialCompreesion=QtWidgets.QPushButton("Small Partial Compression") 
        self.bigPartialCompreesion=QtWidgets.QPushButton("Big Partial Compression") 
        self.tickp=self.smallPartialCompreesion
        self.flexure=QtWidgets.QPushButton("Flexure")
        self.shear=QtWidgets.QPushButton('Shear')
        self.tickf=self.flexure

        self.chooseLabel=QtWidgets.QLabel('Choose component')
        self.chooseBeam=QtWidgets.QRadioButton('Beam')
        self.chooseColumns=QtWidgets.QRadioButton('Columns')
        self.chooseBeam.setChecked(True)
        self.chooseColumns.setChecked(False)
        self.verifiedButton=QtWidgets.QPushButton('ok')

        self.verifiedButton.clicked.connect(self.showFailuremode)
        
        

        # self.leftLayout.addWidget(self.leftClose,0,0,1,1)
        # self.leftLayout.addWidget(self.leftVisit,0,1,1,1)
        # self.leftLayout.addWidget(self.leftMini,0,2,1,1)
        self.leftLayout.addWidget(self.chooseBeam,3,0,1,1)
        self.leftLayout.addWidget(self.chooseColumns,3,1,1,1)
        self.leftLayout.addWidget(self.verifiedButton,3,2,1,1)


    def showFailuremode(self):
        if self.chooseColumns.isChecked():
            if self.tickf==self.flexure:
                self.flexure.deleteLater()
                self.shear.deleteLater()
                self.flexure=0
            self.columnLayout()
        else:
            if self.tickp==self.smallPartialCompreesion:
                self.smallPartialCompreesion.deleteLater()
                self.bigPartialCompreesion.deleteLater()
                self.leftLayout.removeWidget(self.compression)
                self.compression.deleteLater()
                self.leftLayout.removeWidget(self.tension)
                self.tension.deleteLater()
                self.smallPartialCompreesion=0
            self.beamLayout()
    
    def beamLayout(self):
        self.flexure=QtWidgets.QPushButton("Flexure")
        self.shear=QtWidgets.QPushButton('Shear')
        self.tickf=self.flexure
        self.leftLayout.addWidget(self.flexure,6,0,1,3)
        self.leftLayout.addWidget(self.shear,7,0,1,3)
        


    def columnLayout(self):
        self.smallPartialCompreesion=QtWidgets.QPushButton("Small Partial Compression")
        self.bigPartialCompreesion=QtWidgets.QPushButton("Big Partial Compression")
        self.compression=QtWidgets.QPushButton("Compression")
        self.tension=QtWidgets.QPushButton('Tension')
        self.tickp=self.smallPartialCompreesion
        self.leftLayout.addWidget(self.smallPartialCompreesion,6,0,1,3)
        self.leftLayout.addWidget(self.bigPartialCompreesion,7,0,1,3)
        self.leftLayout.addWidget(self.compression,8,0,1,3)
        self.leftLayout.addWidget(self.tension,9,0,1,3)

    def addRightWidget(self):
        '''Right widget is aimed to show unecessary pic\n
        or In the future, this part can display components info'''
        # conceptpix=QtGui.QPixmap(r'picture\1.jpg')
        # self.conceptLabel=QtWidgets.QLabel()
        # self.conceptLabel.setPixmap(conceptpix)
        # self.titleConceptLabel=QtWidgets.QLabel('Concept Pic')
        # self.rightLayout.addStretch(100)
        # self.rightLayout.addWidget(self.conceptLabel)
        # self.rightLayout.addStretch(1)
        # self.rightLayout.addWidget(self.titleConceptLabel,alignment=QtCore.Qt.AlignHCenter)
        # self.rightLayout.addStretch(100)

        '''Describe the para of section:'''
        self.sectionLayout=QtWidgets.QVBoxLayout()
        self.materialLayout=QtWidgets.QVBoxLayout()
        self.loadLayout=QtWidgets.QVBoxLayout()
        paraLabel=QtWidgets.QLabel('Para info: ')
        
        self.rightLayout.addWidget(paraLabel)
        self.rightLayout.addLayout(self.sectionLayout)
        self.rightLayout.addLayout(self.materialLayout)
        self.rightLayout.addLayout(self.loadLayout)

        '''Specify sectionLayout'''
        self.sectionLabel=QtWidgets.QLabel('Section: H,B (mm) :')
        self.sectionValue=QtWidgets.QTextEdit('400,200')
        self.sectionValue.setMaximumHeight(30)
        self.sectionLayout.addWidget(self.sectionLabel)
        self.sectionLayout.addWidget(self.sectionValue)

        self.LengthLabel=QtWidgets.QLabel('Beam Length (mm) :')
        self.LengthValue=QtWidgets.QTextEdit('3000')
        self.LengthValue.setMaximumHeight(30)
        self.sectionLayout.addWidget(self.LengthLabel)
        self.sectionLayout.addWidget(self.LengthValue)

        '''Specify MaterialLayout'''
        self.steelLabel=QtWidgets.QLabel('Steel info:')
        self.constrainSteelLabel=QtWidgets.QLabel('ConstrainSteel info (Strength grade,Diameter,Offset,Legs):')
        self.constrainSteelValue=QtWidgets.QTextEdit('HPB300,14,150,2')
        self.constrainSteelValue.setMaximumHeight(30)
        self.longitudeSteelLabel=QtWidgets.QLabel('LongitudeSteel info (Strength grade,Ylied strength,Diameter,Number):')
        self.longitudeSteelValue=QtWidgets.QTextEdit('HRB400,360,14,3')
        self.longitudeSteelValue.setMaximumHeight(30)
        self.materialLayout.addWidget(self.steelLabel)
        self.materialLayout.addWidget(self.constrainSteelLabel)
        self.materialLayout.addWidget(self.constrainSteelValue)
        self.materialLayout.addWidget(self.longitudeSteelLabel)
        self.materialLayout.addWidget(self.longitudeSteelValue)

        '''Specify loadLayout'''
        self.loadLabel=QtWidgets.QLabel('Load pattern :')
        self.pic=QtGui.QPixmap(r'picture\示意图.png')
        self.loadPic=QtWidgets.QLabel()
        self.loadPic.setMaximumSize(500,200)
        self.loadPic.setPixmap(self.pic)
        self.loadPic.setScaledContents(True)
        self.loadLayout.addWidget(self.loadLabel)
        self.loadLayout.addWidget(self.loadPic)



    def addMidWidget(self):
        '''MidWidget is core part which is used to show gif caculated by abaqus'''
        abaqusReasult=QtGui.QMovie(r'picture\ShearFailure.gif')
        self.abaqusLabel=QtWidgets.QLabel()
        self.abaqusLabel.setMovie(abaqusReasult)
        abaqusReasult.start()
        self.titleAbaqusLabel=QtWidgets.QLabel('Abaqus Pic')
        self.midLayout.addStretch(100)
        self.midLayout.addWidget(self.abaqusLabel,alignment=QtCore.Qt.AlignHCenter)
        self.midLayout.addStretch(1)
        self.midLayout.addWidget(self.titleAbaqusLabel,alignment=QtCore.Qt.AlignHCenter)
        self.midLayout.addStretch(100)


        
        

def main():
    app =QtWidgets.QApplication(sys.argv)

    mw=mywindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()