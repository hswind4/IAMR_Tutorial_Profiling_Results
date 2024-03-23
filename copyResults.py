import os
import shutil
import glob


def CopyFiles(src, dst):
    """
    复制一个单个case中的所有log和input文件
    """
    # case = "LidDrivenCavity"
    case = os.path.basename(src)
    # case_results = [case_results_2d,...]
    list_case_results = os.listdir(src)
    for case_results in list_case_results:
        list_results = os.listdir(f"{src}/{case_results}")
        # results = [cpu2d_skip0_Auto_mgs8_1_regrid4, ...]
        for result in list_results:
            file_dst = f"{dst}/{case}/{case_results}/{result}"
            
            # copy log
            file_src_log = f"{src}/{case_results}/{result}/log.txt"
            os.makedirs(file_dst, exist_ok=True)  
            shutil.copy(file_src_log, file_dst)

            # copy input
            file_src_pattern = f"{src}/{case_results}/{result}/inputs*"
            for file_src_input in glob.glob(file_src_pattern):
                if os.path.isfile(file_src_input):
                    shutil.copy(file_src_input, file_dst)


src = "LidDrivenCavity"
dst = "temp"
CopyFiles(src, dst)

