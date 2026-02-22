# CSV ile Önceden Belirlenmiş Noktaları Kullanma
# Using Predefined Points from CSV

## 📋 Genel Bakış / Overview

Bu özellik, arazi çalışmasından veya diğer kaynaklardan elde edilmiş önceden belirlenmiş doğrulama noktalarını kullanmanıza olanak tanır.

This feature allows you to use predefined validation points obtained from field work or other sources.

---

## 📁 CSV Dosya Formatı / CSV File Format

### Gerekli Sütunlar / Required Columns

CSV dosyanız **mutlaka** şu 4 sütunu içermelidir (başlık satırı dahil):

Your CSV file **must** contain these 4 columns (including header row):

```csv
id,x,y,reference_value
```

| Sütun / Column | Açıklama / Description | Örnek / Example |
|----------------|------------------------|-----------------|
| `id` | Nokta kimliği (benzersiz) / Point identifier (unique) | P001, Site_A, 1 |
| `x` | Boylam (WGS 84) / Longitude (WGS 84) | 30.5234 |
| `y` | Enlem (WGS 84) / Latitude (WGS 84) | 37.8765 |
| `reference_value` | Referans sınıf değeri (tam/ondalıklı) / Reference class value (integer/float) | 1, 2.5, 0.234 |

### 📌 reference_value Formatı

**reference_value** hem **tam sayı** hem de **ondalıklı sayı** olabilir:

**reference_value** can be both **integer** and **float**:

#### Tam Sayı Örneği / Integer Example
```csv
id,x,y,reference_value
P001,30.5234,37.8765,1
P002,30.5456,37.8901,2
P003,30.5678,37.9023,3
```

#### Ondalıklı Sayı Örneği / Float Example
```csv
id,x,y,reference_value
Site_A,30.5234,37.8765,0.234
Site_B,30.5456,37.8901,2.567
Site_C,30.5678,37.9023,4.123
```

#### Karışık Format / Mixed Format
```csv
id,x,y,reference_value
P001,30.5234,37.8765,1.0
P002,30.5456,37.8901,2.5
P003,30.5678,37.9023,3
P004,30.5890,37.9145,4.75
```

---

## ✅ Örnek CSV Dosyası / Sample CSV File

### Tam Sayı Değerler / Integer Values
```csv
id,x,y,reference_value
P001,30.5234,37.8765,1
P002,30.5456,37.8901,2
P003,30.5678,37.9023,1
P004,30.5890,37.9145,3
P005,30.6012,37.9267,2
```

### Ondalıklı Değerler / Float Values
```csv
id,x,y,reference_value
Site_A,30.5234,37.8765,0.234
Site_B,30.5456,37.8901,0.567
Site_C,30.5678,37.9023,0.789
Site_D,30.5890,37.9145,0.456
Site_E,30.6012,37.9267,0.891
```

### Karışık Format / Mixed Format
```csv
id,x,y,reference_value
P001,30.5234,37.8765,1.0
P002,30.5456,37.8901,2.5
P003,30.5678,37.9023,3
P004,30.5890,37.9145,4.75
P005,30.6012,37.9267,5
```

---

## 🌍 Koordinat Sistemi / Coordinate System

**ÖNEMLİ / IMPORTANT:** Koordinatlar **WGS 84 (EPSG:4326)** sisteminde olmalıdır!

Coordinates **must be** in **WGS 84 (EPSG:4326)** system!

### Koordinat Formatı / Coordinate Format

- **X (Boylam/Longitude)**: -180 ile +180 arası / between -180 and +180
- **Y (Enlem/Latitude)**: -90 ile +90 arası / between -90 and +90
- **Ondalık derece formatı** kullanın / Use **decimal degrees** format

### Koordinat Dönüşümü / Coordinate Transformation

Plugin, WGS 84 koordinatlarını otomatik olarak projenizin koordinat sistemine dönüştürür.

The plugin automatically transforms WGS 84 coordinates to your project's coordinate system.

---

## 📍 Kullanım Adımları / Usage Steps

### 1. CSV Dosyasını Hazırlayın / Prepare CSV File

```csv
id,x,y,reference_value
Point_1,30.123456,38.654321,1
Point_2,30.234567,38.765432,2
Point_3,30.345678,38.876543,3
```

### 2. Plugin'de CSV Seçeneğini Seçin / Select CSV Option in Plugin

1. **Örnekleme Yöntemi** / **Sampling Method** → "CSV Dosyasından / From CSV" seçin
2. **Gözat** / **Browse** butonuna tıklayın
3. CSV dosyanızı seçin / Select your CSV file

### 3. Analizi Çalıştırın / Run Analysis

- Plugin otomatik olarak:
  - CSV'den noktaları yükler / Loads points from CSV
  - Koordinatları dönüştürür / Transforms coordinates
  - Sınıflandırılmış haritadan değerleri okur / Reads values from classified map
  - Referans değerleri CSV'den alır / Takes reference values from CSV

---

## 🎯 Referans Değerleri / Reference Values

### reference_value Sütunu

Bu sütun, arazi çalışmanızdan veya uzman yorumunuzdan elde ettiğiniz **gerçek sınıf değerlerini** içermelidir.

This column should contain the **true class values** obtained from your field work or expert interpretation.

### 🔢 Değer Formatları / Value Formats

#### Tam Sayı (Integer) - Kategorik Sınıflar için / For Categorical Classes
Arazi örtüsü, sınıflandırma, vb. için kullanılır.

```csv
id,x,y,reference_value
Field_1,30.123,38.456,1    # 1 = Orman / Forest
Field_2,30.234,38.567,2    # 2 = Tarım / Agriculture
Field_3,30.345,38.678,3    # 3 = Kentsel / Urban
Field_4,30.456,38.789,4    # 4 = Su / Water
Field_5,30.567,38.890,5    # 5 = Çıplak Toprak / Bare Soil
```

#### Ondalıklı Sayı (Float) - Sürekli Değerler için / For Continuous Values
IRSEI, NDVI, ekolojik indeksler vb. için kullanılır.

```csv
id,x,y,reference_value
Site_A,30.111,38.222,0.234    # IRSEI değeri / IRSEI value
Site_B,30.222,38.333,0.567    # IRSEI değeri / IRSEI value
Site_C,30.333,38.444,0.789    # IRSEI değeri / IRSEI value
Site_D,30.444,38.555,0.456    # IRSEI değeri / IRSEI value
```

#### Karma Değerler (Mixed) - Derecelendirme için / For Rating Scales
0.5 aralıklı derecelendirmeler, kalite skorları vb.

```csv
id,x,y,reference_value
Quality_1,30.111,38.222,1.0    # Çok Düşük / Very Low
Quality_2,30.222,38.333,2.5    # Orta / Medium
Quality_3,30.333,38.444,4.0    # Yüksek / High
Quality_4,30.444,38.555,4.75   # Çok Yüksek / Very High
```

**Örnekler / Examples:**

#### Arazi Örtüsü / Land Cover (Kategorik / Categorical)
```csv
id,x,y,reference_value
Field_1,30.123,38.456,1    # 1 = Orman / Forest
Field_2,30.234,38.567,2    # 2 = Tarım / Agriculture
Field_3,30.345,38.678,3    # 3 = Kentsel / Urban
Field_4,30.456,38.789,4    # 4 = Su / Water
Field_5,30.567,38.890,5    # 5 = Çıplak Toprak / Bare Soil
```

#### Ekolojik Kalite / Ecological Quality (Kategorik / Categorical)
```csv
id,x,y,reference_value
Site_A,30.111,38.222,1    # 1 = Kötü / Poor
Site_B,30.222,38.333,3    # 3 = Orta / Moderate
Site_C,30.333,38.444,5    # 5 = Mükemmel / Excellent
```

#### IRSEI İndeksi / IRSEI Index (Sürekli / Continuous)
```csv
id,x,y,reference_value
IRSEI_01,30.111,38.222,0.234    # 0-1 arası / Between 0-1
IRSEI_02,30.222,38.333,0.567
IRSEI_03,30.333,38.444,0.891
```

#### Kalite Skoru / Quality Score (Karma / Mixed)
```csv
id,x,y,reference_value
Q_Point_1,30.111,38.222,1.5    # 1-5 arası / Between 1-5
Q_Point_2,30.222,38.333,3.0
Q_Point_3,30.333,38.444,4.75
```

---

## 📊 Sonuçlarda CSV Bilgileri / CSV Information in Results

Analiz tamamlandığında, shapefile çıktısında şu ek bilgiler yer alır:

When analysis is completed, the shapefile output includes this additional information:

| Alan / Field | Açıklama / Description |
|--------------|------------------------|
| `csv_id` | CSV'deki orijinal nokta ID'si / Original point ID from CSV |
| `ref_value` | CSV'den gelen referans değeri / Reference value from CSV |
| `class_val` | Sınıflandırılmış haritadan okunan değer / Value read from classified map |
| `match` | Eşleşme durumu (Yes/No) / Match status (Yes/No) |

---

## 🔍 CSV Dosya Doğrulama / CSV File Validation

Plugin, CSV dosyanızı yüklerken otomatik olarak kontrol eder:

The plugin automatically validates your CSV file when loading:

### ✅ Kontrol Edilen / Checked Items

1. **Başlık satırı** / **Header row**: `id`, `x`, `y`, `reference_value` sütunları mevcut mu?
2. **Veri formatı** / **Data format**: Her satır 4 sütun içeriyor mu?
3. **Koordinat değerleri** / **Coordinate values**: Sayısal değerler mi?
4. **Referans değerleri** / **Reference values**: Sayısal değerler mi?

### ❌ Hata Durumları / Error Cases

Eğer hata alırsanız / If you get an error:

**"CSV dosyası gerekli sütunları içermiyor"**
- Başlık satırını kontrol edin / Check header row
- Sütun adlarının tam olarak eşleştiğinden emin olun / Ensure column names match exactly
- Virgül ile ayrıldığından emin olun / Ensure comma-separated

**"CSV formatı hatalı"**
- Her satırın 4 değer içerdiğinden emin olun / Ensure each row has 4 values
- Boş satırları kaldırın / Remove empty rows
- Ekstra virgüller veya boşlukları temizleyin / Clean extra commas or spaces

---

## 💡 İpuçları / Tips

### 1. Arazi Çalışması Entegrasyonu / Field Work Integration

GPS cihazınızdan WGS 84 koordinatlarını direkt kullanabilirsiniz:

You can use WGS 84 coordinates directly from your GPS device:

```csv
id,x,y,reference_value
GPS_001,30.123456,38.654321,2
GPS_002,30.234567,38.765432,1
GPS_003,30.345678,38.876543,3
```

### 2. Excel'den CSV'ye Dönüştürme / Converting from Excel to CSV

Excel'de hazırladıysanız:

If you prepared in Excel:

1. Dosya → Farklı Kaydet / File → Save As
2. Dosya türü → CSV (Virgülle Ayrılmış) / File type → CSV (Comma delimited)
3. Kaydet / Save

### 3. Minimum Nokta Sayısı / Minimum Number of Points

- **En az 30 nokta** önerilir / **At least 30 points** recommended
- Sınıf başına en az 10 nokta / At least 10 points per class
- Daha fazla nokta = daha güvenilir sonuçlar / More points = more reliable results

### 4. Nokta Dağılımı / Point Distribution

İyi sonuçlar için / For good results:

- Noktaları çalışma alanına **eşit dağıtın** / **Distribute** points evenly across study area
- Her sınıftan **yeterli örnek** alın / Get **sufficient samples** from each class
- **Sistematik** veya **rastgele** dağılım kullanın / Use **systematic** or **random** distribution

---

## 📖 Örnek Senaryolar / Example Scenarios

### Senaryo 1: Arazi Gözlemi - Kategorik Sınıflar / Field Observation - Categorical Classes

```csv
id,x,y,reference_value
Field_20250115_01,30.5234,37.8765,1
Field_20250115_02,30.5456,37.8901,1
Field_20250115_03,30.5678,37.9023,2
Field_20250115_04,30.5890,37.9145,3
```

### Senaryo 2: IRSEI - Sürekli Değerler / IRSEI - Continuous Values

```csv
id,x,y,reference_value
IRSEI_Site_A,30.1234,38.5678,0.654
IRSEI_Site_B,30.2345,38.6789,0.432
IRSEI_Site_C,30.3456,38.7890,0.789
IRSEI_Site_D,30.4567,38.8901,0.567
```

### Senaryo 3: Arazi Kalitesi - Karma Değerler / Land Quality - Mixed Values

```csv
id,x,y,reference_value
Quality_P1,29.9876,37.5432,2.5
Quality_P2,30.0987,37.6543,3.0
Quality_P3,30.1098,37.7654,1.8
Quality_P4,30.2109,37.8765,4.3
```

### Senaryo 4: NDVI Ölçümleri / NDVI Measurements

```csv
id,x,y,reference_value
NDVI_001,30.111,38.222,0.234
NDVI_002,30.222,38.333,0.456
NDVI_003,30.333,38.444,0.789
NDVI_004,30.444,38.555,0.567
```

---

## 🆚 CSV vs Random/Stratified Sampling

| Özellik / Feature | CSV | Random | Stratified |
|-------------------|-----|--------|------------|
| **Nokta Seçimi** / **Point Selection** | Kullanıcı tanımlı / User-defined | Otomatik rastgele / Auto random | Otomatik grid / Auto grid |
| **Referans Değer** / **Reference Value** | CSV'den / From CSV | Haritadan / From map | Haritadan / From map |
| **Arazi Çalışması** / **Field Work** | Uygun / Suitable | Uygun değil / Not suitable | Uygun değil / Not suitable |
| **Tekrarlanabilirlik** / **Reproducibility** | Yüksek / High | Düşük / Low | Orta / Medium |
| **Esneklik** / **Flexibility** | Yüksek / High | Düşük / Low | Orta / Medium |

---

## ⚠️ Önemli Notlar / Important Notes

1. **Koordinat Sistemi**: Koordinatlar **mutlaka WGS 84** olmalı!
   
   **Coordinate System**: Coordinates **must be WGS 84**!

2. **Karakter Kodlaması**: CSV dosyanız **UTF-8** kodlamasında olmalı
   
   **Character Encoding**: CSV file should be in **UTF-8** encoding

3. **Ondalık Ayırıcı**: Nokta (.) kullanın, virgül (,) değil
   
   **Decimal Separator**: Use dot (.), not comma (,)

4. **Boş Değerler**: Boş satır veya eksik değer olmamalı
   
   **Empty Values**: No empty rows or missing values

---

## 🔧 Sorun Giderme / Troubleshooting

### Problem: "Koordinatlar harita sınırları dışında"

**Çözüm / Solution:**
- Koordinatların WGS 84 formatında olduğundan emin olun
- X ve Y değerlerini ters çevirmediyseniz kontrol edin
- Koordinatların çalışma alanınızda olduğunu doğrulayın

### Problem: "Geçersiz referans değerleri"

**Çözüm / Solution:**
- reference_value sütununun sayısal değerler içerdiğinden emin olun
- Ondalık ayırıcı olarak nokta (.) kullanın
- Negatif değerler veya metin olmamalı

### Problem: "CSV dosyası okunamıyor"

**Çözüm / Solution:**
- Dosya UTF-8 kodlamasında mı?
- Virgülle ayrılmış mı?
- Excel'de açıp CSV olarak yeniden kaydedin

---

## 📞 Ek Yardım / Additional Help

Daha fazla bilgi için:

For more information:

- Plugin README.md dosyasına bakın / See plugin README.md
- QGIS_PLUGIN_KURULUM_REHBERI.md dosyasını inceleyin / Check QGIS_PLUGIN_KURULUM_REHBERI.md
- Örnek CSV dosyasını kullanarak test edin / Test using sample CSV file

---

**İyi çalışmalar! / Good luck with your accuracy assessment!** 🚀
