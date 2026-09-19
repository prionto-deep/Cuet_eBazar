"""
Seed script — populates the database with 5 categories and 50 products.
Run: python seed.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)


# ── Real HD product image URLs ────────────────────────────────────────────────
PRODUCT_IMAGES = {
    # Smartphones
    "Samsung Galaxy S24 Ultra":    "https://images.samsung.com/is/image/samsung/p6pim/uk/2401/gallery/uk-galaxy-s24-ultra-s928-sm-s928bzkgbtu-thumb-539573100",
    "Apple iPhone 15 Pro Max":     "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-7inch-naturaltitanium?wid=800&hei=800&fmt=jpeg&qlt=90&.v=1692845702708",
    "Xiaomi 14 Pro":               "https://i01.appmifile.com/webfile/globalimg/products/m/xiaomi14/pro/section1-phone.png",
    "OnePlus 12":                  "https://oasis.opstatics.com/content/dam/oasis/page/2024/global/products/12/spec/silky-black-img.png",
    "Google Pixel 8 Pro":          "https://store.google.com/gb/images/products/pixel_8_pro/pixel_8_pro_bay_1.jpg",
    "Samsung Galaxy A54 5G":       "https://images.samsung.com/is/image/samsung/p6pim/uk/sm-a546blgabtu/gallery/uk-galaxy-a54-5g-sm-a546-sm-a546blgabtu-thumb-535393332",
    "Realme GT 5 Pro":             "https://image01.realme.net/general/20231116/1700112989474.png",
    "Vivo X100 Pro":               "https://www.vivo.com/content/dam/vivo-site/in-en/products/x100pro/overview/kv-image.png",
    "OPPO Find X7 Ultra":          "https://image.oppo.com/content/dam/oppo/common/mkt/v2-2/find-x7-ultra/navigation/OPPO-Find-X7-Ultra-Sand-Color.png",
    "Motorola Edge 40 Pro":        "https://motorola-global-portal.custhelp.com/ci/fattach/get/1156929/0/filename/Edge40Pro_black.png",
    # Laptops
    "Apple MacBook Air M3":        "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/macbook-air-midnight-config-20240308?wid=820&hei=498&fmt=jpeg&qlt=90",
    "Dell XPS 15 9530":            "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/xps-notebooks/xps-15-9530/media-gallery/notebook-xps-9530-t-black-gallery-3.psd?fmt=pjpg&pscan=auto&scl=1&wid=800&hei=800&qlt=100,1&resMode=sharp2&size=800,800",
    "Lenovo ThinkPad X1 Carbon":   "https://p3-ofp.static.pub/fes/cms/2022/09/23/r8eu0fk8qijbfiqjh3g7g4vamgbzii3626.png",
    "HP Spectre x360 14":          "https://ssl-product-images.www8-hp.com/digmedialib/prodimg/knowledgebase/c08466404.png",
    "ASUS ROG Zephyrus G14":       "https://dlcdnwebimgs.asus.com/gain/73B3F5C0-0AAA-4EDF-B63E-6B4B1B67ACF3",
    "Microsoft Surface Laptop 5":  "https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4OXbO?ver=1e3b",
    "Acer Swift X 14":             "https://static.acer.com/up/Resource/Acer/Laptops/Swift_X_14/Images/20230112/SFX14-72G-Hero-image.png",
    "LG Gram 16":                  "https://www.lg.com/us/images/laptops/md08003747/gallery/D-1.jpg",
    "Razer Blade 15":              "https://assets2.razerzone.com/images/pnx.assets/6d9cc5e0-c9ab-4a9e-a404-3d1a9c8ebe54/razer-blade-15-store-hero-2023.png",
    "Lenovo IdeaPad Slim 5":       "https://p3-ofp.static.pub/fes/cms/2023/11/13/ohu44n42n8evqo1vwxblhao6jlv8hn618.png",
    # Headphones
    "Sony WH-1000XM5":             "https://www.sony.com/image/6345e8ec5f1c2a919a5a5a1b3c1e1e1e?fmt=png-alpha&wid=800",
    "Apple AirPods Pro 2nd Gen":   "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/MQD83?wid=800&hei=800&fmt=jpeg&qlt=90",
    "Bose QuietComfort 45":        "https://assets.bose.com/content/dam/Bose_DAM/Web/consumer_electronics/global/products/headphones/qc45/product_silo_images/QC45_PDP_Ecom-Gallery-B01.png/jcr:content/renditions/cq5dam.web.1280.1280.png",
    "Sennheiser Momentum 4":       "https://assets.sennheiser.com/img/27416/x1_desktop_Momentum4Wireless_Black_front_1080.jpg",
    "JBL Tune 760NC":              "https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dwb1b2c5ce/JBL_TUNE760NC_Product%20Image_Hero_Black.png",
    "Jabra Evolve2 85":            "https://www.jabra.com/~/media/Images/Products/Jabra%20Evolve2%2085/Jabra%20Evolve2%2085%20UC%20Stereo%20right%20view.png",
    "Samsung Galaxy Buds2 Pro":    "https://images.samsung.com/is/image/samsung/p6pim/uk/sm-r510nlvabtu/gallery/uk-galaxy-buds2-pro-sm-r510-sm-r510nlvabtu-thumb-533412812",
    "Sony WF-1000XM5":             "https://www.sony.com/image/5d02da5df552836db894cead8a68f5f3?fmt=png-alpha&wid=800",
    "Anker Soundcore Q45":         "https://cdn.shopify.com/s/files/1/0493/9834/9974/files/A3040_01.jpg",
    "Beyerdynamic DT 770 Pro":     "https://europe.beyerdynamic.com/media/catalog/product/cache/1/image/1800x/040ec09b1e35df139433887a97daa66f/b/e/beyerdynamic_dt770pro_80ohms_front.jpg",
    # Smart TVs
    "Samsung 65\" QLED 4K Q80C":  "https://images.samsung.com/is/image/samsung/p6pim/uk/qe65q80catxxu/gallery/uk-qled-4k-q80c-qe65q80catxxu-thumb-536841848",
    "LG C3 OLED 55\" evo":        "https://www.lg.com/us/images/tvs/md08004993/gallery/D-1.jpg",
    "Sony Bravia XR A80L 65\"":   "https://www.sony.co.uk/image/5d02da5df552836db894cead8a68f5f3?fmt=png&wid=800",
    "TCL 55\" C835 Mini LED":     "https://www.tcl.com/content/dam/tcl/product-images/tv/C835-TCL-TV-GF.png",
    "Hisense 65\" U8K Mini LED":  "https://www.hisense.com.au/content/dam/hisense-au/products/tvs/U8K/65U8K/65U8K-front.png",
    "Samsung 75\" Crystal UHD":   "https://images.samsung.com/is/image/samsung/p6pim/uk/ue75cu8000kxxu/gallery/uk-crystal-uhd-cu8000-ue75cu8000kxxu-thumb-536140764",
    "LG 43\" UHD 4K UR80":       "https://www.lg.com/us/images/tvs/md08004721/gallery/D-1.jpg",
    "Xiaomi TV S Pro 65\"":       "https://i01.appmifile.com/webfile/globalimg/products/m/xiaomi-tv-s-pro/1.jpg",
    "OnePlus TV Y1S Pro 65\"":    "https://image01.oneplus.net/globalimg/products/2022/08/02/oneplustvpro65y1s.png",
    "Vizio 50\" M-Series Quantum": "https://www.vizio.com/content/dam/vizio/images/tv/2023/M50Q7-J01/M50Q7-J01-1000x563.jpg",
    # Cameras
    "Canon EOS R6 Mark II":        "https://www.canon.co.uk/content/dam/Canon/Home/Consumer/camera-product-images/eos-r/eos-r6-mark-ii/gallery/Canon-EOS-R6-Mark-II-Front.jpg",
    "Sony Alpha A7 IV":            "https://www.sony.com/en/articles/product-images/ilce7m4_body_cep_1.png",
    "Nikon Z8":                    "https://imaging.nikon.com/lineup/mirrorless/z8/img/top/kv_image_sp.png",
    "Fujifilm X-T5":               "https://fujifilm-x.com/wp-content/uploads/2022/11/x-t5_silver_front.png",
    "GoPro HERO12 Black":          "https://community.gopro.com/t5/image/serverpage/image-id/698628i8D4A0AEABF7F7DBF/image-size/large?v=v2&px=999",
    "Canon EOS R50":               "https://www.canon.co.uk/content/dam/Canon/Home/Consumer/camera-product-images/eos-r/eos-r50/gallery/Canon-EOS-R50-Front-view.jpg",
    "Sony ZV-E10 II":              "https://www.sony.com/image/8c6a3f59e9c30c4a7e26d1b9c0b79c7a?fmt=png-alpha&wid=800",
    "DJI Osmo Pocket 3":           "https://dji-official-fe.djicdn.com/dps/c0e0a55f0a7aadbb9f27aebe5faa89b5.png",
    "Nikon Z30":                   "https://imaging.nikon.com/lineup/mirrorless/z30/img/top/z30_detail01_02.png",
    "Panasonic Lumix G100D":       "https://panasonic.net/cns/sav/products/lumix/g100d/img/dc_g100d_front.png",
}

CATEGORIES = [
    {"name": "Smartphones",  "slug": "smartphones",  "icon": "📱", "description": "Latest smartphones and mobile devices"},
    {"name": "Laptops",      "slug": "laptops",      "icon": "💻", "description": "Laptops, notebooks, and ultrabooks"},
    {"name": "Headphones",   "slug": "headphones",   "icon": "🎧", "description": "Headphones, earbuds, and audio gear"},
    {"name": "Smart TVs",    "slug": "smart-tvs",    "icon": "📺", "description": "4K and 8K smart televisions"},
    {"name": "Cameras",      "slug": "cameras",      "icon": "📷", "description": "DSLR, mirrorless, and action cameras"},
]

PRODUCTS = {
    "smartphones": [
        {"name": "Samsung Galaxy S24 Ultra", "brand": "Samsung", "price_bdt": 139999, "rating": 4.8, "review_count": 1240, "stock": 50,  "description": "6.8\" QHD+ AMOLED, Snapdragon 8 Gen 3, 200MP camera, 5000mAh battery. The ultimate Samsung flagship."},
        {"name": "Apple iPhone 15 Pro Max",  "brand": "Apple",   "price_bdt": 179999, "rating": 4.9, "review_count": 2100, "stock": 30,  "description": "6.7\" Super Retina XDR, A17 Pro chip, 48MP ProRAW camera system, titanium design."},
        {"name": "Xiaomi 14 Pro",            "brand": "Xiaomi",  "price_bdt": 89999,  "rating": 4.6, "review_count": 780,  "stock": 80,  "description": "6.73\" 2K LTPO AMOLED, Snapdragon 8 Gen 3, Leica Summilux optics, 120W fast charging."},
        {"name": "OnePlus 12",               "brand": "OnePlus", "price_bdt": 79999,  "rating": 4.7, "review_count": 640,  "stock": 60,  "description": "6.82\" LTPO3 AMOLED, Snapdragon 8 Gen 3, Hasselblad camera, 100W SUPERVOOC charging."},
        {"name": "Google Pixel 8 Pro",       "brand": "Google",  "price_bdt": 109999, "rating": 4.7, "review_count": 890,  "stock": 45,  "description": "6.7\" LTPO OLED, Google Tensor G3, 50MP + 48MP + 48MP cameras, 7 years of updates."},
        {"name": "Samsung Galaxy A54 5G",    "brand": "Samsung", "price_bdt": 42999,  "rating": 4.5, "review_count": 2340, "stock": 120, "description": "6.4\" Super AMOLED, 50MP OIS camera, 5000mAh battery, IP67 water resistance."},
        {"name": "Realme GT 5 Pro",          "brand": "Realme",  "price_bdt": 59999,  "rating": 4.4, "review_count": 430,  "stock": 70,  "description": "6.78\" AMOLED, Snapdragon 8 Gen 3, 50MP Sony IMX890, 240W hyper charge."},
        {"name": "Vivo X100 Pro",            "brand": "Vivo",    "price_bdt": 99999,  "rating": 4.6, "review_count": 560,  "stock": 40,  "description": "6.78\" AMOLED, Dimensity 9300, Zeiss optics, 100W wireless charging."},
        {"name": "OPPO Find X7 Ultra",       "brand": "OPPO",    "price_bdt": 119999, "rating": 4.5, "review_count": 310,  "stock": 25,  "description": "6.82\" OLED, Snapdragon 8 Gen 3, dual periscope Hasselblad cameras, 100W charging."},
        {"name": "Motorola Edge 40 Pro",     "brand": "Motorola","price_bdt": 54999,  "rating": 4.3, "review_count": 380,  "stock": 90,  "description": "6.67\" pOLED 165Hz, Snapdragon 8 Gen 2, 165W TurboPower charging, IP68 rated."},
    ],
    "laptops": [
        {"name": "Apple MacBook Air M3",         "brand": "Apple",      "price_bdt": 154999, "rating": 4.9, "review_count": 1780, "stock": 35, "description": "13.6\" Liquid Retina, Apple M3 chip, 16GB RAM, 256GB SSD, 18-hr battery, fanless design."},
        {"name": "Dell XPS 15 9530",             "brand": "Dell",       "price_bdt": 219999, "rating": 4.7, "review_count": 920,  "stock": 20, "description": "15.6\" OLED touch, Intel Core i9-13900H, 32GB DDR5, RTX 4060, 1TB NVMe SSD."},
        {"name": "Lenovo ThinkPad X1 Carbon",    "brand": "Lenovo",     "price_bdt": 189999, "rating": 4.8, "review_count": 1120, "stock": 28, "description": "14\" IPS 2.8K OLED, Intel Core Ultra 7, 32GB LPDDR5, 1TB SSD, MIL-STD-810H certified."},
        {"name": "HP Spectre x360 14",           "brand": "HP",         "price_bdt": 174999, "rating": 4.6, "review_count": 680,  "stock": 30, "description": "14\" 2.8K OLED touchscreen 2-in-1, Intel Core Ultra 7, 16GB RAM, 1TB SSD, OLED stylus."},
        {"name": "ASUS ROG Zephyrus G14",        "brand": "ASUS",       "price_bdt": 194999, "rating": 4.7, "review_count": 840,  "stock": 22, "description": "14\" QHD 165Hz, AMD Ryzen 9 7940HS, RX 7600S, 16GB DDR5, 1TB SSD, AniMe Matrix LED."},
        {"name": "Microsoft Surface Laptop 5",   "brand": "Microsoft",  "price_bdt": 159999, "rating": 4.5, "review_count": 540,  "stock": 40, "description": "13.5\" PixelSense touch, Intel Core i7-1265U, 16GB RAM, 512GB SSD, Windows 11 Home."},
        {"name": "Acer Swift X 14",              "brand": "Acer",       "price_bdt": 109999, "rating": 4.4, "review_count": 430,  "stock": 55, "description": "14\" 2.8K OLED, Intel Core i7-13700H, RTX 4050, 16GB RAM, 1TB SSD, sleek aluminum body."},
        {"name": "LG Gram 16",                   "brand": "LG",         "price_bdt": 144999, "rating": 4.6, "review_count": 390,  "stock": 33, "description": "16\" WQXGA IPS, Intel Core Ultra 7, 16GB RAM, 512GB SSD, only 1.19kg, MIL-STD certified."},
        {"name": "Razer Blade 15",               "brand": "Razer",      "price_bdt": 299999, "rating": 4.7, "review_count": 660,  "stock": 15, "description": "15.6\" QHD 240Hz, Intel Core i9-13950HX, RTX 4070, 32GB RAM, 1TB SSD, CNC aluminum."},
        {"name": "Lenovo IdeaPad Slim 5",        "brand": "Lenovo",     "price_bdt": 69999,  "rating": 4.3, "review_count": 1640, "stock": 80, "description": "14\" 2.8K OLED, AMD Ryzen 5 7530U, 16GB RAM, 512GB SSD, slim profile, great value."},
    ],
    "headphones": [
        {"name": "Sony WH-1000XM5",          "brand": "Sony",         "price_bdt": 34999, "rating": 4.9, "review_count": 3420, "stock": 60,  "description": "Industry-leading ANC, 30-hr battery, LDAC Hi-Res Audio, multipoint connection, foldable."},
        {"name": "Apple AirPods Pro 2nd Gen", "brand": "Apple",        "price_bdt": 29999, "rating": 4.8, "review_count": 4100, "stock": 80,  "description": "Active Noise Cancellation, Adaptive Transparency, MagSafe charging, H2 chip, IPX4."},
        {"name": "Bose QuietComfort 45",      "brand": "Bose",         "price_bdt": 32999, "rating": 4.7, "review_count": 2100, "stock": 50,  "description": "World-class ANC, 24-hr battery, TriPort acoustic, lightweight foldable design."},
        {"name": "Sennheiser Momentum 4",     "brand": "Sennheiser",   "price_bdt": 28999, "rating": 4.7, "review_count": 880,  "stock": 45,  "description": "60-hr battery, adaptive ANC, Hi-Fi sound tuned by Sennheiser engineers, premium build."},
        {"name": "JBL Tune 760NC",            "brand": "JBL",          "price_bdt": 11999, "rating": 4.4, "review_count": 1560, "stock": 120, "description": "35-hr ANC battery, JBL Pure Bass Sound, foldable, multi-point connection, great value."},
        {"name": "Jabra Evolve2 85",          "brand": "Jabra",        "price_bdt": 44999, "rating": 4.6, "review_count": 640,  "stock": 30,  "description": "37-hr ANC battery, 10-mic ANC for calls, professional-grade headset for remote workers."},
        {"name": "Samsung Galaxy Buds2 Pro",  "brand": "Samsung",      "price_bdt": 18999, "rating": 4.5, "review_count": 1240, "stock": 90,  "description": "3-mic ANC, 360 Audio, IPX7 waterproof, 29-hr total battery with case, Hi-Fi 24-bit audio."},
        {"name": "Sony WF-1000XM5",           "brand": "Sony",         "price_bdt": 24999, "rating": 4.8, "review_count": 1890, "stock": 70,  "description": "True wireless ANC earbuds, 8-hr battery (36hr with case), LDAC, IPX4, compact design."},
        {"name": "Anker Soundcore Q45",       "brand": "Anker",        "price_bdt": 8499,  "rating": 4.3, "review_count": 2140, "stock": 150, "description": "50-hr ANC battery, Hi-Res Audio certified, fast charging, foldable, budget champion."},
        {"name": "Beyerdynamic DT 770 Pro",   "brand": "Beyerdynamic", "price_bdt": 19999, "rating": 4.8, "review_count": 760,  "stock": 40,  "description": "Studio-grade closed-back headphones, 80Ω, exceptional clarity for mixing and mastering."},
    ],
    "smart-tvs": [
        {"name": "Samsung 65\" QLED 4K Q80C",  "brand": "Samsung", "price_bdt": 179999, "rating": 4.8, "review_count": 920,  "stock": 20, "description": "65\" Quantum HDR, 4K QLED, Neo Quantum Processor, 120Hz, Game Mode Pro, Tizen OS."},
        {"name": "LG C3 OLED 55\" evo",        "brand": "LG",      "price_bdt": 199999, "rating": 4.9, "review_count": 1340, "stock": 15, "description": "55\" OLED evo, α9 AI Gen6 processor, Dolby Vision IQ, 120Hz, HDMI 2.1, webOS 23."},
        {"name": "Sony Bravia XR A80L 65\"",   "brand": "Sony",    "price_bdt": 239999, "rating": 4.8, "review_count": 680,  "stock": 12, "description": "65\" OLED, Cognitive Processor XR, XR OLED Contrast, Acoustic Surface Audio+, Google TV."},
        {"name": "TCL 55\" C835 Mini LED",     "brand": "TCL",     "price_bdt": 89999,  "rating": 4.5, "review_count": 1120, "stock": 35, "description": "55\" Mini LED QLED 4K, 144Hz, Dolby Vision IQ, ONKYO sound, Google TV, AiPQ Pro."},
        {"name": "Hisense 65\" U8K Mini LED",  "brand": "Hisense", "price_bdt": 109999, "rating": 4.6, "review_count": 780,  "stock": 25, "description": "65\" Mini LED ULED 4K, 144Hz VRR, 1500-nit peak brightness, Dolby Atmos, Google TV."},
        {"name": "Samsung 75\" Crystal UHD",   "brand": "Samsung", "price_bdt": 134999, "rating": 4.4, "review_count": 540,  "stock": 18, "description": "75\" Crystal 4K UHD, PurColor technology, Motion Xcelerator, Smart Hub, Tizen 7.0 OS."},
        {"name": "LG 43\" UHD 4K UR80",       "brand": "LG",      "price_bdt": 49999,  "rating": 4.4, "review_count": 890,  "stock": 50, "description": "43\" 4K UHD, α5 AI Gen6 processor, HDR10 Pro, AirPlay 2, webOS 23, Magic Remote."},
        {"name": "Xiaomi TV S Pro 65\"",       "brand": "Xiaomi",  "price_bdt": 74999,  "rating": 4.5, "review_count": 620,  "stock": 28, "description": "65\" QLED 4K, 144Hz, Dolby Vision & Atmos, MEMC, HDMI 2.1, Android TV, voice control."},
        {"name": "OnePlus TV Y1S Pro 65\"",    "brand": "OnePlus", "price_bdt": 64999,  "rating": 4.3, "review_count": 410,  "stock": 30, "description": "65\" 4K UHD LED, Gamma Engine, 30W stereo Dolby Atmos, Android TV 11, built-in Chromecast."},
        {"name": "Vizio 50\" M-Series Quantum", "brand": "Vizio",  "price_bdt": 54999,  "rating": 4.2, "review_count": 340,  "stock": 40, "description": "50\" Quantum Color 4K, 120Hz, Dolby Vision HDR, V-Gaming Engine, SmartCast OS."},
    ],
    "cameras": [
        {"name": "Canon EOS R6 Mark II",     "brand": "Canon",    "price_bdt": 274999, "rating": 4.9, "review_count": 780,  "stock": 18, "description": "24.2MP full-frame CMOS, DIGIC X processor, up to 40fps, 6K RAW video, IBIS, Dual Pixel CMOS AF."},
        {"name": "Sony Alpha A7 IV",         "brand": "Sony",     "price_bdt": 299999, "rating": 4.8, "review_count": 1120, "stock": 15, "description": "33MP full-frame Exmor R BSI, 4K 60fps, 759-point AF, 10fps, 5-axis IBIS, dual card slots."},
        {"name": "Nikon Z8",                 "brand": "Nikon",    "price_bdt": 349999, "rating": 4.9, "review_count": 560,  "stock": 12, "description": "45.7MP full-frame stacked CMOS, 8K RAW video, 20fps, Expeed 7 processor, 9-axis IBIS."},
        {"name": "Fujifilm X-T5",            "brand": "Fujifilm", "price_bdt": 194999, "rating": 4.8, "review_count": 640,  "stock": 20, "description": "40.2MP APS-C X-Trans 5 HR sensor, 6.2K 30fps video, 7-stop IBIS, 15fps burst, Film Simulations."},
        {"name": "GoPro HERO12 Black",       "brand": "GoPro",    "price_bdt": 49999,  "rating": 4.6, "review_count": 2100, "stock": 60, "description": "5.3K 60fps, HyperSmooth 6.0, HDR video, 27MP photo, waterproof to 10m, Enduro battery."},
        {"name": "Canon EOS R50",            "brand": "Canon",    "price_bdt": 99999,  "rating": 4.6, "review_count": 890,  "stock": 35, "description": "24.2MP APS-C, Dual Pixel CMOS AF II, 4K 30fps, Bluetooth/Wi-Fi, vari-angle LCD, compact body."},
        {"name": "Sony ZV-E10 II",           "brand": "Sony",     "price_bdt": 84999,  "rating": 4.5, "review_count": 540,  "stock": 40, "description": "26.1MP APS-C Exmor R, 4K 120fps, AI-powered AF, vlog-friendly, directional microphone."},
        {"name": "DJI Osmo Pocket 3",        "brand": "DJI",      "price_bdt": 54999,  "rating": 4.7, "review_count": 1240, "stock": 45, "description": "1-inch CMOS, 4K 120fps, 3-axis stabilization gimbal, OLED touchscreen, ActiveTrack 6.0."},
        {"name": "Nikon Z30",                "brand": "Nikon",    "price_bdt": 74999,  "rating": 4.5, "review_count": 420,  "stock": 30, "description": "20.9MP APS-C, 4K 30fps, vari-angle touchscreen, 60fps 1080p, ideal for content creators."},
        {"name": "Panasonic Lumix G100D",    "brand": "Panasonic","price_bdt": 69999,  "rating": 4.4, "review_count": 310,  "stock": 35, "description": "20.3MP MFT sensor, 4K 30fps, mic & headphone jack, direction-detection microphone, compact."},
    ],
}


def seed():
    db = SessionLocal()
    try:
        # Skip if already seeded
        if db.query(models.Category).count() > 0:
            print("Database already seeded. Skipping.")
            return

        # Create categories
        cat_map = {}
        for cat_data in CATEGORIES:
            cat = models.Category(**cat_data)
            db.add(cat)
            db.flush()
            cat_map[cat_data["slug"]] = cat.id

        # Create products
        for slug, products in PRODUCTS.items():
            category_id = cat_map[slug]
            for p in products:
                image_url = PRODUCT_IMAGES.get(p["name"], f"https://picsum.photos/seed/product{p['name']}/400/400")
                product = models.Product(
                    name=p["name"],
                    brand=p["brand"],
                    price_bdt=p["price_bdt"],
                    rating=p["rating"],
                    review_count=p["review_count"],
                    stock=p["stock"],
                    description=p["description"],
                    category_id=category_id,
                    image_url=image_url,
                )
                db.add(product)

        db.commit()
        print(f"✅ Seeded {len(CATEGORIES)} categories and 50 products successfully.")
    except Exception as e:
        db.rollback()
        print(f"❌ Seeding failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
