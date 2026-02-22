# 🌍 Raster Accuracy Assessment Plugin

**QGIS 3.x Compatible | QGIS 3.x Uyumlu**

---

## 🇬🇧 English

### Overview

**Raster Accuracy Assessment** is a general-purpose QGIS plugin for performing validation and accuracy analysis between two raster maps. It is especially useful for evaluating the quality of classified remote sensing products (e.g. land use / land cover maps) by comparing them against a reference (ground truth) dataset.

The plugin was developed with the assistance of Claude AI (Anthropic).

---

### Features

- **Multiple Sampling Methods:** Random, Stratified, Systematic, and CSV file import
- **Flexible Class Mapping:** Interactive dialog for matching class values between the two rasters
- **Comprehensive Accuracy Metrics:**
  - Overall Accuracy (OA)
  - Cohen's Kappa (κ)
  - F1-Score (Macro & Weighted)
  - Precision & Recall (Macro)
  - Producer's Accuracy & User's Accuracy (per class)
  - Confusion Matrix
  - R² (Coefficient of Determination)
  - RMSE (Root Mean Square Error)
  - MAE (Mean Absolute Error)
  - Bias (Mean Error)
- **Export Options:** TXT, JSON, HTML report, and Shapefile (sample points)
- **Bilingual Interface:** Turkish and English labels throughout

---

### Requirements

| Dependency | Version |
|---|---|
| QGIS | ≥ 3.0 |
| Python | ≥ 3.6 |
| NumPy | ≥ 1.18 |
| scikit-learn | ≥ 0.24 |

> Install Python dependencies via OSGeo4W Shell or QGIS Python console:
> ```
> pip install numpy scikit-learn
> ```

---

### Installation

1. Download or clone this repository
2. Copy the plugin folder to your QGIS plugins directory:
   - **Windows:** `C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **Linux:** `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **macOS:** `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
3. Open QGIS → **Plugins** → **Manage and Install Plugins** → Enable **Raster Accuracy Assessment**

---

### Usage

1. Load at least two raster layers into QGIS (reference map and classified map)
2. Open the plugin from the **Plugins** menu or toolbar
3. Select the **Reference Map** (ground truth) and **Classified Map**
4. Choose a **Sampling Method** and set the number of sample points
5. Click **Run Analysis**
6. In the **Class Mapping Dialog**, assign matching categories to class values
7. Review results in the **Results** panel
8. Export the report or save sample points as needed

#### CSV File Format

If using the CSV import option, the file must contain the following columns (with or without a header row):

```
point_id, x_coordinate, y_coordinate, reference_value
```

---

### Metrics Description

| Metric | Description |
|---|---|
| Overall Accuracy | Proportion of correctly classified samples |
| Cohen's Kappa (κ) | Agreement corrected for chance (0–1 scale) |
| F1-Score | Harmonic mean of Precision and Recall |
| Precision | Ratio of true positives to all predicted positives |
| Recall | Ratio of true positives to all actual positives |
| Producer's Accuracy | Per-class recall (omission error complement) |
| User's Accuracy | Per-class precision (commission error complement) |
| R² | Coefficient of determination between reference and classified values |
| RMSE | Root Mean Square Error — sensitive to large deviations |
| MAE | Mean Absolute Error — average magnitude of errors |
| Bias | Systematic over- or underestimation (positive = overestimation) |

#### Kappa Interpretation (Landis & Koch, 1977)

| Kappa | Interpretation |
|---|---|
| < 0.00 | Poor |
| 0.00 – 0.20 | Slight |
| 0.21 – 0.40 | Fair |
| 0.41 – 0.60 | Moderate |
| 0.61 – 0.80 | Substantial |
| 0.81 – 1.00 | Almost Perfect |

---

### Changelog

**v1.1.0**
- Added regression statistics: R², RMSE, MAE, Bias (raw pixel values and category values)
- Improved HTML report with regression statistics section
- Bug fixes in class mapping and NoData handling

**v1.0.0**
- Initial release
- Random, stratified and systematic sampling
- CSV point import with reference values
- Class mapping dialog
- Metrics: OA, Kappa, F1, Precision, Recall, Confusion Matrix
- Export to TXT, JSON, HTML and Shapefile

---

### Author

**Ömer K. ÖRÜCÜ**  
📧 omerorucu@sdu.edu.tr  
Süleyman Demirel University

*Developed with the assistance of Claude AI (Anthropic)*

---

### License

This plugin is distributed under the [GNU General Public License v2 or later (GPL-2.0+)](https://www.gnu.org/licenses/gpl-2.0.html), consistent with QGIS plugin standards.

---
---

## 🇹🇷 Türkçe

### Genel Bakış

**Raster Accuracy Assessment**, iki raster harita arasında doğrulama ve doğruluk analizi yapmak için geliştirilmiş genel amaçlı bir QGIS eklentisidir. Özellikle uzaktan algılama ile üretilen sınıflandırılmış haritaların (arazi kullanımı / arazi örtüsü vb.) referans (gerçek arazi) verileriyle karşılaştırılarak kalitesinin değerlendirilmesinde kullanılır.

Eklenti, Claude AI (Anthropic) desteğiyle geliştirilmiştir.

---

### Özellikler

- **Çoklu Örnekleme Yöntemleri:** Rastgele, Katmanlı, Sistematik ve CSV dosyasından içe aktarım
- **Esnek Sınıf Eşleştirme:** İki raster arasındaki sınıf değerlerini eşleştirmek için interaktif arayüz
- **Kapsamlı Doğruluk Metrikleri:**
  - Genel Doğruluk (Overall Accuracy - OA)
  - Cohen's Kappa (κ)
  - F1-Score (Makro & Ağırlıklı)
  - Kesinlik & Duyarlılık (Precision & Recall - Makro)
  - Üretici Doğruluğu & Kullanıcı Doğruluğu (sınıf bazlı)
  - Karmaşıklık Matrisi (Confusion Matrix)
  - R² (Determinasyon Katsayısı)
  - RMSE (Kök Ortalama Karesel Hata)
  - MAE (Ortalama Mutlak Hata)
  - Bias (Ortalama Hata / Sistematik Sapma)
- **Dışa Aktarım:** TXT, JSON, HTML raporu ve Shapefile (örnekleme noktaları)
- **İki Dilli Arayüz:** Tüm arayüz Türkçe ve İngilizce etiketlerle sunulmaktadır

---

### Gereksinimler

| Bağımlılık | Sürüm |
|---|---|
| QGIS | ≥ 3.0 |
| Python | ≥ 3.6 |
| NumPy | ≥ 1.18 |
| scikit-learn | ≥ 0.24 |

> Python bağımlılıklarını OSGeo4W Shell veya QGIS Python konsolu üzerinden yükleyin:
> ```
> pip install numpy scikit-learn
> ```

---

### Kurulum

1. Bu repoyu indirin veya klonlayın
2. Eklenti klasörünü QGIS eklentiler dizinine kopyalayın:
   - **Windows:** `C:\Users\<kullanıcı_adı>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`
   - **Linux:** `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **macOS:** `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
3. QGIS'i açın → **Eklentiler** → **Eklentileri Yönet ve Kur** → **Raster Accuracy Assessment** eklentisini etkinleştirin

---

### Kullanım

1. QGIS'e en az iki raster katman yükleyin (referans harita ve sınıflandırılmış harita)
2. Eklentiyi **Eklentiler** menüsünden veya araç çubuğundan açın
3. **Referans Harita** (ground truth) ve **Sınıflandırılmış Harita**'yı seçin
4. **Örnekleme Yöntemi**'ni ve nokta sayısını belirleyin
5. **Analizi Çalıştır** butonuna tıklayın
6. Açılan **Sınıf Eşleştirme Diyaloğu**'nda sınıf değerlerini eşleştirin
7. Sonuçları **Sonuçlar** panelinden inceleyin
8. Raporu dışa aktarın veya örnekleme noktalarını kaydedin

#### CSV Dosya Formatı

CSV içe aktarma seçeneğinde dosya şu sütunları içermelidir (başlık satırı isteğe bağlıdır):

```
nokta_id, x_koordinatı, y_koordinatı, referans_değeri
```

---

### Metrik Açıklamaları

| Metrik | Açıklama |
|---|---|
| Overall Accuracy | Doğru sınıflandırılan örneklerin toplam örneklere oranı |
| Cohen's Kappa (κ) | Rastlantısallığa göre düzeltilmiş uyum ölçüsü (0–1 arası) |
| F1-Score | Precision ve Recall'un harmonik ortalaması |
| Precision (Kesinlik) | Gerçek pozitiflerin tahmin edilen tüm pozitiflere oranı |
| Recall (Duyarlılık) | Gerçek pozitiflerin gerçek tüm pozitiflere oranı |
| Üretici Doğruluğu | Sınıf bazlı Recall (atlama hatası tümleyeni) |
| Kullanıcı Doğruluğu | Sınıf bazlı Precision (komisyon hatası tümleyeni) |
| R² | Referans ile sınıflandırılmış değerler arasındaki determinasyon katsayısı |
| RMSE | Kök Ortalama Karesel Hata — büyük sapmalara karşı hassas |
| MAE | Ortalama Mutlak Hata — hataların ortalama büyüklüğü |
| Bias | Sistematik fazla veya az tahmin (pozitif = fazla tahmin) |

#### Kappa Yorumlama Skalası (Landis & Koch, 1977)

| Kappa | Yorum |
|---|---|
| < 0.00 | Zayıf (Poor) |
| 0.00 – 0.20 | Hafif (Slight) |
| 0.21 – 0.40 | Orta (Fair) |
| 0.41 – 0.60 | İyi (Moderate) |
| 0.61 – 0.80 | Çok İyi (Substantial) |
| 0.81 – 1.00 | Mükemmel (Almost Perfect) |

---

### Sürüm Geçmişi

**v1.1.0**
- Regresyon istatistikleri eklendi: R², RMSE, MAE, Bias (ham piksel değerleri ve kategori değerleri)
- HTML raporuna regresyon istatistikleri bölümü eklendi
- Sınıf eşleştirme ve NoData işlemede hata düzeltmeleri

**v1.0.0**
- İlk sürüm yayınlandı
- Rastgele, katmanlı ve sistematik örnekleme
- CSV dosyasından referans değerleri ile nokta yükleme
- Sınıf eşleştirme diyaloğu
- Metrikler: OA, Kappa, F1, Precision, Recall, Confusion Matrix
- TXT, JSON, HTML ve Shapefile olarak dışa aktarım

---

### Yazar

**Ömer K. ÖRÜCÜ**  
📧 omerorucu@sdu.edu.tr  
Süleyman Demirel Üniversitesi

*Claude AI (Anthropic) desteğiyle geliştirilmiştir*

---

### Lisans

Bu eklenti, QGIS eklenti standartlarıyla uyumlu olarak [GNU Genel Kamu Lisansı v2 veya üstü (GPL-2.0+)](https://www.gnu.org/licenses/gpl-2.0.html) kapsamında dağıtılmaktadır.
