import tkinter
from tkinter import filedialog
from tkinter import messagebox

from freqDiscrimAnalysis_Category import freqDiscrimAnalysis_Category
from CategoryTrainingFigure_Funnel import CategoryTrainingFigure_Funnel

class GUI(tkinter.Frame):
	def __init__(self, master=None):
		tkinter.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		optionList = ["Category Training", "Frequency Discrimination"]
		self.sessionType = tkinter.StringVar()							#variable to hold choice
		self.sessionType.set(optionList[0])								#set default option as first option

		self.optionMenu = tkinter.OptionMenu(self, self.sessionType, *optionList)
		self.optionMenu.grid(row = 0, columnspan = 2)					#drop-down list with script options

		self.chooseFileButton = tkinter.Button(self, text = "Choose File...", command = self.chooseFile)
		self.chooseFileButton.grid(row = 2, column = 0, padx = 2)		#open file choice dialog for data file

		self.chosenFile = tkinter.StringVar()
		self.chosenFileField = tkinter.Entry(self, textvariable = self.chosenFile, width = 40)
		self.chosenFileField.grid(row = 2, column = 1)					#shows which data file was selected

		self.sessionLabel = tkinter.Label(self, text = "Session:")
		self.sessionLabel.grid(row = 3, column = 0, padx = 2, sticky = tkinter.E)

		self.session = tkinter.StringVar()
		self.sessionField = tkinter.Entry(self, textvariable = self.session, width = 3)
		self.sessionField.grid(row = 3, column = 1, sticky = tkinter.W)	#field to enter the number of the session

		self.runButton = tkinter.Button(self, text = "Create Figures", command = (lambda: self.runScript(self.sessionType.get(), self.chosenFile.get(), self.session.get())))
		self.runButton.grid(row = 5, columnspan = 2)					#runs the chosen script

		self.status = tkinter.StringVar()
		self.status.set("Ready.")
		self.statusLabel = tkinter.Label(self, textvariable = self.status)
		self.statusLabel.grid(row = 6, columnspan = 2)

	def chooseFile(self):												#file choice dialog
		filename = filedialog.askopenfilename(filetypes = [("MATLAB Data Files", ".mat"), ("All Files", ".*")])
		self.chosenFile.set(filename)

	def runScript(self, sessionType, dataFilename, session):
		self.status.set("Generating figures...")
		self.statusLabel.update()

		if "\\" in dataFilename:										#if the file path uses backslashes
			filename = dataFilename.split("\\")[-1]						#the name after the last slash
		else:															#if the file path uses forward slashes
			filename = dataFilename.split("/")[-1]						#the name after the last slash, and before

		fileDirectory = dataFilename[:-1 * len(filename)]				#file directory is the path up to the name

		if sessionType == "Category Training":
			CategoryTrainingFigure_Funnel(fileDirectory, filename[:-4], session)	#remove ".mat" from filename
		elif sessionType == "Frequency Discrimination":
			freqDiscrimAnalysis_Category(fileDirectory, filename[:-4])				#remove ".mat" from filename

		self.status.set("Done: " + filename)