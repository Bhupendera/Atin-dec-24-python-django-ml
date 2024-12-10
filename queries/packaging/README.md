### **0. Install and setup virtual env**
```
cd queries\hands-on\packaging
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### **1. Build the Package**
Navigate to the root of your project directory (where `setup.py` is located).
```
cd pytoolkit
```

#### **Create the Wheel Package**
Run the following command to build a `.whl` file:
```cmd
python -m compileall pytoolkit_package
python setup.py bdist_wheel
```

#### **Verify the Build Output**
Check the `dist/` directory for the generated files:
```cmd
dir dist
```

Example output:
```
pytoolkit-1.0.0-py3-none-any.whl
```

---

### **2. Install the Package Locally**
To test the package, you can install it locally using `pip`.

#### **Install the Wheel File**
```cmd
pip install dist\pytoolkit-1.0.0-py3-none-any.whl
```

---

### **3. Test the Installed Package**
Write a test script (`test_script.py`) to verify the functionality of your package.

#### Create `test_script.py`:
```cmd
notepad test_script.py
```

#### Add the Following Content:
```python
from pytoolkit_package.toolkit_module import greet, add

print(greet("Alice"))
print(add(5, 7))
```

#### Run the Script:
```cmd
python test_script.py
```

Expected Output:
```
Hello, Alice!
12
```

---

### **4. Uninstall the Package**
If you need to uninstall the package:
```cmd
pip uninstall pytoolkit
```

---

### **5. Distribute the Package**
#### **Upload to PyPI**
1. Install Twine:
   ```cmd
   pip install twine
   ```

2. Upload the Package:
   ```cmd
   twine upload dist/*
   ```

3. Enter your PyPI credentials when prompted.

---

### **6. Summary of Commands**
Here’s a quick summary of all the commands:

#### Build the Package:
```cmd
python setup.py bdist_wheel
```

#### Install Locally:
```cmd
pip install dist\pytoolkit-1.0.0-py3-none-any.whl
```

#### Test the Package:
```cmd
python test_script.py
```

#### Uninstall:
```cmd
pip uninstall pytoolkit
```
