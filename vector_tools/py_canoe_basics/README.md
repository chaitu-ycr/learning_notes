# 1. python basics
## 1.1 python basics cheatsheet [link](./python_basics_cheatsheet.pdf)
# 2. py_canoe
## **_py_canoe_** official documentation [link](https://chaitu-ycr.github.io/py_canoe/)
## 2.1. Dependencies

```powershell
python -m pip install pywin32
```

## 2.2. import necessary pywin32 modules

```python
import pythoncom
import win32com.client
```

## 2.3. create CANoe python package file

## 2.4. create python CANoe class

## 2.5. about win32com module

win32com is a Python package that allows you to interact with Windows COM objects and automate Windows applications1. It is part of the pywin32 extensions, which provide access to many of the Windows APIs from Python.

## 2.6. pythoncom.CoInitialize()

It is a function that initializes the COM library for the current thread. It is required when you want to use COM objects in a multithreaded environment.

## 2.7. create python CANoe application client using win32com module

```python
pythoncom.CoInitialize()
canoe_app_object = win32com.client.Dispatch('CANoe.Application')
```

## 2.8. about CANoe COM objects

## 2.9. print CANoe version

```python
cav = canoe_app_object.Version
print(f'Vector CANoe Application {cav.major}.{cav.minor}.{cav.Build}')
```

## 2.10. write code to open / close a CANoe configuration

## 2.11. write code to get / set a value to signal

## 2.12. write code to get / set a value to system variable

## 2.13. write code to send a diagnostic message
