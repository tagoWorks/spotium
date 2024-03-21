![Banner](./header.png)
<div align="center">
    </a>
    <br />

   ![GitHub last commit](https://img.shields.io/github/last-commit/tagoworks/spotium)
   ![GitHub issues](https://img.shields.io/github/issues-raw/tagoworks/spotium)

   *there is definitely an easier way to make a tkinter menu but idc*

</div>

Spotium does not include any viruses, backdoors, trojans, or any other type of malicious software or code. Additionally, Spotium rarely updates but when it does it is important, Spotium checks for updates automatically. You can view the latest Spotium files VirusTotal result for windows and for macOS. In May of 2023 Spotium was put to a stop since Spotify had fixed the method it used, special thanks to [BlockTheSpot](https://github.com/mrpond/BlockTheSpot) for the new working method that Spotium currently employs. Spotium has gone open source to further prove this, and allow the community to contribute. 

# Building executable file 🧑‍💻

1. Download pyinstaller
   ```sh
   pip install pyinstaller
   ```
   
2. Convert py to executable
   ```sh
   pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --add-data "menu;menu/"  "Spotium.py"
   ```

# License & Information 📃
This project is published under the [MIT license](./LICENSE)

If you are interested in working together, or want to get in contact with me please email me at santiagobuisnessmail@gmail.com
