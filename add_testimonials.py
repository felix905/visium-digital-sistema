import os

base_path = "c:\\Users\\arnal\\OneDrive\\Documentos\\GitHub\\Visium-Digital-Tailwind-CSS"
colegios_path = os.path.join(base_path, "finanzas_colegios.html")

with open(colegios_path, "r", encoding="utf-8") as f:
    content = f.read()

testimonials = """
    <!-- Testimonials -->
    <section class="py-24 bg-[#FAFAFA]">
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl">
            <h2 class="text-3xl lg:text-4xl font-bold text-gray-900 tracking-tight text-center mb-16">Lo que dice nuestra comunidad</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="bg-white p-8 rounded-[2rem] shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100 flex flex-col justify-between hover:-translate-y-1 transition-transform">
                    <div>
                        <div class="flex text-yellow-400 mb-4 text-xs"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                        <p class="text-gray-600 mb-6 font-medium leading-relaxed">"Nuestros alumnos empezaron a hablar de tasas de interés y presupuestos de forma natural. Es el gran complemento que nos faltaba en nuestro currículo."</p>
                    </div>
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center text-blue-700 font-bold">MC</div>
                        <div>
                            <p class="font-bold text-gray-900 text-sm">María Castillo</p>
                            <p class="text-xs text-gray-500">Coordinadora Académica</p>
                        </div>
                    </div>
                </div>

                <div class="bg-white p-8 rounded-[2rem] shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100 flex flex-col justify-between hover:-translate-y-1 transition-transform">
                    <div>
                        <div class="flex text-yellow-400 mb-4 text-xs"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                        <p class="text-gray-600 mb-6 font-medium leading-relaxed">"Como padre, siempre me preocupó que no enseñaran finanzas en la escuela. Con este programa logramos que mi hijo abriera una cuenta de ahorro programado."</p>
                    </div>
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center text-purple-700 font-bold">RJ</div>
                        <div>
                            <p class="font-bold text-gray-900 text-sm">Ricardo Jiménez</p>
                            <p class="text-xs text-gray-500">Representante</p>
                        </div>
                    </div>
                </div>

                <div class="bg-white p-8 rounded-[2rem] shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-100 flex flex-col justify-between md:col-span-2 lg:col-span-1 hover:-translate-y-1 transition-transform">
                    <div>
                        <div class="flex text-yellow-400 mb-4 text-xs"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                        <p class="text-gray-600 mb-6 font-medium leading-relaxed">"Creía que la economía era súper difícil, pero las simulaciones prácticas me enseñaron a visualizar mis ahorros reales y metas para la universidad."</p>
                    </div>
                    <div class="flex items-center gap-4">
                        <div class="w-12 h-12 bg-yellow-100 rounded-full flex items-center justify-center text-yellow-700 font-bold">AD</div>
                        <div>
                            <p class="font-bold text-gray-900 text-sm">Andrés D.</p>
                            <p class="text-xs text-gray-500">Estudiante, 16 años</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Insert right before the contact form section
insert_point = '<section class="py-24 bg-gray-900 relative mt-10 overflow-hidden" id="contacto">'
new_content = content.replace(insert_point, testimonials + '\n' + insert_point)

with open(colegios_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Testimonials inserted successfully.")
