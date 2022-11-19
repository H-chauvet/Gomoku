#!/usr/bin/python3

import platform
import resource

def setMemoryLimit(memoryLimit: int):
    if platform.system() == "Linux":
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS, (memoryLimit, hard))
    elif platform.system() == "Windows":
        raise OSError("Memory not handled on windows.")