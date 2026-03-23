import codecs
import random

html_path = r'c:\Users\sresa\Nueva calculadora\love-calculator\index.html'

with codecs.open(html_path, 'r', 'utf-8') as f:
    content = f.read()

prefixes = [
    "Porque", "Por la forma en que", "Me encanta que", "Amo cuando", 
    "Siempre recordaré cuando", "Gracias a ti", "No hay nada como", 
    "Eres increíble porque", "Mi corazón late más fuerte porque", "Adoro que",
    "Me fascina que", "Me vuelve loco que", "Es mágico cuando",
    "Me haces feliz porque", "El universo tiene sentido porque",
    "Tu luz interior es tan brillante que", "Simplemente porque",
    "Cada vez que te veo siento que", "Mi vida es mejor porque",
    "No imagino un mundo en el que no", "Agradezco a diario que"
]
suffixes = [
    "sonríes.", "me miras.", "haces que el mundo parezca un lugar mejor.", 
    "iluminas mis días.", "me entiendes sin necesidad de hablar.", 
    "eres mi lugar seguro.", "me haces sentir que todo es posible.", 
    "tienes un corazón de oro.", "siempre sabes qué decir.", 
    "cada día a tu lado es una aventura.", "tomas mi mano.",
    "escuchas mis tonterías con atención.", "abrazas mis miedos.",
    "brillas con luz propia.", "tu voz me tranquiliza.",
    "nuestros dedos encajan perfecto.", "me complementas en todo.",
    "me haces reír a carcajadas.", "tu mirada lo dice todo.",
    "mi mundo gira a tu alrededor.", "haces que valga la pena."
]

reasons = []
count = 5000
for i in range(1, count + 1):
    p = random.choice(prefixes)
    s = random.choice(suffixes)
    # Mix romantic variations randomly
    if i == 1:
        phrase = "Porque existes."
    elif i == count:
        phrase = "Porque simplemente, te amo con todo lo que soy."
    else:
        phrase = f"{p} {s}"

    reasons.append(f'  "Razón #{i}: {phrase}",')

array_str = "const milesDeRazones = [\n" + "\n".join(reasons) + "\n];\n"

new_content = content.replace("</body>", "  <script>\n" + array_str + "\n  </script>\n</body>")

with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(new_content)

print(f"Injected {len(reasons)} reasons successfully.")
