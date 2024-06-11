import fm_core
import fm_model_db
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Main_window import Ui_MainWindow

page_counter = 1


def hello():
    print('-------------------------------------WELCOME TO FARMERS MARKETS-------------------------------------')
    print('Enter desired command or type "help":')


def print_help():
    print('Please refer to the following commands to interact with the program:\b "all" - shows all markets available '
          '\b')


def print_invalid_command():
    print('Invalid command! Type "help" to acquire info information \b')


def process_show30():
    tbl = []
    tbl = fm_model_db.show_all()
    cur_list_end = page_counter * 30
    cur_list_start = cur_list_end - 30
    shrt_tbl = []
    for i in range(30):
        shrt_tbl.append(tbl[cur_list_start])
        cur_list_start = cur_list_start + 1
    ui.tableWidget.setColumnCount(6)
    ui.tableWidget.setRowCount(30)
    ui.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
    ui.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Name"))
    ui.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("State"))
    ui.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("ZIP"))
    ui.tableWidget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("X"))
    ui.tableWidget.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Y"))
    row_counter = 0
    col_counter = 0
    for rows in shrt_tbl:
        for items in rows:
            ui.tableWidget.setItem(row_counter, col_counter, QtWidgets.QTableWidgetItem(str(items)))
            col_counter = col_counter + 1


def counter():
    global page_counter
    page_counter = page_counter + 1


def clicked_nextpage():
    counter()
    process_show30()


def process_srch_zip():
    zip = ui.lineEdit.text()
    result = fm_model_db.market_by_zip(zip)
    srch_count = len(result)
    if len(result) > 0:
        ui.tableWidget_2.setColumnCount(6)
        ui.tableWidget_2.setRowCount(srch_count)
        ui.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        ui.tableWidget_2.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Name"))
        ui.tableWidget_2.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("State"))
        ui.tableWidget_2.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("ZIP"))
        ui.tableWidget_2.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("X"))
        ui.tableWidget_2.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Y"))
        row_counter = 0
        col_counter = 0
        for rows in result:
            for items in rows:
                ui.tableWidget_2.setItem(row_counter, col_counter, QtWidgets.QTableWidgetItem(str(items)))
                col_counter = col_counter + 1
    else:
        ui.tableWidget_2.setColumnCount(1)
        ui.tableWidget_2.setRowCount(1)
        ui.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("No data found"))
        ui.tableWidget_2.setItem(1, 1, QtWidgets.QTableWidgetItem("Try another value"))


def process_srch_state():
    state = ui.lineEdit_2.text()
    result = fm_model_db.market_by_state(state)
    srch_count = len(result)
    if len(result) > 0:
        ui.tableWidget_2.setColumnCount(6)
        ui.tableWidget_2.setRowCount(srch_count)
        ui.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        ui.tableWidget_2.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Name"))
        ui.tableWidget_2.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("State"))
        ui.tableWidget_2.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("ZIP"))
        ui.tableWidget_2.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("X"))
        ui.tableWidget_2.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Y"))
        row_counter = 0
        col_counter = 0
        for rows in result:
            for items in rows:
                ui.tableWidget_2.setItem(row_counter, col_counter, QtWidgets.QTableWidgetItem(str(items)))
                col_counter = col_counter + 1
    else:
        ui.tableWidget_2.setColumnCount(1)
        ui.tableWidget_2.setRowCount(1)
        ui.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("No data found"))
        ui.tableWidget_2.setItem(1, 1, QtWidgets.QTableWidgetItem("Try another value"))

def process_srch_point():
    x = ui.lineEdit_3.text()
    y = ui.lineEdit_4.text()
    radius = ui.horizontalSlider.value()
    search_point = (None,None,None,None,float(x), float(y))
    result = fm_core.search_rad(fm_model_db.show_all(),search_point,radius)
    srch_count = len(result)
    if len(result) > 0:
        ui.tableWidget_2.setColumnCount(6)
        ui.tableWidget_2.setRowCount(srch_count)
        ui.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        ui.tableWidget_2.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Name"))
        ui.tableWidget_2.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("State"))
        ui.tableWidget_2.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("ZIP"))
        ui.tableWidget_2.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("X"))
        ui.tableWidget_2.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Y"))
        row_counter = 0
        col_counter = 0
        for rows in result:
            for items in rows:
                ui.tableWidget_2.setItem(row_counter, col_counter, QtWidgets.QTableWidgetItem(str(items)))
                col_counter = col_counter + 1
    else:
        ui.tableWidget_2.setColumnCount(1)
        ui.tableWidget_2.setRowCount(2)
        ui.tableWidget_2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("No data found"))
        ui.tableWidget_2.setItem(1, 1, QtWidgets.QTableWidgetItem("Try another value"))

def process_show_revievs():
    revs = fm_model_db.show_all_reviews()
    """SELECT m.fmid, m.marketname, m.state, m.zip, m.x, m.y, r.rewiew_text, r.score FROM markets m
    INNER JOIN reviews r ON r.rewiew_market_id = m.fmid"""
    count = len(revs)
    col_counter = 0
    for rows in revs:
        ui.listWidget.addItem(str(rows[0]) + ' ' + str(rows[1]) + ' ' + str(rows[2]) + ' ' + str(rows[6]) + '  Score: ' + str(rows[7]))

def process_add_rev():
    id = int(ui.lineEdit_6.text())
    review = ui.lineEdit_5.text()
    score = int(ui.spinBox.value())
    if len(fm_model_db.market_by_id(id)) > 0:
        ui.listWidget.clear()
        fm_model_db.add_review(id,review,score)
        ui.label_8.setText("Enter ID of the market to proceed")
        process_show_revievs()
    else:
        ui.label_8.setText("wrong id number, try again")

def process_full_data():
    id = int(ui.lineEdit_6.text())
    if len(fm_model_db.market_by_id(id)) > 0:
        markt = fm_model_db.market_full_info(id)
        convertinfo = fm_core.convert_fullinfo(markt)
        count = len(convertinfo)
        ui.tableWidget_3.setColumnCount(count)
        ui.tableWidget_3.setRowCount(2)
        col_counter = 0
        row_counter = 1
        for items in convertinfo:
            ui.tableWidget_3.setItem(row_counter,col_counter,QtWidgets.QTableWidgetItem(str(items)))
            col_counter = col_counter+1
    else:
        pass



# Executable part
#print(fm_model_db.market_by_zip("69361"))
#print(fm_model_db.market_by_id(1009994))
#fm_model_db.add_review(1019695, "Someone stole my cabbage", 4)
#markt = fm_model_db.market_full_info(1019695)
#convertinfo = fm_core.convert_fullinfo(markt)
#print(convertinfo)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

process_show30()
process_show_revievs()

ui.pushButton.clicked.connect(clicked_nextpage)
ui.pushButton_2.clicked.connect(process_srch_zip)
ui.pushButton_3.clicked.connect(process_srch_state)
ui.pushButton_4.clicked.connect(process_srch_point)
#ui.tableWidget.cellDoubleClicked.connect()
ui.pushButton_5.clicked.connect(process_add_rev)
ui.lineEdit_6.textChanged.connect(process_full_data)

sys.exit(app.exec_())
