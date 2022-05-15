from pywinauto.application import Application

def foo(vstr):
 fn=str(vstr)+".txt"   
 app=Application(backend="uia").start('notepad.exe').connect(title='Untitled - Notepad',timeout=100)

 
 texte=app.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
 texte.type_keys('test pywinauto with notepad!!!',with_spaces=True)

 filem=app.UntitledNotepad.child_window(title="File", control_type="MenuItem").wrapper_object()
 filem.click_input()
 
 saveas=app.UntitledNotepad.child_window(title="Save As...	Ctrl+Shift+S", auto_id="4", control_type="MenuItem").wrapper_object()
 saveas.click_input()

 #app.UntitledNotepad.print_control_identifiers()
 filen=app.UntitledNotepad.child_window(title="File name:", auto_id="1001", control_type="Edit").wrapper_object()
 filen.type_keys(fn,with_spaces=True)

 buton=app.UntitledNotepad.child_window(title="Save", auto_id="1", control_type="Button").wrapper_object()
 buton.click_input()

 note=fn+' - Notepad'

 app=Application(backend="uia").connect(title=note,timeout=100)
 klise=app.mtxtNotepad.child_window(title="Close", control_type="Button").wrapper_object()
 klise.click_input()


for i in range(1111,1115):
    foo(i)
