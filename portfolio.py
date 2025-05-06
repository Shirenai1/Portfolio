from zipfile import ZipFile
from pathlib import Path

html_content = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Портфоліо – Маркович Марк</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #f0f4f8; color: #333; margin: 0; padding: 0; }
        header { background: linear-gradient(135deg, #00796B, #4DB6AC); color: white; text-align: center; padding: 50px 20px; }
        header h1 { margin: 0; font-size: 36px; }
        header p { font-size: 18px; margin-top: 10px; }
        section { max-width: 800px; margin: 30px auto; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.05); }
        h2 { color: #00796B; }
        ul { list-style: none; padding-left: 0; }
        ul li::before { content: "✔ "; color: #4DB6AC; }
        footer { text-align: center; padding: 20px; background-color: #e0f2f1; color: #00796B; }
    </style>
</head>
<body>
<header>
    <h1>Маркович Марк</h1>
    <p>Онлайн-працівник | Контент-кріейтор | Перекладач-початківець</p>
</header>
<section>
    <h2>Про мене</h2>
    <p>Мене звати Марк, мені 16 років. Я володію англійською мовою на рівні B1 і вже маю досвід роботи онлайн...</p>
</section>
<section>
    <h2>Навички</h2>
    <ul>
        <li>Англійська мова – рівень B1</li>
        <li>Володіння Google Docs, Microsoft Word</li>
        <li>Редагування фото/відео (CapCut, InShot)</li>
        <li>Переклад з англійської / російської на українську</li>
        <li>Створення текстів, оформлення постів</li>
    </ul>
</section>
<section>
    <h2>Досвід</h2>
    <ul>
        <li>Виконання онлайн-завдань з написання текстів і перекладу</li>
        <li>Створення банерів та описів для соцмереж</li>
        <li>Участь у волонтерських проєктах</li>
    </ul>
</section>
<section>
    <h2>Контакти</h2>
    <p>Email: <a href="mailto:markmarkovic268@gmail.com">markmarkovic268@gmail.com</a><br> Telegram / Discord / Instagram – за запитом</p>
</section>
<footer>
    &copy; 2025 Маркович Марк | Усі права захищені
</footer>
</body>
</html>"""

html_path = Path("portfolio.html")
html_path.write_text(html_content, encoding="utf-8")

with ZipFile("portfolio_site.zip", "w") as zipf:
    zipf.write("portfolio.html")
