[EN] OMSI 2 - OPTIMIZATION AND TROUBLESHOOTING GUIDE
====================================================

RECOMMENDED OPTIMIZATIONS
-------------------------
- Settings: Copy the "option.cfg" file to the game folder and confirm changes. If you experience performance drops, set these specific settings to these values or lower:
  * AI Traffic: 80
  * Scheduled Buses: 10
  * Pedestrians: 100
- FPS: If your CPU has weak single-core performance, cap the game at 30 FPS inside the game options. Then, use the "Lossless Scaling" application with "Frame Generation (Fixed 2x)" to upscale it to 60 FPS. Turn off Performance Mode in the app for better results.
- Add "-nolog" parameter to launch options for casual gaming. This prevents the game creating logs and potentially ease the game engine.

TROUBLESHOOTING AND SOLUTIONS
-----------------------------

#### [!!!] FIRST STEPS FOR ANY ERROR:
Before diving into specific fixes, always ensure you have done the following:
1. Check for missing map dependencies using MapTools or an equivalent app.
2. Apply the 4GB Patch directly to your Omsi.exe.
3. Lower your AI/graphic settings, and increase or remove Texture Memory Limit (as setting to 0.0).

------------

>**[Warning]** Before making any changes to files, create a backup for the files you are planning to edit/change.

------------

#### [1] ERROR: "Fehler bei Bereichsprüfung" (Range Check Error)
- Solution: Launch OMSI 2 in editor mode by adding the "-editor" parameter to your launch options. Load the problematic map inside the editor, and simply save it without making any changes. This forces the engine to rewrite and correct character encoding errors within file names.
- When you solve this problem, you most probably face the ERROR number [2] which mentioned below. 

------------

#### [2] ERROR: Map/Textures Not Loading (Only Skybox / Clear Sky Visible)
- Diagnostic: Try loading the map in Editor mode. If it opens perfectly in the editor but fails in the live game, the culprit is a character encoding mismatch between file contents and your Windows locale.
- Fixing the Encoding: Inspect your logfile.txt to see which directory or files are throwing warnings right before the load fails. Those files must be standardized to UTF-8.
  * Example (Gladbeck Map): The Gladbeck map crashes because some files inside the "maps\Gladbeck\TTData" folder are encoded in ANSI while others are in UTF-8.
  * Step 1: Check the files using `check_TTData_if_UTF8_or_ANSI.py` script to see if they are UTF-8 or ANSI. Before that make sure to edit the folder path inside the script matching your directory.
  * Step 2: Run `convert_TTData_to_UTF8.py` script to automatically batch-convert all files in that target folder to UTF-8. Edit the folder path in this script too.

- Alternative Solution: If the issue persists, German characters in the filenames and contents are breaking the engine. You can fix this by saving the map in Editor mode, running "Locale Emulator" targeting German, or changing your Windows System Locale to German. I recommend others before changing your system locale settings, it must be the last thing to do.


------------
[TR] OMSI 2 - OPTİMİZASYON VE SORUN GİDERME KILAVUZU
====================================================

ÖNERİLEN OPTİMİZASYONLAR
------------------------
- Ayarlar: "option.cfg" dosyasını oyun klasörüne kopyalayın ve değişiklikleri onaylayın. Performans düşüşleri yaşarsanız, bu özel ayarları şu değerlere veya daha düşük değerlere ayarlayın:
  * AI Traffic: 80
  * Scheduled Buses: 10
  * Pedestrians: 100
- FPS: İşlemcinizin tek çekirdek performansı zayıfsa, oyun içi seçeneklerden oyunu 30 FPS'ye sabitleyin. Ardından, bunu 60 FPS'ye yükseltmek için "Lossless Scaling" uygulamasının "Frame Generation (Fixed 2x)" ayarıyla Upscale edin. Daha iyi sonuçlar için Performance Mode'u uygulama içinden kapatın.
- Sadece oyun oynamak için başlatma seçeneklerine "-nolog" parametresini ekleyin. Bu, oyunun günlük (log) dosyaları oluşturmasını engeller ve oyun motorunu potansiyel olarak rahatlatır.

SORUN GİDERME VE ÇÖZÜMLER
-------------------------

#### [!!!] HERHANGİ BİR HATA İÇİN İLK ADIMLAR:
Spesifik çözümlere dalmadan önce, her zaman aşağıdakileri yaptığınızdan emin olun:
1. MapTools veya eşdeğer bir uygulama kullanarak haritanın eksik bağımlılıklarını (dosyalarını) kontrol edin.
2. 4GB Patch'i doğrudan Omsi.exe dosyanıza uygulayın.
3. AI ve grafik ayarlarınızı düşürün ve Texture Memory Limit'i artırın veya kaldırın (0.0 yaparak).

------------

>[Uyarı] Dosyalarda herhangi bir değişiklik yapmadan önce, üzerinde değişiklik yapacağınız dosyaların bir yedeğini oluşturun.

------------

#### [1] HATA: "Fehler bei Bereichsprüfung" (Range Check Error)
- Çözüm: Başlatma seçeneklerinize "-editor" parametresini ekleyerek OMSI 2'yi editör modunda başlatın. Sorunlu haritayı editörün içinde yükleyin ve hiçbir değişiklik yapmadan sadece kaydedin. Bu, motoru dosya adlarındaki karakter kodlama hatalarını yeniden yazmaya ve düzeltmeye zorlar.
- Bu sorunu çözdüğünüzde, büyük olasılıkla aşağıda belirtilen [2] numaralı HATA ile karşılaşırsınız.

------------

#### [2] HATA: Harita/Dokular Yüklenmiyor (Sadece Skybox / Gökyüzü Görünüyor)
- Teşhis: Haritayı Editör modunda açmayı deneyin. Editörde kusursuz açılıyor ancak normal oyunda başarısız oluyorsa, sorun dosya içerikleri ile Windows yerel ayarınız (locale) arasındaki karakter kodlama uyuşmazlığıdır.
- Kodlamayı Düzeltme: Açma işlemi başarısız olmadan hemen önce hangi dizinin veya dosyaların uyarı verdiğini görmek için logfile.txt dosyanızı inceleyin. Bu dosyaların UTF-8 olarak standartlaştırılması gerekir.
  * Örnek (Gladbeck Haritası): Gladbeck haritası çöküyor çünkü "maps\Gladbeck\TTData" klasörünün içindeki bazı dosyalar ANSI, diğerleri ise UTF-8 olarak kodlanmış.
  * Adım 1: Dosyaların UTF-8 mi yoksa ANSI mı olduğunu görmek için `check_TTData_if_UTF8_or_ANSI.py` betiğini çalıştırarak dosyaları kontrol edin. İlk önce betiğin içindeki path değerini kendi dosya konumunuz olacak şekilde düzenleyin.
  * Adım 2: Hedef klasördeki tüm dosyaları otomatik olarak toplu halde UTF-8'e dönüştürmek için `convert_TTData_to_UTF8.py` betiğini çalıştırın. Bu betiğin path değerini de çalıştırmadan önce değiştirin.

- Alternatif Çözüm: Sorun devam ederse, dosya adlarındaki ve içeriklerindeki Almanca karakterler oyun motorunu bozuyor demektir. Bunu haritayı Editör modunda kaydederek, Almanca'yı hedefleyen "Locale Emulator" çalıştırarak veya Windows Sistem Yerel Ayarınızı Almanca olarak değiştirerek çözebilirsiniz. Sistem yerel ayarınızı değiştirmeden önce diğerlerini yapmanızı öneririm, bu ayarı değiştirmek en son çareniz olsun.


------------

**If you have anything to add or want something to change, feel free to contribute.**

------------

###### ANYTHING YOU DO IS AT YOUR RESPONSIBILITY.
###### YAPTIĞINIZ HER ŞEY SIZIN SORUMLULUĞUNUZDADIR
