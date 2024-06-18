def get_connection_string():
    f=open('connectionString.txt','r')
    con_str=f.read()
    return con_str

def get_stored_procedure():
    f=open('storedProcedure.txt','r')
    sp=f.read()
    return sp

def get_file_dir_path():
    f=open('fileDirPath.txt','r')
    sp=f.read()
    return sp