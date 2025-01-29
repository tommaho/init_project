# init_project.py  

Initialize a file and directory structure for an analytics project.

## Setup (Windows)

For ease of use on Windows, put the folder containing this python script in your PATH, accompanied by a init_project.bat file that facilitates execution, like:

```bat
PS C:\scripts> cat .\init_project.bat
@echo off
python "%~dp0\init_project.py"
pause
PS C:\scripts>
```

This will allow you to right-click on any folder, open in terminal, and run `init_project` anywhere.

## Usage

Using your shell or terminal of choice, and set up as directed (or similarly): 


```powershell
PS C:\temp> init_project
Enter the project name: my test project
my test project template initialized
Press any key to continue . . .
PS C:\temp> cd "my test project"
PS C:\temp\my test project> tree /F
Folder PATH listing
Volume serial number is 0000-0000
C:.
│   readme.md
│
├───data
├───documents
├───drafts
├───final
├───notebooks
│   │   my test project.ipynb
│   │
│   ├───in
│   └───out
└───sql
PS C:\temp\my test project>
```

## Folders and Files Initialized

As I currently use this:
- `data` is for client-provided data.
- `documents` is for special instructions or requirements.
- `drafts` is for works in progress and not-finalized products.
- `final` is for the finished products.
- `notebooks` is for notebook-based activity.
    - `in` for data loaded into notebooks.
    - `out` for exports from notebooks.
    - A python notebook is created with the same name as the project.
- `sql` is for ad hoc or reference queries related to this project.
- A `readme.md` file is created describing the project structure.

