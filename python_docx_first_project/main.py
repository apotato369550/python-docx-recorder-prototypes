from docxtpl import DocxTemplate

doc = DocxTemplate("Workplan.docx")
context = {
    "workplan_number": "101", 
    "person": "bob", 
    "location:": "London"
}

doc.render(context)
doc.save("Workplan_uwu.docx")