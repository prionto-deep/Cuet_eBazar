"""
Seed script — populates the database with 5 categories and 50 mock products.
Run: python seed.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

# ── Placeholder image URLs (using picsum with product-specific seeds) ─────────
def img(seed: int) -> str:
    return f"https://picsum.photos/seed/product{seed}/400/400"


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
        {"name": "Apple MacBook Air M3",         "brand": "Apple",  "price_bdt": 154999, "rating": 4.9, "review_count": 1780, "stock": 35, "description": "13.6\" Liquid Retina, Apple M3 chip, 16GB RAM, 256GB SSD, 18-hr battery, fanless design."},
        {"name": "Dell XPS 15 9530",             "brand": "Dell",   "price_bdt": 219999, "rating": 4.7, "review_count": 920,  "stock": 20, "description": "15.6\" OLED touch, Intel Core i9-13900H, 32GB DDR5, RTX 4060, 1TB NVMe SSD."},
        {"name": "Lenovo ThinkPad X1 Carbon",    "brand": "Lenovo", "price_bdt": 189999, "rating": 4.8, "review_count": 1120, "stock": 28, "description": "14\" IPS 2.8K OLED, Intel Core Ultra 7, 32GB LPDDR5, 1TB SSD, MIL-STD-810H certified."},
        {"name": "HP Spectre x360 14",           "brand": "HP",     "price_bdt": 174999, "rating": 4.6, "review_count": 680,  "stock": 30, "description": "14\" 2.8K OLED touchscreen 2-in-1, Intel Core Ultra 7, 16GB RAM, 1TB SSD, OLED stylus."},
        {"name": "ASUS ROG Zephyrus G14",        "brand": "ASUS",   "price_bdt": 194999, "rating": 4.7, "review_count": 840,  "stock": 22, "description": "14\" QHD 165Hz, AMD Ryzen 9 7940HS, RX 7600S, 16GB DDR5, 1TB SSD, AniMe Matrix LED."},
        {"name": "Microsoft Surface Laptop 5",   "brand": "Microsoft","price_bdt": 159999,"rating": 4.5,"review_count": 540, "stock": 40, "description": "13.5\" PixelSense touch, Intel Core i7-1265U, 16GB RAM, 512GB SSD, Windows 11 Home."},
        {"name": "Acer Swift X 14",              "brand": "Acer",   "price_bdt": 109999, "rating": 4.4, "review_count": 430,  "stock": 55, "description": "14\" 2.8K OLED, Intel Core i7-13700H, RTX 4050, 16GB RAM, 1TB SSD, sleek aluminum body."},
        {"name": "LG Gram 16",                   "brand": "LG",     "price_bdt": 144999, "rating": 4.6, "review_count": 390,  "stock": 33, "description": "16\" WQXGA IPS, Intel Core Ultra 7, 16GB RAM, 512GB SSD, only 1.19kg, MIL-STD certified."},
        {"name": "Razer Blade 15",               "brand": "Razer",  "price_bdt": 299999, "rating": 4.7, "review_count": 660,  "stock": 15, "description": "15.6\" QHD 240Hz, Intel Core i9-13950HX, RTX 4070, 32GB RAM, 1TB SSD, CNC aluminum."},
        {"name": "Lenovo IdeaPad Slim 5",        "brand": "Lenovo", "price_bdt": 69999,  "rating": 4.3, "review_count": 1640, "stock": 80, "description": "14\" 2.8K OLED, AMD Ryzen 5 7530U, 16GB RAM, 512GB SSD, slim profile, great value."},
    ],
    "headphones": [
        {"name": "Sony WH-1000XM5",         "brand": "Sony",       "price_bdt": 34999, "rating": 4.9, "review_count": 3420, "stock": 60,  "description": "Industry-leading ANC, 30-hr battery, LDAC Hi-Res Audio, multipoint connection, foldable."},
        {"name": "Apple AirPods Pro 2nd Gen","brand": "Apple",      "price_bdt": 29999, "rating": 4.8, "review_count": 4100, "stock": 80,  "description": "Active Noise Cancellation, Adaptive Transparency, MagSafe charging, H2 chip, IPX4."},
        {"name": "Bose QuietComfort 45",     "brand": "Bose",       "price_bdt": 32999, "rating": 4.7, "review_count": 2100, "stock": 50,  "description": "World-class ANC, 24-hr battery, TriPort acoustic, lightweight foldable design."},
        {"name": "Sennheiser Momentum 4",    "brand": "Sennheiser", "price_bdt": 28999, "rating": 4.7, "review_count": 880,  "stock": 45,  "description": "60-hr battery, adaptive ANC, Hi-Fi sound tuned by Sennheiser engineers, premium build."},
        {"name": "JBL Tune 760NC",           "brand": "JBL",        "price_bdt": 11999, "rating": 4.4, "review_count": 1560, "stock": 120, "description": "35-hr ANC battery, JBL Pure Bass Sound, foldable, multi-point connection, great value."},
        {"name": "Jabra Evolve2 85",         "brand": "Jabra",      "price_bdt": 44999, "rating": 4.6, "review_count": 640,  "stock": 30,  "description": "37-hr ANC battery, 10-mic ANC for calls, professional-grade headset for remote workers."},
        {"name": "Samsung Galaxy Buds2 Pro", "brand": "Samsung",    "price_bdt": 18999, "rating": 4.5, "review_count": 1240, "stock": 90,  "description": "3-mic ANC, 360 Audio, IPX7 waterproof, 29-hr total battery with case, Hi-Fi 24-bit audio."},
        {"name": "Sony WF-1000XM5",          "brand": "Sony",       "price_bdt": 24999, "rating": 4.8, "review_count": 1890, "stock": 70,  "description": "True wireless ANC earbuds, 8-hr battery (36hr with case), LDAC, IPX4, compact design."},
        {"name": "Anker Soundcore Q45",      "brand": "Anker",      "price_bdt": 8499,  "rating": 4.3, "review_count": 2140, "stock": 150, "description": "50-hr ANC battery, Hi-Res Audio certified, fast charging, foldable, budget champion."},
        {"name": "Beyerdynamic DT 770 Pro",  "brand": "Beyerdynamic","price_bdt": 19999, "rating": 4.8, "review_count": 760, "stock": 40,  "description": "Studio-grade closed-back headphones, 80Ω, exceptional clarity for mixing and mastering."},
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
        {"name": "Canon EOS R6 Mark II",     "brand": "Canon",   "price_bdt": 274999, "rating": 4.9, "review_count": 780,  "stock": 18, "description": "24.2MP full-frame CMOS, DIGIC X processor, up to 40fps, 6K RAW video, IBIS, Dual Pixel CMOS AF."},
        {"name": "Sony Alpha A7 IV",         "brand": "Sony",    "price_bdt": 299999, "rating": 4.8, "review_count": 1120, "stock": 15, "description": "33MP full-frame Exmor R BSI, 4K 60fps, 759-point AF, 10fps, 5-axis IBIS, dual card slots."},
        {"name": "Nikon Z8",                 "brand": "Nikon",   "price_bdt": 349999, "rating": 4.9, "review_count": 560,  "stock": 12, "description": "45.7MP full-frame stacked CMOS, 8K RAW video, 20fps, Expeed 7 processor, 9-axis IBIS."},
        {"name": "Fujifilm X-T5",            "brand": "Fujifilm","price_bdt": 194999, "rating": 4.8, "review_count": 640,  "stock": 20, "description": "40.2MP APS-C X-Trans 5 HR sensor, 6.2K 30fps video, 7-stop IBIS, 15fps burst, Film Simulations."},
        {"name": "GoPro HERO12 Black",       "brand": "GoPro",   "price_bdt": 49999,  "rating": 4.6, "review_count": 2100, "stock": 60, "description": "5.3K 60fps, HyperSmooth 6.0, HDR video, 27MP photo, waterproof to 10m, Enduro battery."},
        {"name": "Canon EOS R50",            "brand": "Canon",   "price_bdt": 99999,  "rating": 4.6, "review_count": 890,  "stock": 35, "description": "24.2MP APS-C, Dual Pixel CMOS AF II, 4K 30fps, Bluetooth/Wi-Fi, vari-angle LCD, compact body."},
        {"name": "Sony ZV-E10 II",           "brand": "Sony",    "price_bdt": 84999,  "rating": 4.5, "review_count": 540,  "stock": 40, "description": "26.1MP APS-C Exmor R, 4K 120fps, AI-powered AF, vlog-friendly, directional microphone."},
        {"name": "DJI Osmo Pocket 3",        "brand": "DJI",     "price_bdt": 54999,  "rating": 4.7, "review_count": 1240, "stock": 45, "description": "1-inch CMOS, 4K 120fps, 3-axis stabilization gimbal, OLED touchscreen, ActiveTrack 6.0."},
        {"name": "Nikon Z30",                "brand": "Nikon",   "price_bdt": 74999,  "rating": 4.5, "review_count": 420,  "stock": 30, "description": "20.9MP APS-C, 4K 30fps, vari-angle touchscreen, 60fps 1080p, ideal for content creators."},
        {"name": "Panasonic Lumix G100D",    "brand": "Panasonic","price_bdt": 69999, "rating": 4.4, "review_count": 310,  "stock": 35, "description": "20.3MP MFT sensor, 4K 30fps, mic & headphone jack, direction-detection microphone, compact."},
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
        seed_counter = 1
        for slug, products in PRODUCTS.items():
            category_id = cat_map[slug]
            for p in products:
                product = models.Product(
                    name=p["name"],
                    brand=p["brand"],
                    price_bdt=p["price_bdt"],
                    rating=p["rating"],
                    review_count=p["review_count"],
                    stock=p["stock"],
                    description=p["description"],
                    category_id=category_id,
                    image_url=img(seed_counter),
                )
                db.add(product)
                seed_counter += 1

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
