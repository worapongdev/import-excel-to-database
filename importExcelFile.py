import os
import pathlib
from config import get_connection_string, get_stored_procedure
import pandas as pd
from sqlalchemy import create_engine
from writeLog import gen_log_text, write_error_logging, write_complete_list_logging


def importData():    
    try:
        con_str = get_connection_string()
        engine = create_engine(con_str)
        engine.connect()
        
        with engine.connect() as con:
            try:
                files_directory = os.path.join(str(pathlib.Path(__file__).parent.resolve()),'files')
                files = os.listdir(files_directory)
                files.sort()
                log_text=[]
                for file in files:
                    file_path = os.path.join(files_directory, file)
                    xls = pd.ExcelFile(file_path)
                    global sheet_names
                    sheet_names = xls.sheet_names
                    for sheet_name in sheet_names:
                        df_sheet = pd.read_excel(file_path, sheet_name=sheet_name)
                        df_sheet.astype(str).to_sql(name=sheet_name, con=engine, if_exists='append',index=False,chunksize=1000,method='multi')
                        log_text.append(gen_log_text(sheet_name +' imported ' + str(len(df_sheet)) + ' rows'))
                
                con.commit()
                write_complete_list_logging(log_text)
                
                execProc =  engine.raw_connection()
                try:
                    cursor_obj = execProc.cursor()
                    cursor_obj.execute('EXEC ' + get_stored_procedure())
                    #cursor_obj.callproc(get_stored_procedure(), [])
                    cursor_obj.close()
                    execProc.commit()
                except Exception as e:
                    execProc.rollback()
                    write_error_logging(str(e))


            except Exception as e:
                con.rollback()
                write_error_logging(str(e))
                return
            finally:
                con.close()

    except Exception as e:
        print(e)
        return
    

            
    
            

        
    