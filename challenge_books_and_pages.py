
def solution(actual_page, left_pages):         
    temp_left_pages = left_pages - len(str(actual_page))    
    if temp_left_pages<=0:
        last_page = actual_page
        return last_page
    else:           
        while temp_left_pages>0:
            actual_page = actual_page + 1
            temp_left_pages = temp_left_pages - len(str(actual_page))  
            if temp_left_pages == 0:
                last_page = actual_page
                return last_page
            elif temp_left_pages < 0:
                last_page = actual_page - 1
                return last_page


    
