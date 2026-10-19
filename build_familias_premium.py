import re
import os

base_path = "c:\\Users\\arnal\\OneDrive\\Documentos\\GitHub\\Visium-Digital-Tailwind-CSS"
familias_path = os.path.join(base_path, "finanzas_familias.html")
instituto_path = os.path.join(base_path, "el_instituto.html") # We'll base it off the original to ensure clean state

with open(instituto_path, "r", encoding="utf-8") as f:
    content = f.read()

new_main = """<main class="font-sans antialiased text-gray-800 bg-[#FAF9F4] selection:bg-green-200">
    <!-- Hero Section -->
    <section class="relative overflow-hidden pt-24 pb-32">
        <!-- Abstract Shapes & Blobs (Calm style) -->
        <div class="absolute top-0 right-0 -mr-20 -mt-20 w-[600px] h-[600px] rounded-full bg-[#EAF2E3] opacity-60 blur-3xl mix-blend-multiply pointer-events-none"></div>
        <div class="absolute bottom-0 left-[-100px] -mb-20 w-[500px] h-[500px] rounded-full bg-[#E5EBF4] opacity-70 blur-3xl mix-blend-multiply pointer-events-none"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] rounded-full bg-[#FFFBF0] opacity-40 blur-3xl mix-blend-multiply pointer-events-none"></div>
        
        <div class="container mx-auto px-6 lg:px-12 relative z-10 max-w-7xl">
            <div class="flex flex-col lg:flex-row items-center gap-16">
                <!-- Text Content -->
                <div class="lg:w-1/2">
                    <div class="flex flex-wrap items-center gap-3 mb-6">
                        <span class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-green-50 border border-green-100 text-xs font-semibold text-green-700 tracking-wide">
                            <i class="ti ti-leaf"></i> Bienestar Familiar
                        </span>
                        <span class="inline-flex items-center gap-1.5 px-4 py-2 rounded-full bg-blue-50 border border-blue-100 text-xs font-semibold text-blue-700 tracking-wide">
                            Clases Online y Presencial
                        </span>
                    </div>
                    
                    <h1 class="text-5xl md:text-[4rem] font-medium text-gray-800 leading-[1.1] tracking-tight mb-8">
                        Aprende a manejar el dinero en <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#4E8D7C] to-[#4A7C59]">familia</span>
                    </h1>
                    <p class="text-xl text-gray-500 mb-10 leading-relaxed font-normal">
                        Programas prácticos y modernos para enseñar ahorro, presupuesto y hábitos financieros saludables desde casa, adaptados a la comodidad de clases online o dinámicas presenciales.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 mb-12">
                        <a href="#contacto" class="inline-flex justify-center items-center px-8 py-4 rounded-full bg-[#4E8D7C] text-white font-medium hover:bg-[#3d7063] transition-all shadow-md hover:shadow-lg hover:-translate-y-0.5">
                            Comenzar ahora
                        </a>
                        <a href="#programas" class="inline-flex justify-center items-center px-8 py-4 rounded-full bg-white text-gray-700 border border-gray-200 font-medium hover:bg-gray-50 transition-all shadow-sm">
                            Ver programas
                        </a>
                    </div>
                    
                    <!-- Social Proof -->
                    <div class="flex items-center gap-6 border-t border-gray-200/60 pt-8 mt-4">
                        <div class="flex -space-x-3">
                            <img class="w-12 h-12 rounded-full border-[3px] border-[#FAF9F4] object-cover" src="img/yenni.jpg" alt="Familia feliz">
                            <div class="w-12 h-12 rounded-full border-[3px] border-[#FAF9F4] bg-[#FFECCC] flex items-center justify-center text-xs font-bold text-yellow-800">+50</div>
                        </div>
                        <div>
                            <p class="text-sm font-medium text-gray-800">Familias acompañadas</p>
                            <p class="text-xs text-gray-500 mt-1">Sin conocimiento previo necesario</p>
                        </div>
                    </div>
                </div>
                
                <!-- Image / Visuals -->
                <div class="lg:w-1/2 relative hidden lg:block">
                    <!-- Soft organic mask wrapper -->
                    <div class="relative w-full h-[550px]" style="border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; overflow: hidden; box-shadow: 0 20px 50px rgba(78,141,124,0.15);">
                        <img src="https://images.unsplash.com/photo-1511895426328-dc8714191300?q=80&w=2070&auto=format&fit=crop" alt="Familia compartiendo" class="w-full h-full object-cover">
                        <div class="absolute inset-0 bg-[#4E8D7C] mix-blend-overlay opacity-20"></div>
                    </div>
                    
                    <!-- Badges -->
                    <div class="absolute -left-4 top-32 bg-white/90 backdrop-blur-md p-4 rounded-2xl shadow-xl flex items-center gap-3 animate-float border border-white">
                        <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-700">
                            <i class="ti ti-puzzle text-xl"></i>
                        </div>
                        <div>
                            <p class="text-xs text-gray-500 font-medium">Metodología</p>
                            <p class="text-sm font-semibold text-gray-800">Aprendizaje Práctico</p>
                        </div>
                    </div>
                    <div class="absolute -right-4 bottom-24 bg-white/90 backdrop-blur-md p-4 rounded-2xl shadow-xl flex items-center gap-3 animate-float border border-white" style="animation-delay: 1.5s;">
                        <div class="w-10 h-10 rounded-full bg-orange-100 flex items-center justify-center text-orange-700">
                            <i class="ti ti-mood-smile text-xl"></i>
                        </div>
                        <div>
                            <p class="text-xs text-gray-500 font-medium">Diseñado</p>
                            <p class="text-sm font-semibold text-gray-800">Para Padres e Hijos</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- The Problem / Retos Familiares -->
    <section class="py-24 bg-white">
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl">
            <div class="text-center max-w-2xl mx-auto mb-16">
                <span class="text-sm font-bold tracking-widest text-[#4E8D7C] uppercase mb-4 block">Entendemos tu situación</span>
                <h2 class="text-3xl md:text-4xl font-medium text-gray-800 tracking-tight mb-5">
                    Hablemos de los retos de muchas familias hoy
                </h2>
                <p class="text-lg text-gray-500 font-light">
                    Es normal sentir ansiedad cuando se trata de dinero. Sentimos tu frustración cuando el salario no rinde, por eso queremos acompañarte en el proceso de sanar tu relación económica familiar.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Warm cards without heavy shadows -->
                <div class="bg-[#FAF9F4] p-8 rounded-[2rem] border border-[#F2EFE8] flex flex-col hover:bg-[#F2EFE8] transition-colors">
                    <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center mb-6 shadow-sm text-[#E07A5F]">
                        <i class="ti ti-calendar-stats text-2xl"></i>
                    </div>
                    <h3 class="text-lg font-semibold text-gray-800 mb-2">Vivir mes a mes</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">El estrés financiero de llegar justo a fin de mes sin un respirador económico llamado ahorro.</p>
                </div>
                
                <div class="bg-[#FAF9F4] p-8 rounded-[2rem] border border-[#F2EFE8] flex flex-col hover:bg-[#F2EFE8] transition-colors">
                    <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center mb-6 shadow-sm text-[#4E8D7C]">
                        <i class="ti ti-shopping-cart text-2xl"></i>
                    </div>
                    <h3 class="text-lg font-semibold text-gray-800 mb-2">Compras impulsivas</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">Desorden económico derivado de decisiones emocionales, afectando metas a largo plazo de la casa.</p>
                </div>

                <div class="bg-[#FAF9F4] p-8 rounded-[2rem] border border-[#F2EFE8] flex flex-col hover:bg-[#F2EFE8] transition-colors">
                    <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center mb-6 shadow-sm text-[#E29578]">
                        <i class="ti ti-baby-carriage text-2xl"></i>
                    </div>
                    <h3 class="text-lg font-semibold text-gray-800 mb-2">Hijos sin educación</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">Niños y adolescentes creciendo sin dimensionar el esfuerzo detrás del dinero o cómo administrarlo.</p>
                </div>

                <div class="bg-[#FAF9F4] p-8 rounded-[2rem] border border-[#F2EFE8] flex flex-col hover:bg-[#F2EFE8] transition-colors">
                    <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center mb-6 shadow-sm text-blue-400">
                        <i class="ti ti-route text-2xl"></i>
                    </div>
                    <h3 class="text-lg font-semibold text-gray-800 mb-2">Falta de planificación</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">Dificultad para destinar capital hacia metas conjuntas, desde universidad hasta las vacaciones deseadas.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Family Programs -->
    <section class="py-24 bg-[#E5EBF4] relative" id="programas">
        <div class="absolute inset-0 bg-white/40"></div>
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl relative z-10">
            <div class="mb-16 flex flex-col md:flex-row md:items-end md:justify-between gap-6">
                <div class="max-w-2xl">
                    <h2 class="text-3xl lg:text-4xl font-medium text-gray-800 tracking-tight mb-4">Programas Familiares</h2>
                    <p class="text-lg text-gray-600 font-light">Diseñados para ser entendidos, aplicados y disfrutados por todos en casa. Ofrecemos modalidades <span class="font-semibold text-gray-800">online y presenciales</span> según sus preferencias.</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Program Card 1 -->
                <div class="bg-white rounded-[2rem] p-8 shadow-sm border border-white flex flex-col justify-between hover:shadow-xl hover:-translate-y-1 transition-all">
                    <div>
                        <div class="flex justify-between items-start mb-6">
                            <div class="w-14 h-14 rounded-2xl bg-green-50 flex items-center justify-center text-[#4E8D7C]">
                                <i class="ti ti-pig-money text-2xl"></i>
                            </div>
                            <span class="px-3 py-1 bg-gray-100 text-gray-600 text-xs font-semibold rounded-full mt-1">Presencial y Online</span>
                        </div>
                        <h3 class="text-2xl font-semibold text-gray-800 mb-3">Presupuesto y Ahorro Familiar</h3>
                        <p class="text-gray-500 text-sm mb-6 leading-relaxed">Aprende a sentarte en familia para alinear gastos, definir prioridades y construir un fondo de emergencia juntos, de forma respetuosa.</p>
                        
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-center gap-3">
                                <i class="ti ti-check text-green-500"></i> <span class="text-sm border-b border-dashed border-gray-200 pb-1 text-gray-600 block w-full">Metas en común</span>
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="ti ti-check text-green-500"></i> <span class="text-sm border-b border-dashed border-gray-200 pb-1 text-gray-600 block w-full">Organización mensual</span>
                            </li>
                        </ul>
                    </div>
                    <div class="flex items-center justify-between border-t border-gray-100 pt-6">
                        <div>
                            <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Duración</p>
                            <p class="text-sm font-semibold text-gray-800">4 Semanas</p>
                        </div>
                        <div>
                            <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Nivel</p>
                            <p class="text-sm font-semibold text-gray-800">Principiante</p>
                        </div>
                    </div>
                </div>

                <!-- Program Card 2 -->
                <div class="bg-white rounded-[2rem] p-8 shadow-sm border border-white flex flex-col justify-between hover:shadow-xl hover:-translate-y-1 transition-all">
                    <div>
                        <div class="flex justify-between items-start mb-6">
                            <div class="w-14 h-14 rounded-2xl bg-orange-50 flex items-center justify-center text-orange-500">
                                <i class="ti ti-mood-kid text-2xl"></i>
                            </div>
                            <span class="px-3 py-1 bg-gray-100 text-gray-600 text-xs font-semibold rounded-full mt-1">Presencial y Online</span>
                        </div>
                        <h3 class="text-2xl font-semibold text-gray-800 mb-3">Finanzas para Niños y Adolescentes</h3>
                        <p class="text-gray-500 text-sm mb-6 leading-relaxed">Dinámicas lúdicas para hijos de 8 a 17 años. Cómo introducir el concepto de paga (domingo), inversión temprana y toma de decisiones.</p>
                        
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-center gap-3">
                                <i class="ti ti-check text-orange-500"></i> <span class="text-sm border-b border-dashed border-gray-200 pb-1 text-gray-600 block w-full">Valor del trabajo</span>
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="ti ti-check text-orange-500"></i> <span class="text-sm border-b border-dashed border-gray-200 pb-1 text-gray-600 block w-full">Juegos interactivos</span>
                            </li>
                        </ul>
                    </div>
                    <div class="flex items-center justify-between border-t border-gray-100 pt-6">
                        <div>
                            <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Duración</p>
                            <p class="text-sm font-semibold text-gray-800">6 Semanas</p>
                        </div>
                        <div>
                            <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Nivel</p>
                            <p class="text-sm font-semibold text-gray-800">Básico (Adaptable)</p>
                        </div>
                    </div>
                </div>

                <!-- Program Card 3 -->
                <div class="bg-white rounded-[2rem] p-8 shadow-sm border border-white flex flex-col justify-between hover:shadow-xl hover:-translate-y-1 transition-all">
                    <div>
                        <div class="flex justify-between items-start mb-6">
                            <div class="w-14 h-14 rounded-2xl bg-blue-50 flex items-center justify-center text-blue-500">
                                <i class="ti ti-chart-arrows-vertical text-2xl"></i>
                            </div>
                            <span class="px-3 py-1 bg-gray-100 text-gray-600 text-xs font-semibold rounded-full mt-1">Online y Presencial</span>
                        </div>
                        <h3 class="text-2xl font-semibold text-gray-800 mb-3">Hábitos Saludables e Inversión</h3>
                        <p class="text-gray-500 text-sm mb-6 leading-relaxed">Orientado a padres e hijos mayores. Una transición suave desde el ahorro puro hasta el mundo de los activos e inteligencia a futuro.</p>
                        
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-center gap-3">
                                <i class="ti ti-check text-blue-500"></i> <span class="text-sm border-b border-dashed border-gray-200 pb-1 text-gray-600 block w-full">Protección inflación</span>
                            </li>
                            <li class="flex items-center gap-3">
                                <i class="ti ti-check text-blue-500"></i> <span class="text-sm border-b border-dashed border-gray-200 pb-1 text-gray-600 block w-full">Mentalidad protectora</span>
                            </li>
                        </ul>
                    </div>
                    <div class="flex items-center justify-between border-t border-gray-100 pt-6">
                        <div>
                            <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Duración</p>
                            <p class="text-sm font-semibold text-gray-800">8 Semanas</p>
                        </div>
                        <div>
                            <p class="text-xs text-gray-400 font-medium uppercase tracking-wider">Nivel</p>
                            <p class="text-sm font-semibold text-gray-800">Intermedio</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Aprender en Familia -->
    <section class="py-24 bg-white">
        <div class="container mx-auto px-6 lg:px-12 max-w-5xl">
            <div class="text-center mb-20">
                <h2 class="text-3xl lg:text-4xl font-medium text-gray-800 tracking-tight">Metodología paso a paso</h2>
                <p class="text-lg text-gray-500 mt-3 font-light">Un enfoque pensado para generar conversaciones sobre dinero de manera respetuosa, divertida (en el caso de los niños) y con foco emocional.</p>
            </div>
            
            <div class="space-y-12 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-gray-200 before:to-transparent">
                
                <!-- Timeline Item 1 -->
                <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                    <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-[#E07A5F] text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
                        1
                    </div>
                    <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 bg-[#FAF9F4] rounded-2xl shadow-sm border border-[#F2EFE8]">
                        <h4 class="text-lg font-bold text-gray-800 mb-1">El diagnóstico sin culpas</h4>
                        <p class="text-sm text-gray-500 leading-relaxed font-light">Evaluamos la situación actual de los gastos familiares. Analizamos desde dónde parten y establecemos metas realistas con mucha empatía.</p>
                    </div>
                </div>
                
                <!-- Timeline Item 2 -->
                <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                    <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-[#F2CC8F] text-yellow-900 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
                        2
                    </div>
                    <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 bg-[#FAF9F4] rounded-2xl shadow-sm border border-[#F2EFE8]">
                        <h4 class="text-lg font-bold text-gray-800 mb-1">Juegos y Retos Prácticos</h4>
                        <p class="text-sm text-gray-500 leading-relaxed font-light">Involucramos a los hijos con simulaciones. Usamos frascos, alcancías o apps donde ven el impacto del ahorro mes a mes en tiempo real.</p>
                    </div>
                </div>

                <!-- Timeline Item 3 -->
                <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                    <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-[#81B29A] text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
                        3
                    </div>
                    <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-6 bg-[#FAF9F4] rounded-2xl shadow-sm border border-[#F2EFE8]">
                        <h4 class="text-lg font-bold text-gray-800 mb-1">Mesa redonda familiar</h4>
                        <p class="text-sm text-gray-500 leading-relaxed font-light">Consolidamos conversaciones semanales. Enseñamos a hablar de dinero de forma calmada para afianzar esa nueva estructura de bienestar.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Beneficios para la familia Grid -->
    <section class="py-24 bg-[#4E8D7C] text-white">
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl">
            <div class="text-center mb-16">
                <h2 class="text-3xl lg:text-4xl font-medium tracking-tight">Los cambios que verás en casa</h2>
            </div>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="bg-white/10 p-6 rounded-2xl backdrop-blur-sm border border-white/20">
                    <i class="ti ti-yoga text-3xl mb-4 text-green-200"></i>
                    <h3 class="text-lg font-medium mb-2">Menos estrés financiero</h3>
                    <p class="text-sm text-green-50 font-light">Dormirán mejor sabiendo a dónde va el dinero y contando con un fondo de tranquilidad.</p>
                </div>
                <div class="bg-white/10 p-6 rounded-2xl backdrop-blur-sm border border-white/20">
                    <i class="ti ti-heart-handshake text-3xl mb-4 text-green-200"></i>
                    <h3 class="text-lg font-medium mb-2">Mejor comunicación</h3>
                    <p class="text-sm text-green-50 font-light">Terminan las discusiones económicas; el dinero se vuelve una herramienta compartida.</p>
                </div>
                <div class="bg-white/10 p-6 rounded-2xl backdrop-blur-sm border border-white/20">
                    <i class="ti ti-rocket text-3xl mb-4 text-green-200"></i>
                    <h3 class="text-lg font-medium mb-2">Hijos más preparados</h3>
                    <p class="text-sm text-green-50 font-light">Jóvenes con una relación sana y temprana frente al entorno económico del mundo real.</p>
                </div>
                <div class="bg-white/10 p-6 rounded-2xl backdrop-blur-sm border border-white/20">
                    <i class="ti ti-seedling text-3xl mb-4 text-green-200"></i>
                    <h3 class="text-lg font-medium mb-2">Hábitos saludables</h3>
                    <p class="text-sm text-green-50 font-light">Una constancia de ahorro e inversión que se hereda de generación en generación.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="py-24 bg-[#E5EBF4] relative">
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl relative z-10">
            <h2 class="text-3xl lg:text-4xl font-medium text-gray-800 tracking-tight text-center mb-16">Familias que cambiaron su realidad</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Testimonial 1 -->
                <div class="bg-white p-8 rounded-[2rem] shadow-sm flex flex-col justify-between">
                    <div>
                        <div class="flex gap-1 text-yellow-400 mb-4 text-sm">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-gray-600 mb-6 font-medium italic">"Antes sufríamos porque los niños querían que les compráramos todo el tiempo impulsivamente. Después del taller, comprendieron solitos que debíamos ahorrar para ir de vacaciones juntos. Es una paz increíble."</p>
                    </div>
                    <div class="flex items-center gap-4 border-t border-gray-100 pt-4">
                        <img class="w-12 h-12 rounded-full object-cover" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=100&h=100&fit=crop" alt="Mamá">
                        <div>
                            <p class="font-bold text-gray-800 text-sm">Familia Rodríguez</p>
                            <p class="text-xs text-gray-500">2 hijos (8 y 12 años)</p>
                        </div>
                    </div>
                </div>

                <!-- Testimonial 2 -->
                <div class="bg-white p-8 rounded-[2rem] shadow-sm flex flex-col justify-between">
                    <div>
                        <div class="flex gap-1 text-yellow-400 mb-4 text-sm">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-gray-600 mb-6 font-medium italic">"Tomamos clases online y la dinámica fue espectacular. Mi hijo adolescente gestiona su mesada, paga su plan de teléfono y aparta 10% para invertir. Siento que hicimos un gran trabajo."</p>
                    </div>
                    <div class="flex items-center gap-4 border-t border-gray-100 pt-4">
                        <img class="w-12 h-12 rounded-full object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=100&h=100&fit=crop" alt="Papá">
                        <div>
                            <p class="font-bold text-gray-800 text-sm">Carlos Mendoza</p>
                            <p class="text-xs text-gray-500">Representante</p>
                        </div>
                    </div>
                </div>

                <!-- Testimonial 3 -->
                <div class="bg-white p-8 rounded-[2rem] shadow-sm flex flex-col justify-between">
                    <div>
                        <div class="flex gap-1 text-yellow-400 mb-4 text-sm">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-gray-600 mb-6 font-medium italic">"Nunca pudimos hablar de finanzas sin pelear. Aprender de inteligencia financiera con ustedes online nos organizó, sanó nuestra relación y nos hizo ver un futuro más claro."</p>
                    </div>
                    <div class="flex items-center gap-4 border-t border-gray-100 pt-4">
                        <img class="w-12 h-12 rounded-full object-cover" src="https://images.unsplash.com/photo-1588514588265-5c91eeba7650?w=100&h=100&fit=crop" alt="Esposos">
                        <div>
                            <p class="font-bold text-gray-800 text-sm">Mariana & Luis</p>
                            <p class="text-xs text-gray-500">Matrimonio joven</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="py-24 bg-white">
        <div class="container mx-auto px-6 lg:px-12 max-w-4xl">
            <div class="text-center mb-16">
                <h2 class="text-3xl lg:text-4xl font-medium text-gray-800 tracking-tight">Preguntas frecuentes</h2>
            </div>
            
            <div class="space-y-4">
                <details class="group border border-[#F2EFE8] bg-[#FAF9F4] rounded-2xl p-6 open:bg-white open:shadow-sm transition-all [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-gray-800">
                        ¿Ofrecen mentoría online o presencial?
                        <span class="transition group-open:rotate-180">
                            <i class="ti ti-chevron-down text-gray-400"></i>
                        </span>
                    </summary>
                    <div class="text-gray-500 mt-4 leading-relaxed font-light text-sm">
                        ¡Ambas modalidades están disponibles! Nos adaptamos a donde te encuentres para que la educación fluya orgánicamente en el entorno familiar.
                    </div>
                </details>

                <details class="group border border-[#F2EFE8] bg-[#FAF9F4] rounded-2xl p-6 open:bg-white open:shadow-sm transition-all [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-gray-800">
                        ¿Es obligatorio tener conocimientos financieros previos?
                        <span class="transition group-open:rotate-180">
                            <i class="ti ti-chevron-down text-gray-400"></i>
                        </span>
                    </summary>
                    <div class="text-gray-500 mt-4 leading-relaxed font-light text-sm">
                        Totalmente no. Nuestro acercamiento es 100% amigable y empezamos desde lo más fundamental: hábitos de entendimiento básico, comunicación y organización.
                    </div>
                </details>

                <details class="group border border-[#F2EFE8] bg-[#FAF9F4] rounded-2xl p-6 open:bg-white open:shadow-sm transition-all [&_summary::-webkit-details-marker]:hidden">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-gray-800">
                        ¿Desde qué edad pueden participar los hijos?
                        <span class="transition group-open:rotate-180">
                            <i class="ti ti-chevron-down text-gray-400"></i>
                        </span>
                    </summary>
                    <div class="text-gray-500 mt-4 leading-relaxed font-light text-sm">
                        Recomendamos empezar desde los 6 años con conceptos como la alcancía y gratificación diferida, variando las dinámicas según vayan creciendo (adolescentes).
                    </div>
                </details>
            </div>
        </div>
    </section>

    <!-- Contact Form & CTA -->
    <section class="py-24 bg-[#EAF2E3] relative" id="contacto">
        <div class="container mx-auto px-6 lg:px-12 max-w-6xl relative z-10">
            <div class="bg-white rounded-[3rem] p-10 lg:p-16 shadow-lg flex flex-col lg:flex-row gap-16 items-center border border-green-50">
                <!-- Text CTA -->
                <div class="lg:w-1/2 text-center lg:text-left">
                    <div class="inline-block p-4 rounded-3xl bg-green-50 text-[#4E8D7C] mb-6">
                        <i class="ti ti-home-check text-4xl"></i>
                    </div>
                    <h2 class="text-4xl md:text-5xl font-medium text-gray-800 tracking-tight mb-6 leading-tight">
                        Los hábitos financieros también se enseñan en casa.
                    </h2>
                    <p class="text-lg text-gray-500 mb-8 font-light">
                        Agenda una orientación gratuita online o presencial. Te ayudaremos a encontrar el programa ideal para restablecer la paz económica en tu familia. 
                    </p>
                </div>

                <!-- Form -->
                <div class="lg:w-1/2 w-full">
                    <form class="space-y-5">
                        <h3 class="text-2xl font-medium text-gray-800 mb-6">Agenda una orientación gratuita</h3>
                        
                        <div>
                            <input type="text" class="w-full px-5 py-4 rounded-2xl border border-gray-200 focus:ring-2 focus:ring-[#4E8D7C] focus:border-[#4E8D7C] bg-[#FAF9F4] placeholder-gray-400 outline-none transition-all" placeholder="Nombre completo">
                        </div>
                        <div>
                            <input type="tel" class="w-full px-5 py-4 rounded-2xl border border-gray-200 focus:ring-2 focus:ring-[#4E8D7C] focus:border-[#4E8D7C] bg-[#FAF9F4] placeholder-gray-400 outline-none transition-all" placeholder="Número de WhatsApp">
                        </div>
                        <div class="grid grid-cols-2 gap-4">
                            <input type="number" class="w-full px-5 py-4 rounded-2xl border border-gray-200 focus:ring-2 focus:ring-[#4E8D7C] focus:border-[#4E8D7C] bg-[#FAF9F4] placeholder-gray-400 outline-none transition-all" placeholder="Cant. de hijos">
                            <input type="text" class="w-full px-5 py-4 rounded-2xl border border-gray-200 focus:ring-2 focus:ring-[#4E8D7C] focus:border-[#4E8D7C] bg-[#FAF9F4] placeholder-gray-400 outline-none transition-all" placeholder="Edades relativas">
                        </div>
                        <div>
                            <select class="w-full px-5 py-4 rounded-2xl border border-gray-200 focus:ring-2 focus:ring-[#4E8D7C] focus:border-[#4E8D7C] bg-[#FAF9F4] text-gray-600 outline-none transition-all">
                                <option disabled selected>Modalidad preferida</option>
                                <option>Online (Videoconferencia)</option>
                                <option>Clases Presenciales</option>
                            </option>
                            </select>
                        </div>
                        <div>
                            <input type="text" class="w-full px-5 py-4 rounded-2xl border border-gray-200 focus:ring-2 focus:ring-[#4E8D7C] focus:border-[#4E8D7C] bg-[#FAF9F4] placeholder-gray-400 outline-none transition-all" placeholder="¿Cuál es la meta familiar actual? (Ej: Ahorro, deudas)">
                        </div>
                        
                        <button type="button" class="w-full bg-[#4E8D7C] hover:bg-[#3d7063] text-white font-medium py-4 px-6 rounded-2xl transition-colors shadow hover:shadow-md mt-2">
                            Comenzar en familia
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</main>"""

# Process output
output_content = re.sub(r"<main.*?</main>", new_main, content, flags=re.DOTALL)
output_content = output_content.replace("<body class=\"font-['Inter'] bg-gray-100\">", "<body class=\"bg-white font-sans\">")
output_content = output_content.replace("<title>El Instituto | Visium Digital – Educación Financiera para Instituciones</title>", "<title>Educación Financiera para Familias | Visium Digital</title>")

with open(familias_path, "w", encoding="utf-8") as f:
    f.write(output_content)

print("Redesign for familias applied successfully.")
