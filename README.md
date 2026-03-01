# Bio-Preserve-Design-Engine-
(Disiplinler Arası Proje)

PROBLEM TANIMI (Akademik ve Net)
 Problem Tanımı

Gıda endüstrisinde mikrobiyal bozulmayı ve patojen kaynaklı riskleri önlemek amacıyla yaygın olarak sentetik kimyasal koruyucular (E-kodlu katkı maddeleri) kullanılmaktadır. Ancak bu maddelerin uzun vadede insan sağlığı, bağırsak mikrobiyotası ve tüketici algısı üzerindeki olumsuz etkileri giderek daha fazla tartışılmaktadır.

Bu kimyasal koruyuculara doğal alternatifler arasında antimikrobiyal peptitler (AMP’ler) öne çıkmaktadır. AMP’ler bakterileri fiziksel mekanizmalarla etkisiz hale getirebilen doğal moleküllerdir. Ancak:

Uygun AMP’lerin laboratuvar ortamında keşfi

Yüksek maliyetlidir

Uzun zaman alır

Deneme–yanılma temellidir

Bu durum, gıda endüstrisinde doğal koruyucuların ticarileşmesini ciddi şekilde yavaşlatmaktadır.

 Temel problem:
Doğru doğal antimikrobiyal peptidin keşfi, mevcut yöntemlerle verimsizdir.

PROJENİN ÇÖZÜM YAKLAŞIMI (Ne Yapıyoruz?)
 Önerilen Çözüm

Bu proje, laboratuvar öncesi aşamada kullanılmak üzere, açık biyolojik veritabanlarını kullanan ve biyolojik kurallarla desteklenmiş hesaplamalı bir karar destek sistemi tasarlamayı amaçlamaktadır.

Sistem:

Bilinen AMP veritabanlarını tarar

Biyolojik uygunluk kriterlerini uygular

Hedef gıda patojenine göre adayları filtreler

Makine öğrenmesi ile adayları olasılıksal olarak değerlendirir

 Amaç:

Laboratuvara girecek peptit sayısını ciddi biçimde azaltmak

 GÜNDELİK HAYATTA NEYE ÇÖZÜM?

Bu proje şu gerçek sorunlara dokunur:

 Gıda Güvenliği

Peynir, et, hazır gıdalarda bakteri riski

Özellikle Listeria monocytogenes gibi patojenler

Kimyasal Katkı Endişesi

Tüketicinin “E-kodsuz ürün” talebi

Doğal içerikli ambalaj ve koruyucu ihtiyacı

Endüstriyel Ar-Ge Maliyeti

Binlerce molekülün tek tek test edilmesi

Yıllar süren ürün geliştirme süreçleri

 Sistem, bu sorunları erken aşamada hafifletir.

UYGULAMAYA NASIL GEÇİRİLİR? (Somutlaştırma)

Bu proje “yazılım ürünü” değil,
“hesaplamalı tasarım aracı”dır.

Uygulama Şekli
 Girdi

Hedef bakteri (ör. Listeria monocytogenes)

Biyolojik sınırlar (yük, uzunluk, toksisite vb.)

Sistem Çalışması

Açık AMP veritabanlarından veri çekilir

Peptit dizileri sayısal özelliklere dönüştürülür

Kurallara uymayanlar elenir

ML modeli ile başarı olasılığı değerlendirilir

 Çıktı

5–10 adet teorik olarak umut vadeden peptit

Her biri için:

Uzunluk

Yük

Hidrofobiklik

Tahmini etki skoru

Bu çıktı laboratuvara öneri listesi olarak verilir.

DAHA ÖNCE YAPILMIŞ BENZER ÇALIŞMALAR VAR MI?

ÇOK ÖNEMLİ:
Bu projeyi güçlü yapan şey, “hiç yapılmamış” olması değil,
“yapılmış akademik çalışmaların sadeleştirilmiş bir sistem mimarisi” olmasıdır.

Literatürde Neler Var?
Var olanlar:

AMP’leri makine öğrenmesiyle sınıflandıran akademik makaleler

AMP tahmini yapan araştırma prototipleri

Biyoinformatik filtreleme yaklaşımları

 Eksik olan:

Gıda endüstrisine özel hedefleme

Disiplinler arası (MBG + Gıda + Bilgisayar) çerçeve

Anlaşılır sistem mimarisi

Endüstriyel ön-eleme amacı

Yani:

Araştırma düzeyinde parçalar var,
ama bizim önerdiğimiz gibi bütüncül ve uygulanabilir bir tasarım yok.
