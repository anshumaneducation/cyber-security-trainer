import py_compile
import os
import shutil

# List of Python scripts to compile
scripts = ["client.py", "server.py", "cryptography-start.py", "hacker.py", "password_verifier.py", 
           "digital-signer.py", "digital-verifier.py", "RC4.py", "RSA.py", "sDES.py", "TDES.py"]

# Compile each script
for script in scripts:
    try:
        # Compile the script
        compiled_file = py_compile.compile(script, doraise=True)
        print(f"Compiled {script} successfully.")
        
        # Renaming the compiled file to match the original script name without version suffix
        pyc_file = compiled_file.replace(".cpython-310.pyc", ".pyc")
        shutil.move(compiled_file, pyc_file)
        print(f"Renamed {compiled_file} to {pyc_file}")
        
    except py_compile.PyCompileError as e:
        print(f"Failed to compile {script}: {e.msg}")
