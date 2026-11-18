; Paso 4 - Wizard de instalación (Inno Setup 6, Windows)
; Requiere haber ejecutado build.bat antes (genera ..\dist\Calculadora7).
[Setup]
AppName=Calculadora de 7 números
AppVersion=1.0
AppPublisher=Eskul
DefaultDirName={autopf}\Calculadora7
DefaultGroupName=Calculadora de 7 números
OutputDir=Output
OutputBaseFilename=Instalador_Calculadora7
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
UninstallDisplayIcon={app}\Calculadora7.exe

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "Crear icono en el escritorio"; GroupDescription: "Iconos adicionales:"

[Files]
Source: "..\dist\Calculadora7\*"; DestDir: "{app}"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Calculadora de 7 números"; Filename: "{app}\Calculadora7.exe"
Name: "{group}\Desinstalar"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Calculadora de 7 números"; Filename: "{app}\Calculadora7.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Calculadora7.exe"; Description: "Abrir la calculadora"; Flags: nowait postinstall skipifsilent
