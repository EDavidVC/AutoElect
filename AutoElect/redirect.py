from AutoElect.reply import *
def redirect_reply(q_type, answer):
    #01 - NORMAL
    if(q_type == "01"):
        normal(answer)
    #02 - PRES ELEMENT
    if(q_type == "02_css"):
    	push_css(answer)
    if(q_type == "02_id"):
    	push_id(answer)
    if(q_type == "02_class"):
        push_class(answer)
    #03 - Change Style
    if(q_type == "03_ids"):
        change_style_ids(answer)
    #04 - TRUE OR FALSE
    if(q_type == "04"):
    	trueOrFalse(answer)
    #05 - INSERT DATA IN TEXT BOX
    if(q_type == "05"):
    	fill(answer)
    #06 - DRAG AND DROP
    if(q_type == "06_class_id"):
        drag_drop_class_id(answer)
    if(q_type == "06_id_class"):
        drag_drop_id_class(answer)
    if(q_type == "06_id_id"):
        drag_drop_id_id(answer)
    if(q_type == "06_css_css"):
        drag_drop_css_css(answer)
    if(q_type == "06_x_x"):
        drag_drop_x_x(answer)
    if(q_type == "06_id_offset"):
        drag_drop_id_offset(answer)
    #multi - UNLIMITED PROCCES IN ONE QUESTION
    if(q_type == "multi"):
        multiPro(answer)
    #end - This Function is Active in the Final of cource
    if(q_type == "end"):
    	end()

def multiPro(answer):
    for q_type in answer:
        redirect_reply(q_type, answer[q_type])
