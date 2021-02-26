# Final-Project-JCDS-0506-BDG-Bernard-Evan-Kanigara
Memprediksi pekerja yang akan melakukan 'attrition' (pengunduran diri) pada sebuah perusahaan

## Latar Belakang
Employee Attrition merupakan sebuah kondisi di mana perusahaan kehilangan pekerjanya. Hal tersebut dapat terjadi karena berbagai macam alasan, sebut saja alasan personal, rendahnya kepuasan di kantor, gaji yang kurang, dan lingkungan kerja yang buruk. Perusahaan yang kehilangan pekerjanya dapat merugi karena perusahaan telah menginvestasikan dana dan waktu untuk merekrut dan melatih pekerjanya. Memprediksi pekerja yang akan melakukan attrition dapat digunakan untuk mencegah pekerja resign. Perusahaan dapat melaukan pendekatan ke pekerja yang bersangkutan agar kecenderungan pekerja untuk pergi menjadi menurun. Selain itu, prediksi dapat digunakan sebagai tolak ukur evaluasi terhadap lingkungan kerja itu sendiri.  

## Tujuan
Memprediksi pekerja yang akan melakukan attrition berdasarkan data dari rekam jejak kerjanya selama di perusahaan. 

## Data 
Data terdiri dari 1470 baris dan 35 kolom. Fitur-fiturnya terdiri dari:
- Age: Umur
- BusinessTravel: Frekuensi perjalanan kantor
- DailyRate: Upah Harian
- Department: Departemen 
- DistanceFromHome: Jarak rumah dari kantor
- Education: Tingkatan pendidikan (ordinal)
- EducationField: Bidang studi pendidikan
- EnvironmentStatisfaction: Tingkat kepuasan pekerja terhadap lingkungan kerjanya
- Gender: Gender
- Hourlyrate: Upah perjam
- JobInvolvement: Jumlah proyek perusahaan yang pernah digeluti
- JobLevel: Tingakatan jabatan
- JobRole: Subdivisi dalam perusahaan
- JobStatisfaction: Tingkat kepuasaan pekerja terhadap tugas kerjanya
- MaritalStatus: Hubungan dengan pasangan
- MonthlyIncome: Gaji bulanan
- MonthlyRate: Upah bulanan
- NumCompaniesWorked: Jumlah perusahaan yang pernah ditempati
- OverTime: Status lembur
- PercentSalaryHike: Jumlah persentase kenaikan gaji
- PerformanceRating: Tingkat performa kerja
- RelationshipSatisfaction: Tingkat kebahagiaan dalam hubungan 
- StockOptionLevel: Jumlah opsi saham yang dimiliki
- TotalWorkingYears: Lamanya bekerja dalam tahun
- TrainingTimesLastYear: Lamanya bekerja tahun lalu
- WorkLifeBalance: Kualitas work life balance
- YearsAtCompany: Lama kerja di perusahaan saat ini
- YearsInCurrentRole: Lama kerja di divisi saat ini
- YearsSinceLastPromotion: Lama tahun sejak promosi terakhir
- YearsWithCurrManager: Lama tahun dengan manajer saat ini

## Visualisasi Data 1
<img src='/static/visual1.png'>
Pekerja yang lembur cenderung untuk resign

## Visualisasi Data 2
<img src='/static/visual2.png'>
Semakin lama pekerja berada pada perusahaan maka cenderung untuk tidak melakukan resign


## Pre-processing Data
<img src='/static/drawio.jpg'>
Proses pembersihan dan transformasi dilakukan dalam sebuah pipeline. Dalam pipeline dilakukan imputasi untuk meng-handle missing values. Lalu setelah itu dilakukan standarisasi. Untuk data categorical dilakukan encode berupa one hot encoder. PCA juga dilakukan pada fitur yang memiliki korelasi yang cukup tinggi. Setelah proses cleaning dan transformasi maka akan dilakukan feature selection menggunakan RFE. Jumlah data yang tidak berimbang akan diimbangi dengan oversampling SMOTE. Setelah itu data akan siap untuk dilatih dalam model yang sudah dipilih. 

## Hasil
| Algoritma      | Recall_CV | Recall_Benchmark      | Recall_Tuned |
| ----------- | ----------- |----------- | ----------- |
| logit      | 0.68       |0.68      | 0.77       |
| dtc   | 0.43        |0.45      | 0.70   |
| knn   | 0.58        |0.62      | 0.74       |
| naive-bayes   | 0.84        |0.77      | -       |
| RandomForest   | 0.17        |0.28      | 0.28       |
| Balanced RandomForest   | 0.72        |0.68      | 0.66       |
| Balanced Bagging   | 0.63        |0.6      | 0.68       |

Scoring yang diutamakan dalam klasifikasi adalah Recall. Perusahaan ingin sebanyak-banyaknya mencegah pekerjanya yang hendak resign. Kehilangan pekerja akan menyebabkan perusahaan merugi karena harus melaukan rekrutmen dan pelatihan ulang. Setelah berbagai algoritma digunakan untuk melihat hasil recall terbaik, maka dipilihlah logistic regression. Meskipun begitu, tingkatan presisi secara umum cenderung rendah. Perusahaan harus berhati-hati jangan sampai proses perawatan pekerjanya justru membuat perusahaan merugi lebih banyak. 

## Dashboard
<img src='/static/dashboard.PNG'>

## Kesimpulan
<a href='https://mnwi.usi.com/Resources/Resource-Library/Resource-Library-Article/ArtMID/666/ArticleID/782/Cost-of-employee-turnover#:~:text=The%20Society%20for%20Human%20Resource,in%20recruiting%20and%20training%20costs.'>Penelitian</a> dari Society for Human Resource Management (SHRM) mengatakan bahwa kerugian rekrutmen dan pelatihan ulang akibat employee attrition adalah sebesar 6 sampai 9 kali dari gaji pekerja yang resign. Rata-rata gaji bulanan pekerja IBM adalah $6500. Maka kerugian IBM karena satu pekerjanya yang resign adalah $39000. Dengan asumsi perusahaan pada akhirnya dapat mencegah semua employee attrition yang diprediksi, recall prediksi klasifikasi sebesar 77% akan membuat perusahaan menghemat pengeluaran sebesar $1404000.
