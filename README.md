# Meganex Superlight 8K - Render Target Patch by Sabre (Discord: sabre9504)

The original Render Target is 3552x3552, which is a limiting factor for a Headset with such a high resolution panels.

### Patches
| Installers                                                                             | Render Target Patches                                                                                        |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [1.4.0.0](https://delivery.shopifyapps.com/-/96cb3b96914f1d02/baaf8635523d9be1)        | [see available patches](https://github.com/jameskitt616/m8k_render_target_patch/tree/master/patches/1.4.0.0) |
| [1.4.1.0 (Beta)](https://delivery.shopifyapps.com/-/a27101f7e972be92/baac146f73c78fd6) | -                                                                                                            |

### How to Patch
1. Pick the Render Target Patch of your installers version above at the "Patches" section
2. Download the Python file with the wanted Render Target (`patch_meganex_compositor_<render_target>.py`)
3. Create a new folder somewhere on your PC and move the Python script there
4. Go to `C:\Program Files\MeganeXSuperlight\OpenVRMiddleware\MeganeXSuperlight\bin\win64` and copy `MeganeX_Compositor.exe` to your new created folder which contains the Python script!
5. Go to the [Microsoft Store and Install Python](https://apps.microsoft.com/detail/9pnrbtzxmb4z)
6. Now go to your folder and right-click on your mouse somewhere to get the windows context-menu and select "open terminal"
7. Now write the following `python .\patch_meganex_compositor_<render_target>.py` (Note: sometimes it can be `python3` or `py` instead of `python`)
8. If the script is done, you receive your patched .exe file, which looks something like this `MeganeX_Compositor.<render_target>.exe`. Continue reading at the "How to install" section

### How to install
1. Take your patched `MeganeX_Compositor.<render_target>.exe` file and rename it to `MeganeX_Compositor.exe`
2. Close the Meganex Configurator Program (Check your Windows tray icons as well if it's still running)
3. Go to the following path `C:\Program Files\MeganeXSuperlight\OpenVRMiddleware\MeganeXSuperlight\bin\win64` and replace your existing `MeganeX_Compositor.exe` file, with the one you just patched and renamed (NOTE: you may want to copy the original `MeganeX_Compositor.exe` somewhere as a backup to go back to if you wish. You can always go back by completely uninstalling and reinstalling the Software again). 
4. You can start the Meganex Configurator again

### Honorable Mention
A heartfelt thank you to Sabre (Discord: sabre9504) for generously developing and providing us with this patch!
