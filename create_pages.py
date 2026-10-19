import re
import os

base_path = "c:\\Users\\arnal\\OneDrive\\Documentos\\GitHub\\Visium-Digital-Tailwind-CSS"
template_path = os.path.join(base_path, "el_instituto.html")

with open(template_path, "r", encoding="utf-8") as f:
    content = f.read()

# Generate Colegios content
colegios_main = """<main>
    <!-- Mission Section -->
    <section class="py-12 bg-gray-100">
        <div class="container mx-auto px-4">
            <div class="max-w-5xl">
                <h5 class="text-gray-600">Educación Financiera Institucional</h5>
                <h3 class="mt-3 text-4xl font-normal text-gray-800 pt-2 pb-10">
                    Programas de educación financiera estructurados para colegios, liceos y universidades. Transformamos academias con conocimientos sólidos.
                </h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">
                <div class="bg_courses_5 rounded-3xl p-6 h-full">
                    <div class="flex flex-col items-center text-center">
                        <img class="icon_36987 mb-4" src="img/01_02_svg.svg" alt="Icon" />
                        <p class="text-gray-700">Currículos adaptados a cada nivel educativo: primaria, secundaria y nivel superior.</p>
                    </div>
                </div>
                <div class="bg_courses_6 rounded-3xl p-6 h-full">
                    <div class="flex flex-col items-center text-center">
                        <img class="icon_36987 mb-4" src="img/01_03_svg.svg" alt="Icon" />
                        <p class="text-gray-700">Capacitación docente especializada para formar multiplicadores del conocimiento.</p>
                    </div>
                </div>
                <div class="bg_courses_7 rounded-3xl p-6 h-full">
                    <div class="flex flex-col items-center text-center">
                        <img class="icon_36987 mb-4" src="img/01_04_svg.svg" alt="Icon" />
                        <p class="text-gray-700">Herramientas prácticas para estudiantes, fomentando ahorro e inversión temprana.</p>
                    </div>
                </div>
                <div class="bg_courses_8 rounded-3xl p-6 h-full">
                    <div class="flex flex-col items-center text-center">
                        <img class="icon_36987 mb-4" src="img/01_05_svg.svg" alt="Icon" />
                        <p class="text-gray-700">Acompañamiento continuo y evaluación de impacto en el desarrollo estudiantil.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="py-12 bg-gray-100">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl">
                <h4 class="text-2xl font-normal text-gray-800">Programas de Estudio</h4>
                <p class="font_p mt-6 text-gray-700 pt-5 pb-5">
                   Nuestra metodología se integra fácilmente en las actividades complementarias o extracurriculares de las instituciones, abordando desde conceptos básicos del dinero hasta planificación financiera aplicada.
                </p>
            </div>
            <div class="border-t border-gray-300 pt-10 pb-10 mt-10">
                <div class="flex flex-wrap gap-8">
                    <div class="w-full lg:w-1/5">
                        <span class="text-lg font-semibold text-gray-800">Estructura Curricular</span>
                    </div>
                    <div class="w-full lg:w-3/4">
                        <div class="space-y-6">
                            <span class="block text-gray-600">
                               Aseguramos que el contenido sea atractivo, relevante y comprensible, preparando a la institución para liderar el cambio en la cultura financiera de la comunidad educativa. 
                            </span>
                            <div class="pt-4">
                                <ul class="flex flex-wrap gap-4">
                                    <li class="badge bg-courses-01 text-gray-800 px-5 py-4 rounded-full">Talleres prácticos</li>
                                    <li class="badge bg-courses-02 text-gray-800 px-5 py-4 rounded-full">Simulaciones</li>
                                    <li class="badge bg-courses-03 text-gray-800 px-5 py-4 rounded-full">Material de apoyo guiado</li>
                                    <li class="badge bg-courses-04 text-gray-800 px-5 py-4 rounded-full">Certificaciones</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>"""

# Generate Familias content
familias_main = """<main>
    <!-- Mission Section -->
    <section class="py-12 bg-gray-100">
        <div class="container mx-auto px-4">
            <div class="max-w-5xl">
                <h5 class="text-gray-600">Educación Financiera en el Hogar</h5>
                <h3 class="mt-3 text-4xl font-normal text-gray-800 pt-2 pb-10">
                   Empoderamos a las familias para gestionar mejor sus recursos, construir un patrimonio sólido y enseñar a los hijos el valor del dinero con el ejemplo.
                </h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">
                <div class="bg_courses_1 rounded-3xl p-6 h-full">
                    <div class="flex flex-col items-center text-center">
                        <img class="icon_36987 mb-4" src="img/01_02_svg.svg" alt="Icon" />
                        <p class="text-gray-700">Asesorías personalizadas para identificar los retos financieros del hogar.</p>
                    </div>
                </div>
                <div class="bg_courses_2 rounded-3xl p-6 h-full">
                    <div class="flex flex-col items-center text-center">
                        <img class="icon_36987 mb-4" src="img/01_03_svg.svg" alt="Icon" />
                        <p class="text-gray-700">Construcción de hábitos de ahorro y gasto responsable que involucra a todos.</p>
                    </div>
                </div>
                <div class="bg_courses_3 rounded-3xl p-6 h-full">
                    <div class="flex flex-col items-center text-center">
                        <img class="icon_36987 mb-4" src="img/01_04_svg.svg" alt="Icon" />
                        <p class="text-gray-700">Metodologías lúdicas para hablar de dinero con los niños en casa.</p>
                    </div>
                </div>
                <div class="bg_courses_4 rounded-3xl p-6 h-full">
                    <div class="flex flex-col items-center text-center">
                        <img class="icon_36987 mb-4" src="img/01_05_svg.svg" alt="Icon" />
                        <p class="text-gray-700">Estrategias de inversión básica pensadas en la tranquilidad familiar.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="py-12 bg-gray-100">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl">
                <h4 class="text-2xl font-normal text-gray-800">Construyendo Bienestar Juntos</h4>
                <p class="font_p mt-6 text-gray-700 pt-5 pb-5">
                   Creemos que la tranquilidad empieza con las decisiones financieras correctas en el hogar. Por eso hemos diseñado acompañamientos integrales donde cada miembro aprende haciendo.
                </p>
            </div>
            <div class="border-t border-gray-300 pt-10 pb-10 mt-10">
                <div class="flex flex-wrap gap-8">
                    <div class="w-full lg:w-1/5">
                        <span class="text-lg font-semibold text-gray-800">Servicios Familiares</span>
                    </div>
                    <div class="w-full lg:w-3/4">
                        <div class="space-y-6">
                            <span class="block text-gray-600">
                               Abordamos desde la creación del primer presupuesto familiar y control de deudas hasta la creación de fondos para la educación superior de los hijos.
                            </span>
                            <div class="pt-4">
                                <ul class="flex flex-wrap gap-4">
                                    <li class="badge bg-courses-05 text-gray-800 px-5 py-4 rounded-full">Mentoría 1:1</li>
                                    <li class="badge bg-courses-06 text-gray-800 px-5 py-4 rounded-full">Talleres grupales</li>
                                    <li class="badge bg-courses-07 text-gray-800 px-5 py-4 rounded-full">Presupuesto en equipo</li>
                                    <li class="badge bg-courses-08 text-gray-800 px-5 py-4 rounded-full">Planificación de futuro</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>"""

# Process Colegios
colegios_content = re.sub(r"<main>.*?</main>", colegios_main, content, flags=re.DOTALL)
colegios_content = colegios_content.replace("<title>El Instituto | Visium Digital – Educación Financiera para Instituciones</title>", "<title>Finanzas para Colegios | Visium Digital</title>")
colegios_content = colegios_content.replace('href="el_instituto.html"', 'href="finanzas_colegios.html"')
colegios_path = os.path.join(base_path, "finanzas_colegios.html")
with open(colegios_path, "w", encoding="utf-8") as f:
    f.write(colegios_content)

# Process Familias
familias_content = re.sub(r"<main>.*?</main>", familias_main, content, flags=re.DOTALL)
familias_content = familias_content.replace("<title>El Instituto | Visium Digital – Educación Financiera para Instituciones</title>", "<title>Finanzas para Familias | Visium Digital</title>")
familias_content = familias_content.replace('href="el_instituto.html"', 'href="finanzas_familias.html"')
familias_path = os.path.join(base_path, "finanzas_familias.html")
with open(familias_path, "w", encoding="utf-8") as f:
    f.write(familias_content)

print("Pages created successfully.")
