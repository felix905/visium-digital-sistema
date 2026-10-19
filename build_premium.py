import re
import os

base_path = "c:\\Users\\arnal\\OneDrive\\Documentos\\GitHub\\Visium-Digital-Tailwind-CSS"
colegios_path = os.path.join(base_path, "finanzas_colegios.html")

with open(colegios_path, "r", encoding="utf-8") as f:
    content = f.read()

new_main = """<main class="font-sans antialiased text-gray-900 bg-white selection:bg-purple-200">
    <!-- Hero Section -->
    <section class="relative overflow-hidden pt-24 pb-32">
        <div class="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 rounded-full bg-blue-100 opacity-50 blur-3xl mix-blend-multiply pointer-events-none"></div>
        <div class="absolute bottom-0 left-0 -ml-20 -mb-20 w-96 h-96 rounded-full bg-purple-100 opacity-50 blur-3xl mix-blend-multiply pointer-events-none"></div>
        
        <div class="container mx-auto px-6 lg:px-12 relative z-10 max-w-7xl">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <!-- Text Content -->
                <div class="lg:w-1/2">
                    <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-50 border border-blue-100 mb-6">
                        <span class="flex h-2 w-2 relative">
                            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                            <span class="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                        </span>
                        <span class="text-xs font-semibold text-blue-700 tracking-wide uppercase">Para Instituciones Educativas</span>
                    </div>
                    <h1 class="text-5xl md:text-6xl font-bold text-gray-900 leading-[1.05] tracking-tight mb-8">
                        Educación financiera para jóvenes preparados para el <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">mundo real</span>
                    </h1>
                    <p class="text-xl text-gray-500 mb-10 leading-relaxed font-normal">
                        Programas modernos para colegios e instituciones que buscan desarrollar liderazgo, pensamiento crítico y habilidades financieras desde temprana edad.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 mb-12">
                        <a href="#contacto" class="inline-flex justify-center items-center px-8 py-4 rounded-full bg-gray-900 text-white font-medium hover:bg-gray-800 transition-all shadow-lg hover:shadow-xl hover:-translate-y-0.5">
                            Solicitar presentación
                        </a>
                        <a href="https://chat.whatsapp.com/DiuJOk1J1uF9keuVIxOcA0" class="inline-flex justify-center items-center px-8 py-4 rounded-full bg-white text-gray-800 border border-gray-200 font-medium hover:bg-gray-50 transition-all shadow-sm">
                            <i class="ti ti-brand-whatsapp mr-2 text-xl text-green-600"></i> Hablar con un asesor
                        </a>
                    </div>
                    
                    <!-- Stats / Social Proof -->
                    <div class="flex items-center gap-6 border-t border-gray-100 pt-8">
                        <div class="flex -space-x-3">
                            <img class="w-10 h-10 rounded-full border-2 border-white shadow-sm object-cover" src="img/yenni.jpg" alt="Student">
                            <div class="w-10 h-10 rounded-full border-2 border-white bg-blue-50 flex items-center justify-center text-xs font-bold text-blue-700">+10</div>
                        </div>
                        <div>
                            <p class="text-sm font-medium text-gray-900">Instituciones aliadas</p>
                            <div class="flex items-center gap-1 text-yellow-400 mt-0.5 text-xs">
                                <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Image / Visuals -->
                <div class="lg:w-1/2 relative perspective-1000 hidden lg:block">
                    <div class="absolute inset-0 bg-gradient-to-tr from-blue-100/50 to-purple-50/50 rounded-[2.5rem] transform rotate-3 scale-105 -z-10"></div>
                    <div class="bg-white p-4 rounded-[2.5rem] shadow-2xl relative overflow-hidden h-[500px]">
                        <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=2071&auto=format&fit=crop" alt="Jóvenes colaborando" class="rounded-[1.5rem] w-full h-full object-cover">
                    </div>
                    <!-- Badges -->
                    <div class="absolute -left-6 top-20 bg-white p-4 rounded-2xl shadow-xl flex items-center gap-3 border border-gray-100 backdrop-blur-md">
                        <div class="w-12 h-12 rounded-xl bg-yellow-50 flex items-center justify-center text-yellow-600">
                            <i class="ti ti-bulb text-2xl"></i>
                        </div>
                        <div>
                            <p class="text-xs text-gray-500 font-medium">Metodología</p>
                            <p class="text-sm font-bold text-gray-900">Pensamiento Crítico</p>
                        </div>
                    </div>
                    <div class="absolute -right-6 bottom-20 bg-white p-4 rounded-2xl shadow-xl flex items-center gap-3 border border-gray-100 backdrop-blur-md">
                        <div class="w-12 h-12 rounded-xl bg-indigo-50 flex items-center justify-center text-indigo-600">
                            <i class="ti ti-rocket text-2xl"></i>
                        </div>
                        <div>
                            <p class="text-xs text-gray-500 font-medium">Resultados</p>
                            <p class="text-sm font-bold text-gray-900">Mentalidad Futura</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- The Problem Section -->
    <section class="py-24 bg-[#FCFCFD] border-t border-gray-100">
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 tracking-tight mb-5">
                    El gran vacío de la educación tradicional
                </h2>
                <p class="text-lg text-gray-500">
                    Nuestros jóvenes se gradúan resolviendo ecuaciones complejas, pero sin las herramientas fundamentales para entender la economía de su propio futuro.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-white p-8 rounded-[2rem] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-gray-100 hover:shadow-[0_8px_40px_rgba(0,0,0,0.06)] transition-all duration-300 transform hover:-translate-y-1">
                    <div class="w-14 h-14 bg-red-50 text-red-500 rounded-2xl flex items-center justify-center mb-6">
                        <i class="ti ti-receipt text-2xl"></i>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 mb-3 block">Gestión nula</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">Fallas para crear presupuestos, administrar gastos y entender el valor del capital propio a corto y mediano plazo.</p>
                </div>
                
                <div class="bg-white p-8 rounded-[2rem] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-gray-100 hover:shadow-[0_8px_40px_rgba(0,0,0,0.06)] transition-all duration-300 transform hover:-translate-y-1">
                    <div class="w-14 h-14 bg-orange-50 text-orange-500 rounded-2xl flex items-center justify-center mb-6">
                        <i class="ti ti-trending-down text-2xl"></i>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 mb-3 block">Desconocen el ahorro</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">No existe un hábito de protección ni visión de inversión, haciéndolos dependientes económicamente.</p>
                </div>

                <div class="bg-white p-8 rounded-[2rem] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-gray-100 hover:shadow-[0_8px_40px_rgba(0,0,0,0.06)] transition-all duration-300 transform hover:-translate-y-1">
                    <div class="w-14 h-14 bg-purple-50 text-purple-600 rounded-2xl flex items-center justify-center mb-6">
                        <i class="ti ti-brain text-2xl"></i>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 mb-3 block">Sin pensamiento moderno</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">Ignoran cómo funciona la nueva economía digital, los activos tangibles o intangibles y la mentalidad emprendedora.</p>
                </div>

                <div class="bg-white p-8 rounded-[2rem] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-gray-100 hover:shadow-[0_8px_40px_rgba(0,0,0,0.06)] transition-all duration-300 transform hover:-translate-y-1">
                    <div class="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center mb-6">
                        <i class="ti ti-shield-x text-2xl"></i>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 mb-3 block">Vulnerabilidad financiera</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">Al salir al mundo real son propensos a endeudamientos tempranos y malas decisiones de créditos, préstamos y financiamientos.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Educational Programs Catalog -->
    <section class="py-24 bg-white relative">
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl relative z-10">
            <div class="mb-16">
                <h2 class="text-4xl font-bold text-gray-900 tracking-tight mb-4">Programas Educativos</h2>
                <p class="text-xl text-gray-500 max-w-2xl">Módulos adaptables al bloque académico de su institución, diseñados para empoderar desde el primer día.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Card 1 -->
                <div class="group bg-white rounded-[2rem] border border-gray-100 shadow-[0_8px_30px_rgb(0,0,0,0.04)] overflow-hidden hover:shadow-[0_20px_50px_rgb(0,0,0,0.08)] transition-all">
                    <div class="h-48 bg-gradient-to-br from-indigo-50 to-blue-50 p-6 flex flex-col justify-between relative overflow-hidden">
                        <div class="absolute top-0 right-0 -mr-8 -mt-8 w-32 h-32 bg-white/40 rounded-full blur-2xl"></div>
                        <span class="inline-block px-3 py-1 bg-white text-indigo-700 text-xs font-bold rounded-full w-fit shadow-sm">13 a 17 años</span>
                        <div>
                            <h3 class="text-2xl font-bold text-gray-900 mt-2">Finanzas para adolescentes</h3>
                        </div>
                    </div>
                    <div class="p-8">
                        <ul class="space-y-4 mb-8">
                            <li class="flex items-start">
                                <i class="ti ti-check text-indigo-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Creación de presupuesto personal</span>
                            </li>
                            <li class="flex items-start">
                                <i class="ti ti-check text-indigo-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Uso inteligente de tarjetas</span>
                            </li>
                            <li class="flex items-start">
                                <i class="ti ti-check text-indigo-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Metas de ahorro a corto plazo</span>
                            </li>
                        </ul>
                        <div class="pt-6 border-t border-gray-100 grid grid-cols-2 gap-4">
                            <div>
                                <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Duración</p>
                                <p class="text-sm font-semibold text-gray-900">4 Semanas</p>
                            </div>
                            <div>
                                <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Modalidad</p>
                                <p class="text-sm font-semibold text-gray-900">Presencial</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 2 -->
                <div class="group bg-white rounded-[2rem] border border-gray-100 shadow-[0_8px_30px_rgb(0,0,0,0.04)] overflow-hidden hover:shadow-[0_20px_50px_rgb(0,0,0,0.08)] transition-all">
                    <div class="h-48 bg-gradient-to-br from-purple-50 to-pink-50 p-6 flex flex-col justify-between relative overflow-hidden">
                        <div class="absolute top-0 right-0 -mr-8 -mt-8 w-32 h-32 bg-white/40 rounded-full blur-2xl"></div>
                        <span class="inline-block px-3 py-1 bg-white text-purple-700 text-xs font-bold rounded-full w-fit shadow-sm">Todas las edades</span>
                        <div>
                            <h3 class="text-2xl font-bold text-gray-900 mt-2">Liderazgo y Emprendimiento</h3>
                        </div>
                    </div>
                    <div class="p-8">
                        <ul class="space-y-4 mb-8">
                            <li class="flex items-start">
                                <i class="ti ti-check text-purple-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Design Thinking para jóvenes</span>
                            </li>
                            <li class="flex items-start">
                                <i class="ti ti-check text-purple-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Presentación de ideas (Pitch)</span>
                            </li>
                            <li class="flex items-start">
                                <i class="ti ti-check text-purple-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Manejo de proyectos escolares</span>
                            </li>
                        </ul>
                        <div class="pt-6 border-t border-gray-100 grid grid-cols-2 gap-4">
                            <div>
                                <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Duración</p>
                                <p class="text-sm font-semibold text-gray-900">8 Semanas</p>
                            </div>
                            <div>
                                <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Modalidad</p>
                                <p class="text-sm font-semibold text-gray-900">Híbrida</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="group bg-white rounded-[2rem] border border-gray-100 shadow-[0_8px_30px_rgb(0,0,0,0.04)] overflow-hidden hover:shadow-[0_20px_50px_rgb(0,0,0,0.08)] transition-all">
                    <div class="h-48 bg-gradient-to-br from-yellow-50 to-orange-50 p-6 flex flex-col justify-between relative overflow-hidden">
                        <div class="absolute top-0 right-0 -mr-8 -mt-8 w-32 h-32 bg-white/40 rounded-full blur-2xl"></div>
                        <span class="inline-block px-3 py-1 bg-white text-orange-700 text-xs font-bold rounded-full w-fit shadow-sm">15 a 18 años</span>
                        <div>
                            <h3 class="text-2xl font-bold text-gray-900 mt-2">Introducción a Inversión</h3>
                        </div>
                    </div>
                    <div class="p-8">
                        <ul class="space-y-4 mb-8">
                            <li class="flex items-start">
                                <i class="ti ti-check text-orange-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Fundamentos de bolsa y mercados</span>
                            </li>
                            <li class="flex items-start">
                                <i class="ti ti-check text-orange-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Economía digital y nuevos activos</span>
                            </li>
                            <li class="flex items-start">
                                <i class="ti ti-check text-orange-500 mt-0.5 mr-3"></i>
                                <span class="text-gray-600 text-sm">Riesgo vs Recompensa (Simulador)</span>
                            </li>
                        </ul>
                        <div class="pt-6 border-t border-gray-100 grid grid-cols-2 gap-4">
                            <div>
                                <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Duración</p>
                                <p class="text-sm font-semibold text-gray-900">6 Semanas</p>
                            </div>
                            <div>
                                <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Modalidad</p>
                                <p class="text-sm font-semibold text-gray-900">Virtual / Presencial</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Learning Experience Timeline -->
    <section class="py-24 bg-[#FAFAFA] border-y border-gray-100">
        <div class="container mx-auto px-6 lg:px-12 max-w-5xl">
            <div class="text-center mb-16">
                <h2 class="text-3xl lg:text-4xl font-bold text-gray-900 tracking-tight">Una experiencia dinámica</h2>
                <p class="text-lg text-gray-500 mt-3">Alejados de las aulas tradicionales, fomentamos el <span class="font-semibold">aprender haciendo</span>.</p>
            </div>
            
            <div class="relative">
                <!-- Vertical Line -->
                <div class="absolute left-6 md:left-1/2 md:-ml-[1px] top-4 bottom-4 w-0.5 bg-gray-200"></div>
                
                <!-- Step 1 -->
                <div class="relative flex flex-col md:flex-row items-center justify-between mb-12">
                    <div class="md:w-5/12 hidden md:block"></div>
                    <div class="absolute left-6 md:left-1/2 -ml-[19px] md:-ml-5 w-10 h-10 rounded-full bg-white border-4 border-blue-500 shadow-sm flex items-center justify-center z-10 text-white">
                    </div>
                    <div class="pl-16 md:pl-0 md:w-5/12 w-full text-left">
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
                            <span class="text-blue-600 text-sm font-bold uppercase tracking-wide">Fase 1</span>
                            <h4 class="text-xl font-bold text-gray-900 mt-1 mb-2">Simulaciones Prácticas</h4>
                            <p class="text-gray-500 text-sm">Escenarios de toma de decisiones financieras en tiempo real. Salarios, pago de impuestos y mercado laboral.</p>
                        </div>
                    </div>
                </div>
                
                <!-- Step 2 -->
                <div class="relative flex flex-col md:flex-row items-center justify-between mb-12">
                    <div class="pl-16 md:pl-0 md:w-5/12 w-full text-left md:text-right md:-mr-4">
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
                            <span class="text-purple-600 text-sm font-bold uppercase tracking-wide">Fase 2</span>
                            <h4 class="text-xl font-bold text-gray-900 mt-1 mb-2">Retos Financieros</h4>
                            <p class="text-gray-500 text-sm">Equipos estructurando modelos de negocio, gestionando presupuestos de empresas ficticias y asimilando riesgos.</p>
                        </div>
                    </div>
                    <div class="absolute left-6 md:left-1/2 -ml-[19px] md:-ml-5 w-10 h-10 rounded-full bg-white border-4 border-purple-500 shadow-sm flex items-center justify-center z-10 text-white">
                    </div>
                    <div class="md:w-5/12 hidden md:block"></div>
                </div>

                <!-- Step 3 -->
                <div class="relative flex flex-col md:flex-row items-center justify-between">
                    <div class="md:w-5/12 hidden md:block"></div>
                    <div class="absolute left-6 md:left-1/2 -ml-[19px] md:-ml-5 w-10 h-10 rounded-full bg-white border-4 border-yellow-400 shadow-sm flex items-center justify-center z-10 text-white">
                    </div>
                    <div class="pl-16 md:pl-0 md:w-5/12 w-full text-left">
                        <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
                            <span class="text-yellow-600 text-sm font-bold uppercase tracking-wide">Fase 3</span>
                            <h4 class="text-xl font-bold text-gray-900 mt-1 mb-2">Pitches Colaborativos</h4>
                            <p class="text-gray-500 text-sm">Presentación de resultados frente a paneles simulados de inversión, estimulando la oratoria y autoconfianza.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Benefits for Schools -->
    <section class="py-24 bg-white relative">
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl">
            <div class="flex flex-col lg:flex-row items-end justify-between mb-16 gap-8">
                <div>
                    <h2 class="text-3xl lg:text-4xl font-bold text-gray-900 tracking-tight">Valor agregado exclusivo</h2>
                    <p class="text-lg text-gray-500 mt-4 max-w-2xl">¿Por qué las instituciones nos escogen? Diferenciación académica pura para el desarrollo del individuo.</p>
                </div>
                <div class="hidden lg:block relative">
                   <!-- Decorative lines -->
                   <svg width="150" height="40" viewBox="0 0 150 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M0 20C40 20 60 0 150 0M0 40C50 40 70 20 150 20" stroke="#E5E7EB" stroke-width="2"/>
                   </svg>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="p-8 rounded-[2rem] bg-[#FAFAFA] border border-gray-100">
                    <div class="w-12 h-12 bg-gray-900 text-white rounded-xl flex items-center justify-center mb-6 shadow-sm">
                        <i class="ti ti-school text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Diferenciación institucional</h3>
                    <p class="text-gray-600 text-sm">Incorpore una materia altamente demandada, agregando prestigio y preparando realmente a su alumnado.</p>
                </div>
                <div class="p-8 rounded-[2rem] bg-[#FAFAFA] border border-gray-100">
                    <div class="w-12 h-12 bg-gray-900 text-white rounded-xl flex items-center justify-center mb-6 shadow-sm">
                        <i class="ti ti-building-community text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Integración Familiar</h3>
                    <p class="text-gray-600 text-sm">Ofrecemos talleres complementarios para padres, creando una comunidad escolar más sólida y cohesionada.</p>
                </div>
                <div class="p-8 rounded-[2rem] bg-[#FAFAFA] border border-gray-100 md:col-span-3 lg:col-span-1">
                    <div class="w-12 h-12 bg-gray-900 text-white rounded-xl flex items-center justify-center mb-6 shadow-sm">
                        <i class="ti ti-star text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3">Habilidades de por vida</h3>
                    <p class="text-gray-600 text-sm">Generación de graduados con inteligencia emocional económica, aumentando su tasa de éxito profesional.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Form and Final CTA -->
    <section class="py-24 bg-gray-900 relative mt-10 overflow-hidden" id="contacto">
        <div class="absolute inset-0 bg-gradient-to-br from-indigo-900/20 to-purple-900/20"></div>
        <div class="container mx-auto px-6 lg:px-12 max-w-6xl relative z-10">
            <div class="flex flex-col lg:flex-row gap-16 items-center">
                <!-- Text CTA -->
                <div class="lg:w-5/12 text-center lg:text-left">
                    <h2 class="text-4xl md:text-5xl font-bold text-white tracking-tight mb-6 leading-tight">
                        El futuro financiero también se enseña.
                    </h2>
                    <p class="text-lg text-gray-400 mb-8 font-light">
                        Agenda una presentación personalizada para tu institución y conoce nuestro plan de estudios a profundidad.
                    </p>
                    <div class="hidden lg:block space-y-4">
                        <div class="flex items-center gap-3">
                            <i class="ti ti-check text-green-400 text-xl"></i>
                            <span class="text-gray-300">Asesoría sin compromiso</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <i class="ti ti-check text-green-400 text-xl"></i>
                            <span class="text-gray-300">Evaluación del entorno académico</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <i class="ti ti-check text-green-400 text-xl"></i>
                            <span class="text-gray-300">Propuesta de estructura curricular</span>
                        </div>
                    </div>
                </div>

                <!-- Form -->
                <div class="lg:w-7/12 w-full">
                    <form class="bg-white p-8 md:p-10 rounded-[2rem] shadow-2xl">
                        <h3 class="text-2xl font-bold text-gray-900 mb-6">Solicitar información</h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Colegio / Institución</label>
                                <input type="text" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all placeholder-gray-400" placeholder="Ej. Instituto Los Andes">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Persona Responsable</label>
                                <input type="text" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all" placeholder="Tu nombre">
                            </div>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Cantidad de alumnos</label>
                                <select class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all bg-white text-gray-700">
                                    <option>Menos de 100</option>
                                    <option>100 - 500</option>
                                    <option>500 - 1000</option>
                                    <option>Más de 1000</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">WhatsApp</label>
                                <input type="tel" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all" placeholder="+58 424 0000000">
                            </div>
                        </div>
                        <div class="mb-8">
                            <label class="block text-sm font-medium text-gray-700 mb-2">Tipo de Institución</label>
                            <div class="flex gap-4">
                                <label class="flex items-center gap-2">
                                    <input type="radio" name="tipo" class="text-blue-600 focus:ring-blue-500 w-4 h-4" checked>
                                    <span class="text-gray-700 text-sm">Colegio / Liceo</span>
                                </label>
                                <label class="flex items-center gap-2">
                                    <input type="radio" name="tipo" class="text-blue-600 focus:ring-blue-500 w-4 h-4">
                                    <span class="text-gray-700 text-sm">Universidad / Instituto</span>
                                </label>
                            </div>
                        </div>
                        <button type="button" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-4 px-6 rounded-xl transition-colors shadow-lg hover:shadow-xl hover:-translate-y-0.5">
                            Quiero agendar la reunión
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</main>"""

# Process output
output_content = re.sub(r"<main.*?</main>", new_main, content, flags=re.DOTALL)
output_content = output_content.replace("<body class=\"font-['Inter'] bg-gray-100\">", "<body class=\"bg-[#FAFAFA] font-sans\">")

with open(colegios_path, "w", encoding="utf-8") as f:
    f.write(output_content)

print("Redesign applied successfully.")
