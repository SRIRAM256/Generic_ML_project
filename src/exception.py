import sys
from src.logger import logging

def error_msg_detail(error,err_detail:sys)->str:
    _,_,exec_tb=err_detail.exc_info()
    file_name=exec_tb.tb_frame.f_code.co_filename
    lineno=exec_tb.tb_lineno
    error_message=str(error)

    error_desc=f"error happened at filename:{file_name}  lineno:{lineno}  error:{error_message}"

    return error_desc


class CustomException(Exception):

    def __init__(self, err_msg,err_detail) -> None:
        super().__init__(err_msg)
        self.error_msg=error_msg_detail(err_msg,err_detail)
    
    def __str__(self) -> str:
        return self.error_msg


if __name__=="__main__":
    try:
        print(4/0)
    except Exception as e:
        logging.info(CustomException(e,sys))
