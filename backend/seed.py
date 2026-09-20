"""
Seed script — populates the database with 10 categories and 100 products.
Run: python seed.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)


# ── Real Unsplash product image URLs ─────────────────────────────────────────
# Using Unsplash source API which always returns valid images
PRODUCT_IMAGES = {
    # ── Smartphones ──────────────────────────────────────────────────────────
    "Samsung Galaxy S24 Ultra":    "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&q=80",
    "Apple iPhone 15 Pro Max":     "https://images.unsplash.com/photo-1696446701796-da61225697cc?w=600&q=80",
    "Xiaomi 14 Pro":               "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&q=80",
    "OnePlus 12":                  "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=600&q=80",
    "Google Pixel 8 Pro":          "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&q=80",
    "Samsung Galaxy A54 5G":       "https://images.unsplash.com/photo-1567581935884-3349723552ca?w=600&q=80",
    "Realme GT 5 Pro":             "https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=600&q=80",
    "Vivo X100 Pro":               "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=600&q=80",
    "OPPO Find X7 Ultra":          "https://images.unsplash.com/photo-1591337676887-a217a6970a8a?w=600&q=80",
    "Motorola Edge 40 Pro":        "https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?w=600&q=80",

    # ── Laptops ──────────────────────────────────────────────────────────────
    "Apple MacBook Air M3":        "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&q=80",
    "Dell XPS 15 9530":            "https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=600&q=80",
    "Lenovo ThinkPad X1 Carbon":   "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=600&q=80",
    "HP Spectre x360 14":          "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=600&q=80",
    "ASUS ROG Zephyrus G14":       "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&q=80",
    "Microsoft Surface Laptop 5":  "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&q=80",
    "Acer Swift X 14":             "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=600&q=80",
    "LG Gram 16":                  "https://images.unsplash.com/photo-1484788984921-03950022c9ef?w=600&q=80",
    "Razer Blade 15":              "https://images.unsplash.com/photo-1547394765-185e1e68f34e?w=600&q=80",
    "Lenovo IdeaPad Slim 5":       "https://images.unsplash.com/photo-1588702547919-26089e690ecc?w=600&q=80",

    # ── Headphones ────────────────────────────────────────────────────────────
    "Sony WH-1000XM5":             "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&q=80",
    "Apple AirPods Pro 2nd Gen":   "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=600&q=80",
    "Bose QuietComfort 45":        "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=600&q=80",
    "Sennheiser Momentum 4":       "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=600&q=80",
    "JBL Tune 760NC":              "https://images.unsplash.com/photo-1484704849700-f032a568e944?w=600&q=80",
    "Jabra Evolve2 85":            "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600&q=80",
    "Samsung Galaxy Buds2 Pro":    "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=600&q=80",
    "Sony WF-1000XM5":             "https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?w=600&q=80",
    "Anker Soundcore Q45":         "https://images.unsplash.com/photo-1558756520-22cfe5d382ca?w=600&q=80",
    "Beyerdynamic DT 770 Pro":     "https://images.unsplash.com/photo-1524678606370-a47ad25cb82a?w=600&q=80",

    # ── Smart TVs ─────────────────────────────────────────────────────────────
    "Samsung 65\" QLED 4K Q80C":  "https://images.unsplash.com/photo-1593359677879-a4bb92f4834e?w=600&q=80",
    "LG C3 OLED 55\" evo":        "https://images.unsplash.com/photo-1571415060716-baff5f717be1?w=600&q=80",
    "Sony Bravia XR A80L 65\"":   "https://images.unsplash.com/photo-1539187577537-e54cf54ae2f8?w=600&q=80",
    "TCL 55\" C835 Mini LED":     "https://images.unsplash.com/photo-1461151304267-38535e780c79?w=600&q=80",
    "Hisense 65\" U8K Mini LED":  "https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=600&q=80",
    "Samsung 75\" Crystal UHD":   "https://images.unsplash.com/photo-1560169897-fc0cdbdfa4d5?w=600&q=80",
    "LG 43\" UHD 4K UR80":       "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=600&q=80",
    "Xiaomi TV S Pro 65\"":       "https://images.unsplash.com/photo-1593784991095-a205069533cd?w=600&q=80",
    "OnePlus TV Y1S Pro 65\"":    "https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=600&q=80",
    "Vizio 50\" M-Series Quantum": "https://images.unsplash.com/photo-1555680202-c86f0e12f086?w=600&q=80",

    # ── Cameras ───────────────────────────────────────────────────────────────
    "Canon EOS R6 Mark II":        "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=600&q=80",
    "Sony Alpha A7 IV":            "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=600&q=80",
    "Nikon Z8":                    "https://images.unsplash.com/photo-1606983340126-99ab4feaa64a?w=600&q=80",
    "Fujifilm X-T5":               "https://images.unsplash.com/photo-1584270354949-c26b0d5b4a0c?w=600&q=80",
    "GoPro HERO12 Black":          "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=600&q=80",
    "Canon EOS R50":               "https://images.unsplash.com/photo-1542038784456-1ea8e935640e?w=600&q=80",
    "Sony ZV-E10 II":              "https://images.unsplash.com/photo-1614164185128-e4ec99c436d7?w=600&q=80",
    "DJI Osmo Pocket 3":           "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=600&q=80",
    "Nikon Z30":                   "https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=600&q=80",
    "Panasonic Lumix G100D":       "https://images.unsplash.com/photo-1485965120184-e220f721d03e?w=600&q=80",

    # ── Gaming ────────────────────────────────────────────────────────────────
    "Sony PlayStation 5":          "https://images.unsplash.com/photo-1607853202273-797f1c22a38e?w=600&q=80",
    "Xbox Series X":               "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=600&q=80",
    "Nintendo Switch OLED":        "https://images.unsplash.com/photo-1600950207944-0d63e8edbc3f?w=600&q=80",
    "ASUS ROG Ally":               "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=600&q=80",
    "Razer DeathAdder V3":         "https://images.unsplash.com/photo-1527814050087-3793815479db?w=600&q=80",
    "Logitech G Pro X Superlight": "https://images.unsplash.com/photo-1563297007-0686b7003af7?w=600&q=80",
    "SteelSeries Arctis Nova Pro": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=600&q=80",
    "Razer BlackWidow V4 Pro":     "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=600&q=80",
    "ASUS ROG Swift PG27UQ":       "https://images.unsplash.com/photo-1547394765-185e1e68f34e?w=600&q=80",
    "Logitech G923 Racing Wheel":  "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600&q=80",

    # ── Tablets ───────────────────────────────────────────────────────────────
    "Apple iPad Pro M4 12.9\"":   "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=600&q=80",
    "Samsung Galaxy Tab S9 Ultra": "https://images.unsplash.com/photo-1561154464-82e9adf32764?w=600&q=80",
    "Xiaomi Pad 6 Pro":            "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600&q=80",
    "Lenovo Tab P12 Pro":          "https://images.unsplash.com/photo-1623479322729-28b25c16b011?w=600&q=80",
    "Amazon Fire HD 10":           "https://images.unsplash.com/photo-1516321165247-4aa89a48be55?w=600&q=80",
    "Apple iPad Air M1":           "https://images.unsplash.com/photo-1589739900243-4b52cd9b104e?w=600&q=80",
    "Samsung Galaxy Tab A9+":      "https://images.unsplash.com/photo-1536859355448-76f92ebdc33d?w=600&q=80",
    "Realme Pad 2":                "https://images.unsplash.com/photo-1598327106026-d9521da673d1?w=600&q=80",
    "Huawei MatePad Pro 13.2\"":  "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80",
    "OnePlus Pad 2":               "https://images.unsplash.com/photo-1542229021-44b5d7e1e5ad?w=600&q=80",

    # ── Wearables ─────────────────────────────────────────────────────────────
    "Apple Watch Series 9":        "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=600&q=80",
    "Samsung Galaxy Watch 6":      "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&q=80",
    "Garmin Fenix 7 Pro":          "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=600&q=80",
    "Fitbit Charge 6":             "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=600&q=80",
    "Amazfit GTR 4":               "https://images.unsplash.com/photo-1617625802912-cde586faf331?w=600&q=80",
    "Xiaomi Band 8 Pro":           "https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=600&q=80",
    "Huawei Watch GT 4":           "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=600&q=80",
    "Fossil Gen 6 Hybrid":         "https://images.unsplash.com/photo-1587836374828-4dbafa94cf0e?w=600&q=80",
    "Withings ScanWatch 2":        "https://images.unsplash.com/photo-1501001350405-e7de23efabce?w=600&q=80",
    "Google Pixel Watch 2":        "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&q=80",

    # ── Home Appliances ───────────────────────────────────────────────────────
    "Dyson V15 Detect Vacuum":     "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80",
    "Samsung 25L Microwave":       "https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?w=600&q=80",
    "LG 9kg Front Load Washer":    "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=600&q=80",
    "Philips Air Purifier AC3858": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600&q=80",
    "Instant Pot Duo 7-in-1":      "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&q=80",
    "Dyson Airwrap Multi-Styler":  "https://images.unsplash.com/photo-1522338242992-e1a54906a8da?w=600&q=80",
    "Nespresso Vertuo Next":       "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&q=80",
    "iRobot Roomba j9+":           "https://images.unsplash.com/photo-1589405858862-2ac9cbb41321?w=600&q=80",
    "Philips Airfryer XXL HD9650": "https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&q=80",
    "Breville Smart Oven Air Fry": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&q=80",

    # ── Accessories ───────────────────────────────────────────────────────────
    "Anker 200W GaN Charger":      "https://images.unsplash.com/photo-1601524909162-ae8725290836?w=600&q=80",
    "Baseus 20000mAh Power Bank":  "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=600&q=80",
    "Sandisk Extreme 1TB SSD":     "https://images.unsplash.com/photo-1531492746076-161ca9bcad58?w=600&q=80",
    "Logitech MX Master 3S":       "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600&q=80",
    "Keychron Q1 Pro Keyboard":    "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=600&q=80",
    "Dell 27\" 4K USB-C Monitor":  "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=600&q=80",
    "Belkin 3-in-1 MagSafe Dock":  "https://images.unsplash.com/photo-1563770660941-20978e870e26?w=600&q=80",
    "Samsung T7 Shield SSD 2TB":   "https://images.unsplash.com/photo-1625014618427-fbc980b974f5?w=600&q=80",
    "Ugreen 100W USB-C Cable":     "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80",
    "Elgato Stream Deck MK.2":     "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80",
}

CATEGORIES = [
    {"name": "Smartphones",     "slug": "smartphones",      "icon": "📱", "description": "Latest smartphones and mobile devices"},
    {"name": "Laptops",         "slug": "laptops",          "icon": "💻", "description": "Laptops, notebooks, and ultrabooks"},
    {"name": "Headphones",      "slug": "headphones",       "icon": "🎧", "description": "Headphones, earbuds, and audio gear"},
    {"name": "Smart TVs",       "slug": "smart-tvs",        "icon": "📺", "description": "4K and 8K smart televisions"},
    {"name": "Cameras",         "slug": "cameras",          "icon": "📷", "description": "DSLR, mirrorless, and action cameras"},
    {"name": "Gaming",          "slug": "gaming",           "icon": "🎮", "description": "Consoles, controllers, and PC gaming gear"},
    {"name": "Tablets",         "slug": "tablets",          "icon": "📲", "description": "Tablets and e-readers for work and play"},
    {"name": "Wearables",       "slug": "wearables",        "icon": "⌚", "description": "Smartwatches and fitness trackers"},
    {"name": "Home Appliances", "slug": "home-appliances",  "icon": "🏠", "description": "Smart home and kitchen appliances"},
    {"name": "Accessories",     "slug": "accessories",      "icon": "🔌", "description": "Chargers, cables, storage and more"},
]

PRODUCTS = {
    "smartphones": [
        {"name": "Samsung Galaxy S24 Ultra", "brand": "Samsung",  "price_bdt": 139999, "rating": 4.8, "review_count": 1240, "stock": 50,  "description": "6.8\" QHD+ AMOLED, Snapdragon 8 Gen 3, 200MP camera, 5000mAh battery. The ultimate Samsung flagship."},
        {"name": "Apple iPhone 15 Pro Max",  "brand": "Apple",    "price_bdt": 179999, "rating": 4.9, "review_count": 2100, "stock": 30,  "description": "6.7\" Super Retina XDR, A17 Pro chip, 48MP ProRAW camera system, titanium design."},
        {"name": "Xiaomi 14 Pro",            "brand": "Xiaomi",   "price_bdt": 89999,  "rating": 4.6, "review_count": 780,  "stock": 80,  "description": "6.73\" 2K LTPO AMOLED, Snapdragon 8 Gen 3, Leica Summilux optics, 120W fast charging."},
        {"name": "OnePlus 12",               "brand": "OnePlus",  "price_bdt": 79999,  "rating": 4.7, "review_count": 640,  "stock": 60,  "description": "6.82\" LTPO3 AMOLED, Snapdragon 8 Gen 3, Hasselblad camera, 100W SUPERVOOC charging."},
        {"name": "Google Pixel 8 Pro",       "brand": "Google",   "price_bdt": 109999, "rating": 4.7, "review_count": 890,  "stock": 45,  "description": "6.7\" LTPO OLED, Google Tensor G3, 50MP + 48MP + 48MP cameras, 7 years of updates."},
        {"name": "Samsung Galaxy A54 5G",    "brand": "Samsung",  "price_bdt": 42999,  "rating": 4.5, "review_count": 2340, "stock": 120, "description": "6.4\" Super AMOLED, 50MP OIS camera, 5000mAh battery, IP67 water resistance."},
        {"name": "Realme GT 5 Pro",          "brand": "Realme",   "price_bdt": 59999,  "rating": 4.4, "review_count": 430,  "stock": 70,  "description": "6.78\" AMOLED, Snapdragon 8 Gen 3, 50MP Sony IMX890, 240W hyper charge."},
        {"name": "Vivo X100 Pro",            "brand": "Vivo",     "price_bdt": 99999,  "rating": 4.6, "review_count": 560,  "stock": 40,  "description": "6.78\" AMOLED, Dimensity 9300, Zeiss optics, 100W wireless charging."},
        {"name": "OPPO Find X7 Ultra",       "brand": "OPPO",     "price_bdt": 119999, "rating": 4.5, "review_count": 310,  "stock": 25,  "description": "6.82\" OLED, Snapdragon 8 Gen 3, dual periscope Hasselblad cameras, 100W charging."},
        {"name": "Motorola Edge 40 Pro",     "brand": "Motorola", "price_bdt": 54999,  "rating": 4.3, "review_count": 380,  "stock": 90,  "description": "6.67\" pOLED 165Hz, Snapdragon 8 Gen 2, 165W TurboPower charging, IP68 rated."},
    ],
    "laptops": [
        {"name": "Apple MacBook Air M3",       "brand": "Apple",     "price_bdt": 154999, "rating": 4.9, "review_count": 1780, "stock": 35, "description": "13.6\" Liquid Retina, Apple M3 chip, 16GB RAM, 256GB SSD, 18-hr battery, fanless design."},
        {"name": "Dell XPS 15 9530",           "brand": "Dell",      "price_bdt": 219999, "rating": 4.7, "review_count": 920,  "stock": 20, "description": "15.6\" OLED touch, Intel Core i9-13900H, 32GB DDR5, RTX 4060, 1TB NVMe SSD."},
        {"name": "Lenovo ThinkPad X1 Carbon",  "brand": "Lenovo",    "price_bdt": 189999, "rating": 4.8, "review_count": 1120, "stock": 28, "description": "14\" IPS 2.8K OLED, Intel Core Ultra 7, 32GB LPDDR5, 1TB SSD, MIL-STD-810H certified."},
        {"name": "HP Spectre x360 14",         "brand": "HP",        "price_bdt": 174999, "rating": 4.6, "review_count": 680,  "stock": 30, "description": "14\" 2.8K OLED touchscreen 2-in-1, Intel Core Ultra 7, 16GB RAM, 1TB SSD, OLED stylus."},
        {"name": "ASUS ROG Zephyrus G14",      "brand": "ASUS",      "price_bdt": 194999, "rating": 4.7, "review_count": 840,  "stock": 22, "description": "14\" QHD 165Hz, AMD Ryzen 9 7940HS, RX 7600S, 16GB DDR5, 1TB SSD, AniMe Matrix LED."},
        {"name": "Microsoft Surface Laptop 5", "brand": "Microsoft", "price_bdt": 159999, "rating": 4.5, "review_count": 540,  "stock": 40, "description": "13.5\" PixelSense touch, Intel Core i7-1265U, 16GB RAM, 512GB SSD, Windows 11 Home."},
        {"name": "Acer Swift X 14",            "brand": "Acer",      "price_bdt": 109999, "rating": 4.4, "review_count": 430,  "stock": 55, "description": "14\" 2.8K OLED, Intel Core i7-13700H, RTX 4050, 16GB RAM, 1TB SSD, sleek aluminum body."},
        {"name": "LG Gram 16",                 "brand": "LG",        "price_bdt": 144999, "rating": 4.6, "review_count": 390,  "stock": 33, "description": "16\" WQXGA IPS, Intel Core Ultra 7, 16GB RAM, 512GB SSD, only 1.19kg, MIL-STD certified."},
        {"name": "Razer Blade 15",             "brand": "Razer",     "price_bdt": 299999, "rating": 4.7, "review_count": 660,  "stock": 15, "description": "15.6\" QHD 240Hz, Intel Core i9-13950HX, RTX 4070, 32GB RAM, 1TB SSD, CNC aluminum."},
        {"name": "Lenovo IdeaPad Slim 5",      "brand": "Lenovo",    "price_bdt": 69999,  "rating": 4.3, "review_count": 1640, "stock": 80, "description": "14\" 2.8K OLED, AMD Ryzen 5 7530U, 16GB RAM, 512GB SSD, slim profile, great value."},
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
        {"name": "GoPro HERO12 Black",       "brand": "GoPro",   "price_bdt": 49999,  "rating": 4.6, "review_count": 2100, "stock": 60, "description": "5.3K 60fps, HyperSmooth 6.0, HDR video, 27MP photo, waterproof to 10m, Enduro battery."},
        {"name": "Canon EOS R50",            "brand": "Canon",   "price_bdt": 99999,  "rating": 4.6, "review_count": 890,  "stock": 35, "description": "24.2MP APS-C, Dual Pixel CMOS AF II, 4K 30fps, Bluetooth/Wi-Fi, vari-angle LCD, compact body."},
        {"name": "Sony ZV-E10 II",           "brand": "Sony",    "price_bdt": 84999,  "rating": 4.5, "review_count": 540,  "stock": 40, "description": "26.1MP APS-C Exmor R, 4K 120fps, AI-powered AF, vlog-friendly, directional microphone."},
        {"name": "DJI Osmo Pocket 3",        "brand": "DJI",     "price_bdt": 54999,  "rating": 4.7, "review_count": 1240, "stock": 45, "description": "1-inch CMOS, 4K 120fps, 3-axis stabilization gimbal, OLED touchscreen, ActiveTrack 6.0."},
        {"name": "Nikon Z30",                "brand": "Nikon",   "price_bdt": 74999,  "rating": 4.5, "review_count": 420,  "stock": 30, "description": "20.9MP APS-C, 4K 30fps, vari-angle touchscreen, 60fps 1080p, ideal for content creators."},
        {"name": "Panasonic Lumix G100D",    "brand": "Panasonic","price_bdt": 69999, "rating": 4.4, "review_count": 310,  "stock": 35, "description": "20.3MP MFT sensor, 4K 30fps, mic & headphone jack, direction-detection microphone, compact."},
    ],
    "gaming": [
        {"name": "Sony PlayStation 5",          "brand": "Sony",     "price_bdt": 64999,  "rating": 4.9, "review_count": 4200, "stock": 30,  "description": "AMD Zen 2 CPU, RDNA 2 GPU, ultra-fast SSD, 4K 120fps, ray tracing, DualSense haptic controller."},
        {"name": "Xbox Series X",               "brand": "Microsoft","price_bdt": 59999,  "rating": 4.8, "review_count": 3100, "stock": 35,  "description": "12 teraflops GPU, Xbox Velocity Architecture, 4K 120fps, Quick Resume, Game Pass compatible."},
        {"name": "Nintendo Switch OLED",        "brand": "Nintendo", "price_bdt": 44999,  "rating": 4.8, "review_count": 5800, "stock": 50,  "description": "7\" OLED screen, enhanced audio, wide adjustable stand, 64GB storage, dock included."},
        {"name": "ASUS ROG Ally",               "brand": "ASUS",     "price_bdt": 79999,  "rating": 4.5, "review_count": 980,  "stock": 25,  "description": "AMD Ryzen Z1 Extreme, 7\" FHD 120Hz touch display, Windows 11, 40Wh battery, handheld PC."},
        {"name": "Razer DeathAdder V3",         "brand": "Razer",    "price_bdt": 8999,   "rating": 4.7, "review_count": 2300, "stock": 100, "description": "Focus Pro 30K optical sensor, 59g ultralight, 90-hr battery, HyperSpeed wireless, 6 programmable buttons."},
        {"name": "Logitech G Pro X Superlight", "brand": "Logitech", "price_bdt": 12999,  "rating": 4.8, "review_count": 1800, "stock": 80,  "description": "HERO 25K sensor, 61g ultralight, 70-hr battery, LIGHTSPEED 1ms wireless, zero side buttons."},
        {"name": "SteelSeries Arctis Nova Pro", "brand": "SteelSeries","price_bdt": 34999,"rating": 4.7, "review_count": 760,  "stock": 40,  "description": "Dual wireless (2.4GHz + Bluetooth), active noise cancellation, hot-swappable battery, multi-platform."},
        {"name": "Razer BlackWidow V4 Pro",     "brand": "Razer",    "price_bdt": 22999,  "rating": 4.6, "review_count": 1100, "stock": 55,  "description": "Razer Yellow mechanical switches, chroma RGB, multi-function roller, USB passthrough, programmable macros."},
        {"name": "ASUS ROG Swift PG27UQ",       "brand": "ASUS",     "price_bdt": 84999,  "rating": 4.6, "review_count": 540,  "stock": 18,  "description": "27\" 4K 144Hz IPS, DisplayHDR 1000, G-Sync Ultimate, DCI-P3 98%, ELMB-Sync, ergonomic stand."},
        {"name": "Logitech G923 Racing Wheel",  "brand": "Logitech", "price_bdt": 29999,  "rating": 4.6, "review_count": 870,  "stock": 30,  "description": "TRUEFORCE feedback motor, 24-bit precision steering, dual-clutch launch assist, compatible PS5 & PC."},
    ],
    "tablets": [
        {"name": "Apple iPad Pro M4 12.9\"",   "brand": "Apple",   "price_bdt": 174999, "rating": 4.9, "review_count": 1560, "stock": 25, "description": "M4 chip, Ultra Retina XDR OLED, Nano-texture glass option, Apple Pencil Pro support, Thunderbolt 4."},
        {"name": "Samsung Galaxy Tab S9 Ultra", "brand": "Samsung", "price_bdt": 159999, "rating": 4.8, "review_count": 1020, "stock": 20, "description": "14.6\" Dynamic AMOLED 2X, Snapdragon 8 Gen 2, S Pen included, IP68, 12GB RAM, 256GB storage."},
        {"name": "Xiaomi Pad 6 Pro",            "brand": "Xiaomi",  "price_bdt": 54999,  "rating": 4.6, "review_count": 640,  "stock": 60, "description": "11\" 2.8K 144Hz LCD, Snapdragon 8+ Gen 1, 8600mAh, 67W fast charge, quad speakers with Dolby Atmos."},
        {"name": "Lenovo Tab P12 Pro",          "brand": "Lenovo",  "price_bdt": 89999,  "rating": 4.5, "review_count": 420,  "stock": 35, "description": "12.6\" AMOLED, Snapdragon 870, 8GB RAM, optional keyboard folio, Precision Pen 3, productivity beast."},
        {"name": "Amazon Fire HD 10",           "brand": "Amazon",  "price_bdt": 18999,  "rating": 4.3, "review_count": 3400, "stock": 120, "description": "10.1\" 1080p display, Octa-core processor, 32GB/64GB, USB-C, 12-hr battery, Alexa built-in."},
        {"name": "Apple iPad Air M1",           "brand": "Apple",   "price_bdt": 99999,  "rating": 4.8, "review_count": 2100, "stock": 40, "description": "10.9\" Liquid Retina, M1 chip, Touch ID, 5G capable, Apple Pencil 2nd gen & Magic Keyboard support."},
        {"name": "Samsung Galaxy Tab A9+",      "brand": "Samsung", "price_bdt": 34999,  "rating": 4.4, "review_count": 890,  "stock": 80, "description": "11\" 90Hz LCD, Snapdragon 695, 4GB RAM, quad speakers, kids mode, stylus support, great value."},
        {"name": "Realme Pad 2",                "brand": "Realme",  "price_bdt": 24999,  "rating": 4.3, "review_count": 560,  "stock": 90, "description": "11.5\" 2K 120Hz LCD, MediaTek Helio G99, 8GB RAM, 8360mAh, 33W dart charge, aluminum unibody."},
        {"name": "Huawei MatePad Pro 13.2\"",  "brand": "Huawei",  "price_bdt": 129999, "rating": 4.6, "review_count": 380,  "stock": 22, "description": "13.2\" 2.8K OLED 144Hz, Kirin 9000S, 12GB RAM, M-Pencil 3rd gen, HarmonyOS 4, satellite messaging."},
        {"name": "OnePlus Pad 2",               "brand": "OnePlus", "price_bdt": 59999,  "rating": 4.5, "review_count": 480,  "stock": 45, "description": "12.1\" 3K 144Hz LCD, Snapdragon 8 Gen 3, 9510mAh, 67W SUPERVOOC, Stylo 2 support, 12GB RAM."},
    ],
    "wearables": [
        {"name": "Apple Watch Series 9",        "brand": "Apple",   "price_bdt": 44999, "rating": 4.8, "review_count": 3200, "stock": 60, "description": "S9 chip, Always-On Retina, double tap gesture, ECG, blood oxygen, crash detection, 18-hr battery."},
        {"name": "Samsung Galaxy Watch 6",      "brand": "Samsung", "price_bdt": 34999, "rating": 4.6, "review_count": 1800, "stock": 70, "description": "1.5\" Super AMOLED, BP monitoring, ECG, 40-hr battery, Snapdragon W5+, sapphire crystal glass."},
        {"name": "Garmin Fenix 7 Pro",          "brand": "Garmin",  "price_bdt": 89999, "rating": 4.8, "review_count": 920,  "stock": 30, "description": "Multi-GNSS, solar charging, 37-day battery, full-color mapping, advanced health metrics, dive computer."},
        {"name": "Fitbit Charge 6",             "brand": "Google",  "price_bdt": 14999, "rating": 4.5, "review_count": 2400, "stock": 100, "description": "ECG app, EDA stress sensor, GPS, 7-day battery, Google Maps integration, SpO2 monitoring."},
        {"name": "Amazfit GTR 4",               "brand": "Amazfit", "price_bdt": 19999, "rating": 4.5, "review_count": 1100, "stock": 80, "description": "1.43\" AMOLED, Zepp OS 2.0, 14-day battery, dual-band GPS, 150 sports modes, Alexa built-in."},
        {"name": "Xiaomi Band 8 Pro",           "brand": "Xiaomi",  "price_bdt": 8999,  "rating": 4.4, "review_count": 3100, "stock": 150, "description": "1.74\" AMOLED, GPS, blood oxygen, heart rate, 14-day battery, 150 workout modes, 5ATM waterproof."},
        {"name": "Huawei Watch GT 4",           "brand": "Huawei",  "price_bdt": 24999, "rating": 4.6, "review_count": 780,  "stock": 55, "description": "1.43\" AMOLED, 14-day battery, TruSeen 5.5+ heart rate, ECG, SpO2, Precise dual-band GPS."},
        {"name": "Fossil Gen 6 Hybrid",         "brand": "Fossil",  "price_bdt": 18999, "rating": 4.3, "review_count": 560,  "stock": 45, "description": "2-week battery, health tracking, always-on analog hands, wellness metrics, e-ink display, classic design."},
        {"name": "Withings ScanWatch 2",        "brand": "Withings","price_bdt": 34999, "rating": 4.7, "review_count": 640,  "stock": 35, "description": "Medical-grade ECG, atrial fibrillation detection, 30-day battery, SpO2, FDA-cleared health metrics."},
        {"name": "Google Pixel Watch 2",        "brand": "Google",  "price_bdt": 34999, "rating": 4.5, "review_count": 1200, "stock": 50, "description": "Snapdragon W5 Gen 1, 24-hr battery, continuous ECG, cEDA stress tracking, Fitbit integration, Wear OS 4."},
    ],
    "home-appliances": [
        {"name": "Dyson V15 Detect Vacuum",     "brand": "Dyson",    "price_bdt": 89999, "rating": 4.8, "review_count": 1200, "stock": 30, "description": "Laser Detect reveals hidden dust, piezo sensor counts particles, HEPA filtration, 60-min runtime, LCD screen."},
        {"name": "Samsung 25L Microwave",       "brand": "Samsung",  "price_bdt": 19999, "rating": 4.5, "review_count": 890,  "stock": 60, "description": "25L capacity, 900W, Smart Humidity Sensor, Easy Clean interior, eco mode, child safety lock."},
        {"name": "LG 9kg Front Load Washer",    "brand": "LG",       "price_bdt": 74999, "rating": 4.7, "review_count": 760,  "stock": 25, "description": "9kg, TurboWash 360, AI DD motor, Steam+, ThinQ WiFi control, 6 Motion Direct Drive, energy A+++."},
        {"name": "Philips Air Purifier AC3858", "brand": "Philips",  "price_bdt": 34999, "rating": 4.6, "review_count": 640,  "stock": 40, "description": "True HEPA filter, removes 99.97% particles, covers 95sqm, real-time AQI display, auto mode, quiet sleep mode."},
        {"name": "Instant Pot Duo 7-in-1",      "brand": "Instant",  "price_bdt": 12999, "rating": 4.7, "review_count": 5600, "stock": 80, "description": "7-in-1: pressure cooker, slow cooker, rice cooker, steamer, sauté, yogurt maker, warmer. 8-quart, 14 programs."},
        {"name": "Dyson Airwrap Multi-Styler",  "brand": "Dyson",    "price_bdt": 59999, "rating": 4.7, "review_count": 2100, "stock": 35, "description": "Coanda airflow curls and waves, 6 attachments, no extreme heat, smoothing, volumizing, all hair types."},
        {"name": "Nespresso Vertuo Next",       "brand": "Nespresso","price_bdt": 14999, "rating": 4.6, "review_count": 1800, "stock": 55, "description": "Centrifusion technology, 5 cup sizes, 1.1L water tank, Bluetooth & WiFi, energy saving auto-off, recyclable pods."},
        {"name": "iRobot Roomba j9+",           "brand": "iRobot",   "price_bdt": 89999, "rating": 4.6, "review_count": 920,  "stock": 20, "description": "Smart Dirt Detective, auto-empty base, obstacle avoidance, room-specific suggestions, PrecisionVision navigation."},
        {"name": "Philips Airfryer XXL HD9650", "brand": "Philips",  "price_bdt": 24999, "rating": 4.7, "review_count": 3400, "stock": 60, "description": "7.3L XXL, Fat Removal Technology, 6 presets, digital touchscreen, dishwasher-safe basket, rapid air circulation."},
        {"name": "Breville Smart Oven Air Fry", "brand": "Breville", "price_bdt": 44999, "rating": 4.6, "review_count": 1100, "stock": 30, "description": "13 cooking functions, Element IQ system, 0.8cu ft capacity, air fry, dehydrate, proof bread, built-in light."},
    ],
    "accessories": [
        {"name": "Anker 200W GaN Charger",      "brand": "Anker",    "price_bdt": 8999,  "rating": 4.7, "review_count": 1800, "stock": 100, "description": "200W 4-port GaN charger, 3x USB-C + 1x USB-A, charges 4 devices simultaneously, foldable plug, compact."},
        {"name": "Baseus 20000mAh Power Bank",  "brand": "Baseus",   "price_bdt": 5999,  "rating": 4.6, "review_count": 2300, "stock": 120, "description": "20000mAh, 65W max output, 2x USB-C + USB-A, fast charges laptop & phone simultaneously, LED display."},
        {"name": "Sandisk Extreme 1TB SSD",     "brand": "SanDisk",  "price_bdt": 14999, "rating": 4.8, "review_count": 2100, "stock": 80,  "description": "1TB portable SSD, 1050MB/s read, 1000MB/s write, IP65 water/dust resistant, 2m drop proof, NVMe technology."},
        {"name": "Logitech MX Master 3S",       "brand": "Logitech", "price_bdt": 12999, "rating": 4.8, "review_count": 3200, "stock": 90,  "description": "8000 DPI optical, MagSpeed scroll wheel, 70-day battery, Bluetooth multi-device, ergonomic, works on glass."},
        {"name": "Keychron Q1 Pro Keyboard",    "brand": "Keychron", "price_bdt": 17999, "rating": 4.7, "review_count": 980,  "stock": 50,  "description": "QMK/VIA hot-swappable, gasket mount, wireless & wired, RGB, aluminum body, 75% compact layout, fully programmable."},
        {"name": "Dell 27\" 4K USB-C Monitor",  "brand": "Dell",     "price_bdt": 54999, "rating": 4.7, "review_count": 760,  "stock": 30,  "description": "27\" 4K IPS, 60Hz, 100W USB-C PD, HDMI 2.0, DP 1.4, built-in USB hub, ComfortView Plus, height adjustable."},
        {"name": "Belkin 3-in-1 MagSafe Dock",  "brand": "Belkin",   "price_bdt": 12999, "rating": 4.5, "review_count": 640,  "stock": 60,  "description": "MagSafe 15W iPhone charging, Apple Watch Fast Charge, AirPods charging, all-in-one premium desk stand."},
        {"name": "Samsung T7 Shield SSD 2TB",   "brand": "Samsung",  "price_bdt": 18999, "rating": 4.7, "review_count": 1400, "stock": 70,  "description": "2TB portable SSD, 1050MB/s, IP65 rated, dynamic thermal guard, USB 3.2 Gen 2, rugged rubber exterior."},
        {"name": "Ugreen 100W USB-C Cable",     "brand": "Ugreen",   "price_bdt": 1299,  "rating": 4.6, "review_count": 4100, "stock": 200, "description": "100W USB-C to USB-C, 48Gbps data transfer, 10Gbps USB 3.2 Gen 2, 8K@60Hz video, braided nylon, 2m length."},
        {"name": "Elgato Stream Deck MK.2",     "brand": "Elgato",   "price_bdt": 14999, "rating": 4.8, "review_count": 1600, "stock": 45,  "description": "15 LCD keys, fully customizable, one-touch streaming control, multi-action keys, plugin ecosystem, detachable cable."},
    ],
}


def seed():
    db = SessionLocal()
    try:
        # ── Create admin account (idempotent) ────────────────────────────────
        admin_email = "chaningdeep@gmail.com"
        existing_admin = db.query(models.Seller).filter(models.Seller.email == admin_email).first()
        if not existing_admin:
            from auth import get_password_hash
            admin = models.Seller(
                name="Prionyx Shop",
                email=admin_email,
                hashed_password=get_password_hash("Prionyx@2024"),
                shop_name="Prionyx Shop",
                is_admin=True,
                is_active=True,
            )
            db.add(admin)
            db.commit()
            print(f"✅ Admin account created: {admin_email} / Prionyx@2024")
        else:
            # Ensure existing account is marked as admin
            if not existing_admin.is_admin:
                existing_admin.is_admin = True
                existing_admin.shop_name = "Prionyx Shop"
                db.commit()
                print(f"✅ Admin flag granted to: {admin_email}")
            else:
                print(f"ℹ️  Admin account already exists: {admin_email}")

        # ── Skip product seeding if already done ─────────────────────────────
        if db.query(models.Category).count() > 0:
            print("Database already seeded. Skipping product seed.")
            return

        # Create categories
        cat_map = {}
        for cat_data in CATEGORIES:
            cat = models.Category(**cat_data)
            db.add(cat)
            db.flush()
            cat_map[cat_data["slug"]] = cat.id

        # Create products
        total = 0
        for slug, products in PRODUCTS.items():
            category_id = cat_map[slug]
            for p in products:
                image_url = PRODUCT_IMAGES.get(p["name"], f"https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&q=80")
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
                total += 1

        db.commit()
        print(f"✅ Seeded {len(CATEGORIES)} categories and {total} products successfully.")
    except Exception as e:
        db.rollback()
        print(f"❌ Seeding failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
