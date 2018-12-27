import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QGroupBox, QDialog, QGridLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


class App(QDialog):
	def __init__(self):
		super().__init__()
		self.top = 200
		self.left = 200
		self.width = 400
		self.height = 200
		self.title = "BMI Calculator"
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowIcon(QIcon("bmi_calc_logo.png"))

		self.verticalLayoutOutput()
		self.verticalLayoutInput()
		windowLayout = QHBoxLayout()
		windowLayout.addWidget(self.inputBox)
		windowLayout.addLayout(self.outputBox)
		self.setLayout(windowLayout)

		self.show()

	def verticalLayoutInput(self):
		self.inputBox = QGroupBox()
		layout = QVBoxLayout()

		self.weightLabel = QLabel("Weight (in kg)", self)
		self.weightInput = QLineEdit(self)
		self.heightLabel = QLabel("Height (in m)", self)
		self.heightInput = QLineEdit(self)
		self.btn = QPushButton("Calculate")
		self.btn.clicked.connect(self.calculate)

		layout.addWidget(self.weightLabel)
		layout.addWidget(self.weightInput)
		layout.addSpacing(5)
		layout.addWidget(self.heightLabel)
		layout.addWidget(self.heightInput)
		layout.addStretch(1)
		layout.addWidget(self.btn)

		self.inputBox.setLayout(layout)

	def verticalLayoutOutput(self):
		self.outputBox = QVBoxLayout()
		self.spacingLayout = QHBoxLayout()
		self.spacingLayout2 = QHBoxLayout()
		self.spacingLayout3 = QHBoxLayout()
		self.bmilabel = QLabel("BMI is:")
		self.bmilabel.setStyleSheet("font-size: 15px")
		self.result = QLabel("0.0")
		self.result.setStyleSheet("font-size: 15px")
		self.analysis = QLabel("")

		self.spacingLayout.addStretch(1)
		self.spacingLayout.addWidget(self.bmilabel)
		self.spacingLayout.addStretch(1)
		self.spacingLayout2.addStretch(1)
		self.spacingLayout2.addWidget(self.result)
		self.spacingLayout2.addStretch(1)
		self.spacingLayout3.addStretch(1)
		self.spacingLayout3.addWidget(self.analysis)
		self.spacingLayout3.addStretch(1)

		self.outputBox.addStretch(1)
		self.outputBox.addLayout(self.spacingLayout)
		self.outputBox.addLayout(self.spacingLayout2)
		self.outputBox.addLayout(self.spacingLayout3)
		self.outputBox.addStretch(1)

	@pyqtSlot()
	def calculate(self):
		try:
			wt = float(self.weightInput.text())
			ht = float(self.heightInput.text())
			bmi = wt / ht**2
			self.result.setText(str(round(bmi, 2)))
			if bmi <= 18.5:
				self.analysis.setText("Underweight")
				self.result.setStyleSheet("color: red")
				self.analysis.setStyleSheet("color: red")
			elif 18.5 < bmi < 25:
				self.analysis.setText("Healthy")
				self.result.setStyleSheet("color: green")
				self.analysis.setStyleSheet("color: green")
			else:
				self.analysis.setText("Overweight")
				self.result.setStyleSheet("color: red")
				self.analysis.setStyleSheet("color: red")

		except ValueError:
			QMessageBox.question(self, 'Info', 'Enter correct values', QMessageBox.Ok, QMessageBox.Ok)
		except ZeroDivisionError:
			QMessageBox.question(self, 'Info', 'Enter non zero height', QMessageBox.Ok, QMessageBox.Ok)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())