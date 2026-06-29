import sys
# Import your custom logging configuration

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # exc_info returns (type, value, traceback)
        _, _, exc_tb = error_detail.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
        self.error_message = error_message

    def __str__(self):
        return f"Error occurred in script [{self.filename}] at line number [{self.lineno}] with error message [{self.error_message}]"

# if __name__=="__main__":
#     try:
#         logging.info("This is a test log message.")
#         # This will trigger the ZeroDivisionError
#         a = 1 / 0 
#     except Exception as e:
#         # We catch the ZeroDivisionError and wrap it in our custom exception
#         logging.error("Dividing by zero is not allowed.")
#         raise NetworkSecurityException(e, sys)