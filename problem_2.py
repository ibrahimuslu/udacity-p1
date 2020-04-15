import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    cList = []
    return recurFindFiles(suffix,path,cList)
def recurFindFiles (suffix,path,cList):
    # print(path,os.path.isdir(path))
    if(os.path.isdir(path)):
      # print(os.listdir(path))
      for f in os.listdir(path):
        # print(f,os.path.isdir(path+"/"+f))
        if(os.path.isdir(path+"/"+f)):
          # print(os.listdir(path+"/"+f))
          recurFindFiles(suffix,(path+"/"+f),cList)
        # print(f,f.endswith(suffix))
        if (f.endswith(suffix)):
          cList.append(f)
        
    return cList
print(find_files('.c','testdir'))