MESAJ="DTÖUserBot Yükleyici"
MESAJ+="\nTelegram: @DTOUserBot"
pkg upgrade
clear
echo -e $MESAJ
echo "Python yüklenir"
pkg install python -y
clear
echo -e $MESAJ
echo "TeleThon yüklenir"
pip install telethon
echo "Requests/BS4 yüklenir"
pip install requests
pip install bs4
clear
echo -e $MESAJ
echo "Fayl yazılır..."
curl "https://raw.githubusercontent.com/umudmmmdov1/DTOUserBot/master/dto.py" --output "dto.py"
clear
echo -e $MESAJ
echo "Qurulum hazırdır, İndi StringSessionu ala bilersiz"
clear
python dto.py
