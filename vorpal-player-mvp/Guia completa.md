
# Época I: Fundación y Validación\
\
### Operaciones de la Pista Cero:\
 Paralelamente al desarrollo del MVP, las operaciones de negocio se centrarán en Marketing Orgánico Fundacional. Esto incluye la creación de perfiles en redes sociales clave, la participación en comunidades de TTRPG para construir reputación (sin vender) y la gestión directa del feedback como el 'equipo de soporte' fundador.\
\
## Capítulo 1: La Fundación Técnica y Metodológica\
**Objetivo Estratégico:** Establecer un entorno de desarrollo profesional y un flujo de trabajo claro que garantice la escalabilidad y la eficiencia desde el primer día.\
\
### El Taller Local\
- [x] Instalar y configurar VS Code en la Lenovo G50.\
- [x] Instalar las extensiones de VS Code recomendadas (e.g., Prettier, ESLint, Live Server).\
- [ ] Inicializar un nuevo proyecto con la pila tecnológica Vanilla: HTML5, CSS3, JavaScript (ES6+).\
- [ ] Crear la estructura de directorios del proyecto (`/src`, `/public`, `/css`, `/js`).\
\
### 1.4 La Doctrina del Presupuesto de Rendimiento y Accesibilidad\
- [ ] Crear un documento `PERFORMANCE_BUDGET.md` que formalice las reglas de rendimiento.\
- [ ] Implementar un sistema de medición en el entorno de desarrollo para monitorizar el tiempo de carga y la respuesta de la UI.\
- [ ] Configurar las herramientas de desarrollo del navegador para simular una conexión 3G para todas las pruebas de rendimiento.\
- [ ] Durante las revisiones de código, evaluar cada nueva característica contra el presupuesto de rendimiento: carga <3s en 3G, respuesta de UI <100ms, usando la Lenovo G50 como hardware de referencia.\
\
### El Puente a la Nube\
- [ ] Inicializar un repositorio Git local con `git init`.\
- [ ] Crear un nuevo repositorio en GitHub para el proyecto Vorpal.\
- [ ] Realizar el primer commit con la estructura inicial del proyecto.\
- [ ] Conectar el repositorio local con el remoto de GitHub y hacer push del commit inicial.\
- [ ] Configurar GitHub Pages para que se despliegue automáticamente desde la rama principal (`main`).\
\
### Nuestra Metodología\
- [ ] Crear un documento `ROLES.md` que defina formalmente el rol de \"Director de Producto/Desarrollador IA\".\
- [ ] Establecer un sistema de gestión de tareas (e.g., GitHub Projects) para visualizar el backlog y el progreso.\
- [ ] Definir y documentar el ciclo de \"Sprint\" de desarrollo basado en prompts, especificando la duración y los rituales (planificación, revisión).\
\
## Capítulo 2: El Prototipo Funcional - El Núcleo de Vorpal Player\
**Objetivo Estratégico:** Construir la primera versión funcional e interactiva del producto, enfocándose en la experiencia del usuario final sin la complejidad de la persistencia de datos.\
\
### La Arquitectura Visual (HTML/CSS)\
- [ ] Crear el archivo `index.html` con una estructura semántica HTML5 (header, main, section, footer).\
- [ ] Desarrollar la hoja de estilos CSS principal (`style.css`) siguiendo una metodología mobile-first.\
- [ ] Implementar un diseño responsivo utilizando Flexbox y/o Grid Layout para adaptarse a pantallas de escritorio, tableta y móvil.\
- [ ] Estructurar visualmente las áreas clave de la ficha de personaje (datos básicos, atributos, inventario, etc.).\
\
### La Lógica de Interacción (JavaScript)\
- [ ] Desarrollar la lógica del DOM para crear dinámicamente nuevos bloques de contenido en la ficha.\
- [ ] Implementar la funcionalidad para eliminar bloques de contenido de la ficha.\
- [ ] Desarrollar la lógica de arrastrar y soltar (drag-and-drop) para reorganizar los bloques dentro de la ficha de personaje.\
- [ ] Asegurar que todas las interacciones del DOM cumplan con el presupuesto de rendimiento de <100ms.\
\
## Capítulo 3: La Implementación de la \"Memoria\" - Persistencia de Datos\
**Objetivo Estratégico:** Transformar el prototipo en una herramienta útil, asegurando que el trabajo del usuario se guarde y se restaure de manera fiable.\
\
### 3.1 El Diseño del Esquema de Datos v1.0 (Principio de Escalabilidad)\
- [ ] Crear un archivo `data-schema-v1.md` para documentar la estructura del objeto JSON del personaje.\
- [ ] Implementar una función para generar identificadores únicos universales (UUID) para cada entidad principal (personaje, bloque, ítem).\
- [ ] Diseñar la estructura del objeto JSON para prever relaciones futuras (e.g., `campaignId`, `gmId`), aunque se dejen como `null` inicialmente.\
- [ ] Validar que la estructura del esquema es compatible con un futuro almacenamiento en una base de datos NoSQL como Firestore o Supabase.\
\
### El Modelo de Datos\
- [ ] Traducir el esquema de datos documentado a un objeto JavaScript que represente el estado de la ficha del personaje en la aplicación.\
\
### El Motor de Guardado/Carga\
- [ ] Implementar una función `saveToLocalStorage()` que serialice el objeto de estado del personaje a JSON y lo guarde en el `localStorage` del navegador.\
- [ ] Implementar una función `loadFromLocalStorage()` que recupere el JSON del `localStorage`, lo deserialice y lo utilice para reconstruir el estado de la aplicación al cargar la página.\
- [ ] Añadir listeners de eventos que activen `saveToLocalStorage()` después de cada cambio significativo realizado por el usuario.\
\
### 3.3 El Diseño del Esquema de Datos para Eventos y Logros\
- [ ] En el archivo `data-schema-v1.md`, añadir una sección para el esquema de eventos de usuario anónimos.\
- [ ] Definir la estructura del evento (e.g., `{ eventName: 'string', timestamp: 'number', metadata: {} }`).\
- [ ] Documentar eventos clave a rastrear en el futuro, como `character_created`, `session_started`, para asegurar la compatibilidad con el futuro sistema de gamificación.\
\
## Capítulo 4: El Producto Mínimo Viable (MVP) - Finalización y Pulido\
**Objetivo Estratégico:** Completar el conjunto de características del MVP y realizar una fase de pruebas internas para asegurar un lanzamiento de calidad.\
\
### Las Funciones de Portabilidad\
- [ ] Implementar un botón \"Exportar Personaje\" que convierta el estado actual del personaje a un archivo `.json` y lo descargue en el dispositivo del usuario.\
- [ ] Implementar un botón \"Importar Personaje\" que permita al usuario seleccionar un archivo `.json` de su dispositivo, lo parsee y reemplace el estado actual de la aplicación con los datos importados.\
- [ ] Añadir validación de datos en la función de importación para manejar errores si el archivo JSON no tiene el formato esperado.\
\
### La Fase de Alpha Interna\
- [ ] Crear un documento de plan de pruebas (`ALPHA_TEST_PLAN.md`).\
- [ ] Definir escenarios de prueba clave para el equipo fundador (creación de personaje, edición, guardado/carga, importación/exportación).\
- [ ] Ejecutar el plan de pruebas exhaustivamente en la Lenovo G50 y otros dispositivos disponibles.\
- [ ] Utilizar el sistema de gestión de tareas (GitHub Issues) para registrar todos los bugs encontrados.\
- [ ] Iterar en la corrección de bugs y el refinamiento de la UI/UX basándose en el feedback interno hasta que el producto sea estable.\
\
## Capítulo 5: El Lanzamiento Público y la Creación de la Comunidad\
**Objetivo Estratégico:** Lanzar el MVP al mundo, atraer a los primeros usuarios (\"early adopters\") y establecer los canales y procesos para convertir su feedback en la hoja de ruta del futuro.\
\
### La Estrategia de Lanzamiento\
- [ ] Redactar el mensaje de lanzamiento, enfocándose en la misión de Vorpal de potenciar la creatividad y eliminar la fricción.\
- [ ] Identificar y seleccionar los canales de lanzamiento inicial (e.g., subreddits específicos de TTRPG, foros de rol).\
- [ ] Ejecutar el \"lanzamiento suave\" publicando el mensaje y el enlace a la aplicación en los canales seleccionados.\
\
### La Infraestructura Comunitaria\
- [ ] Crear el servidor de Discord oficial de Vorpal.\
- [ ] Estructurar los canales del servidor: `#anuncios`, `#general`, `#sugerencias`, `#reporte-de-bugs`.\
\
### El Bucle de Feedback\
- [ ] Establecer y documentar un proceso para revisar regularmente los canales `#sugerencias` y `#reporte-de-bugs`.\
- [ ] Transferir los bugs y sugerencias válidas al backlog del proyecto en GitHub Issues.\
- [ ] Publicar actualizaciones regulares en el canal `#anuncios` para comunicar los cambios y correcciones, reconociendo las contribuciones de la comunidad.\
\
### 5.4 El Lanzamiento de la \"Galería de Creaciones\" (Cultura del Creador)\
- [ ] Crear el canal `#galeria-de-creaciones` en el servidor de Discord.\
- [ ] Redactar y fijar un mensaje en el canal explicando cómo compartir plantillas de personaje `.json` y animando a la participación.\
- [ ] Monitorizar activamente el canal para destacar las creaciones interesantes e identificar a los usuarios más prolíficos como futuros \"Pioneros\".\
\
### 5.5 La Implementación del Andamiaje Legal Básico\
- [ ] Redactar una Política de Privacidad simple, explicando que todos los datos se almacenan localmente en el navegador del usuario.\
- [ ] Redactar unos Términos de Servicio básicos utilizando una plantilla estándar adaptada.\
- [ ] Añadir enlaces a ambos documentos en el pie de página de la aplicación Vorpal Player.\
\
### 5.6 La Introducción del Concepto de Gamificación\
- [ ] Incluir una sección en el mensaje de lanzamiento y en el mensaje de bienvenida de Discord mencionando la visión a largo plazo de \"La Senda del Cronista\".\
- [ ] Crear un canal `#ideas-gamificacion` en Discord para que la comunidad pueda empezar a compartir ideas sobre logros y recompensas.\
\
### Estrategia de Construcción de Marca\
- [ ] Asegurar que toda la comunicación de lanzamiento se centre en la misión y la \"causa\" de Vorpal.\
- [ ] Responder activamente y de manera positiva a todos los comentarios y publicaciones en Discord para establecer un tono de comunidad acogedor y constructivo.\
\
# Época II: Comercialización y Conexión\
\
### Operaciones de la Pista Cero:\
 Con el lanzamiento comercial, la Pista Cero evoluciona a Crecimiento y Soporte Inicial. Esto implica establecer un sistema de tickets de soporte básico (puede ser un canal de Discord o un email), empezar a crear contenido de valor (posts de blog, tutoriales en video) y analizar las primeras métricas de conversión.\
\
### Ritual de Época II: El Bucle de Inteligencia Competitiva\
- [ ] Ejecutar un \"sprint cero\" de análisis antes de iniciar el desarrollo.\
- [ ] Analizar y sintetizar todo el feedback del MVP de la comunidad para identificar las características más valoradas.\
- [ ] Investigar y documentar los modelos de precios y características de al menos 3 herramientas de productividad freemium.\
- [ ] Identificar una lista de los 5-10 usuarios más activos y positivos de la comunidad como candidatos para la Beta Cerrada.\
- [ ] Crear un documento de resumen con los hallazgos para informar el diseño de las suscripciones \"Plus\" y \"Pro\".\
\
## Capítulo 6: La Infraestructura Técnica del Negocio\
**Objetivo Estratégico:** Construir la columna vertebral técnica que soportará las cuentas de usuario, los datos en la nuba y las transacciones financieras.\
\
### La Transición a la Nube\
- [ ] Seleccionar y configurar un proveedor de Backend como Servicio (BaaS), como Firebase o Supabase.\
- [ ] Diseñar y crear las tablas/colecciones de la base de datos para `users` y `characters`.\
- [ ] Implementar la lógica en la aplicación cliente para sincronizar los datos del personaje con la base de datos en la nube en lugar de `localStorage` para los usuarios autenticados.\
\
### El Sistema de Autenticación\
- [ ] Implementar las funciones de registro de nuevos usuarios (email/contraseña).\
- [ ] Implementar las funciones de inicio y cierre de sesión.\
- [ ] Integrar la lógica de autenticación en la UI de la aplicación, protegiendo las rutas y funciones conectadas.\
\
### La Integración de la Pasarela de Pagos\
- [ ] Crear una cuenta de desarrollador en Stripe (o la alternativa seleccionada).\
- [ ] Integrar el SDK de Stripe en la aplicación cliente.\
- [ ] Desarrollar las funciones de backend (cloud functions) para gestionar los intentos de pago, la creación de suscripciones y la verificación del estado de las mismas.\
\
### 6.4 La Integración de Analítica de Privacidad (El Filo del Freemium)\
- [ ] Seleccionar e integrar una herramienta de análisis de eventos anónima y respetuosa con la privacidad (e.g., Plausible, Fathom).\
- [ ] Implementar el seguimiento de eventos clave anónimos, como `feature_used`, `subscription_page_viewed`, `signup_completed`.\
- [ ] Crear un panel de control para visualizar estas métricas y responder a preguntas de negocio.\
\
### 6.5 La Construcción del Motor de Gamificación v1.0\
- [ ] Diseñar y crear las tablas/colecciones en la base de datos para `user_achievements` y `achievement_rules`.\
- [ ] Desarrollar un servicio de backend que reciba eventos de usuario anónimos y los procese contra las `achievement_rules`.\
- [ ] Crear una API RESTful (`/api/users/{userId}/achievements`) que la aplicación cliente pueda consultar para obtener los logros desbloqueados de un usuario.\
\
## Capítulo 7: Pista del Jugador (v2.0) - El Producto Mínimo Suscribible\
**Objetivo Estratégico:** Crear la primera oferta de pago para nuestra base de usuarios más grande, probando su disposición a pagar por conveniencia y personalización.\
\
### El Desarrollo de \"Vorpal Plus\"\
- [ ] Implementar la sincronización de múltiples personajes en la nube para usuarios con suscripción \"Plus\".\
- [ ] Desarrollar una biblioteca de temas visuales (CSS) y un mecanismo para que los suscriptores los seleccionen y apliquen.\
- [ ] Crear la funcionalidad de \"crónica de personaje\", que guarda snapshots del personaje a lo largo del tiempo.\
\
### La Arquitectura de Permisos\
- [ ] Desarrollar una función o middleware en el cliente que verifique el estado de la suscripción del usuario.\
- [ ] Utilizar esta función para ocultar o deshabilitar las características \"Plus\" para los usuarios del plan gratuito.\
- [ ] Asegurar que la verificación de permisos también se realice en el backend para evitar el acceso no autorizado a las APIs de pago.\
\
### 7.3 La Introducción de Ganchos de Compromiso\
- [ ] Implementar la UI para mostrar notificaciones de logros desbloqueados.\
- [ ] Crear una sección en el perfil del usuario donde se listen todos los logros (bloqueados y desbloqueados).\
- [ ] Definir e implementar el primer conjunto de logros simples (e.g., 'Personaje Creado', 'Primera Semana de Uso').\
\
### 7.4 La Activación de 'La Senda del Aventurero' (Fase 1)\
- [ ] Configurar las reglas para los primeros logros del jugador en el backend del Motor de Gamificación.\
- [ ] Desarrollar la interfaz de usuario en Vorpal Player para mostrar el progreso de los logros.\
- [ ] Conectar las recompensas cosméticas (temas, skins de dados) a logros específicos, de modo que se desbloqueen automáticamente.\
\
## Capítulo 8: Pista del GM (v1.0) - El Producto Mínimo Vendible\
**Objetivo Estratégico:** Construir y definir la oferta principal que será nuestro motor de ingresos recurrente, resolviendo los problemas más agudos del Director de Juego.\
\
### El Desarrollo de \"GM Pro\"\
- [ ] Crear una nueva aplicación o una nueva sección en la aplicación existente para el \"Vorpal GM\".\
- [ ] Desarrollar la dashboard de gestión de campañas y jugadores.\
- [ ] Implementar el \"códice de campaña\", permitiendo al GM crear y organizar notas, PNJs y localizaciones con almacenamiento ilimitado en la nube.\
- [ ] Construir herramientas de preparación de sesión (e.g., generadores de encuentros básicos, gestores de iniciativa).\
\
### 8.4 La Primera Integración de IA Experimental\
- [ ] Seleccionar y obtener una clave de API para un servicio de IA de generación de texto de bajo coste.\
- [ ] Crear una función de backend segura que actúe como proxy para las llamadas a la API de IA, utilizando la clave de la API del servidor.\
- [ ] Implementar un botón \"Generar Nombre de PNJ\" en la interfaz de GM Pro que llame a esta función y muestre el resultado.\
- [ ] Añadir seguimiento de eventos anónimos para medir la frecuencia de uso de esta característica.\
\
### 8.5 La Activación de 'La Senda del Guardián' (Fase 1)\
- [ ] Definir y configurar las reglas para los primeros logros del GM en el backend (e.g., 'Primera Campaña Creada', 'Primer Jugador Invitado').\
- [ ] Desarrollar la interfaz en Vorpal GM para mostrar los logros y los emblemas/títulos desbloqueados.\
- [ ] Crear una sección de perfil de comunidad pública donde estos títulos sean visibles para otros usuarios.\
\
## Capítulo 9: El Puente Conector - La Sinergia en Tiempo Real\
**Objetivo Estratégico:** Desarrollar la \"magia\" tecnológica que conecta a jugadores y GMs, creando una propuesta de valor única que ninguna herramienta aislada puede ofrecer.\
\
### La Arquitectura de Datos en Tiempo Real\
- [ ] Utilizar las capacidades de tiempo real del BaaS seleccionado (e.g., Firestore Listeners, Supabase Realtime).\
- [ ] Diseñar la estructura de la base de datos para que la \"campaña\" del GM contenga referencias a las fichas de sus jugadores.\
- [ ] Implementar las reglas de seguridad de la base de datos para que un GM solo pueda leer/escribir en las fichas de los jugadores de su campaña.\
\
### La Implementación de \"Listeners\"\
- [ ] En la aplicación Vorpal Player, implementar un \"listener\" que se suscriba a los cambios en la ficha del personaje del usuario cuando está en una campaña activa.\
- [ ] En la aplicación Vorpal GM, implementar listeners que se suscriban a los cambios en las fichas de todos los personajes de la campaña activa.\
- [ ] Desarrollar la lógica para que, cuando el GM realice un cambio (e.g., \"dañar\" a un jugador), el cambio se escriba en la base de datos y la interfaz del jugador se actualice instantáneamente.\
\
## Capítulo 10: La Prueba de Fuego - La Fase Beta Cerrada\
**Objetivo Estratégico:** Probar la estabilidad de la nueva infraestructura conectada y validar la percepción de valor de nuestras ofertas de pago con un grupo selecto de usuarios leales.\
\
### La Estrategia de la Beta\
- [ ] Contactar a los candidatos a testers identificados en el \"Ritual de Época II\".\
- [ ] Crear un canal privado en Discord para los participantes de la beta.\
- [ ] Otorgar acceso gratuito a las suscripciones \"Plus\" y \"Pro\" a las cuentas de los testers.\
\
### El Bucle de Iteración de la Beta\
- [ ] Crear y distribuir un formulario de feedback estructurado a los testers.\
- [ ] El formulario debe incluir preguntas sobre estabilidad, usabilidad, valor de las características y percepción del precio propuesto.\
- [ ] Organizar sesiones de feedback en vivo (opcional) en el canal privado de Discord.\
- [ ] Utilizar los datos recopilados para realizar ajustes finales en el producto y en la estrategia de precios antes del lanzamiento público.\
\
## Capítulo 11: La Apertura de Puertas - El Lanzamiento Público de la Plataforma Comercial\
**Objetivo Estratégico:** Lanzar oficialmente las suscripciones \"Vorpal Plus\" y \"GM Pro\" a toda la base de usuarios.\
\
### La Estrategia de Comunicación del Lanzamiento\
- [ ] Redactar una publicación de blog y anuncios para Discord y redes sociales explicando las nuevas funcionalidades.\
- [ ] Enfatizar que la versión gratuita sigue siendo una herramienta potente y que las suscripciones apoyan el desarrollo futuro.\
- [ ] Preparar una sección de Preguntas Frecuentes (FAQ) sobre las nuevas suscripciones.\
\
### El Proceso de \"Onboarding\" para Clientes\
- [ ] Diseñar y desarrollar la página de precios y suscripción.\
- [ ] Implementar un flujo de pago claro y sencillo utilizando la integración de Stripe.\
- [ ] Crear correos electrónicos de bienvenida para los nuevos suscriptores, guiándolos hacia las nuevas funciones.\
\
### 11.3 La Creación del \"Viaje del GM\" (Onboarding)\
- [ ] Desarrollar un tutorial interactivo para los nuevos suscriptores de \"GM Pro\".\
- [ ] Implementar tooltips y guías contextuales que aparezcan la primera vez que un GM accede a funciones clave como el códice o la conexión de jugadores.\
- [ ] Asegurarse de que el onboarding demuestre el valor inmediato del producto.\
\
# Época III: Expansión y Creación del Efecto de Red\
\
### Operaciones de la Pista Cero:\
 Con la expansión del ecosistema, la Pista Cero se enfoca en Escala Comunitaria y Desarrollo de Negocio. Aquí se ejecuta el plan de la primera contratación (Community Manager) y se comienzan a explorar alianzas estratégicas (con influencers, otros creadores de herramientas, etc.).\
\
### Ritual de Época III: El Bucle de Inteligencia Competitiva\
- [ ] Ejecutar un \"sprint cero\" de análisis de mercado antes de iniciar el desarrollo.\
- [ ] Investigar y documentar las características y frustraciones de los usuarios de World Anvil, LegendKeeper y otras herramientas de world-building.\
- [ ] Analizar las estructuras de comisiones y promoción de creadores en DriveThruRPG, DMsGuild y la Unity Asset Store.\
- [ ] Analizar el contenido compartido en la \"#galeria-de-creaciones\" para identificar los tipos de contenido casero más populares y priorizar los \"Paquetes de Fichas\" de Worldforge.\
- [ ] Crear un documento de resumen con los hallazgos para guiar la estrategia de desarrollo de Worldforge y el Mercado.\
\
## Capítulo 12: Pista de Worldforge (v1.0) - La Construcción de la Forja Creativa\
**Objetivo Estratégico:** Construir el pilar tecnológico que permitirá la creación de contenido estructurado, atrayendo a una nueva demografía de usuarios (creadores).\
\
### La Arquitectura de \"Fichas\"\
- [ ] Diseñar un sistema de base de datos modular y flexible para almacenar diferentes tipos de \"Fichas\" (Ciudades, PNJs, Facciones, etc.).\
- [ ] Desarrollar una interfaz de usuario que permita a los creadores añadir, editar y conectar estas fichas de forma intuitiva.\
- [ ] Implementar una vista de \"árbol\" o \"grafo\" para visualizar las conexiones entre las diferentes fichas de un mundo.\
\
### El Modelo de Monetización Nativo\
- [ ] Implementar una lógica de permisos que limite el número de mundos o fichas para los usuarios gratuitos.\
- [ ] Integrar el sistema de pagos para permitir la compra de \"Paquetes de Fichas\" (e.g., Paquete de Facciones Avanzadas).\
- [ ] Crear la suscripción \"Worldforge Pro\" que desbloquee todas las fichas y ofrezca características avanzadas.\
\
## Capítulo 13: La Infraestructura del Mercado - La Construcción de la Economía\
**Objetivo Estratégico:** Desarrollar la infraestructura de e-commerce para que los creadores puedan empaquetar, vender y gestionar sus creaciones.\
\
### 13.1 El Andamiaje Legal del Mercado\
- [ ] Redactar un borrador de los \"Términos del Creador\" en colaboración con asesoría legal.\
- [ ] El documento debe definir claramente la propiedad intelectual (el creador la mantiene), las licencias de uso para Vorpal y los compradores, y las políticas de contenido.\
- [ ] Implementar un flujo en el que los creadores deban aceptar estos términos antes de poder publicar en el mercado.\
\
### El Portal del Creador\
- [ ] Desarrollar una nueva sección de la aplicación para el dashboard del creador.\
- [ ] Implementar el formulario para subir productos, incluyendo título, descripción, imágenes y el archivo de contenido de Worldforge.\
- [ ] Crear una interfaz para que los creadores fijen el precio de sus productos.\
- [ ] Desarrollar un panel de análisis que muestre las ventas, ingresos y número de descargas.\
\
### El Sistema de Transacciones y Comisiones\
- [ ] Ampliar la integración con Stripe para utilizar Stripe Connect, que permite gestionar pagos a terceros (creadores).\
- [ ] Desarrollar un servicio de backend que, tras una compra, calcule y divida el pago entre Vorpal y el creador según la comisión aplicable.\
- [ ] Implementar la lógica de \"La Senda del Creador\", ajustando dinámicamente el porcentaje de comisión según el nivel del creador.\
\
### El Escaparate Público\
- [ ] Diseñar y desarrollar la interfaz pública del mercado.\
- [ ] Implementar funcionalidades de búsqueda, filtrado por categorías y ordenación.\
- [ ] Desarrollar un sistema de valoraciones y reseñas para los productos.\
\
### 13.4 La Integración del Motor de Gamificación en el Mercado\
- [ ] Definir los niveles de creador (Aspirante, Maestro, Leyenda) como logros en el Motor de Gamificación, con reglas basadas en ventas o número de productos.\
- [ ] Integrar la API de logros en el perfil público del creador y en las páginas de sus productos para mostrar sus emblemas y nivel.\
- [ ] Asegurar que el sistema de prestigio visual sea coherente con el de los GMs en la \"Senda del Guardián\".\
\
## Capítulo 14: El Programa de Pioneros - Sembrando el Ecosistema\
**Objetivo Estratégico:** Colaborar con creadores seleccionados para asegurar un catálogo de contenido de alta calidad en el lanzamiento del mercado.\
\
### La Estrategia de Reclutamiento\
- [ ] Identificar a los principales contribuidores de la \"#galeria-de-creaciones\".\
- [ ] Investigar y crear una lista de micro-influencers y creadores de contenido homebrew en el ecosistema TTRPG.\
- [ ] Redactar un mensaje de invitación personalizado para contactar a los candidatos seleccionados.\
\
### El Paquete de Incentivos\
- [ ] Implementar la lógica para otorgar acceso anticipado a las herramientas de Worldforge a las cuentas de los \"Pioneros\".\
- [ ] Configurar un sistema en el backend para establecer una comisión del 0% para las ventas de los Pioneros durante un período inicial.\
- [ ] Planificar la estrategia de promoción para destacar a los Pioneros y sus productos durante el lanzamiento del mercado.\
\
### El Bucle de Feedback del Creador\
- [ ] Crear un canal privado de Discord exclusivo para los \"Pioneros\".\
- [ ] Establecer un canal de comunicación directo para proporcionar soporte técnico y recopilar feedback sobre las herramientas de Worldforge y el proceso de publicación.\
\
### 14.4 La Doctrina de la Simplicidad en las Herramientas del Creador\
- [ ] Durante el programa de Pioneros, realizar entrevistas de usabilidad para evaluar la complejidad de las herramientas.\
- [ ] Mantener un documento de \"Decisiones de Diseño\" que justifique cada característica en función de si facilita la publicación de contenido de calidad.\
- [ ] Priorizar las mejoras de UX/UI solicitadas por los Pioneros para reducir la fricción.\
\
## Capítulo 15: Pista del GM (v2.0) - La Integración del Ecosistema\
**Objetivo Estratégico:** Aumentar drásticamente el valor de \"GM Pro\" al integrarlo con el contenido del nuevo mercado.\
\
### La Pestaña del Mercado\
- [ ] Implementar una nueva pestaña o sección \"Mercado\" dentro de la interfaz de Vorpal GM.\
- [ ] Esta sección mostrará productos relevantes del mercado, utilizando la misma API que el escaparate público.\
\
### El Motor de Importación \"One-Click\"\
- [ ] Desarrollar la funcionalidad que, tras la compra de un producto por parte de un GM, añade el contenido directamente a su lista de recursos disponibles.\
- [ ] Implementar un botón \"Importar a Campaña\" que parsee el contenido del producto comprado y lo integre en el Códice de la campaña activa del GM.\
\
### La Evolución del Códice\
- [ ] Refactorizar y mejorar la estructura de datos y la UI del Códice de Campaña para manejar los tipos de contenido más complejos y estructurados de Worldforge.\
- [ ] Asegurar que los datos importados (monstruos, localizaciones, PNJs) se muestren de forma nativa y utilizable dentro del Códice.\
\
## Capítulo 16: Pista del Jugador (v2.1) - El Beneficiario del Ecosistema\
**Objetivo Estratégico:** Asegurar que la evolución de la plataforma beneficie directamente a los jugadores, manteniéndolos comprometidos.\
\
### La Integración del Mercado en Vorpal Player\
- [ ] Añadir una sección en Vorpal Player para que los jugadores puedan navegar y comprar productos del mercado, como plantillas de ficha de personaje y temas visuales.\
- [ ] Implementar la funcionalidad para instalar y aplicar estos productos comprados.\
\
### La Mejora de la Creación de Personajes\
- [ ] Implementar un sistema de permisos que permita a un GM \"compartir\" contenido comprado (e.g., un nuevo arquetipo) con los jugadores de su campaña.\
- [ ] Desarrollar la lógica en Vorpal Player para que los jugadores puedan acceder e importar este contenido compartido a sus fichas de personaje.\
\
### 16.3 La Planificación de la Transición de Fundadores a Equipo\
- [ ] Redactar una descripción de puesto detallada para un \"Community & Support Manager\".\
- [ ] Diseñar y documentar un \"Programa de Moderadores Voluntarios\", definiendo roles, responsabilidades y recompensas (e.g., suscripciones gratuitas, emblemas especiales).\
- [ ] Iniciar el proceso de reclutamiento para el programa de moderadores dentro de la comunidad existente.\
\
## Capítulo 17: El Lanzamiento Público del Ecosistema Vorpal\
**Objetivo Estratégico:** Comunicar la transformación de Vorpal de una herramienta a una plataforma.\
\
### La Estrategia de Marketing de Expansión\
- [ ] Diseñar y ejecutar campañas de marketing digital dirigidas a audiencias de escritores y diseñadores de juegos.\
- [ ] Crear contenido (artículos de blog, videos) que muestre las capacidades de Worldforge y el potencial del mercado.\
\
### El Evento de Lanzamiento\
- [ ] Planificar y organizar un evento de lanzamiento en línea (e.g., stream en Twitch o YouTube).\
- [ ] Coordinar con los \"Pioneros\" para que participen, muestren sus creaciones y compartan su experiencia.\
\
### 17.3 La Implementación del Motor de Curación y Descubrimiento v1.0\
- [ ] Desarrollar una herramienta interna para que el equipo de Vorpal pueda seleccionar y marcar productos como \"Selección Vorpal\" (Staff Picks).\
- [ ] Implementar una sección destacada en la página principal del mercado que muestre estas selecciones.\
- [ ] Asegurar que los niveles de creador (logros de gamificación) se muestren de forma prominente en los listados de productos como un filtro de calidad.\
\
### Estrategia de Construcción de Marca\
- [ ] Producir y publicar una serie de artículos de blog y videos tutoriales sobre creación de contenido para TTRPG.\
- [ ] Crear \"Casos de Éxito\" o \"Entrevistas a Creadores\" destacando las historias de los Pioneros.\
- [ ] Posicionar activamente la marca Vorpal como el mejor lugar para que los creadores de rol tengan éxito.\
\
## Capítulo 17.5: El Ritual del Jardín Cuidado\
**Objetivo Estratégico:** Formalizar el proceso de revisión del producto para combatir el 'bloatware' y mantener la fidelidad a la Doctrina de la Simplicidad.\
\
- [ ] Tras el lanzamiento, utilizar los datos de análisis anónimos para identificar las 3-5 características menos utilizadas en Vorpal Player y GM.\
- [ ] Realizar una reunión de \"Poda del Producto\" para evaluar cada una de estas características.\
- [ ] Por cada característica, decidir si se mejora su UX, se rediseña o se elimina por completo del producto.\
- [ ] Documentar las decisiones y añadirlas al backlog de desarrollo.\
- [ ] Calendarizar este ritual para que se repita al final de cada Época futura.\
\
# Época IV: Unificación y Escala\
\
### Operaciones de la Pista Cero:\
 Con la unificación, la Pista Cero se convierte en un Equipo de Crecimiento Formal. Se exploran canales de marketing de pago, se optimiza el embudo de ventas y se establecen KPIs (Indicadores Clave de Rendimiento) de negocio más robustos.\
\
### Ritual de Época IV: El Bucle de Inteligencia Competitiva\
- [ ] Ejecutar un \"sprint cero\" de análisis antes de la re-arquitectura.\
- [ ] Investigar y documentar las quejas más comunes y puntos de fricción de los usuarios de Roll20, Foundry VTT y Fantasy Grounds.\
- [ ] Evaluar y crear un prototipo de las tecnologías de comunicación en tiempo real más recientes (WebSockets, WebRTC) para determinar la mejor opción.\
- [ ] Realizar encuestas a los suscriptores de \"GM Pro\" para validar la demanda de un VTT y priorizar las características esenciales.\
- [ ] Crear un documento de especificaciones para el VTT basado en los hallazgos, enfocado en resolver los problemas clave del mercado.\
\
## Capítulo 18: La Infraestructura de la Unificación - La Re-arquitectura del Backend\
**Objetivo Estratégico:** Evolucionar la infraestructura para manejar interacciones complejas y multi-usuario en tiempo real.\
\
### Análisis de Tecnologías de Tiempo Real\
- [ ] Realizar una evaluación técnica profunda y comparativa entre WebSockets y WebRTC para las necesidades del VTT.\
- [ ] Seleccionar la tecnología y, si es necesario, un servicio gestionado o un framework de backend que la soporte de manera robusta.\
\
### El Modelo de Datos Unificado\
- [ ] Diseñar un nuevo esquema de base de datos que represente un \"universo de datos\" único.\
- [ ] Refactorizar los esquemas existentes de Worldforge, GM y Player para que sean vistas o subconjuntos de este modelo unificado.\
\
### El Plan de Migración\
- [ ] Escribir scripts de migración para transferir todos los datos de usuario existentes (personajes, campañas, mundos) a la nueva estructura de datos.\
- [ ] Planificar un período de mantenimiento para ejecutar la migración, con una estrategia de comunicación clara para los usuarios.\
- [ ] Realizar pruebas exhaustivas de la migración en un entorno de staging antes de ejecutarla en producción.\
\
### 18.4 El Mandato de la Documentación Técnica\
- [ ] Establecer como requisito que toda nueva API o servicio del backend de tiempo real debe tener documentación en formato OpenAPI/Swagger.\
- [ ] Integrar la generación de documentación en el proceso de CI/CD.\
- [ ] Asignar tiempo dentro de cada sprint de desarrollo para la creación y actualización de la documentación técnica.\
\
## Capítulo 19: Pista del VTT (v0.5) - El Tablero de Batalla Compartido (Prueba de Concepto)\
**Objetivo Estratégico:** Probar la nueva infraestructura de tiempo real con una funcionalidad de bajo riesgo y obtener feedback temprano.\
\
### El Desarrollo del \"Battlemap Helper\"\
- [ ] Implementar la funcionalidad para que un GM (con suscripción Pro) pueda subir una imagen de mapa.\
- [ ] Desarrollar la capacidad de aplicar una superposición de rejilla (cuadrada o hexagonal) sobre el mapa.\
- [ ] Utilizar la nueva infraestructura de tiempo real para compartir la vista del mapa con los jugadores conectados a la campaña.\
- [ ] Implementar una función de \"ping\" que permita al GM hacer clic en el mapa y que un marcador temporal aparezca en la pantalla de todos los jugadores.\
\
### La Medición del Rendimiento\
- [ ] Integrar herramientas de monitoreo en el backend para medir la latencia y la carga de los servicios de tiempo real.\
- [ ] Recopilar datos de rendimiento durante el uso real del \"Battlemap Helper\" para identificar cuellos de botella.\
- [ ] Optimizar la infraestructura basándose en los datos recopilados antes de construir el VTT completo.\
\
## Capítulo 20: Pista del VTT (v1.0) - La Mesa Virtual Integrada\
**Objetivo Estratégico:** Construir y lanzar la primera versión completa de nuestro VTT, enfocada en simplicidad, velocidad e integración nativa.\
\
### 20.3 La Aplicación de la Doctrina de la Simplicidad al VTT\
- [ ] Crear un documento de \"Anti-Features\" para el VTT v1.0, listando explícitamente funcionalidades complejas que NO se construirán (e.g., iluminación dinámica, scripting avanzado).\
- [ ] Evaluar cada propuesta de nueva característica para el VTT con la pregunta: \"¿Esto elimina más fricción de la que añade complejidad?\".\
\
### El Desarrollo del Núcleo del VTT\
- [ ] Implementar la carga y gestión de múltiples mapas por campaña.\
- [ ] Desarrollar la funcionalidad de tokens interactivos: arrastrables, redimensionables y vinculados a las fichas de personaje de Vorpal.\
- [ ] Crear un lanzador de dados 3D compartido y un log de tiradas visible para todos.\
- [ ] Implementar herramientas de medición de distancia en la rejilla.\
- [ ] Añadir un panel de chat de texto integrado en la sesión de VTT.\
\
### La Filosofía de la Interfaz\
- [ ] Diseñar un prototipo de la interfaz del VTT en Figma o una herramienta similar, con un enfoque radical en la simplicidad y la intuición.\
- [ ] Realizar pruebas de usabilidad del prototipo con usuarios actuales antes de escribir el código.\
- [ ] Implementar la interfaz de acuerdo con el prototipo validado.\
\
## Capítulo 21: La Convergencia del Ecosistema - La Evolución de los Pilares\
**Objetivo Estratégico:** Rediseñar y expandir los pilares existentes para que converjan con el VTT en una experiencia simbiótica.\
\
### Pista de Worldforge (v2.0) - El Taller del Cartógrafo\
- [ ] Integrar una herramienta de creación de mapas simple (basada en tiles o dibujo básico) en Worldforge.\
- [ ] Desarrollar un gestor de activos donde los creadores puedan subir y organizar imágenes para tokens y texturas de mapa.\
- [ ] Ampliar el mercado para permitir la venta de \"paquetes de activos de VTT\" (mapas, tokens, etc.).\
\
### Pista del Jugador (v3.0) - La Interfaz del Aventurero\
- [ ] Diseñar y desarrollar una \"vista de VTT\" para la ficha de personaje de Vorpal Player.\
- [ ] Esta vista debe funcionar como un HUD (Heads-Up Display) superpuesto o anclado a la interfaz del VTT.\
- [ ] Permitir que acciones en la ficha (e.g., hacer clic en una tirada de ataque) interactúen directamente con el VTT (e.g., activando el lanzador de dados).\
\
### 21.3 La Evolución de 'La Senda del Cronista' (Gamificación Unificada)\
- [ ] Diseñar y definir nuevos logros interconectados en el sistema de gamificación.\
- [ ] Implementar los triggers de backend para estos logros (e.g., un evento `monster_defeated_from_marketplace_asset`).\
- [ ] Actualizar la UI de logros para mostrar estas nuevas conexiones entre las \"Sendas\" del Jugador, Guardián y ahora \"Forjador\" (el nuevo nombre para la Senda del Creador).\
\
## Capítulo 22: El Modelo de Negocio Unificado\
**Objetivo Estratégico:** Definir y estructurar la nueva oferta comercial que refleje el valor añadido por la plataforma unificada.\
\
### La Creación de la Suscripción \"Vorpal Ultimate\"\
- [ ] Definir el conjunto de características que incluirá la suscripción \"Vorpal Ultimate\": acceso a todas las funciones de Player Plus, GM Pro, Worldforge Pro y el nuevo Vorpal VTT.\
- [ ] Implementar la lógica de permisos en el backend y frontend para este nuevo nivel de suscripción.\
\
### La Estrategia de Precios y Actualización\
- [ ] Realizar un análisis de mercado para establecer un precio competitivo para \"Vorpal Ultimate\".\
- [ ] Diseñar y desarrollar un flujo de actualización sencillo para los suscriptores existentes, aplicando descuentos prorrateados.\
- [ ] Comunicar claramente la nueva estructura de precios y las ventajas de la actualización.\
\
## Capítulo 23: El Segundo Gran Lanzamiento - La Plataforma Unificada Vorpal\
**Objetivo Estratégico:** Ejecutar una campaña a gran escala para anunciar la transformación de Vorpal en una plataforma de juego online completa.\
\
### La Estrategia de Posicionamiento en el Mercado\
- [ ] Redactar el nuevo mensaje de marketing central: \"Vorpal: La plataforma de rol más integrada del mundo\".\
- [ ] Crear una nueva página de inicio para el sitio web que comunique esta propuesta de valor de forma clara y visual.\
\
### La Campaña de Lanzamiento\
- [ ] Producir videos de demostración de alta calidad que muestren el flujo de trabajo integrado desde Worldforge hasta el VTT.\
- [ ] Colaborar con influencers de TTRPG para que muestren la plataforma unificada en sus canales.\
- [ ] Planificar y ejecutar una campaña de promociones de lanzamiento para incentivar la adopción de la suscripción \"Ultimate\".\
\
# Época V: Inteligencia y Dominancia del Mercado\
\
### Operaciones de la Pista Cero:\
 La Pista Cero es ahora un Equipo de Negocio Completo, con roles definidos para marketing, operaciones, finanzas y estrategia, asegurando la dominancia del mercado a largo plazo.\
\
### Ritual de Época V: El Bucle de Inteligencia Competitiva\
- [ ] Ejecutar un \"sprint cero\" de análisis de IA antes de la inversión en desarrollo.\
- [ ] Realizar una evaluación comparativa técnica y de costes de las APIs de IA de OpenAI, Anthropic, Google y modelos open-source relevantes.\
- [ ] Investigar y documentar el sentimiento de la comunidad TTRPG sobre el uso de IA, identificando preocupaciones éticas clave.\
- [ ] Analizar los datos de uso del \"Generador de Nombres de PNJ\" experimental para validar la demanda de herramientas de IA más avanzadas.\
- [ ] Crear una hoja de ruta para el desarrollo de IA que priorice las herramientas más solicitadas y aborde proactivamente las preocupaciones éticas.\
\
## Capítulo 24: La Infraestructura de la Inteligencia - El Núcleo Neuronal de Vorpal\
**Objetivo Estratégico:** Construir la base técnica, ética y económica para la integración de la IA a gran escala.\
\
### 24.4 El Andamiaje Legal y Ético de la IA\
- [ ] Redactar y publicar una \"Política de Uso Aceptable de la IA\" que prohíba la generación de contenido dañino o ilegal.\
- [ ] Redactar y publicar una \"Política de Datos de IA\" transparente, explicando que se usan datos anónimos y agregados para mejorar los modelos y permitiendo un opt-out.\
- [ ] Implementar mecanismos para que los usuarios acepten estas políticas antes de usar las funciones de IA.\
\
### La Arquitectura de APIs de IA\
- [ ] Desarrollar un servicio de \"gateway\" de IA interno en el backend.\
- [ ] Este gateway debe abstraer las llamadas a los proveedores de IA, permitiendo cambiar de modelo con una configuración en lugar de reescribir código.\
- [ ] Implementar la lógica para dirigir diferentes tipos de solicitudes (texto, imagen) al modelo más adecuado.\
\
### El Modelo Económico de \"Tokens\"\
- [ ] Integrar un sistema de contabilidad en el gateway de IA para rastrear el coste (en tokens o créditos) de cada llamada a la API por usuario.\
- [ ] Diseñar y crear la tabla en la base de datos para almacenar el saldo de \"créditos de IA\" de cada usuario.\
- [ ] Implementar la lógica de monetización: una asignación mensual de créditos para suscriptores y la opción de comprar paquetes de créditos adicionales.\
\
### La Política de Datos y Ética\
- [ ] Implementar filtros de contenido automáticos en el gateway de IA para prevenir la generación de material inapropiado.\
- [ ] Establecer un pipeline de datos que anonimice y agregue las interacciones de los usuarios con la IA para fines de mejora del modelo, en cumplimiento con la política de datos.\
\
## Capítulo 25: Pista de Worldforge (v3.0) - El Socio Creativo (\"Motor Génesis\")\
**Objetivo Estratégico:** Transformar Worldforge de una herramienta de documentación a un socio de brainstorming activo.\
\
### La Implementación del Diálogo Creativo\
- [ ] Desarrollar una interfaz de chat en Worldforge que se comunique con el gateway de IA.\
- [ ] Implementar un parser que pueda interpretar las respuestas estructuradas de la IA y utilizarlas para rellenar automáticamente nuevas fichas de Worldforge (PNJs, localizaciones).\
\
### La Generación de Contenido Aumentado\
- [ ] Añadir botones de \"sugerir detalles\" o \"expandir\" en los campos de las fichas de Worldforge.\
- [ ] Al hacer clic, la aplicación enviará el contexto de la ficha a la IA y rellenará el campo con la sugerencia generada.\
\
### El Taller del Artista Conceptual\
- [ ] Integrar una API de generación de imágenes en el gateway de IA.\
- [ ] Desarrollar una interfaz en Worldforge que permita a los usuarios escribir un prompt y generar arte conceptual para sus mundos, personajes y lugares.\
\
## Capítulo 26: Pista del GM (v3.0) - El Asistente de Improvisación (\"Motor de Improvisación\")\
**Objetivo Estratégico:** Otorgar al GM \"superpoderes\" de improvisación durante las partidas en vivo.\
\
### El Generador de Entidades en Tiempo Real\
- [ ] Crear una herramienta en la interfaz de Vorpal GM (y VTT) que permita al GM introducir un prompt simple (e.g., \"orco chamán con un solo ojo\").\
- [ ] La herramienta llamará a la IA para generar una ficha completa de PNJ o monstruo, incluyendo estadísticas y descripción, y la añadirá al Códice de Campaña.\
\
### El \"Pincel\" Narrativo\
- [ ] Implementar botones de acceso rápido en el VTT para generar descripciones dinámicas (e.g., \"Describir esta taberna\", \"Describir el tiempo que hace\").\
- [ ] La IA utilizará el contexto de la campaña para generar texto descriptivo que el GM pueda leer o adaptar.\
\
## Capítulo 27: Pista del Jugador (v4.0) - El Aumento de la Inmersión (\"Motor de Persona\")\
**Objetivo Estratégico:** Utilizar la IA para ayudar a los jugadores a conectarse más profundamente con sus personajes.\
\
### El Taller del Personaje\
- [ ] Desarrollar un asistente de creación de personajes que utilice la IA para ayudar a los jugadores a generar ideas de trasfondo, personalidad y motivaciones basadas en su clase y raza.\
- [ ] Implementar una función que genere una \"voz de personaje\" (ejemplos de cómo hablaría) basada en sus rasgos.\
\
### El Sugeridor de Acciones\
- [ ] Añadir un botón opcional \"Sugerir acción\" a la interfaz del jugador.\
- [ ] Al activarlo, la IA analizará la situación actual del juego y los rasgos del personaje para ofrecer 2-3 posibles líneas de acción o diálogo, ayudando a superar el bloqueo del jugador.\
\
## Capítulo 28: La Convergencia Definitiva - El VTT Aumentado por IA\
**Objetivo Estratégico:** Unificar todas las herramientas de IA en la experiencia de juego en vivo.\
\
### La Interfaz de IA Unificada\
- [ ] Diseñar y desarrollar un panel de control de IA para el GM dentro del VTT.\
- [ ] Este panel debe dar acceso rápido a todas las herramientas del \"Motor de Improvisación\" y \"Génesis\" sin necesidad de salir de la interfaz del VTT.\
\
### La Sinergia de los Motores\
- [ ] Implementar el flujo de trabajo completo: GM genera un PNJ con el \"Motor Génesis\" -> lo personaliza -> con un clic, genera un token de imagen para él con el \"Taller del Artista\" -> lo arrastra al VTT, donde ya está vinculado a su ficha.\
- [ ] Crear un video de demostración de este flujo para usarlo en marketing.\
\
### 28.3 El Onboarding para la IA (\"El Viaje del Creador Aumentado\")\
- [ ] Desarrollar una serie de tutoriales interactivos para las nuevas funciones de IA.\
- [ ] Los tutoriales deben enseñar no solo el \"cómo\" (hacer clic en el botón), sino también el \"por qué\" (mejores prácticas de \"prompt engineering\" para obtener mejores resultados).\
\
## Capítulo 29: La Frontera Final - \"The Oracle Engine\" y el Ecosistema Auto-mejorado\
**Objetivo Estratégico:** Abrir un mercado de juego en solitario y establecer una plataforma que aprende y mejora por sí misma.\
\
### El Desarrollo del \"Oracle Engine\"\
- [ ] Desarrollar una nueva capa de IA entrenada para actuar como GM.\
- [ ] Implementar la lógica para que el Oracle Engine pueda dirigir aventuras pre-hechas del mercado, presentando la narrativa, controlando los PNJs y respondiendo a las acciones del jugador.\
- [ ] Crear la interfaz para el juego en solitario, integrando el Oracle Engine con Vorpal Player y el VTT.\
\
### El Bucle de Retroalimentación de IA\
- [ ] Diseñar y construir la arquitectura para un sistema de auto-mejora.\
- [ ] El sistema recopilará datos anónimos y agregados sobre las partidas (e.g., qué encuentros resultaron en TPK, qué ganchos de trama fueron más seguidos).\
- [ ] Utilizar estos datos para realizar un ajuste fino (fine-tuning) periódico de los modelos de IA de Vorpal, mejorando su calidad y equilibrio con el tiempo.\
\
### 29.3 La Gobernanza de la Comunidad y la IA\
- [ ] Establecer formalmente un \"Consejo Comunitario de IA\".\
- [ ] Invitar a los creadores de nivel \"Leyenda\" y a los GMs más veteranos a formar parte de él.\
- [ ] Crear un foro privado para el consejo y organizar reuniones trimestrales para discutir la hoja de ruta ética y funcional de las herramientas de IA, asegurando que el desarrollo permanezca alineado con los valores de la comunidad.",
    "vorpalActionPlan": "Of course. Here is the comprehensive Action Plan and Development Checklist for the Vorpal software project, based exclusively on the provided document.\
    \
    # Época I: Fundación y Validación\
    \
    ### Operaciones de la Pista Cero:\
     Paralelamente al desarrollo del MVP, las operaciones de negocio se centrarán en Marketing Orgánico Fundacional. Esto incluye la creación de perfiles en redes sociales clave, la participación en comunidades de TTRPG para construir reputación (sin vender) y la gestión directa del feedback como el 'equipo de soporte' fundador.\
    \
    ## Capítulo 1: La Fundación Técnica y Metodológica\
    **Objetivo Estratégico:** Establecer un entorno de desarrollo profesional y un flujo de trabajo claro que garantice la escalabilidad y la eficiencia desde el primer día.\
    \
    ### El Taller Local\
    - [ ] Instalar y configurar VS Code en la Lenovo G50.\
    - [ ] Instalar las extensiones de VS Code recomendadas (e.g., Prettier, ESLint, Live Server).\
    - [ ] Inicializar un nuevo proyecto con la pila tecnológica Vanilla: HTML5, CSS3, JavaScript (ES6+).\
    - [ ] Crear la estructura de directorios del proyecto (`/src`, `/public`, `/css`, `/js`).\
    \
    ### 1.4 La Doctrina del Presupuesto de Rendimiento y Accesibilidad\
    - [ ] Crear un documento `PERFORMANCE_BUDGET.md` que formalice las reglas de rendimiento.\
    - [ ] Implementar un sistema de medición en el entorno de desarrollo para monitorizar el tiempo de carga y la respuesta de la UI.\
    - [ ] Configurar las herramientas de desarrollo del navegador para simular una conexión 3G para todas las pruebas de rendimiento.\
    - [ ] Durante las revisiones de código, evaluar cada nueva característica contra el presupuesto de rendimiento: carga <3s en 3G, respuesta de UI <100ms, usando la Lenovo G50 como hardware de referencia.\
    \
    ### El Puente a la Nube\
    - [ ] Inicializar un repositorio Git local con `git init`.\
    - [ ] Crear un nuevo repositorio en GitHub para el proyecto Vorpal.\
    - [ ] Realizar el primer commit con la estructura inicial del proyecto.\
    - [ ] Conectar el repositorio local con el remoto de GitHub y hacer push del commit inicial.\
    - [ ] Configurar GitHub Pages para que se despliegue automáticamente desde la rama principal (`main`).\
    \
    ### Nuestra Metodología\
    - [ ] Crear un documento `ROLES.md` que defina formalmente el rol de \"Director de Producto/Desarrollador IA\".\
    - [ ] Establecer un sistema de gestión de tareas (e.g., GitHub Projects) para visualizar el backlog y el progreso.\
    - [ ] Definir y documentar el ciclo de \"Sprint\" de desarrollo basado en prompts, especificando la duración y los rituales (planificación, revisión).\
    \
    ## Capítulo 2: El Prototipo Funcional - El Núcleo de Vorpal Player\
    **Objetivo Estratégico:** Construir la primera versión funcional e interactiva del producto, enfocándose en la experiencia del usuario final sin la complejidad de la persistencia de datos.\
    \
    ### La Arquitectura Visual (HTML/CSS)\
    - [ ] Crear el archivo `index.html` con una estructura semántica HTML5 (header, main, section, footer).\
    - [ ] Desarrollar la hoja de estilos CSS principal (`style.css`) siguiendo una metodología mobile-first.\
    - [ ] Implementar un diseño responsivo utilizando Flexbox y/o Grid Layout para adaptarse a pantallas de escritorio, tableta y móvil.\
    - [ ] Estructurar visualmente las áreas clave de la ficha de personaje (datos básicos, atributos, inventario, etc.).\
    \
    ### La Lógica de Interacción (JavaScript)\
    - [ ] Desarrollar la lógica del DOM para crear dinámicamente nuevos bloques de contenido en la ficha.\
    - [ ] Implementar la funcionalidad para eliminar bloques de contenido de la ficha.\
    - [ ] Desarrollar la lógica de arrastrar y soltar (drag-and-drop) para reorganizar los bloques dentro de la ficha de personaje.\
    - [ ] Asegurar que todas las interacciones del DOM cumplan con el presupuesto de rendimiento de <100ms.\
    \
    ## Capítulo 3: La Implementación de la \"Memoria\" - Persistencia de Datos\
    **Objetivo Estratégico:** Transformar el prototipo en una herramienta útil, asegurando que el trabajo del usuario se guarde y se restaure de manera fiable.\
    \
    ### 3.1 El Diseño del Esquema de Datos v1.0 (Principio de Escalabilidad)\
    - [ ] Crear un archivo `data-schema-v1.md` para documentar la estructura del objeto JSON del personaje.\
    - [ ] Implementar una función para generar identificadores únicos universales (UUID) para cada entidad principal (personaje, bloque, ítem).\
    - [ ] Diseñar la estructura del objeto JSON para prever relaciones futuras (e.g., `campaignId`, `gmId`), aunque se dejen como `null` inicialmente.\
    - [ ] Validar que la estructura del esquema es compatible con un futuro almacenamiento en una base de datos NoSQL como Firestore o Supabase.\
    \
    ### El Modelo de Datos\
    - [ ] Traducir el esquema de datos documentado a un objeto JavaScript que represente el estado de la ficha del personaje en la aplicación.\
    \
    ### El Motor de Guardado/Carga\
    - [ ] Implementar una función `saveToLocalStorage()` que serialice el objeto de estado del personaje a JSON y lo guarde en el `localStorage` del navegador.\
    - [ ] Implementar una función `loadFromLocalStorage()` que recupere el JSON del `localStorage`, lo deserialice y lo utilice para reconstruir el estado de la aplicación al cargar la página.\
    - [ ] Añadir listeners de eventos que activen `saveToLocalStorage()` después de cada cambio significativo realizado por el usuario.\
    \
    ### 3.3 El Diseño del Esquema de Datos para Eventos y Logros\
    - [ ] En el archivo `data-schema-v1.md`, añadir una sección para el esquema de eventos de usuario anónimos.\
    - [ ] Definir la estructura del evento (e.g., `{ eventName: 'string', timestamp: 'number', metadata: {} }`).\
    - [ ] Documentar eventos clave a rastrear en el futuro, como `character_created`, `session_started`, para asegurar la compatibilidad con el futuro sistema de gamificación.\
    \
    ## Capítulo 4: El Producto Mínimo Viable (MVP) - Finalización y Pulido\
    **Objetivo Estratégico:** Completar el conjunto de características del MVP y realizar una fase de pruebas internas para asegurar un lanzamiento de calidad.\
    \
    ### Las Funciones de Portabilidad\
    - [ ] Implementar un botón \"Exportar Personaje\" que convierta el estado actual del personaje a un archivo `.json` y lo descargue en el dispositivo del usuario.\
    - [ ] Implementar un botón \"Importar Personaje\" que permita al usuario seleccionar un archivo `.json` de su dispositivo, lo parsee y reemplace el estado actual de la aplicación con los datos importados.\
    - [ ] Añadir validación de datos en la función de importación para manejar errores si el archivo JSON no tiene el formato esperado.\
    \
    ### La Fase de Alpha Interna\
    - [ ] Crear un documento de plan de pruebas (`ALPHA_TEST_PLAN.md`).\
    - [ ] Definir escenarios de prueba clave para el equipo fundador (creación de personaje, edición, guardado/carga, importación/exportación).\
    - [ ] Ejecutar el plan de pruebas exhaustivamente en la Lenovo G50 y otros dispositivos disponibles.\
    - [ ] Utilizar el sistema de gestión de tareas (GitHub Issues) para registrar todos los bugs encontrados.\
    - [ ] Iterar en la corrección de bugs y el refinamiento de la UI/UX basándose en el feedback interno hasta que el producto sea estable.\
    \
    ## Capítulo 5: El Lanzamiento Público y la Creación de la Comunidad\
    **Objetivo Estratégico:** Lanzar el MVP al mundo, atraer a los primeros usuarios (\"early adopters\") y establecer los canales y procesos para convertir su feedback en la hoja de ruta del futuro.\
    \
    ### La Estrategia de Lanzamiento\
    - [ ] Redactar el mensaje de lanzamiento, enfocándose en la misión de Vorpal de potenciar la creatividad y eliminar la fricción.\
    - [ ] Identificar y seleccionar los canales de lanzamiento inicial (e.g., subreddits específicos de TTRPG, foros de rol).\
    - [ ] Ejecutar el \"lanzamiento suave\" publicando el mensaje y el enlace a la aplicación en los canales seleccionados.\
    \
    ### La Infraestructura Comunitaria\
    - [ ] Crear el servidor de Discord oficial de Vorpal.\
    - [ ] Estructurar los canales del servidor: `#anuncios`, `#general`, `#sugerencias`, `#reporte-de-bugs`.\
    \
    ### El Bucle de Feedback\
    - [ ] Establecer y documentar un proceso para revisar regularmente los canales `#sugerencias` y `#reporte-de-bugs`.\
    - [ ] Transferir los bugs y sugerencias válidas al backlog del proyecto en GitHub Issues.\
    - [ ] Publicar actualizaciones regulares en el canal `#anuncios` para comunicar los cambios y correcciones, reconociendo las contribuciones de la comunidad.\
    \
    ### 5.4 El Lanzamiento de la \"Galería de Creaciones\" (Cultura del Creador)\
    - [ ] Crear el canal `#galeria-de-creaciones` en el servidor de Discord.\
    - [ ] Redactar y fijar un mensaje en el canal explicando cómo compartir plantillas de personaje `.json` y animando a la participación.\
    - [ ] Monitorizar activamente el canal para destacar las creaciones interesantes e identificar a los usuarios más prolíficos como futuros \"Pioneros\".\
    \
    ### 5.5 La Implementación del Andamiaje Legal Básico\
    - [ ] Redactar una Política de Privacidad simple, explicando que todos los datos se almacenan localmente en el navegador del usuario.\
    - [ ] Redactar unos Términos de Servicio básicos utilizando una plantilla estándar adaptada.\
    - [ ] Añadir enlaces a ambos documentos en el pie de página de la aplicación Vorpal Player.\
    \
    ### 5.6 La Introducción del Concepto de Gamificación\
    - [ ] Incluir una sección en el mensaje de lanzamiento y en el mensaje de bienvenida de Discord mencionando la visión a largo plazo de \"La Senda del Cronista\".\
    - [ ] Crear un canal `#ideas-gamificacion` en Discord para que la comunidad pueda empezar a compartir ideas sobre logros y recompensas.\
    \
    ### Estrategia de Construcción de Marca\
    - [ ] Asegurar que toda la comunicación de lanzamiento se centre en la misión y la \"causa\" de Vorpal.\
    - [ ] Responder activamente y de manera positiva a todos los comentarios y publicaciones en Discord para establecer un tono de comunidad acogedor y constructivo.\
    \
    # Época II: Comercialización y Conexión\
    \
    ### Operaciones de la Pista Cero:\
     Con el lanzamiento comercial, la Pista Cero evoluciona a Crecimiento y Soporte Inicial. Esto implica establecer un sistema de tickets de soporte básico (puede ser un canal de Discord o un email), empezar a crear contenido de valor (posts de blog, tutoriales en video) y analizar las primeras métricas de conversión.\
    \
    ### Ritual de Época II: El Bucle de Inteligencia Competitiva\
    - [ ] Ejecutar un \"sprint cero\" de análisis antes de iniciar el desarrollo.\
    - [ ] Analizar y sintetizar todo el feedback del MVP de la comunidad para identificar las características más valoradas.\
    - [ ] Investigar y documentar los modelos de precios y características de al menos 3 herramientas de productividad freemium.\
    - [ ] Identificar una lista de los 5-10 usuarios más activos y positivos de la comunidad como candidatos para la Beta Cerrada.\
    - [ ] Crear un documento de resumen con los hallazgos para informar el diseño de las suscripciones \"Plus\" y \"Pro\".\
    \
    ## Capítulo 6: La Infraestructura Técnica del Negocio\
    **Objetivo Estratégico:** Construir la columna vertebral técnica que soportará las cuentas de usuario, los datos en la nuba y las transacciones financieras.\
    \
    ### La Transición a la Nube\
    - [ ] Seleccionar y configurar un proveedor de Backend como Servicio (BaaS), como Firebase o Supabase.\
    - [ ] Diseñar y crear las tablas/colecciones de la base de datos para `users` y `characters`.\
    - [ ] Implementar la lógica en la aplicación cliente para sincronizar los datos del personaje con la base de datos en la nube en lugar de `localStorage` para los usuarios autenticados.\
    \
    ### El Sistema de Autenticación\
    - [ ] Implementar las funciones de registro de nuevos usuarios (email/contraseña).\
    - [ ] Implementar las funciones de inicio y cierre de sesión.\
    - [ ] Integrar la lógica de autenticación en la UI de la aplicación, protegiendo las rutas y funciones conectadas.\
    \
    ### La Integración de la Pasarela de Pagos\
    - [ ] Crear una cuenta de desarrollador en Stripe (o la alternativa seleccionada).\
    - [ ] Integrar el SDK de Stripe en la aplicación cliente.\
    - [ ] Desarrollar las funciones de backend (cloud functions) para gestionar los intentos de pago, la creación de suscripciones y la verificación del estado de las mismas.\
    \
    ### 6.4 La Integración de Analítica de Privacidad (El Filo del Freemium)\
    - [ ] Seleccionar e integrar una herramienta de análisis de eventos anónima y respetuosa con la privacidad (e.g., Plausible, Fathom).\
    - [ ] Implementar el seguimiento de eventos clave anónimos, como `feature_used`, `subscription_page_viewed`, `signup_completed`.\
    - [ ] Crear un panel de control para visualizar estas métricas y responder a preguntas de negocio.\
    \
    ### 6.5 La Construcción del Motor de Gamificación v1.0\
    - [ ] Diseñar y crear las tablas/colecciones en la base de datos para `user_achievements` y `achievement_rules`.\
    - [ ] Desarrollar un servicio de backend que reciba eventos de usuario anónimos y los procese contra las `achievement_rules`.\
    - [ ] Crear una API RESTful (`/api/users/{userId}/achievements`) que la aplicación cliente pueda consultar para obtener los logros desbloqueados de un usuario.\
    \
    ## Capítulo 7: Pista del Jugador (v2.0) - El Producto Mínimo Suscribible\
    **Objetivo Estratégico:** Crear la primera oferta de pago para nuestra base de usuarios más grande, probando su disposición a pagar por conveniencia y personalización.\
    \
    ### El Desarrollo de \"Vorpal Plus\"\
    - [ ] Implementar la sincronización de múltiples personajes en la nube para usuarios con suscripción \"Plus\".\
    - [ ] Desarrollar una biblioteca de temas visuales (CSS) y un mecanismo para que los suscriptores los seleccionen y apliquen.\
    - [ ] Crear la funcionalidad de \"crónica de personaje\", que guarda snapshots del personaje a lo largo del tiempo.\
    \
    ### La Arquitectura de Permisos\
    - [ ] Desarrollar una función o middleware en el cliente que verifique el estado de la suscripción del usuario.\
    - [ ] Utilizar esta función para ocultar o deshabilitar las características \"Plus\" para los usuarios del plan gratuito.\
    - [ ] Asegurar que la verificación de permisos también se realice en el backend para evitar el acceso no autorizado a las APIs de pago.\
    \
    ### 7.3 La Introducción de Ganchos de Compromiso\
    - [ ] Implementar la UI para mostrar notificaciones de logros desbloqueados.\
    - [ ] Crear una sección en el perfil del usuario donde se listen todos los logros (bloqueados y desbloqueados).\
    - [ ] Definir e implementar el primer conjunto de logros simples (e.g., 'Personaje Creado', 'Primera Semana de Uso').\
    \
    ### 7.4 La Activación de 'La Senda del Aventurero' (Fase 1)\
    - [ ] Configurar las reglas para los primeros logros del jugador en el backend del Motor de Gamificación.\
    - [ ] Desarrollar la interfaz de usuario en Vorpal Player para mostrar el progreso de los logros.\
    - [ ] Conectar las recompensas cosméticas (temas, skins de dados) a logros específicos, de modo que se desbloqueen automáticamente.\
    \
    ## Capítulo 8: Pista del GM (v1.0) - El Producto Mínimo Vendible\
    **Objetivo Estratégico:** Construir y definir la oferta principal que será nuestro motor de ingresos recurrente, resolviendo los problemas más agudos del Director de Juego.\
    \
    ### El Desarrollo de \"GM Pro\"\
    - [ ] Crear una nueva aplicación o una nueva sección en la aplicación existente para el \"Vorpal GM\".\
    - [ ] Desarrollar la dashboard de gestión de campañas y jugadores.\
    - [ ] Implementar el \"códice de campaña\", permitiendo al GM crear y organizar notas, PNJs y localizaciones con almacenamiento ilimitado en la nube.\
    - [ ] Construir herramientas de preparación de sesión (e.g., generadores de encuentros básicos, gestores de iniciativa).\
    \
    ### 8.4 La Primera Integración de IA Experimental\
    - [ ] Seleccionar y obtener una clave de API para un servicio de IA de generación de texto de bajo coste.\
    - [ ] Crear una función de backend segura que actúe como proxy para las llamadas a la API de IA, utilizando la clave de la API del servidor.\
    - [ ] Implementar un botón \"Generar Nombre de PNJ\" en la interfaz de GM Pro que llame a esta función y muestre el resultado.\
    - [ ] Añadir seguimiento de eventos anónimos para medir la frecuencia de uso de esta característica.\
    \
    ### 8.5 La Activación de 'La Senda del Guardián' (Fase 1)\
    - [ ] Definir y configurar las reglas para los primeros logros del GM en el backend (e.g., 'Primera Campaña Creada', 'Primer Jugador Invitado').\
    - [ ] Desarrollar la interfaz en Vorpal GM para mostrar los logros y los emblemas/títulos desbloqueados.\
    - [ ] Crear una sección de perfil de comunidad pública donde estos títulos sean visibles para otros usuarios.\
    \
    ## Capítulo 9: El Puente Conector - La Sinergia en Tiempo Real\
    **Objetivo Estratégico:** Desarrollar la \"magia\" tecnológica que conecta a jugadores y GMs, creando una propuesta de valor única que ninguna herramienta aislada puede ofrecer.\
    \
    ### La Arquitectura de Datos en Tiempo Real\
    - [ ] Utilizar las capacidades de tiempo real del BaaS seleccionado (e.g., Firestore Listeners, Supabase Realtime).\
    - [ ] Diseñar la estructura de la base de datos para que la \"campaña\" del GM contenga referencias a las fichas de sus jugadores.\
    - [ ] Implementar las reglas de seguridad de la base de datos para que un GM solo pueda leer/escribir en las fichas de los jugadores de su campaña.\
    \
    ### La Implementación de \"Listeners\"\
    - [ ] En la aplicación Vorpal Player, implementar un \"listener\" que se suscriba a los cambios en la ficha del personaje del usuario cuando está en una campaña activa.\
    - [ ] En la aplicación Vorpal GM, implementar listeners que se suscriban a los cambios en las fichas de todos los personajes de la campaña activa.\
    - [ ] Desarrollar la lógica para que, cuando el GM realice un cambio (e.g., \"dañar\" a un jugador), el cambio se escriba en la base de datos y la interfaz del jugador se actualice instantáneamente.\
    \
    ## Capítulo 10: La Prueba de Fuego - La Fase Beta Cerrada\
    **Objetivo Estratégico:** Probar la estabilidad de la nueva infraestructura conectada y validar la percepción de valor de nuestras ofertas de pago con un grupo selecto de usuarios leales.\
    \
    ### La Estrategia de la Beta\
    - [ ] Contactar a los candidatos a testers identificados en el \"Ritual de Época II\".\
    - [ ] Crear un canal privado en Discord para los participantes de la beta.\
    - [ ] Otorgar acceso gratuito a las suscripciones \"Plus\" y \"Pro\" a las cuentas de los testers.\
    \
    ### El Bucle de Iteración de la Beta\
    - [ ] Crear y distribuir un formulario de feedback estructurado a los testers.\
    - [ ] El formulario debe incluir preguntas sobre estabilidad, usabilidad, valor de las características y percepción del precio propuesto.\
    - [ ] Organizar sesiones de feedback en vivo (opcional) en el canal privado de Discord.\
    - [ ] Utilizar los datos recopilados para realizar ajustes finales en el producto y en la estrategia de precios antes del lanzamiento público.\
    \
    ## Capítulo 11: La Apertura de Puertas - El Lanzamiento Público de la Plataforma Comercial\
    **Objetivo Estratégico:** Lanzar oficialmente las suscripciones \"Vorpal Plus\" y \"GM Pro\" a toda la base de usuarios.\
    \
    ### La Estrategia de Comunicación del Lanzamiento\
    - [ ] Redactar una publicación de blog y anuncios para Discord y redes sociales explicando las nuevas funcionalidades.\
    - [ ] Enfatizar que la versión gratuita sigue siendo una herramienta potente y que las suscripciones apoyan el desarrollo futuro.\
    - [ ] Preparar una sección de Preguntas Frecuentes (FAQ) sobre las nuevas suscripciones.\
    \
    ### El Proceso de \"Onboarding\" para Clientes\
    - [ ] Diseñar y desarrollar la página de precios y suscripción.\
    - [ ] Implementar un flujo de pago claro y sencillo utilizando la integración de Stripe.\
    - [ ] Crear correos electrónicos de bienvenida para los nuevos suscriptores, guiándolos hacia las nuevas funciones.\
    \
    ### 11.3 La Creación del \"Viaje del GM\" (Onboarding)\
    - [ ] Desarrollar un tutorial interactivo para los nuevos suscriptores de \"GM Pro\".\
    - [ ] Implementar tooltips y guías contextuales que aparezcan la primera vez que un GM accede a funciones clave como el códice o la conexión de jugadores.\
    - [ ] Asegurarse de que el onboarding demuestre el valor inmediato del producto.\
    \
    # Época III: Expansión y Creación del Efecto de Red\
    \
    ### Operaciones de la Pista Cero:\
     Con la expansión del ecosistema, la Pista Cero se enfoca en Escala Comunitaria y Desarrollo de Negocio. Aquí se ejecuta el plan de la primera contratación (Community Manager) y se comienzan a explorar alianzas estratégicas (con influencers, otros creadores de herramientas, etc.).\
    \
    ### Ritual de Época III: El Bucle de Inteligencia Competitiva\
    - [ ] Ejecutar un \"sprint cero\" de análisis de mercado antes de iniciar el desarrollo.\
    - [ ] Investigar y documentar las características y frustraciones de los usuarios de World Anvil, LegendKeeper y otras herramientas de world-building.\
    - [ ] Analizar las estructuras de comisiones y promoción de creadores en DriveThruRPG, DMsGuild y la Unity Asset Store.\
    - [ ] Analizar el contenido compartido en la \"#galeria-de-creaciones\" para identificar los tipos de contenido casero más populares y priorizar los \"Paquetes de Fichas\" de Worldforge.\
    - [ ] Crear un documento de resumen con los hallazgos para guiar la estrategia de desarrollo de Worldforge y el Mercado.\
    \
    ## Capítulo 12: Pista de Worldforge (v1.0) - La Construcción de la Forja Creativa\
    **Objetivo Estratégico:** Construir el pilar tecnológico que permitirá la creación de contenido estructurado, atrayendo a una nueva demografía de usuarios (creadores).\
    \
    ### La Arquitectura de \"Fichas\"\
    - [ ] Diseñar un sistema de base de datos modular y flexible para almacenar diferentes tipos de \"Fichas\" (Ciudades, PNJs, Facciones, etc.).\
    - [ ] Desarrollar una interfaz de usuario que permita a los creadores añadir, editar y conectar estas fichas de forma intuitiva.\
    - [ ] Implementar una vista de \"árbol\" o \"grafo\" para visualizar las conexiones entre las diferentes fichas de un mundo.\
    \
    ### El Modelo de Monetización Nativo\
    - [ ] Implementar una lógica de permisos que limite el número de mundos o fichas para los usuarios gratuitos.\
    - [ ] Integrar el sistema de pagos para permitir la compra de \"Paquetes de Fichas\" (e.g., Paquete de Facciones Avanzadas).\
    - [ ] Crear la suscripción \"Worldforge Pro\" que desbloquee todas las fichas y ofrezca características avanzadas.\
    \
    ## Capítulo 13: La Infraestructura del Mercado - La Construcción de la Economía\
    **Objetivo Estratégico:** Desarrollar la infraestructura de e-commerce para que los creadores puedan empaquetar, vender y gestionar sus creaciones.\
    \
    ### 13.1 El Andamiaje Legal del Mercado\
    - [ ] Redactar un borrador de los \"Términos del Creador\" en colaboración con asesoría legal.\
    - [ ] El documento debe definir claramente la propiedad intelectual (el creador la mantiene), las licencias de uso para Vorpal y los compradores, y las políticas de contenido.\
    - [ ] Implementar un flujo en el que los creadores deban aceptar estos términos antes de poder publicar en el mercado.\
    \
    ### El Portal del Creador\
    - [ ] Desarrollar una nueva sección de la aplicación para el dashboard del creador.\
    - [ ] Implementar el formulario para subir productos, incluyendo título, descripción, imágenes y el archivo de contenido de Worldforge.\
    - [ ] Crear una interfaz para que los creadores fijen el precio de sus productos.\
    - [ ] Desarrollar un panel de análisis que muestre las ventas, ingresos y número de descargas.\
    \
    ### El Sistema de Transacciones y Comisiones\
    - [ ] Ampliar la integración con Stripe para utilizar Stripe Connect, que permite gestionar pagos a terceros (creadores).\
    - [ ] Desarrollar un servicio de backend que, tras una compra, calcule y divida el pago entre Vorpal y el creador según la comisión aplicable.\
    - [ ] Implementar la lógica de \"La Senda del Creador\", ajustando dinámicamente el porcentaje de comisión según el nivel del creador.\
    \
    ### El Escaparate Público\
    - [ ] Diseñar y desarrollar la interfaz pública del mercado.\
    - [ ] Implementar funcionalidades de búsqueda, filtrado por categorías y ordenación.\
    - [ ] Desarrollar un sistema de valoraciones y reseñas para los productos.\
    \
    ### 13.4 La Integración del Motor de Gamificación en el Mercado\
    - [ ] Definir los niveles de creador (Aspirante, Maestro, Leyenda) como logros en el Motor de Gamificación, con reglas basadas en ventas o número de productos.\
    - [ ] Integrar la API de logros en el perfil público del creador y en las páginas de sus productos para mostrar sus emblemas y nivel.\
    - [ ] Asegurar que el sistema de prestigio visual sea coherente con el de los GMs en la \"Senda del Guardián\".\
    \
    ## Capítulo 14: El Programa de Pioneros - Sembrando el Ecosistema\
    **Objetivo Estratégico:** Colaborar con creadores seleccionados para asegurar un catálogo de contenido de alta calidad en el lanzamiento del mercado.\
    \
    ### La Estrategia de Reclutamiento\
    - [ ] Identificar a los principales contribuidores de la \"#galeria-de-creaciones\".\
    - [ ] Investigar y crear una lista de micro-influencers y creadores de contenido homebrew en el ecosistema TTRPG.\
    - [ ] Redactar un mensaje de invitación personalizado para contactar a los candidatos seleccionados.\
    \
    ### El Paquete de Incentivos\
    - [ ] Implementar la lógica para otorgar acceso anticipado a las herramientas de Worldforge a las cuentas de los \"Pioneros\".\
    - [ ] Configurar un sistema en el backend para establecer una comisión del 0% para las ventas de los Pioneros durante un período inicial.\
    - [ ] Planificar la estrategia de promoción para destacar a los Pioneros y sus productos durante el lanzamiento del mercado.\
    \
    ### El Bucle de Feedback del Creador\
    - [ ] Crear un canal privado de Discord exclusivo para los \"Pioneros\".\
    - [ ] Establecer un canal de comunicación directo para proporcionar soporte técnico y recopilar feedback sobre las herramientas de Worldforge y el proceso de publicación.\
    \
    ### 14.4 La Doctrina de la Simplicidad en las Herramientas del Creador\
    - [ ] Durante el programa de Pioneros, realizar entrevistas de usabilidad para evaluar la complejidad de las herramientas.\
    - [ ] Mantener un documento de \"Decisiones de Diseño\" que justifique cada característica en función de si facilita la publicación de contenido de calidad.\
    - [ ] Priorizar las mejoras de UX/UI solicitadas por los Pioneros para reducir la fricción.\
    \
    ## Capítulo 15: Pista del GM (v2.0) - La Integración del Ecosistema\
    **Objetivo Estratégico:** Aumentar drásticamente el valor de \"GM Pro\" al integrarlo con el contenido del nuevo mercado.\
    \
    ### La Pestaña del Mercado\
    - [ ] Implementar una nueva pestaña o sección \"Mercado\" dentro de la interfaz de Vorpal GM.\
    - [ ] Esta sección mostrará productos relevantes del mercado, utilizando la misma API que el escaparate público.\
    \
    ### El Motor de Importación \"One-Click\"\
    - [ ] Desarrollar la funcionalidad que, tras la compra de un producto por parte de un GM, añade el contenido directamente a su lista de recursos disponibles.\
    - [ ] Implementar un botón \"Importar a Campaña\" que parsee el contenido del producto comprado y lo integre en el Códice de la campaña activa del GM.\
    \
    ### La Evolución del Códice\
    - [ ] Refactorizar y mejorar la estructura de datos y la UI del Códice de Campaña para manejar los tipos de contenido más complejos y estructurados de Worldforge.\
    - [ ] Asegurar que los datos importados (monstruos, localizaciones, PNJs) se muestren de forma nativa y utilizable dentro del Códice.\
    \
    ## Capítulo 16: Pista del Jugador (v2.1) - El Beneficiario del Ecosistema\
    **Objetivo Estratégico:** Asegurar que la evolución de la plataforma beneficie directamente a los jugadores, manteniéndolos comprometidos.\
    \
    ### La Integración del Mercado en Vorpal Player\
    - [ ] Añadir una sección en Vorpal Player para que los jugadores puedan navegar y comprar productos del mercado, como plantillas de ficha de personaje y temas visuales.\
    - [ ] Implementar la funcionalidad para instalar y aplicar estos productos comprados.\
    \
    ### La Mejora de la Creación de Personajes\
    - [ ] Implementar un sistema de permisos que permita a un GM \"compartir\" contenido comprado (e.g., un nuevo arquetipo) con los jugadores de su campaña.\
    - [ ] Desarrollar la lógica en Vorpal Player para que los jugadores puedan acceder e importar este contenido compartido a sus fichas de personaje.\
    \
    ### 16.3 La Planificación de la Transición de Fundadores a Equipo\
    - [ ] Redactar una descripción de puesto detallada para un \"Community & Support Manager\".\
    - [ ] Diseñar y documentar un \"Programa de Moderadores Voluntarios\", definiendo roles, responsabilidades y recompensas (e.g., suscripciones gratuitas, emblemas especiales).\
    - [ ] Iniciar el proceso de reclutamiento para el programa de moderadores dentro de la comunidad existente.\
    \
    ## Capítulo 17: El Lanzamiento Público del Ecosistema Vorpal\
    **Objetivo Estratégico:** Comunicar la transformación de Vorpal de una herramienta a una plataforma.\
    \
    ### La Estrategia de Marketing de Expansión\
    - [ ] Diseñar y ejecutar campañas de marketing digital dirigidas a audiencias de escritores y diseñadores de juegos.\
    - [ ] Crear contenido (artículos de blog, videos) que muestre las capacidades de Worldforge y el potencial del mercado.\
    \
    ### El Evento de Lanzamiento\
    - [ ] Planificar y organizar un evento de lanzamiento en línea (e.g., stream en Twitch o YouTube).\
    - [ ] Coordinar con los \"Pioneros\" para que participen, muestren sus creaciones y compartan su experiencia.\
    \
    ### 17.3 La Implementación del Motor de Curación y Descubrimiento v1.0\
    - [ ] Desarrollar una herramienta interna para que el equipo de Vorpal pueda seleccionar y marcar productos como \"Selección Vorpal\" (Staff Picks).\
    - [ ] Implementar una sección destacada en la página principal del mercado que muestre estas selecciones.\
    - [ ] Asegurar que los niveles de creador (logros de gamificación) se muestren de forma prominente en los listados de productos como un filtro de calidad.\
    \
    ### Estrategia de Construcción de Marca\
    - [ ] Producir y publicar una serie de artículos de blog y videos tutoriales sobre creación de contenido para TTRPG.\
    - [ ] Crear \"Casos de Éxito\" o \"Entrevistas a Creadores\" destacando las historias de los Pioneros.\
    - [ ] Posicionar activamente la marca Vorpal como el mejor lugar para que los creadores de rol tengan éxito.\
    \
    ## Capítulo 17.5: El Ritual del Jardín Cuidado\
    **Objetivo Estratégico:** Formalizar el proceso de revisión del producto para combatir el 'bloatware' y mantener la fidelidad a la Doctrina de la Simplicidad.\
    \
    - [ ] Tras el lanzamiento, utilizar los datos de análisis anónimos para identificar las 3-5 características menos utilizadas en Vorpal Player y GM.\
    - [ ] Realizar una reunión de \"Poda del Producto\" para evaluar cada una de estas características.\
    - [ ] Por cada característica, decidir si se mejora su UX, se rediseña o se elimina por completo del producto.\
    - [ ] Documentar las decisiones y añadirlas al backlog de desarrollo.\
    - [ ] Calendarizar este ritual para que se repita al final de cada Época futura.\
    \
    # Época IV: Unificación y Escala\
    \
    ### Operaciones de la Pista Cero:\
     Con la unificación, la Pista Cero se convierte en un Equipo de Crecimiento Formal. Se exploran canales de marketing de pago, se optimiza el embudo de ventas y se establecen KPIs (Indicadores Clave de Rendimiento) de negocio más robustos.\
    \
    ### Ritual de Época IV: El Bucle de Inteligencia Competitiva\
    - [ ] Ejecutar un \"sprint cero\" de análisis antes de la re-arquitectura.\
    - [ ] Investigar y documentar las quejas más comunes y puntos de fricción de los usuarios de Roll20, Foundry VTT y Fantasy Grounds.\
    - [ ] Evaluar y crear un prototipo de las tecnologías de comunicación en tiempo real más recientes (WebSockets, WebRTC) para determinar la mejor opción.\
    - [ ] Realizar encuestas a los suscriptores de \"GM Pro\" para validar la demanda de un VTT y priorizar las características esenciales.\
    - [ ] Crear un documento de especificaciones para el VTT basado en los hallazgos, enfocado en resolver los problemas clave del mercado.\
    \
    ## Capítulo 18: La Infraestructura de la Unificación - La Re-arquitectura del Backend\
    **Objetivo Estratégico:** Evolucionar la infraestructura para manejar interacciones complejas y multi-usuario en tiempo real.\
    \
    ### Análisis de Tecnologías de Tiempo Real\
    - [ ] Realizar una evaluación técnica profunda y comparativa entre WebSockets y WebRTC para las necesidades del VTT.\
    - [ ] Seleccionar la tecnología y, si es necesario, un servicio gestionado o un framework de backend que la soporte de manera robusta.\
    \
    ### El Modelo de Datos Unificado\
    - [ ] Diseñar un nuevo esquema de base de datos que represente un \"universo de datos\" único.\
    - [ ] Refactorizar los esquemas existentes de Worldforge, GM y Player para que sean vistas o subconjuntos de este modelo unificado.\
    \
    ### El Plan de Migración\
    - [ ] Escribir scripts de migración para transferir todos los datos de usuario existentes (personajes, campañas, mundos) a la nueva estructura de datos.\
    - [ ] Planificar un período de mantenimiento para ejecutar la migración, con una estrategia de comunicación clara para los usuarios.\
    - [ ] Realizar pruebas exhaustivas de la migración en un entorno de staging antes de ejecutarla en producción.\
    \
    ### 18.4 El Mandato de la Documentación Técnica\
    - [ ] Establecer como requisito que toda nueva API o servicio del backend de tiempo real debe tener documentación en formato OpenAPI/Swagger.\
    - [ ] Integrar la generación de documentación en el proceso de CI/CD.\
    - [ ] Asignar tiempo dentro de cada sprint de desarrollo para la creación y actualización de la documentación técnica.\
    \
    ## Capítulo 19: Pista del VTT (v0.5) - El Tablero de Batalla Compartido (Prueba de Concepto)\
    **Objetivo Estratégico:** Probar la nueva infraestructura de tiempo real con una funcionalidad de bajo riesgo y obtener feedback temprano.\
    \
    ### El Desarrollo del \"Battlemap Helper\"\
    - [ ] Implementar la funcionalidad para que un GM (con suscripción Pro) pueda subir una imagen de mapa.\
    - [ ] Desarrollar la capacidad de aplicar una superposición de rejilla (cuadrada o hexagonal) sobre el mapa.\
    - [ ] Utilizar la nueva infraestructura de tiempo real para compartir la vista del mapa con los jugadores conectados a la campaña.\
    - [ ] Implementar una función de \"ping\" que permita al GM hacer clic en el mapa y que un marcador temporal aparezca en la pantalla de todos los jugadores.\
    \
    ### La Medición del Rendimiento\
    - [ ] Integrar herramientas de monitoreo en el backend para medir la latencia y la carga de los servicios de tiempo real.\
    - [ ] Recopilar datos de rendimiento durante el uso real del \"Battlemap Helper\" para identificar cuellos de botella.\
    - [ ] Optimizar la infraestructura basándose en los datos recopilados antes de construir el VTT completo.\
    \
    ## Capítulo 20: Pista del VTT (v1.0) - La Mesa Virtual Integrada\
    **Objetivo Estratégico:** Construir y lanzar la primera versión completa de nuestro VTT, enfocada en simplicidad, velocidad e integración nativa.\
    \
    ### 20.3 La Aplicación de la Doctrina de la Simplicidad al VTT\
    - [ ] Crear un documento de \"Anti-Features\" para el VTT v1.0, listando explícitamente funcionalidades complejas que NO se construirán (e.g., iluminación dinámica, scripting avanzado).\
    - [ ] Evaluar cada propuesta de nueva característica para el VTT con la pregunta: \"¿Esto elimina más fricción de la que añade complejidad?\".\
    \
    ### El Desarrollo del Núcleo del VTT\
    - [ ] Implementar la carga y gestión de múltiples mapas por campaña.\
    - [ ] Desarrollar la funcionalidad de tokens interactivos: arrastrables, redimensionables y vinculados a las fichas de personaje de Vorpal.\
    - [ ] Crear un lanzador de dados 3D compartido y un log de tiradas visible para todos.\
    - [ ] Implementar herramientas de medición de distancia en la rejilla.\
    - [ ] Añadir un panel de chat de texto integrado en la sesión de VTT.\
    \
    ### La Filosofía de la Interfaz\
    - [ ] Diseñar un prototipo de la interfaz del VTT en Figma o una herramienta similar, con un enfoque radical en la simplicidad y la intuición.\
    - [ ] Realizar pruebas de usabilidad del prototipo con usuarios actuales antes de escribir el código.\
    - [ ] Implementar la interfaz de acuerdo con el prototipo validado.\
    \
    ## Capítulo 21: La Convergencia del Ecosistema - La Evolución de los Pilares\
    **Objetivo Estratégico:** Rediseñar y expandir los pilares existentes para que converjan con el VTT en una experiencia simbiótica.\
    \
    ### Pista de Worldforge (v2.0) - El Taller del Cartógrafo\
    - [ ] Integrar una herramienta de creación de mapas simple (basada en tiles o dibujo básico) en Worldforge.\
    - [ ] Desarrollar un gestor de activos donde los creadores puedan subir y organizar imágenes para tokens y texturas de mapa.\
    - [ ] Ampliar el mercado para permitir la venta de \"paquetes de activos de VTT\" (mapas, tokens, etc.).\
    \
    ### Pista del Jugador (v3.0) - La Interfaz del Aventurero\
    - [ ] Diseñar y desarrollar una \"vista de VTT\" para la ficha de personaje de Vorpal Player.\
    - [ ] Esta vista debe funcionar como un HUD (Heads-Up Display) superpuesto o anclado a la interfaz del VTT.\
    - [ ] Permitir que acciones en la ficha (e.g., hacer clic en una tirada de ataque) interactúen directamente con el VTT (e.g., activando el lanzador de dados).\
    \
    ### 21.3 La Evolución de 'La Senda del Cronista' (Gamificación Unificada)\
    - [ ] Diseñar y definir nuevos logros interconectados en el sistema de gamificación.\
    - [ ] Implementar los triggers de backend para estos logros (e.g., un evento `monster_defeated_from_marketplace_asset`).\
    - [ ] Actualizar la UI de logros para mostrar estas nuevas conexiones entre las \"Sendas\" del Jugador, Guardián y ahora \"Forjador\" (el nuevo nombre para la Senda del Creador).\
    \
    ## Capítulo 22: El Modelo de Negocio Unificado\
    **Objetivo Estratégico:** Definir y estructurar la nueva oferta comercial que refleje el valor añadido por la plataforma unificada.\
    \
    ### La Creación de la Suscripción \"Vorpal Ultimate\"\
    - [ ] Definir el conjunto de características que incluirá la suscripción \"Vorpal Ultimate\": acceso a todas las funciones de Player Plus, GM Pro, Worldforge Pro y el nuevo Vorpal VTT.\
    - [ ] Implementar la lógica de permisos en el backend y frontend para este nuevo nivel de suscripción.\
    \
    ### La Estrategia de Precios y Actualización\
    - [ ] Realizar un análisis de mercado para establecer un precio competitivo para \"Vorpal Ultimate\".\
    - [ ] Diseñar y desarrollar un flujo de actualización sencillo para los suscriptores existentes, aplicando descuentos prorrateados.\
    - [ ] Comunicar claramente la nueva estructura de precios y las ventajas de la actualización.\
    \
    ## Capítulo 23: El Segundo Gran Lanzamiento - La Plataforma Unificada Vorpal\
    **Objetivo Estratégico:** Ejecutar una campaña a gran escala para anunciar la transformación de Vorpal en una plataforma de juego online completa.\
    \
    ### La Estrategia de Posicionamiento en el Mercado\
    - [ ] Redactar el nuevo mensaje de marketing central: \"Vorpal: La plataforma de rol más integrada del mundo\".\
    - [ ] Crear una nueva página de inicio para el sitio web que comunique esta propuesta de valor de forma clara y visual.\
    \
    ### La Campaña de Lanzamiento\
    - [ ] Producir videos de demostración de alta calidad que muestren el flujo de trabajo integrado desde Worldforge hasta el VTT.\
    - [ ] Colaborar con influencers de TTRPG para que muestren la plataforma unificada en sus canales.\
    - [ ] Planificar y ejecutar una campaña de promociones de lanzamiento para incentivar la adopción de la suscripción \"Ultimate\".\
    \
    # Época V: Inteligencia y Dominancia del Mercado\
    \
    ### Operaciones de la Pista Cero:\
     La Pista Cero es ahora un Equipo de Negocio Completo, con roles definidos para marketing, operaciones, finanzas y estrategia, asegurando la dominancia del mercado a largo plazo.\
    \
    ### Ritual de Época V: El Bucle de Inteligencia Competitiva\
    - [ ] Ejecutar un \"sprint cero\" de análisis de IA antes de la inversión en desarrollo.\
    - [ ] Realizar una evaluación comparativa técnica y de costes de las APIs de IA de OpenAI, Anthropic, Google y modelos open-source relevantes.\
    - [ ] Investigar y documentar el sentimiento de la comunidad TTRPG sobre el uso de IA, identificando preocupaciones éticas clave.\
    - [ ] Analizar los datos de uso del \"Generador de Nombres de PNJ\" experimental para validar la demanda de herramientas de IA más avanzadas.\
    - [ ] Crear una hoja de ruta para el desarrollo de IA que priorice las herramientas más solicitadas y aborde proactivamente las preocupaciones éticas.\
    \
    ## Capítulo 24: La Infraestructura de la Inteligencia - El Núcleo Neuronal de Vorpal\
    **Objetivo Estratégico:** Construir la base técnica, ética y económica para la integración de la IA a gran escala.\
    \
    ### 24.4 El Andamiaje Legal y Ético de la IA\
    - [ ] Redactar y publicar una \"Política de Uso Aceptable de la IA\" que prohíba la generación de contenido dañino o ilegal.\
    - [ ] Redactar y publicar una \"Política de Datos de IA\" transparente, explicando que se usan datos anónimos y agregados para mejorar los modelos y permitiendo un opt-out.\
    - [ ] Implementar mecanismos para que los usuarios acepten estas políticas antes de usar las funciones de IA.\
    \
    ### La Arquitectura de APIs de IA\
    - [ ] Desarrollar un servicio de \"gateway\" de IA interno en el backend.\
    - [ ] Este gateway debe abstraer las llamadas a los proveedores de IA, permitiendo cambiar de modelo con una configuración en lugar de reescribir código.\
    - [ ] Implementar la lógica para dirigir diferentes tipos de solicitudes (texto, imagen) al modelo más adecuado.\
    \
    ### El Modelo Económico de \"Tokens\"\
    - [ ] Integrar un sistema de contabilidad en el gateway de IA para rastrear el coste (en tokens o créditos) de cada llamada a la API por usuario.\
    - [ ] Diseñar y crear la tabla en la base de datos para almacenar el saldo de \"créditos de IA\" de cada usuario.\
    - [ ] Implementar la lógica de monetización: una asignación mensual de créditos para suscriptores y la opción de comprar paquetes de créditos adicionales.\
    \
    ### La Política de Datos y Ética\
    - [ ] Implementar filtros de contenido automáticos en el gateway de IA para prevenir la generación de material inapropiado.\
    - [ ] Establecer un pipeline de datos que anonimice y agregue las interacciones de los usuarios con la IA para fines de mejora del modelo, en cumplimiento con la política de datos.\
    \
    ## Capítulo 25: Pista de Worldforge (v3.0) - El Socio Creativo (\"Motor Génesis\")\
    **Objetivo Estratégico:** Transformar Worldforge de una herramienta de documentación a un socio de brainstorming activo.\
    \
    ### La Implementación del Diálogo Creativo\
    - [ ] Desarrollar una interfaz de chat en Worldforge que se comunique con el gateway de IA.\
    - [ ] Implementar un parser que pueda interpretar las respuestas estructuradas de la IA y utilizarlas para rellenar automáticamente nuevas fichas de Worldforge (PNJs, localizaciones).\
    \
    ### La Generación de Contenido Aumentado\
    - [ ] Añadir botones de \"sugerir detalles\" o \"expandir\" en los campos de las fichas de Worldforge.\
    - [ ] Al hacer clic, la aplicación enviará el contexto de la ficha a la IA y rellenará el campo con la sugerencia generada.\
    \
    ### El Taller del Artista Conceptual\
    - [ ] Integrar una API de generación de imágenes en el gateway de IA.\
    - [ ] Desarrollar una interfaz en Worldforge que permita a los usuarios escribir un prompt y generar arte conceptual para sus mundos, personajes y lugares.\
    \
    ## Capítulo 26: Pista del GM (v3.0) - El Asistente de Improvisación (\"Motor de Improvisación\")\
    **Objetivo Estratégico:** Otorgar al GM \"superpoderes\" de improvisación durante las partidas en vivo.\
    \
    ### El Generador de Entidades en Tiempo Real\
    - [ ] Crear una herramienta en la interfaz de Vorpal GM (y VTT) que permita al GM introducir un prompt simple (e.g., \"orco chamán con un solo ojo\").\
    - [ ] La herramienta llamará a la IA para generar una ficha completa de PNJ o monstruo, incluyendo estadísticas y descripción, y la añadirá al Códice de Campaña.\
    \
    ### El \"Pincel\" Narrativo\
    - [ ] Implementar botones de acceso rápido en el VTT para generar descripciones dinámicas (e.g., \"Describir esta taberna\", \"Describir el tiempo que hace\").\
    - [ ] La IA utilizará el contexto de la campaña para generar texto descriptivo que el GM pueda leer o adaptar.\
    \
    ## Capítulo 27: Pista del Jugador (v4.0) - El Aumento de la Inmersión (\"Motor de Persona\")\
    **Objetivo Estratégico:** Utilizar la IA para ayudar a los jugadores a conectarse más profundamente con sus personajes.\
    \
    ### El Taller del Personaje\
    - [ ] Desarrollar un asistente de creación de personajes que utilice la IA para ayudar a los jugadores a generar ideas de trasfondo, personalidad y motivaciones basadas en su clase y raza.\
    - [ ] Implementar una función que genere una \"voz de personaje\" (ejemplos de cómo hablaría) basada en sus rasgos.\
    \
    ### El Sugeridor de Acciones\
    - [ ] Añadir un botón opcional \"Sugerir acción\" a la interfaz del jugador.\
    - [ ] Al activarlo, la IA analizará la situación actual del juego y los rasgos del personaje para ofrecer 2-3 posibles líneas de acción o diálogo, ayudando a superar el bloqueo del jugador.\
    \
    ## Capítulo 28: La Convergencia Definitiva - El VTT Aumentado por IA\
    **Objetivo Estratégico:** Unificar todas las herramientas de IA en la experiencia de juego en vivo.\
    \
    ### La Interfaz de IA Unificada\
    - [ ] Diseñar y desarrollar un panel de control de IA para el GM dentro del VTT.\
    - [ ] Este panel debe dar acceso rápido a todas las herramientas del \"Motor de Improvisación\" y \"Génesis\" sin necesidad de salir de la interfaz del VTT.\
    \
    ### La Sinergia de los Motores\
    - [ ] Implementar el flujo de trabajo completo: GM genera un PNJ con el \"Motor Génesis\" -> lo personaliza -> con un clic, genera un token de imagen para él con el \"Taller del Artista\" -> lo arrastra al VTT, donde ya está vinculado a su ficha.\
    - [ ] Crear un video de demostración de este flujo para usarlo en marketing.\
    \
    ### 28.3 El Onboarding para la IA (\"El Viaje del Creador Aumentado\")\
    - [ ] Desarrollar una serie de tutoriales interactivos para las nuevas funciones de IA.\
    - [ ] Los tutoriales deben enseñar no solo el \"cómo\" (hacer clic en el botón), sino también el \"por qué\" (mejores prácticas de \"prompt engineering\" para obtener mejores resultados).\
    \
    ## Capítulo 29: La Frontera Final - \"The Oracle Engine\" y el Ecosistema Auto-mejorado\
    **Objetivo Estratégico:** Abrir un mercado de juego en solitario y establecer una plataforma que aprende y mejora por sí misma.\
    \
    ### El Desarrollo del \"Oracle Engine\"\
    - [ ] Desarrollar una nueva capa de IA entrenada para actuar como GM.\
    - [ ] Implementar la lógica para que el Oracle Engine pueda dirigir aventuras pre-hechas del mercado, presentando la narrativa, controlando los PNJs y respondiendo a las acciones del jugador.\
    - [ ] Crear la interfaz para el juego en solitario, integrando el Oracle Engine con Vorpal Player y el VTT.\
    \
    ### El Bucle de Retroalimentación de IA\
    - [ ] Diseñar y construir la arquitectura para un sistema de auto-mejora.\
    - [ ] El sistema recopilará datos anónimos y agregados sobre las partidas (e.g., qué encuentros resultaron en TPK, qué ganchos de trama fueron más seguidos).\
    - [ ] Utilizar estos datos para realizar un ajuste fino (fine-tuning) periódico de los modelos de IA de Vorpal, mejorando su calidad y equilibrio con el tiempo.\
    \
    ### 29.3 La Gobernanza de la Comunidad y la IA\
    - [ ] Establecer formalmente un \"Consejo Comunitario de IA\".\
    - [ ] Invitar a los creadores de nivel \"Leyenda\" y a los GMs más veteranos a formar parte de él.\
    - [ ] Crear un foro privado para el consejo y organizar reuniones trimestrales para discutir la hoja de ruta ética y funcional de las herramientas de IA, asegurando que el desarrollo permanezca alineado con los valores de la comunidad.",
    "generatedAt": "2025-11-09T16:19:44.801-05:00"
  },
  {
    "output": "Of course. As an expert Project Management Assistant and technical writer, I will now generate the comprehensive Action Plan and Development Checklist for the Vorpal software project. All content is derived exclusively from the provided document, expanding each chapter's action points into a granular, step-by-step guide for the Project Director.\
    \
    # Vorpal: Action Plan and Development Checklist\
    \
    ## Época I: Fundación y Validación\
    \
    ### Operaciones de la Pista Cero:\
     Paralelamente al desarrollo del MVP, las operaciones de negocio se centrarán en Marketing Orgánico Fundacional. Esto incluye la creación de perfiles en redes sociales clave, la participación en comunidades de TTRPG para construir reputación (sin vender) y la gestión directa del feedback como el 'equipo de soporte' fundador.\
    \
    ---\
    \
    ### **Capítulo 1: La Fundación Técnica y Metodológica**\
    **Objetivo Estratégico:** Establecer un entorno de desarrollo profesional y un flujo de trabajo claro que garantice la escalabilidad y la eficiencia desde el primer día.\
    \
    #### **El Taller Local: Configuración del Entorno**\
    - [ ] Install Visual Studio Code on the Lenovo G50 development machine.\
    - [ ] Configure VS Code with essential extensions for web development (e.g., Prettier, ESLint, Live Server).\
    - [ ] Initialize the project folder structure for the Vanilla Stack: `index.html`, `css/style.css`, `js/main.js`.\
    - [ ] Create and configure `.eslintrc.json` and `.prettierrc` files to enforce consistent code style and quality from the first line of code.\
    \
    #### **1.4 La Doctrina del Presupuesto de Rendimiento y Accesibilidad**\
    - [ ] Document the official Performance and Accessibility Budget in the project's `README.md`.\
    - [ ] Establish a protocol to run Google Lighthouse audits before every major feature merge, using the Lenovo G50 on a throttled 3G connection as the benchmark environment.\
    - [ ] Implement immediate visual feedback (e.g., loading states, button disabled states) for every user interaction to comply with the <100ms response time rule.\
    \
    #### **El Puente a la Nube: Git y Despliegue Inicial**\
    - [ ] Initialize a local Git repository in the project folder (`git init`).\
    - [ ] Create a new public repository on GitHub named `vorpal-player`.\
    - [ ] Create a comprehensive `.gitignore` file to exclude unnecessary files (e.g., OS-specific files, local configuration).\
    - [ ] Link the local repository to the remote GitHub repository.\
    - [ ] Configure the repository's settings to enable GitHub Pages, deploying from the `main` branch.\
    - [ ] Perform the initial commit of the boilerplate project and push to GitHub.\
    - [ ] Verify that the initial `index.html` is successfully deployed and accessible via its GitHub Pages URL.\
    \
    #### **Nuestra Metodología: Flujo de Trabajo y Roles**\
    - [ ] Create a `METHODOLOGY.md` file in the root of the repository.\
    - [ ] Formally define the role and responsibilities of the \"Director de Producto/Desarrollador IA\" within `METHODOLOGY.md`.\
    - [ ] Document the \"Sprint de desarrollo basado en prompts\" cycle, specifying its duration, key ceremonies (e.g., weekly planning, daily sync), and task management process using GitHub Issues.\
    \
    ### **Capítulo 2: El Prototipo Funcional - El Núcleo de Vorpal Player**\
    **Objetivo Estratégico:** Construir la primera versión funcional e interactiva del producto, enfocándose en la experiencia del usuario final sin la complejidad de la persistencia de datos.\
    \
    #### **La Arquitectura Visual (HTML/CSS)**\
    - [ ] Develop the semantic HTML structure for the main application interface, including containers for character stats, inventory, and notes.\
    - [ ] Implement a responsive CSS layout using modern techniques (Flexbox/Grid) to ensure usability on desktop and mobile devices.\
    - [ ] Style all core UI elements (buttons, inputs, text areas) to establish the initial visual identity of Vorpal.\
    \
    #### **La Lógica de Interacción (JavaScript)**\
    - [ ] Implement JavaScript functions to dynamically create new content blocks (e.g., a new skill, a new inventory item) in the DOM.\
    - [ ] Implement JavaScript functions to delete content blocks from the DOM.\
    - [ ] Implement drag-and-drop functionality to allow users to visually reorganize content blocks on their character sheet.\
    - [ ] Ensure all DOM manipulations are efficient to maintain adherence to the performance budget.\
    \
    ### **Capítulo 3: La Implementación de la \"Memoria\" - Persistencia de Datos**\
    **Objetivo Estratégico:** Transformar el prototipo en una herramienta útil, asegurando que el trabajo del usuario se guarde y se restaure de manera fiable.\
    \
    #### **3.1 El Diseño del Esquema de Datos v1.0 (Principio de Escalabilidad)**\
    - [ ] Design the primary JSON object structure for a character sheet in a separate design document (`SCHEMA.md`).\
    - [ ] Assign a field for a unique ID (UUID) to every primary entity (character, block, item, skill) within the JSON schema.\
    - [ ] Structure the schema to anticipate future relationships (e.g., `campaignId`, `gmId`), even if they will be null in v1.0, to facilitate future migration.\
    \
    #### **El Modelo de Datos y el Motor de Guardado/Carga**\
    - [ ] Implement a JavaScript module to manage the application's state, representing the character sheet based on the defined JSON schema.\
    - [ ] Develop a `saveState()` function that serializes the current application state object into a JSON string and saves it to the browser's `localStorage`.\
    - [ ] Develop a `loadState()` function that retrieves the JSON string from `localStorage`, parses it, and repopulates the application's state and UI on page load.\
    - [ ] Implement an auto-save mechanism that triggers the `saveState()` function on any significant data change.\
    \
    #### **3.3 El Diseño del Esquema de Datos para Eventos y Logros**\
    - [ ] Within `SCHEMA.md`, design a simple, generic JSON structure for tracking anonymous user events (e.g., `{ event: 'character_created', timestamp: '...' }`).\
    - [ ] Document this event schema, noting it is for future implementation of the gamification system and will not be implemented in Época I.\
    \
    ### **Capítulo 4: El Producto Mínimo Viable (MVP) - Finalización y Pulido**\
    **Objetivo Estratégico:** Completar el conjunto de características del MVP y realizar una fase de pruebas internas para asegurar un lanzamiento de calidad.\
    \
    #### **Las Funciones de Portabilidad**\
    - [ ] Implement an \"Export Character\" button that serializes the current character state into a JSON string and triggers a browser download of a `.json` file.\
    - [ ] Implement an \"Import Character\" button that opens a file picker, reads a selected `.json` file, validates its structure, and loads it into the application state.\
    \
    #### **La Fase de Alpha Interna**\
    - [ ] Create a test plan checklist in a new `TESTING.md` file, covering all core functionalities.\
    - [ ] Execute the test plan with the founding team (you and your girlfriend), documenting every bug or UI/UX issue as a GitHub Issue.\
    - [ ] Prioritize and resolve all critical bugs identified during the alpha phase.\
    - [ ] Refine UI/UX based on feedback to ensure the application is intuitive before public release.\
    \
    ### **Capítulo 5: El Lanzamiento Público y la Creación de la Comunidad**\
    **Objetivo Estratégico:** Lanzar el MVP al mundo, atraer a los primeros usuarios (\"early adopters\") y establecer los canales y procesos para convertir su feedback en la hoja de ruta del futuro.\
    \
    #### **La Estrategia de Lanzamiento**\
    - [ ] Draft the launch announcement message, focusing on the mission of Vorpal (potenciating creativity, eliminating friction).\
    - [ ] Identify and select primary channels for the \"soft launch\" (e.g., specific subreddits, TTRPG forums).\
    - [ ] Execute the launch by posting the announcement on the selected channels.\
    \
    #### **La Infraestructura Comunitaria**\
    - [ ] Create the official Vorpal Discord server.\
    - [ ] Structure the Discord server with clear channels: `#announcements`, `#general`, `#bug-reports`, `#suggestions`, and `#showcase`.\
    \
    #### **El Bucle de Feedback**\
    - [ ] Establish a formal process for converting posts in `#bug-reports` and `#suggestions` into structured GitHub Issues.\
    - [ ] Create a template for responding to user feedback to ensure they feel heard and valued.\
    - [ ] Schedule and communicate a regular update cadence (e.g., weekly devlog in `#announcements`) to inform the community of progress.\
    \
    #### **5.4 El Lanzamiento de la \"Galería de Creaciones\" (Cultura del Creador)**\
    - [ ] Rename the `#showcase` channel to `#galeria-de-creaciones`.\
    - [ ] Post a pinned message in the channel actively encouraging users to share their exported `.json` character templates.\
    - [ ] Actively monitor this channel to identify potential \"Pioneer\" creators for future programs.\
    \
    #### **5.5 La Implementación del Andamiaje Legal Básico**\
    - [ ] Draft a basic Privacy Policy document, explaining that all data is stored locally in the browser.\
    - [ ] Draft a basic Terms of Service document from a standard template.\
    - [ ] Add links to both the Privacy Policy and Terms of Service in the application's footer.\
    \
    #### **5.6 La Introducción del Concepto de Gamificación**\
    - [ ] Incorporate the long-term vision of \"La Senda del Cronista\" into the launch messaging and community welcome messages.\
    - [ ] Create a discussion thread or channel to begin gathering community ideas about potential achievements and rewards.\
    \
    #### **Estrategia de Construcción de Marca**\
    - [ ] Ensure all public communication consistently reinforces the core mission of Vorpal.\
    - [ ] Engage actively and positively with every community member in Discord to build a reputation for being responsive and user-focused.\
    \
    ## Época II: Comercialización y Conexión\
    \
    ### Operaciones de la Pista Cero:\
     Con el lanzamiento comercial, la Pista Cero evoluciona a Crecimiento y Soporte Inicial. Esto implica establecer un sistema de tickets de soporte básico (puede ser un canal de Discord o un email), empezar a crear contenido de valor (posts de blog, tutoriales en video) y analizar las primeras métricas de conversión.\
    \
    ---\
    \
    ### **Ritual de Época II: El Bucle de Inteligencia Competitiva**\
    - [ ] Analyze all community feedback from Época I to create a ranked list of the most and least valued features of the MVP.\
    - [ ] Research the pricing pages and feature tiers of at least 3 successful freemium productivity tools (both within and outside the TTRPG space).\
    - [ ] Identify the top 5-10 most active and constructive members of the Discord community as candidates for the Closed Beta.\
    - [ ] Synthesize all findings into a design document that will guide the feature set and pricing for \"Plus\" and \"Pro\" subscriptions.\
    \
    ### **Capítulo 6: La Infraestructura Técnica del Negocio**\
    **Objetivo Estratégico:** Construir la columna vertebral técnica que soportará las cuentas de usuario, los datos en la nube y las transacciones financieras.\
    \
    #### **La Transición a la Nube**\
    - [ ] Evaluate and select a Backend as a Service (BaaS) provider (Firebase or Supabase).\
    - [ ] Set up the BaaS project, including development and production environments.\
    - [ ] Design and implement the database schema for `users` (linking to auth ID) and `characters` (linking to a `userId`).\
    - [ ] Integrate the BaaS SDK into the Vorpal codebase.\
    \
    #### **El Sistema de Autenticación**\
    - [ ] Implement the UI components for user registration, login, and password reset.\
    - [ ] Integrate the BaaS authentication service to handle user creation and session management.\
    - [ ] Implement logic to show/hide UI elements based on the user's authentication state.\
    - [ ] Refactor the data persistence logic to save/load character data from the cloud for authenticated users, while retaining `localStorage` functionality for anonymous users.\
    \
    #### **La Integración de la Pasarela de Pagos**\
    - [ ] Create a Stripe developer account and configure API keys.\
    - [ ] Define the subscription products (\"Vorpal Plus\", \"GM Pro\") in the Stripe dashboard.\
    - [ ] Implement a serverless backend function (e.g., Cloud Function) to handle Stripe webhook events (`invoice.payment_succeeded`, `customer.subscription.deleted`, etc.).\
    - [ ] Implement the front-end interface for users to select a plan and complete the checkout process using Stripe.js.\
    - [ ] Implement logic in the backend webhook to update a user's subscription status in the application database.\
    \
    #### **6.4 La Integración de Analítica de Privacidad**\
    - [ ] Select and integrate a privacy-focused analytics tool (e.g., Plausible, Fathom).\
    - [ ] Implement anonymous event tracking for key user interactions (e.g., `feature_used_X`, `subscription_page_viewed`).\
    - [ ] Create a dashboard to monitor key metrics without collecting any Personally Identifiable Information (PII).\
    \
    #### **6.5 La Construcción del Motor de Gamificación v1.0**\
    - [ ] Design the database schema for the gamification system: a `user_achievements` table/collection to link `userId` with `achievementId`.\
    - [ ] Create a service (e.g., a set of serverless functions) to process incoming user events against a predefined set of achievement rules.\
    - [ ] Develop an API endpoint for the client application to query and retrieve a user's unlocked achievements and corresponding rewards.\
    \
    ### **Capítulo 7: Pista del Jugador (v2.0) - El Producto Mínimo Suscribible**\
    **Objetivo Estratégico:** Crear la primera oferta de pago para nuestra base de usuarios más grande, probando su disposición a pagar por conveniencia y personalización.\
    \
    #### **El Desarrollo de \"Vorpal Plus\"**\
    - [ ] Implement the cloud synchronization feature for character sheets.\
    - [ ] Develop the UI for a library of visual themes and dice skins.\
    - [ ] Implement the advanced character chronicle feature, logging significant events or changes to the character sheet.\
    \
    #### **La Arquitectura de Permisos**\
    - [ ] Develop a client-side function `hasActiveSubscription('plus')` that checks the user's status from the database.\
    - [ ] Wrap all \"Vorpal Plus\" features in conditional logic that checks for an active subscription before rendering or enabling them.\
    - [ ] Implement UI \"upsells\" that prompt free users to subscribe when they attempt to access a premium feature.\
    \
    #### **7.3 La Introducción de Ganchos de Compromiso**\
    - [ ] Implement the first set of simple achievements for all users (e.g., 'First Character Created', 'Used Vorpal for 7 days').\
    - [ ] Develop a basic UI element to notify users when they have unlocked an achievement.\
    \
    #### **7.4 La Activación de 'La Senda del Aventurero' (Fase 1)**\
    - [ ] Define the rules for the first 10 player-focused achievements in the gamification backend.\
    - [ ] Develop the UI in Vorpal Player for an \"Achievements\" page, showing locked/unlocked achievements and their rewards.\
    - [ ] Implement the logic to automatically apply unlocked cosmetic rewards (themes, dice skins) to the user's account.\
    \
    ### **Capítulo 8: Pista del GM (v1.0) - El Producto Mínimo Vendible**\
    **Objetivo Estratégico:** Construir y definir la oferta principal que será nuestro motor de ingresos recurrente, resolviendo los problemas más agudos del Director de Juego.\
    \
    #### **El Desarrollo de \"GM Pro\"**\
    - [ ] Develop a new application view for the \"GM Dashboard\" to manage multiple campaigns and players.\
    - [ ] Implement the \"Campaign Codex\" feature, allowing GMs to create and organize unlimited campaign notes, NPCs, and locations in the cloud.\
    - [ ] Build the session preparation tools, such as encounter builders and loot generators.\
    \
    #### **8.4 La Primera Integración de IA Experimental**\
    - [ ] Select and obtain an API key for a lightweight, low-cost AI language model.\
    - [ ] Implement a simple \"NPC Name Generator\" button within the Campaign Codex.\
    - [ ] Develop the backend function to call the AI API and return a list of names to the GM's interface.\
    - [ ] Track usage of this feature with the anonymous analytics tool to measure community interest.\
    \
    #### **8.5 La Activación de 'La Senda del Guardián' (Fase 1)**\
    - [ ] Define the rules for the first set of GM-focused achievements (e.g., 'Ran First Session', 'Created 10 NPCs') in the gamification backend.\
    - [ ] Develop the UI in the GM Dashboard to display these achievements.\
    - [ ] Implement a system of unlockable \"Titles\" and \"Emblems\" that are displayed on the GM's public-facing community profile.\
    \
    ### **Capítulo 9: El Puente Conector - La Sinergia en Tiempo Real**\
    **Objetivo Estratégico:** Desarrollar la \"magia\" tecnológica que conecta a jugadores y GMs, creando una propuesta de valor única.\
    \
    #### **La Arquitectura de Datos en Tiempo Real**\
    - [ ] Redesign the database schema to support many-to-many relationships between `campaigns`, `gms`, and `players`.\
    - [ ] Structure the data to allow a GM to have read/write permissions over specific parts of their players' character sheets (e.g., HP, status effects).\
    - [ ] Implement security rules in the BaaS to ensure users can only access data they are explicitly permitted to.\
    \
    #### **La Implementación de \"Listeners\"**\
    - [ ] Refactor the application's data-fetching logic to use real-time listeners (e.g., Firestore's `onSnapshot`, Supabase's Realtime) instead of one-time queries.\
    - [ ] Ensure that any change made by the GM to a player's sheet is instantly reflected on the player's screen, and vice-versa.\
    - [ ] Optimize the listeners to minimize data transfer and client-side processing.\
    \
    ### **Capítulo 10: La Prueba de Fuego - La Fase Beta Cerrada**\
    **Objetivo Estratégico:** Probar la estabilidad de la nueva infraestructura conectada y validar la percepción de valor de nuestras ofertas de pago.\
    \
    #### **La Estrategia de la Beta**\
    - [ ] Contact the pre-selected community champions and invite them to the Closed Beta.\
    - [ ] Create a private Discord channel exclusively for beta testers.\
    - [ ] Provide beta testers with free access to \"Vorpal Plus\" and \"GM Pro\" for the duration of the test.\
    \
    #### **El Bucle de Iteración de la Beta**\
    - [ ] Create and distribute a structured feedback form for testers covering usability, bugs, perceived value, and pricing suggestions.\
    - [ ] Schedule weekly sync-up calls with the beta group to discuss findings.\
    - [ ] Create and prioritize GitHub issues based on beta feedback.\
    - [ ] Iterate on the feature set and refine the pricing model based on the collected data before the public launch.\
    \
    ### **Capítulo 11: La Apertura de Puertas - El Lanzamiento Público de la Plataforma Comercial**\
    **Objetivo Estratégico:** Lanzar oficialmente las suscripciones \"Vorpal Plus\" y \"GM Pro\" a toda la base de usuarios.\
    \
    #### **La Estrategia de Comunicación del Lanzamiento**\
    - [ ] Draft a launch announcement that clearly explains the new paid features while reassuring users about the value and continued support of the free tier.\
    - [ ] Prepare a comprehensive FAQ addressing questions about subscriptions, data, and the future of the platform.\
    - [ ] Post the announcement across all channels (Discord, social media, blog).\
    \
    #### **El Proceso de \"Onboarding\" para Clientes**\
    - [ ] Design and implement a smooth, multi-step UI flow for purchasing and activating a subscription.\
    - [ ] Create a user-friendly \"Account Management\" page where users can view their subscription status, update payment methods, and cancel.\
    \
    #### **11.3 La Creación del \"Viaje del GM\" (Onboarding)**\
    - [ ] Develop a series of interactive, contextual tooltips that appear the first time a new \"GM Pro\" subscriber uses a key feature.\
    - [ ] Create a \"Welcome to GM Pro\" guide that walks the user through connecting their first player and using the Campaign Codex.\
    \
    ## Época III: Expansión y Creación del Ecosistema\
    \
    ### Operaciones de la Pista Cero:\
     Con la expansión del ecosistema, la Pista Cero se enfoca en Escala Comunitaria y Desarrollo de Negocio. Aquí se ejecuta el plan de la primera contratación (Community Manager) y se comienzan a explorar alianzas estratégicas (con influencers, otros creadores de herramientas, etc.).\
    \
    ---\
    \
    ### **Ritual de Época III: El Bucle de Inteligencia Competitiva**\
    - [ ] Conduct a competitive analysis of World Anvil, LegendKeeper, and other world-building tools, identifying their key strengths and user-reported weaknesses.\
    - [ ] Analyze the business models of content marketplaces like DriveThruRPG and DMsGuild, focusing on commission structures, content curation, and creator promotion.\
    - [ ] Review the content shared in the `#galeria-de-creaciones` channel to identify the most popular types of homebrew content, which will inform the prioritization of Worldforge \"Ficha\" types.\
    - [ ] Compile these findings into a Product Requirements Document for Worldforge and the Marketplace.\
    \
    ### **Capítulo 12: Pista de Worldforge (v1.0) - La Construcción de la Forja Creativa**\
    **Objetivo Estratégico:** Construir el pilar tecnológico que permitirá la creación de contenido estructurado y de alta calidad.\
    \
    #### **La Arquitectura de \"Fichas\"**\
    - [ ] Design a flexible, NoSQL-friendly database schema for modular content \"Fichas\" (e.g., Faction, City, Magic System).\
    - [ ] Develop a dynamic UI that can render forms and views based on a selected \"Ficha\" template.\
    - [ ] Implement the core create, read, update, and delete (CRUD) functionality for these Fichas.\
    \
    #### **El Modelo de Monetización Nativo**\
    - [ ] Implement a feature flag system to limit the number of Fichas a free user can create.\
    - [ ] Develop the e-commerce logic for one-time purchases of \"Paquetes de Fichas\".\
    - [ ] Create a new \"Worldforge Pro\" subscription tier in Stripe and the application backend, unlocking unlimited Ficha creation.\
    \
    ### **Capítulo 13: La Infraestructura del Mercado - La Construcción de la Economía**\
    **Objetivo Estratégico:** Desarrollar la infraestructura de e-commerce que permitirá a los creadores vender sus creaciones.\
    \
    #### **13.1 El Andamiaje Legal del Mercado**\
    - [ ] Draft the \"Creator Terms of Service\" document, clearly outlining intellectual property rights, content policies, and commission structures.\
    - [ ] Integrate a mandatory acceptance checkbox for these terms into the creator onboarding flow.\
    \
    #### **El Portal del Creador**\
    - [ ] Design and build a \"Creator Dashboard\" UI.\
    - [ ] Implement functionality for creators to upload content packages, add product descriptions and images, and set pricing.\
    - [ ] Develop a view for creators to see their sales data and earning statements.\
    \
    #### **El Sistema de Transacciones y Comisiones**\
    - [ ] Integrate Stripe Connect to handle payouts to creators.\
    - [ ] Develop a backend process that, upon a successful purchase, automatically calculates and allocates Vorpal's commission and the creator's share.\
    - [ ] Implement the logic for the tiered commission rates of \"La Senda del Creador\".\
    \
    #### **El Escaparate Público**\
    - [ ] Design and build the public-facing Marketplace UI, including category browsing, search functionality, and product detail pages.\
    - [ ] Implement a user rating and review system for marketplace products.\
    \
    #### **13.4 La Integración del Motor de Gamificación en el Mercado**\
    - [ ] Extend the gamification engine to include creator-specific achievements (e.g., 'First Sale', '100 Sales', 'Published 5 Products').\
    - [ ] Integrate creator levels ('Aspirante', 'Maestro') as achievements that are publicly displayed as badges on their profile and product pages.\
    \
    ### **Capítulo 14: El Programa de Pioneros - Sembrando el Ecosistema**\
    **Objetivo Estratégico:** Resolver el problema del \"mercado vacío\" al lanzar, asegurando un catálogo de contenido de alta calidad desde el primer día.\
    \
    #### **La Estrategia de Reclutamiento**\
    - [ ] Create a list of top candidates for the \"Pioneer Program\" from the most active creators in the Discord community.\
    - [ ] Draft a formal invitation outlining the program's benefits.\
    - [ ] Contact the selected candidates personally to invite them.\
    \
    #### **El Paquete de Incentivos**\
    - [ ] Implement the technical infrastructure to grant \"Pioneer\" accounts early access to Worldforge tools.\
    - [ ] Configure a 0% commission rate for all sales made by Pioneer accounts during the launch period.\
    - [ ] Design a \"Featured Pioneer\" section on the Marketplace homepage.\
    \
    #### **El Bucle de Feedback del Creador**\
    - [ ] Create a private Discord channel for the Pioneer Program members.\
    - [ ] Establish a direct line of communication for technical support and feedback on the Worldforge and Marketplace tools.\
    \
    #### **14.4 La Doctrina de la Simplicidad en las Herramientas del Creador**\
    - [ ] During feedback sessions with Pioneers, explicitly ask: \"Does this feature make it easier to publish high-quality content, or does it add unnecessary complexity?\"\
    - [ ] Ruthlessly prioritize development based on feedback that aligns with simplifying the creator workflow.\
    \
    ### **Capítulo 15: Pista del GM (v2.0) - La Integración del Ecosistema**\
    **Objetivo Estratégico:** Aumentar drásticamente el valor de la suscripción \"GM Pro\" al integrarla con el nuevo contenido del ecosistema.\
    \
    #### **La Pestaña del Mercado**\
    - [ ] Implement a new \"Marketplace\" tab within the Vorpal GM interface that displays a curated view of available products.\
    \
    #### **El Motor de Importación \"One-Click\"**\
    - [ ] Develop a function that, upon purchase, automatically parses a marketplace content package and imports its contents into the GM's Campaign Codex.\
    - [ ] Ensure the process is seamless and requires no manual data entry from the GM.\
    \
    #### **La Evolución del Códice**\
    - [ ] Refactor the Campaign Codex UI and data models to natively handle the complex, structured data imported from Worldforge (e.g., linked NPCs, location maps).\
    \
    ### **Capítulo 16: Pista del Jugador (v2.1) - El Beneficiario del Ecosistema**\
    **Objetivo Estratégico:** Asegurar que la evolución de la plataforma beneficie directamente a los jugadores.\
    \
    #### **La Integración del Mercado en Vorpal Player**\
    - [ ] Add a section in Vorpal Player for browsing and purchasing player-centric content from the Marketplace (e.g., character sheet templates, themes).\
    - [ ] Implement the \"one-click install\" functionality for these assets.\
    \
    #### **La Mejora de la Creación de Personajes**\
    - [ ] Develop the permission system that allows a GM to share specific content from their purchased \"world-kits\" (e.g., new spells, classes) with players in their campaign.\
    - [ ] Implement the UI for players to browse and import this GM-approved content directly into their character sheets.\
    \
    #### **16.3 La Planificación de la Transición de Fundadores a Equipo**\
    - [ ] Draft a detailed job description for a \"Community & Support Manager\" role.\
    - [ ] Create a formal \"Volunteer Moderator Program\" document, outlining roles, responsibilities, and rewards.\
    \
    ### **Capítulo 17: El Lanzamiento Público del Ecosistema Vorpal**\
    **Objetivo Estratégico:** Comunicar la transformación de Vorpal de una herramienta a una plataforma.\
    \
    #### **La Estrategia de Marketing de Expansión**\
    - [ ] Design and execute targeted ad campaigns aimed at new audiences like world-builders and TTRPG writers.\
    - [ ] Prepare marketing copy that highlights the benefits of Worldforge and the Marketplace.\
    \
    #### **El Evento de Lanzamiento**\
    - [ ] Plan and schedule a live-streamed launch event on platforms like Twitch or YouTube.\
    - [ ] Coordinate with \"Pioneer\" creators to showcase their content during the event.\
    \
    #### **17.3 La Implementación del Motor de Curación y Descubrimiento v1.0**\
    - [ ] Develop the backend tools for internal staff to tag products for the \"Selección Vorpal\" (Staff Picks) feature.\
    - [ ] Ensure creator tier badges ('Maestro', 'Leyenda') are prominently displayed on product cards and search results as a signal of quality.\
    \
    #### **Estrategia de Construcción de Marca**\
    - [ ] Create a content calendar for blog posts and videos focused on teaching creative skills (e.g., \"How to Design a Memorable Villain\").\
    - [ ] Produce and publish case studies or interviews highlighting the success stories of Pioneer creators on the platform.\
    \
    ### **Capítulo 17.5: El Ritual del Jardín Cuidado**\
    **Objetivo Estratégico:** Formalizar el proceso de revisión del producto para combatir el 'bloatware'.\
    \
    - [ ] Analyze usage data from the privacy-focused analytics tool to identify the least-used features in Vorpal Player and GM.\
    - [ ] For each identified feature, conduct a formal review to decide whether to improve its usability or deprecate and remove it entirely.\
    - [ ] Document the decisions and communicate any removals transparently to the community.\
    - [ ] Schedule this \"Product Pruning\" ritual in the project calendar to occur at the end of every future Época.\
    \
    ## Época IV: Unificación y Escala\
    \
    ### Operaciones de la Pista Cero:\
     Con la unificación, la Pista Cero se convierte en un Equipo de Crecimiento Formal. Se exploran canales de marketing de pago, se optimiza el embudo de ventas y se establecen KPIs (Indicadores Clave de Rendimiento) de negocio más robustos.\
    \
    ---\
    \
    ### **Ritual de Época IV: El Bucle de Inteligencia Competitiva**\
    - [ ] Scrape and analyze user reviews and forum posts for Roll20, Foundry VTT, and Fantasy Grounds to compile a list of the most common user complaints (performance, UI/UX, cost).\
    - [ ] Research and prototype with modern real-time communication technologies (WebSockets, WebRTC) to evaluate their suitability for a VTT.\
    - [ ] Survey existing \"GM Pro\" subscribers to gauge demand for a VTT and to rank their most-desired VTT features.\
    - [ ] Use these findings to create a VTT development roadmap focused on solving existing market pain points, not just replicating features.\
    \
    ### **Capítulo 18: La Infraestructura de la Unificación - La Re-arquitectura del Backend**\
    **Objetivo Estratégico:** Evolucionar la infraestructura para manejar interacciones complejas y multi-usuario en tiempo real.\
    \
    #### **Análisis de Tecnologías de Tiempo Real**\
    - [ ] Conduct a formal evaluation of WebSocket libraries and managed services to select the core technology for the VTT's real-time layer.\
    - [ ] Design the architecture for a more robust backend service capable of handling persistent connections from multiple clients in a game session.\
    \
    #### **El Modelo de Datos Unificado**\
    - [ ] Redesign the database schema to create a single, coherent data universe where a \"world,\" \"campaign,\" and \"characters\" are tightly linked views of the same underlying data.\
    - [ ] Ensure the new schema can efficiently support real-time queries for a VTT session (e.g., token positions, player cursors).\
    \
    #### **El Plan de Migración**\
    - [ ] Write and test scripts to migrate all existing user data from the old schema to the new unified model.\
    - [ ] Plan a maintenance window for the migration and a communication strategy to inform users of the scheduled downtime.\
    \
    #### **18.4 El Mandato de la Documentación Técnica**\
    - [ ] For every new backend service or major data model, create a corresponding technical documentation page in a shared knowledge base (e.g., Confluence, Notion, or a `docs/` folder in the repo).\
    - [ ] Make \"write the docs\" a required step in the definition of \"done\" for all backend development tasks.\
    \
    ### **Capítulo 19: Pista del VTT (v0.5) - El Tablero de Batalla Compartido (Prueba de Concepto)**\
    **Objetivo Estratégico:** Probar la nueva infraestructura de tiempo real con una funcionalidad de bajo riesgo.\
    \
    #### **El Desarrollo del \"Battlemap Helper\"**\
    - [ ] Implement a new view within \"GM Pro\" where a GM can upload an image file as a battlemap.\
    - [ ] Add functionality for the GM to overlay a square or hex grid on the map.\
    - [ ] Implement the real-time sharing mechanism so that connected players see the map and grid.\
    - [ ] Develop a simple \"ping\" tool that allows the GM to place temporary markers on the map, visible to all players in real-time.\
    \
    #### **La Medición del Rendimiento**\
    - [ ] Integrate performance monitoring tools (e.g., server load, message latency, client-side frame rate) into the \"Battlemap Helper\".\
    - [ ] Organize stress-test sessions with internal and beta users to identify and resolve performance bottlenecks under real-world load.\
    \
    ### **Capítulo 20: Pista del VTT (v1.0) - La Mesa Virtual Integrada**\
    **Objetivo Estratégico:** Construir y lanzar la primera versión completa de nuestro VTT, enfocada en la simplicidad y la velocidad.\
    \
    #### **20.3 La Aplicación de la Doctrina de la Simplicidad al VTT**\
    - [ ] Create an \"Anti-Features\" list document, explicitly stating complex features (e.g., dynamic lighting, advanced macros) that will NOT be included in v1.0.\
    - [ ] Establish a feature review process where every proposed VTT feature is strictly evaluated against the question: \"Does this eliminate more friction than it adds complexity?\"\
    \
    #### **El Desarrollo del Núcleo del VTT**\
    - [ ] Implement the full map and grid system with support for layers (e.g., GM-only layer, player layer).\
    - [ ] Develop the token system, allowing GMs to place tokens on the map that are directly linked to character or monster data from the Campaign Codex.\
    - [ ] Implement player control of assigned tokens.\
    - [ ] Build a shared, real-time dice roller with a visible log for all participants.\
    - [ ] Create basic VTT tools: measurement (ruler), and a persistent campaign chat log.\
    \
    #### **La Filosofía de la Interfaz**\
    - [ ] Design a clean, minimal VTT interface that prioritizes the map and minimizes UI chrome.\
    - [ ] Ensure all core functions are accessible with a minimum number of clicks, adhering to the project's foundational principle of eliminating friction.\
    \
    ### **Capítulo 21: La Convergencia del Ecosistema - La Evolución de los Pilares**\
    **Objetivo Estratégico:** Rediseñar los pilares existentes para que converjan con el VTT en una experiencia simbiótica.\
    \
    #### **Pista de Worldforge (v2.0) - El Taller del Cartógrafo**\
    - [ ] Implement a simple, tile-based map creator within Worldforge.\
    - [ ] Develop an asset manager for uploading and organizing VTT assets (tokens, map tiles, textures).\
    - [ ] Extend the Marketplace to support a new product category: \"VTT Asset Packs.\"\
    \
    #### **Pista del Jugador (v3.0) - La Interfaz del Aventurero**\
    - [ ] Develop a \"VTT View\" for the Vorpal Player character sheet, designed as a compact Heads-Up Display (HUD).\
    - [ ] Implement the ability for players to overlay this HUD on the VTT screen, allowing them to roll dice and track resources without switching tabs or windows.\
    \
    #### **21.3 La Evolución de 'La Senda del Cronista' (Gamificación Unificada)**\
    - [ ] Expand the gamification engine to support interconnected achievements.\
    - [ ] Implement rules for new achievements, such as a GM achievement for using a marketplace map in a VTT session.\
    - [ ] Implement an achievement for a creator when their monster asset is used for the first time in a VTT combat.\
    \
    ### **Capítulo 22: El Modelo de Negocio Unificado**\
    **Objetivo Estratégico:** Definir y estructurar la nueva oferta comercial que refleje el valor de la plataforma unificada.\
    \
    #### **La Creación de la Suscripción \"Vorpal Ultimate\"**\
    - [ ] Define a new \"Vorpal Ultimate\" subscription tier in Stripe and the backend that bundles all premium features: Player Plus, GM Pro, Worldforge Pro, and the Vorpal VTT.\
    - [ ] Update the application's permission system to recognize the new \"Ultimate\" tier.\
    \
    #### **La Estrategia de Precios y Actualización**\
    - [ ] Conduct a pricing analysis to determine a competitive yet profitable price point for the \"Ultimate\" tier.\
    - [ ] Design and implement a clear, prorated upgrade path for existing \"GM Pro\" and \"Worldforge Pro\" subscribers.\
    \
    ### **Capítulo 23: El Segundo Gran Lanzamiento - La Plataforma Unificada Vorpal**\
    **Objetivo Estratégico:** Ejecutar una campaña a gran escala para anunciar la transformación de Vorpal en una plataforma de juego online completa.\
    \
    #### **La Estrategia de Posicionamiento en el Mercado**\
    - [ ] Develop new marketing materials (website copy, ads, press releases) that consistently use the tagline: \"Vorpal: The world's most integrated roleplaying platform.\"\
    - [ ] Focus all messaging on the key differentiator: the seamless workflow from world-building to gameplay.\
    \
    #### **La Campaña de Lanzamiento**\
    - [ ] Produce high-quality video demonstrations of the complete, integrated workflow.\
    - [ ] Collaborate with TTRPG influencers for sponsored streams and reviews showcasing the unified platform.\
    - [ ] Plan and execute a launch-day promotion to incentivize new subscriptions and upgrades to the \"Ultimate\" tier.\
    \
    ## Época V: Inteligencia y Dominancia del Mercado\
    \
    ### Operaciones de la Pista Cero:\
     La Pista Cero es ahora un Equipo de Negocio Completo, con roles definidos para marketing, operaciones, finanzas y estrategia, asegurando la dominancia del mercado a largo plazo.\
    \
    ---\
    \
    ### **Ritual de Época V: El Bucle de Inteligencia Competitiva**\
    - [ ] Evaluate the cost, quality, and API policies of leading AI models (e.g., GPT series, Claude series, open-source alternatives) for both text and image generation.\
    - [ ] Analyze sentiment in the TTRPG community regarding AI in creative tools, identifying key ethical concerns and user desires.\
    - [ ] Review the usage data of the experimental \"NPC Name Generator\" to quantify user demand for more advanced AI features.\
    - [ ] Use these findings to create a strategic, ethical, and demand-driven roadmap for AI integration.\
    \
    ### **Capítulo 24: La Infraestructura de la Inteligencia - El Núcleo Neuronal de Vorpal**\
    **Objetivo Estratégico:** Construir la base técnica, ética y económica para la integración de la IA a gran escala.\
    \
    #### **24.4 El Andamiaje Legal y Ético de la IA**\
    - [ ] Draft and publish a clear \"AI Acceptable Use Policy\" and \"AI Data Policy.\"\
    - [ ] Ensure these policies transparently explain how anonymized data is used for model improvement and define the intellectual property rights of AI-generated content.\
    \
    #### **La Arquitectura de APIs de IA**\
    - [ ] Develop an internal \"AI Gateway\" service that acts as an abstraction layer between the Vorpal application and various third-party AI APIs.\
    - [ ] Design the gateway to allow for easy switching of AI providers or models with minimal code changes in the core application.\
    \
    #### **El Modelo Económico de \"Tokens\"**\
    - [ ] Implement a backend system to track the token consumption (cost) of every AI API call made by a user.\
    - [ ] Design a \"credit\" system for users, where subscriptions include a monthly allotment of AI credits, with options to purchase more.\
    \
    #### **La Política de Datos y Ética**\
    - [ ] Implement strict data anonymization processes for any data used to fine-tune models.\
    - [ ] Integrate content filters and safety mechanisms into the AI Gateway to prevent the generation of harmful or prohibited content.\
    \
    ### **Capítulo 25: Pista de Worldforge (v3.0) - El Socio Creativo (\"Motor Génesis\")**\
    **Objetivo Estratégico:** Transformar Worldforge de una herramienta de documentación a un socio de brainstorming activo.\
    \
    #### **La Implementación del Diálogo Creativo**\
    - [ ] Develop a chat-based UI within Worldforge that allows users to brainstorm ideas with an AI.\
    - [ ] Implement the logic to parse the AI's structured output and automatically populate new Worldforge Fichas (e.g., \"Create a faction of desert elves\" -> generates a Faction ficha).\
    \
    #### **La Generación de Contenido Aumentado**\
    - [ ] Add \"Generate Details\" buttons within specific fields of Worldforge Fichas.\
    - [ ] Implement contextual prompts that use the existing data in the ficha to generate relevant details (e.g., generate street names for a city ficha).\
    \
    #### **El Taller del Artista Conceptual**\
    - [ ] Integrate an image generation AI service via the AI Gateway.\
    - [ ] Develop a UI in Worldforge for users to write prompts and generate concept art for their worlds, characters, and locations.\
    \
    ### **Capítulo 26: Pista del GM (v3.0) - El Asistente de Improvisación (\"Motor de Improvisación\")**\
    **Objetivo Estratégico:** Otorgar al GM \"superpoderes\" de improvisación durante el juego.\
    \
    #### **El Generador de Entidades en Tiempo Real**\
    - [ ] Build a tool accessible from the VTT interface for the GM to generate a complete monster or NPC ficha (stats, description, abilities) with a single prompt.\
    - [ ] Ensure the generated ficha is immediately usable within the VTT and Campaign Codex.\
    \
    #### **El \"Pincel\" Narrativo**\
    - [ ] Implement quick-action buttons in the VTT for generating descriptive text for locations, environments, and sensory details (\"Describe a spooky forest\").\
    \
    ### **Capítulo 27: Pista del Jugador (v4.0) - El Aumento de la Inmersión (\"Motor de Persona\")**\
    **Objetivo Estratégico:** Utilizar la IA para ayudar a los jugadores a conectarse más profundamente con sus personajes.\
    \
    #### **El Taller del Personaje**\
    - [ ] Develop an AI-powered assistant in the character creation process that helps generate backstories, personality traits, and character voices based on user inputs.\
    \
    #### **El Sugeridor de Acciones**\
    - [ ] Implement an optional, player-controlled feature that analyzes the character's traits and the current game context to suggest potential actions or lines of dialogue.\
    \
    ### **Capítulo 28: La Convergencia Definitiva - El VTT Aumentado por IA**\
    **Objetivo Estratégico:** Unificar todas las herramientas de IA en la experiencia de juego en vivo.\
    \
    #### **La Interfaz de IA Unificada**\
    - [ ] Design and implement a single, consolidated AI panel within the VTT for the GM, providing access to all generation tools without leaving the game screen.\
    \
    #### **La Sinergia de los Motores**\
    - [ ] Create and refine the end-to-end workflow: a GM brainstorms an NPC with the \"Motor Génesis,\" generates its stats with the \"Motor de Improvisación,\" generates its portrait with the \"Taller del Artista,\" and drags it onto the VTT as a functional token, all within seconds.\
    \
    #### **28.3 El Onboarding para la IA (\"El Viaje del Creador Aumentado\")**\
    - [ ] Develop a new set of interactive tutorials specifically for the AI features.\
    - [ ] Create guides and tooltips on \"prompt engineering\" to teach users how to get the best results from the generative tools.\
    \
    ### **Capítulo 29: La Frontera Final - \"The Oracle Engine\" y el Ecosistema Auto-mejorado**\
    **Objetivo Estratégico:** Abrir el mercado del juego en solitario y establecer una plataforma que aprende y mejora por sí misma.\
    \
    #### **El Desarrollo del \"Oracle Engine\"**\
    - [ ] Implement the core logic for an AI to act as a GM, using pre-made modules from the Marketplace as its source material.\
    - [ ] Develop a new \"Solo Play\" mode in the application that allows a single player to interact with the Oracle Engine.\
    - [ ] Evolve the engine to eventually run custom adventures using a GM's Worldforge data.\
    \
    #### **El Bucle de Retroalimentación de IA**\
    - [ ] Design and build an architecture for collecting anonymized, aggregated data on game interactions and outcomes (e.g., encounter difficulty ratings, popular plot hooks).\
    - [ ] Develop a system to use this data to fine-tune the AI models, continuously improving the quality and balance of its generations over time.\
    \
    #### **29.3 La Gobernanza de la Comunidad y la IA**\
    - [ ] Establish a formal charter for a new \"Vorpal Community Council.\"\
    - [ ] Invite top-tier creators ('Leyenda' level) and veteran GMs to join the council.\
    - [ ] Institute a regular meeting cadence for the council to provide feedback and advise on the ethical and functional roadmap of Vorpal's AI tools.",
    "vorpalActionPlan": "Of course. As an expert Project Management Assistant and technical writer, I will now generate the comprehensive Action Plan and Development Checklist for the Vorpal software project. All content is derived exclusively from the provided document, expanding each chapter's action points into a granular, step-by-step guide for the Project Director.\
    \
    # Vorpal: Action Plan and Development Checklist\
    \
    ## Época I: Fundación y Validación\
    \
    ### Operaciones de la Pista Cero:\
     Paralelamente al desarrollo del MVP, las operaciones de negocio se centrarán en Marketing Orgánico Fundacional. Esto incluye la creación de perfiles en redes sociales clave, la participación en comunidades de TTRPG para construir reputación (sin vender) y la gestión directa del feedback como el 'equipo de soporte' fundador.\
    \
    ---\
    \
    ### **Capítulo 1: La Fundación Técnica y Metodológica**\
    **Objetivo Estratégico:** Establecer un entorno de desarrollo profesional y un flujo de trabajo claro que garantice la escalabilidad y la eficiencia desde el primer día.\
    \
    #### **El Taller Local: Configuración del Entorno**\
    - [ ] Install Visual Studio Code on the Lenovo G50 development machine.\
    - [ ] Configure VS Code with essential extensions for web development (e.g., Prettier, ESLint, Live Server).\
    - [ ] Initialize the project folder structure for the Vanilla Stack: `index.html`, `css/style.css`, `js/main.js`.\
    - [ ] Create and configure `.eslintrc.json` and `.prettierrc` files to enforce consistent code style and quality from the first line of code.\
    \
    #### **1.4 La Doctrina del Presupuesto de Rendimiento y Accesibilidad**\
    - [ ] Document the official Performance and Accessibility Budget in the project's `README.md`.\
    - [ ] Establish a protocol to run Google Lighthouse audits before every major feature merge, using the Lenovo G50 on a throttled 3G connection as the benchmark environment.\
    - [ ] Implement immediate visual feedback (e.g., loading states, button disabled states) for every user interaction to comply with the <100ms response time rule.\
    \
    #### **El Puente a la Nube: Git y Despliegue Inicial**\
    - [ ] Initialize a local Git repository in the project folder (`git init`).\
    - [ ] Create a new public repository on GitHub named `vorpal-player`.\
    - [ ] Create a comprehensive `.gitignore` file to exclude unnecessary files (e.g., OS-specific files, local configuration).\
    - [ ] Link the local repository to the remote GitHub repository.\
    - [ ] Configure the repository's settings to enable GitHub Pages, deploying from the `main` branch.\
    - [ ] Perform the initial commit of the boilerplate project and push to GitHub.\
    - [ ] Verify that the initial `index.html` is successfully deployed and accessible via its GitHub Pages URL.\
    \
    #### **Nuestra Metodología: Flujo de Trabajo y Roles**\
    - [ ] Create a `METHODOLOGY.md` file in the root of the repository.\
    - [ ] Formally define the role and responsibilities of the \"Director de Producto/Desarrollador IA\" within `METHODOLOGY.md`.\
    - [ ] Document the \"Sprint de desarrollo basado en prompts\" cycle, specifying its duration, key ceremonies (e.g., weekly planning, daily sync), and task management process using GitHub Issues.\
    \
    ### **Capítulo 2: El Prototipo Funcional - El Núcleo de Vorpal Player**\
    **Objetivo Estratégico:** Construir la primera versión funcional e interactiva del producto, enfocándose en la experiencia del usuario final sin la complejidad de la persistencia de datos.\
    \
    #### **La Arquitectura Visual (HTML/CSS)**\
    - [ ] Develop the semantic HTML structure for the main application interface, including containers for character stats, inventory, and notes.\
    - [ ] Implement a responsive CSS layout using modern techniques (Flexbox/Grid) to ensure usability on desktop and mobile devices.\
    - [ ] Style all core UI elements (buttons, inputs, text areas) to establish the initial visual identity of Vorpal.\
    \
    #### **La Lógica de Interacción (JavaScript)**\
    - [ ] Implement JavaScript functions to dynamically create new content blocks (e.g., a new skill, a new inventory item) in the DOM.\
    - [ ] Implement JavaScript functions to delete content blocks from the DOM.\
    - [ ] Implement drag-and-drop functionality to allow users to visually reorganize content blocks on their character sheet.\
    - [ ] Ensure all DOM manipulations are efficient to maintain adherence to the performance budget.\
    \
    ### **Capítulo 3: La Implementación de la \"Memoria\" - Persistencia de Datos**\
    **Objetivo Estratégico:** Transformar el prototipo en una herramienta útil, asegurando que el trabajo del usuario se guarde y se restaure de manera fiable.\
    \
    #### **3.1 El Diseño del Esquema de Datos v1.0 (Principio de Escalabilidad)**\
    - [ ] Design the primary JSON object structure for a character sheet in a separate design document (`SCHEMA.md`).\
    - [ ] Assign a field for a unique ID (UUID) to every primary entity (character, block, item, skill) within the JSON schema.\
    - [ ] Structure the schema to anticipate future relationships (e.g., `campaignId`, `gmId`), even if they will be null in v1.0, to facilitate future migration.\
    \
    #### **El Modelo de Datos y el Motor de Guardado/Carga**\
    - [ ] Implement a JavaScript module to manage the application's state, representing the character sheet based on the defined JSON schema.\
    - [ ] Develop a `saveState()` function that serializes the current application state object into a JSON string and saves it to the browser's `localStorage`.\
    - [ ] Develop a `loadState()` function that retrieves the JSON string from `localStorage`, parses it, and repopulates the application's state and UI on page load.\
    - [ ] Implement an auto-save mechanism that triggers the `saveState()` function on any significant data change.\
    \
    #### **3.3 El Diseño del Esquema de Datos para Eventos y Logros**\
    - [ ] Within `SCHEMA.md`, design a simple, generic JSON structure for tracking anonymous user events (e.g., `{ event: 'character_created', timestamp: '...' }`).\
    - [ ] Document this event schema, noting it is for future implementation of the gamification system and will not be implemented in Época I.\
    \
    ### **Capítulo 4: El Producto Mínimo Viable (MVP) - Finalización y Pulido**\
    **Objetivo Estratégico:** Completar el conjunto de características del MVP y realizar una fase de pruebas internas para asegurar un lanzamiento de calidad.\
    \
    #### **Las Funciones de Portabilidad**\
    - [ ] Implement an \"Export Character\" button that serializes the current character state into a JSON string and triggers a browser download of a `.json` file.\
    - [ ] Implement an \"Import Character\" button that opens a file picker, reads a selected `.json` file, validates its structure, and loads it into the application state.\
    \
    #### **La Fase de Alpha Interna**\
    - [ ] Create a test plan checklist in a new `TESTING.md` file, covering all core functionalities.\
    - [ ] Execute the test plan with the founding team (you and your girlfriend), documenting every bug or UI/UX issue as a GitHub Issue.\
    - [ ] Prioritize and resolve all critical bugs identified during the alpha phase.\
    - [ ] Refine UI/UX based on feedback to ensure the application is intuitive before public release.\
    \
    ### **Capítulo 5: El Lanzamiento Público y la Creación de la Comunidad**\
    **Objetivo Estratégico:** Lanzar el MVP al mundo, atraer a los primeros usuarios (\"early adopters\") y establecer los canales y procesos para convertir su feedback en la hoja de ruta del futuro.\
    \
    #### **La Estrategia de Lanzamiento**\
    - [ ] Draft the launch announcement message, focusing on the mission of Vorpal (potenciating creativity, eliminating friction).\
    - [ ] Identify and select primary channels for the \"soft launch\" (e.g., specific subreddits, TTRPG forums).\
    - [ ] Execute the launch by posting the announcement on the selected channels.\
    \
    #### **La Infraestructura Comunitaria**\
    - [ ] Create the official Vorpal Discord server.\
    - [ ] Structure the Discord server with clear channels: `#announcements`, `#general`, `#bug-reports`, `#suggestions`, and `#showcase`.\
    \
    #### **El Bucle de Feedback**\
    - [ ] Establish a formal process for converting posts in `#bug-reports` and `#suggestions` into structured GitHub Issues.\
    - [ ] Create a template for responding to user feedback to ensure they feel heard and valued.\
    - [ ] Schedule and communicate a regular update cadence (e.g., weekly devlog in `#announcements`) to inform the community of progress.\
    \
    #### **5.4 El Lanzamiento de la \"Galería de Creaciones\" (Cultura del Creador)**\
    - [ ] Rename the `#showcase` channel to `#galeria-de-creaciones`.\
    - [ ] Post a pinned message in the channel actively encouraging users to share their exported `.json` character templates.\
    - [ ] Actively monitor this channel to identify potential \"Pioneer\" creators for future programs.\
    \
    #### **5.5 La Implementación del Andamiaje Legal Básico**\
    - [ ] Draft a basic Privacy Policy document, explaining that all data is stored locally in the browser.\
    - [ ] Draft a basic Terms of Service document from a standard template.\
    - [ ] Add links to both the Privacy Policy and Terms of Service in the application's footer.\
    \
    #### **5.6 La Introducción del Concepto de Gamificación**\
    - [ ] Incorporate the long-term vision of \"La Senda del Cronista\" into the launch messaging and community welcome messages.\
    - [ ] Create a discussion thread or channel to begin gathering community ideas about potential achievements and rewards.\
    \
    #### **Estrategia de Construcción de Marca**\
    - [ ] Ensure all public communication consistently reinforces the core mission of Vorpal.\
    - [ ] Engage actively and positively with every community member in Discord to build a reputation for being responsive and user-focused.\
    \
    ## Época II: Comercialización y Conexión\
    \
    ### Operaciones de la Pista Cero:\
     Con el lanzamiento comercial, la Pista Cero evoluciona a Crecimiento y Soporte Inicial. Esto implica establecer un sistema de tickets de soporte básico (puede ser un canal de Discord o un email), empezar a crear contenido de valor (posts de blog, tutoriales en video) y analizar las primeras métricas de conversión.\
    \
    ---\
    \
    ### **Ritual de Época II: El Bucle de Inteligencia Competitiva**\
    - [ ] Analyze all community feedback from Época I to create a ranked list of the most and least valued features of the MVP.\
    - [ ] Research the pricing pages and feature tiers of at least 3 successful freemium productivity tools (both within and outside the TTRPG space).\
    - [ ] Identify the top 5-10 most active and constructive members of the Discord community as candidates for the Closed Beta.\
    - [ ] Synthesize all findings into a design document that will guide the feature set and pricing for \"Plus\" and \"Pro\" subscriptions.\
    \
    ### **Capítulo 6: La Infraestructura Técnica del Negocio**\
    **Objetivo Estratégico:** Construir la columna vertebral técnica que soportará las cuentas de usuario, los datos en la nube y las transacciones financieras.\
    \
    #### **La Transición a la Nube**\
    - [ ] Evaluate and select a Backend as a Service (BaaS) provider (Firebase or Supabase).\
    - [ ] Set up the BaaS project, including development and production environments.\
    - [ ] Design and implement the database schema for `users` (linking to auth ID) and `characters` (linking to a `userId`).\
    - [ ] Integrate the BaaS SDK into the Vorpal codebase.\
    \
    #### **El Sistema de Autenticación**\
    - [ ] Implement the UI components for user registration, login, and password reset.\
    - [ ] Integrate the BaaS authentication service to handle user creation and session management.\
    - [ ] Implement logic to show/hide UI elements based on the user's authentication state.\
    - [ ] Refactor the data persistence logic to save/load character data from the cloud for authenticated users, while retaining `localStorage` functionality for anonymous users.\
    \
    #### **La Integración de la Pasarela de Pagos**\
    - [ ] Create a Stripe developer account and configure API keys.\
    - [ ] Define the subscription products (\"Vorpal Plus\", \"GM Pro\") in the Stripe dashboard.\
    - [ ] Implement a serverless backend function (e.g., Cloud Function) to handle Stripe webhook events (`invoice.payment_succeeded`, `customer.subscription.deleted`, etc.).\
    - [ ] Implement the front-end interface for users to select a plan and complete the checkout process using Stripe.js.\
    - [ ] Implement logic in the backend webhook to update a user's subscription status in the application database.\
    \
    #### **6.4 La Integración de Analítica de Privacidad**\
    - [ ] Select and integrate a privacy-focused analytics tool (e.g., Plausible, Fathom).\
    - [ ] Implement anonymous event tracking for key user interactions (e.g., `feature_used_X`, `subscription_page_viewed`).\
    - [ ] Create a dashboard to monitor key metrics without collecting any Personally Identifiable Information (PII).\
    \
    #### **6.5 La Construcción del Motor de Gamificación v1.0**\
    - [ ] Design the database schema for the gamification system: a `user_achievements` table/collection to link `userId` with `achievementId`.\
    - [ ] Create a service (e.g., a set of serverless functions) to process incoming user events against a predefined set of achievement rules.\
    - [ ] Develop an API endpoint for the client application to query and retrieve a user's unlocked achievements and corresponding rewards.\
    \
    ### **Capítulo 7: Pista del Jugador (v2.0) - El Producto Mínimo Suscribible**\
    **Objetivo Estratégico:** Crear la primera oferta de pago para nuestra base de usuarios más grande, probando su disposición a pagar por conveniencia y personalización.\
    \
    #### **El Desarrollo de \"Vorpal Plus\"**\
    - [ ] Implement the cloud synchronization feature for character sheets.\
    - [ ] Develop the UI for a library of visual themes and dice skins.\
    - [ ] Implement the advanced character chronicle feature, logging significant events or changes to the character sheet.\
    \
    #### **La Arquitectura de Permisos**\
    - [ ] Develop a client-side function `hasActiveSubscription('plus')` that checks the user's status from the database.\
    - [ ] Wrap all \"Vorpal Plus\" features in conditional logic that checks for an active subscription before rendering or enabling them.\
    - [ ] Implement UI \"upsells\" that prompt free users to subscribe when they attempt to access a premium feature.\
    \
    #### **7.3 La Itroducción de Ganchos de Compromiso**\
    - [ ] Implement the first set of simple achievements for all users (e.g., 'First Character Created', 'Used Vorpal for 7 days').\
    - [ ] Develop a basic UI element to notify users when they have unlocked an achievement.\
    \
    #### **7.4 La Activación de 'La Senda del Aventurero' (Fase 1)**\
    - [ ] Define the rules for the first 10 player-focused achievements in the gamification backend.\
    - [ ] Develop the UI in Vorpal Player for an \"Achievements\" page, showing locked/unlocked achievements and their rewards.\
    - [ ] Implement the logic to automatically apply unlocked cosmetic rewards (themes, dice skins) to the user's account.\
    \
    ### **Capítulo 8: Pista del GM (v1.0) - El Producto Mínimo Vendible**\
    **Objetivo Estratégico:** Construir y definir la oferta principal que será nuestro motor de ingresos recurrente, resolviendo los problemas más agudos del Director de Juego.\
    \
    #### **El Desarrollo de \"GM Pro\"**\
    - [ ] Develop a new application view for the \"GM Dashboard\" to manage multiple campaigns and players.\
    - [ ] Implement the \"Campaign Codex\" feature, allowing GMs to create and organize unlimited campaign notes, NPCs, and locations in the cloud.\
    - [ ] Build the session preparation tools, such as encounter builders and loot generators.\
    \
    #### **8.4 La Primera Integración de IA Experimental**\
    - [ ] Select and obtain an API key for a lightweight, low-cost AI language model.\
    - [ ] Implement a simple \"NPC Name Generator\" button within the Campaign Codex.\
    - [ ] Develop the backend function to call the AI API and return a list of names to the GM's interface.\
    - [ ] Track usage of this feature with the anonymous analytics tool to measure community interest.\
    \
    #### **8.5 La Activación de 'La Senda del Guardián' (Fase 1)**\
    - [ ] Define the rules for the first set of GM-focused achievements (e.g., 'Ran First Session', 'Created 10 NPCs') in the gamification backend.\
    - [ ] Develop the UI in the GM Dashboard to display these achievements.\
    - [ ] Implement a system of unlockable \"Titles\" and \"Emblems\" that are displayed on the GM's public-facing community profile.\
    \
    ### **Capítulo 9: El Puente Conector - La Sinergia en Tiempo Real**\
    **Objetivo Estratégico:** Desarrollar la \"magia\" tecnológica que conecta a jugadores y GMs, creando una propuesta de valor única.\
    \
    #### **La Arquitectura de Datos en Tiempo Real**\
    - [ ] Redesign the database schema to support many-to-many relationships between `campaigns`, `gms`, and `players`.\
    - [ ] Structure the data to allow a GM to have read/write permissions over specific parts of their players' character sheets (e.g., HP, status effects).\
    - [ ] Implement security rules in the BaaS to ensure users can only access data they are explicitly permitted to.\
    \
    #### **La Implementación de \"Listeners\"**\
    - [ ] Refactor the application's data-fetching logic to use real-time listeners (e.g., Firestore's `onSnapshot`, Supabase's Realtime) instead of one-time queries.\
    - [ ] Ensure that any change made by the GM to a player's sheet is instantly reflected on the player's screen, and vice-versa.\
    - [ ] Optimize the listeners to minimize data transfer and client-side processing.\
    \
    ### **Capítulo 10: La Prueba de Fuego - La Fase Beta Cerrada**\
    **Objetivo Estratégico:** Probar la estabilidad de la nueva infraestructura conectada y validar la percepción de valor de nuestras ofertas de pago.\
    \
    #### **La Estrategia de la Beta**\
    - [ ] Contact the pre-selected community champions and invite them to the Closed Beta.\
    - [ ] Create a private Discord channel exclusively for beta testers.\
    - [ ] Provide beta testers with free access to \"Vorpal Plus\" and \"GM Pro\" for the duration of the test.\
    \
    #### **El Bucle de Iteración de la Beta**\
    - [ ] Create and distribute a structured feedback form for testers covering usability, bugs, perceived value, and pricing suggestions.\
    - [ ] Schedule weekly sync-up calls with the beta group to discuss findings.\
    - [ ] Create and prioritize GitHub issues based on beta feedback.\
    - [ ] Iterate on the feature set and refine the pricing model based on the collected data before the public launch.\
    \
    ### **Capítulo 11: La Apertura de Puertas - El Lanzamiento Público de la Plataforma Comercial**\
    **Objetivo Estratégico:** Lanzar oficialmente las suscripciones \"Vorpal Plus\" y \"GM Pro\" a toda la base de usuarios.\
    \
    #### **La Estrategia de Comunicación del Lanzamiento**\
    - [ ] Draft a launch announcement that clearly explains the new paid features while reassuring users about the value and continued support of the free tier.\
    - [ ] Prepare a comprehensive FAQ addressing questions about subscriptions, data, and the future of the platform.\
    - [ ] Post the announcement across all channels (Discord, social media, blog).\
    \
    #### **El Proceso de \"Onboarding\" para Clientes**\
    - [ ] Design and implement a smooth, multi-step UI flow for purchasing and activating a subscription.\
    - [ ] Create a user-friendly \"Account Management\" page where users can view their subscription status, update payment methods, and cancel.\
    \
    #### **11.3 La Creación del \"Viaje del GM\" (Onboarding)**\
    - [ ] Develop a series of interactive, contextual tooltips that appear the first time a new \"GM Pro\" subscriber uses a key feature.\
    - [ ] Create a \"Welcome to GM Pro\" guide that walks the user through connecting their first player and using the Campaign Codex.\
    \
    ## Época III: Expansión y Creación del Ecosistema\
    \
    ### Operaciones de la Pista Cero:\
     Con la expansión del ecosistema, la Pista Cero se enfoca en Escala Comunitaria y Desarrollo de Negocio. Aquí se ejecuta el plan de la primera contratación (Community Manager) y se comienzan a explorar alianzas estratégicas (con influencers, otros creadores de herramientas, etc.).\
    \
    ---\
    \
    ### **Ritual de Época III: El Bucle de Inteligencia Competitiva**\
    - [ ] Conduct a competitive analysis of World Anvil, LegendKeeper, and other world-building tools, identifying their key strengths and user-reported weaknesses.\
    - [ ] Analyze the business models of content marketplaces like DriveThruRPG and DMsGuild, focusing on commission structures, content curation, and creator promotion.\
    - [ ] Review the content shared in the `#galeria-de-creaciones` channel to identify the most popular types of homebrew content, which will inform the prioritization of Worldforge \"Ficha\" types.\
    - [ ] Compile these findings into a Product Requirements Document for Worldforge and the Marketplace.\
    \
    ### **Capítulo 12: Pista de Worldforge (v1.0) - La Construcción de la Forja Creativa**\
    **Objetivo Estratégico:** Construir el pilar tecnológico que permitirá la creación de contenido estructurado y de alta calidad.\
    \
    #### **La Arquitectura de \"Fichas\"**\
    - [ ] Design a flexible, NoSQL-friendly database schema for modular content \"Fichas\" (e.g., Faction, City, Magic System).\
    - [ ] Develop a dynamic UI that can render forms and views based on a selected \"Ficha\" template.\
    - [ ] Implement the core create, read, update, and delete (CRUD) functionality for these Fichas.\
    \
    #### **El Modelo de Monetización Nativo**\
    - [ ] Implement a feature flag system to limit the number of Fichas a free user can create.\
    - [ ] Develop the e-commerce logic for one-time purchases of \"Paquetes de Fichas\".\
    - [ ] Create a new \"Worldforge Pro\" subscription tier in Stripe and the application backend, unlocking unlimited Ficha creation.\
    \
    ### **Capítulo 13: La Infraestructura del Mercado - La Construcción de la Economía**\
    **Objetivo Estratégico:** Desarrollar la infraestructura de e-commerce que permitirá a los creadores vender sus creaciones.\
    \
    #### **13.1 El Andamiaje Legal del Mercado**\
    - [ ] Draft the \"Creator Terms of Service\" document, clearly outlining intellectual property rights, content policies, and commission structures.\
    - [ ] Integrate a mandatory acceptance checkbox for these terms into the creator onboarding flow.\
    \
    #### **El Portal del Creador**\
    - [ ] Design and build a \"Creator Dashboard\" UI.\
    - [ ] Implement functionality for creators to upload content packages, add product descriptions and images, and set pricing.\
    - [ ] Develop a view for creators to see their sales data and earning statements.\
    \
    #### **El Sistema de Transacciones y Comisiones**\
    - [ ] Integrate Stripe Connect to handle payouts to creators.\
    - [ ] Develop a backend process that, upon a successful purchase, automatically calculates and allocates Vorpal's commission and the creator's share.\
    - [ ] Implement the logic for the tiered commission rates of \"La Senda del Creador\".\
    \
    #### **El Escaparate Público**\
    - [ ] Design and build the public-facing Marketplace UI, including category browsing, search functionality, and product detail pages.\
    - [ ] Implement a user rating and review system for marketplace products.\
    \
    #### **13.4 La Integración del Motor de Gamificación en el Mercado**\
    - [ ] Extend the gamification engine to include creator-specific achievements (e.g., 'First Sale', '100 Sales', 'Published 5 Products').\
    - [ ] Integrate creator levels ('Aspirante', 'Maestro') as achievements that are publicly displayed as badges on their profile and product pages.\
    \
    ### **Capítulo 14: El Programa de Pioneros - Sembrando el Ecosistema**\
    **Objetivo Estratégico:** Resolver el problema del \"mercado vacío\" al lanzar, asegurando un catálogo de contenido de alta calidad desde el primer día.\
    \
    #### **La Estrategia de Reclutamiento**\
    - [ ] Create a list of top candidates for the \"Pioneer Program\" from the most active creators in the Discord community.\
    - [ ] Draft a formal invitation outlining the program's benefits.\
    - [ ] Contact the selected candidates personally to invite them.\
    \
    #### **El Paquete de Incentivos**\
    - [ ] Implement the technical infrastructure to grant \"Pioneer\" accounts early access to Worldforge tools.\
    - [ ] Configure a 0% commission rate for all sales made by Pioneer accounts during the launch period.\
    - [ ] Design a \"Featured Pioneer\" section on the Marketplace homepage.\
    \
    #### **El Bucle de Feedback del Creador**\
    - [ ] Create a private Discord channel for the Pioneer Program members.\
    - [ ] Establish a direct line of communication for technical support and feedback on the Worldforge and Marketplace tools.\
    \
    #### **14.4 La Doctrina de la Simplicidad en las Herramientas del Creador**\
    - [ ] During feedback sessions with Pioneers, explicitly ask: \"Does this feature make it easier to publish high-quality content, or does it add unnecessary complexity?\"\
    - [ ] Ruthlessly prioritize development based on feedback that aligns with simplifying the creator workflow.\
    \
    ### **Capítulo 15: Pista del GM (v2.0) - La Integración del Ecosistema**\
    **Objetivo Estratégico:** Aumentar drásticamente el valor de la suscripción \"GM Pro\" al integrarla con el nuevo contenido del ecosistema.\
    \
    #### **La Pestaña del Mercado**\
    - [ ] Implement a new \"Marketplace\" tab within the Vorpal GM interface that displays a curated view of available products.\
    \
    #### **El Motor de Importación \"One-Click\"**\
    - [ ] Develop a function that, upon purchase, automatically parses a marketplace content package and imports its contents into the GM's Campaign Codex.\
    - [ ] Ensure the process is seamless and requires no manual data entry from the GM.\
    \
    #### **La Evolución del Códice**\
    - [ ] Refactor the Campaign Codex UI and data models to natively handle the complex, structured data imported from Worldforge (e.g., linked NPCs, location maps).\
    \
    ### **Capítulo 16: Pista del Jugador (v2.1) - El Beneficiario del Ecosistema**\
    **Objetivo Estratégico:** Asegurar que la evolución de la plataforma beneficie directamente a los jugadores.\
    \
    #### **La Integración del Mercado en Vorpal Player**\
    - [ ] Add a section in Vorpal Player for browsing and purchasing player-centric content from the Marketplace (e.g., character sheet templates, themes).\
    - [ ] Implement the \"one-click install\" functionality for these assets.\
    \
    #### **La Mejora de la Creación de Personajes**\
    - [ ] Develop the permission system that allows a GM to share specific content from their purchased \"world-kits\" (e.g., new spells, classes) with players in their campaign.\
    - [ ] Implement the UI for players to browse and import this GM-approved content directly into their character sheets.\
    \
    #### **16.3 La Planificación de la Transición de Fundadores a Equipo**\
    - [ ] Draft a detailed job description for a \"Community & Support Manager\" role.\
    - [ ] Create a formal \"Volunteer Moderator Program\" document, outlining roles, responsibilities, and rewards.\
    \
    ### **Capítulo 17: El Lanzamiento Público del Ecosistema Vorpal**\
    **Objetivo Estratégico:** Comunicar la transformación de Vorpal de una herramienta a una plataforma.\
    \
    #### **La Estrategia de Marketing de Expansión**\
    - [ ] Design and execute targeted ad campaigns aimed at new audiences like world-builders and TTRPG writers.\
    - [ ] Prepare marketing copy that highlights the benefits of Worldforge and the Marketplace.\
    \
    #### **El Evento de Lanzamiento**\
    - [ ] Plan and schedule a live-streamed launch event on platforms like Twitch or YouTube.\
    - [ ] Coordinate with \"Pioneer\" creators to showcase their content during the event.\
    \
    #### **17.3 La Implementación del Motor de Curación y Descubrimiento v1.0**\
    - [ ] Develop the backend tools for internal staff to tag products for the \"Selección Vorpal\" (Staff Picks) feature.\
    - [ ] Ensure creator tier badges ('Maestro', 'Leyenda') are prominently displayed on product cards and search results as a signal of quality.\
    \
    #### **Estrategia de Construcción de Marca**\
    - [ ] Create a content calendar for blog posts and videos focused on teaching creative skills (e.g., \"How to Design a Memorable Villain\").\
    - [ ] Produce and publish case studies or interviews highlighting the success stories of Pioneer creators on the platform.\
    \
    ### **Capítulo 17.5: El Ritual del Jardín Cuidado**\
    **Objetivo Estratégico:** Formalizar el proceso de revisión del producto para combatir el 'bloatware'.\
    \
    - [ ] Analyze usage data from the privacy-focused analytics tool to identify the least-used features in Vorpal Player and GM.\
    - [ ] For each identified feature, conduct a formal review to decide whether to improve its usability or deprecate and remove it entirely.\
    - [ ] Document the decisions and communicate any removals transparently to the community.\
    - [ ] Schedule this \"Product Pruning\" ritual in the project calendar to occur at the end of every future Época.\
    \
    ## Época IV: Unificación y Escala\
    \
    ### Operaciones de la Pista Cero:\
     Con la unificación, la Pista Cero se convierte en un Equipo de Crecimiento Formal. Se exploran canales de marketing de pago, se optimiza el embudo de ventas y se establecen KPIs (Indicadores Clave de Rendimiento) de negocio más robustos.\
    \
    ---\
    \
    ### **Ritual de Época IV: El Bucle de Inteligencia Competitiva**\
    - [ ] Scrape and analyze user reviews and forum posts for Roll20, Foundry VTT, and Fantasy Grounds to compile a list of the most common user complaints (performance, UI/UX, cost).\
    - [ ] Research and prototype with modern real-time communication technologies (WebSockets, WebRTC) to evaluate their suitability for a VTT.\
    - [ ] Survey existing \"GM Pro\" subscribers to gauge demand for a VTT and to rank their most-desired VTT features.\
    - [ ] Use these findings to create a VTT development roadmap focused on solving existing market pain points, not just replicating features.\
    \
    ### **Capítulo 18: La Infraestructura de la Unificación - La Re-arquitectura del Backend**\
    **Objetivo Estratégico:** Evolucionar la infraestructura para manejar interacciones complejas y multi-usuario en tiempo real.\
    \
    #### **Análisis de Tecnologías de Tiempo Real**\
    - [ ] Conduct a formal evaluation of WebSocket libraries and managed services to select the core technology for the VTT's real-time layer.\
    - [ ] Design the architecture for a more robust backend service capable of handling persistent connections from multiple clients in a game session.\
    \
    #### **El Modelo de Datos Unificado**\
    - [ ] Redesign the database schema to create a single, coherent data universe where a \"world,\" \"campaign,\" and \"characters\" are tightly linked views of the same underlying data.\
    - [ ] Ensure the new schema can efficiently support real-time queries for a VTT session (e.g., token positions, player cursors).\
    \
    #### **El Plan de Migración**\
    - [ ] Write and test scripts to migrate all existing user data from the old schema to the new unified model.\
    - [ ] Plan a maintenance window for the migration and a communication strategy to inform users of the scheduled downtime.\
    \
    #### **18.4 El Mandato de la Documentación Técnica**\
    - [ ] For every new backend service or major data model, create a corresponding technical documentation page in a shared knowledge base (e.g., Confluence, Notion, or a `docs/` folder in the repo).\
    - [ ] Make \"write the docs\" a required step in the definition of \"done\" for all backend development tasks.\
    \
    ### **Capítulo 19: Pista del VTT (v0.5) - El Tablero de Batalla Compartido (Prueba de Concepto)**\
    **Objetivo Estratégico:** Probar la nueva infraestructura de tiempo real con una funcionalidad de bajo riesgo.\
    \
    #### **El Desarrollo del \"Battlemap Helper\"**\
    - [ ] Implement a new view within \"GM Pro\" where a GM can upload an image file as a battlemap.\
    - [ ] Add functionality for the GM to overlay a square or hex grid on the map.\
    - [ ] Implement the real-time sharing mechanism so that connected players see the map and grid.\
    - [ ] Develop a simple \"ping\" tool that allows the GM to place temporary markers on the map, visible to all players in real-time.\
    \
    #### **La Medición del Rendimiento**\
    - [ ] Integrate performance monitoring tools (e.g., server load, message latency, client-side frame rate) into the \"Battlemap Helper\".\
    - [ ] Organize stress-test sessions with internal and beta users to identify and resolve performance bottlenecks under real-world load.\
    \
    ### **Capítulo 20: Pista del VTT (v1.0) - La Mesa Virtual Integrada**\
    **Objetivo Estratégico:** Construir y lanzar la primera versión completa de nuestro VTT, enfocada en la simplicidad y la velocidad.\
    \
    #### **20.3 La Aplicación de la Doctrina de la Simplicidad al VTT**\
    - [ ] Create an \"Anti-Features\" list document, explicitly stating complex features (e.g., dynamic lighting, advanced macros) that will NOT be included in v1.0.\
    - [ ] Establish a feature review process where every proposed VTT feature is strictly evaluated against the question: \"Does this eliminate more friction than it adds complexity?\"\
    \
    #### **El Desarrollo del Núcleo del VTT**\
    - [ ] Implement the full map and grid system with support for layers (e.g., GM-only layer, player layer).\
    - [ ] Develop the token system, allowing GMs to place tokens on the map that are directly linked to character or monster data from the Campaign Codex.\
    - [ ] Implement player control of assigned tokens.\
    - [ ] Build a shared, real-time dice roller with a visible log for all participants.\
    - [ ] Create basic VTT tools: measurement (ruler), and a persistent campaign chat log.\
    \
    #### **La Filosofía de la Interfaz**\
    - [ ] Design a clean, minimal VTT interface that prioritizes the map and minimizes UI chrome.\
    - [ ] Ensure all core functions are accessible with a minimum number of clicks, adhering to the project's foundational principle of eliminating friction.\
    \
    ### **Capítulo 21: La Convergencia del Ecosistema - La Evolución de los Pilares**\
    **Objetivo Estratégico:** Rediseñar los pilares existentes para que converjan con el VTT en una experiencia simbiótica.\
    \
    #### **Pista de Worldforge (v2.0) - El Taller del Cartógrafo**\
    - [ ] Implement a simple, tile-based map creator within Worldforge.\
    - [ ] Develop an asset manager for uploading and organizing VTT assets (tokens, map tiles, textures).\
    - [ ] Extend the Marketplace to support a new product category: \"VTT Asset Packs.\"\
    \
    #### **Pista del Jugador (v3.0) - La Interfaz del Aventurero**\
    - [ ] Develop a \"VTT View\" for the Vorpal Player character sheet, designed as a compact Heads-Up Display (HUD).\
    - [ ] Implement the ability for players to overlay this HUD on the VTT screen, allowing them to roll dice and track resources without switching tabs or windows.\
    \
    #### **21.3 La Evolución de 'La Senda del Cronista' (Gamificación Unificada)**\
    - [ ] Expand the gamification engine to support interconnected achievements.\
    - [ ] Implement rules for new achievements, such as a GM achievement for using a marketplace map in a VTT session.\
    - [ ] Implement an achievement for a creator when their monster asset is used for the first time in a VTT combat.\
    \
    ### **Capítulo 22: El Modelo de Negocio Unificado**\
    **Objetivo Estratégico:** Definir y estructurar la nueva oferta comercial que refleje el valor de la plataforma unificada.\
    \
    #### **La Creación de la Suscripción \"Vorpal Ultimate\"**\
    - [ ] Define a new \"Vorpal Ultimate\" subscription tier in Stripe and the backend that bundles all premium features: Player Plus, GM Pro, Worldforge Pro, and the Vorpal VTT.\
    - [ ] Update the application's permission system to recognize the new \"Ultimate\" tier.\
    \
    #### **La Estrategia de Precios y Actualización**\
    - [ ] Conduct a pricing analysis to determine a competitive yet profitable price point for the \"Ultimate\" tier.\
    - [ ] Design and implement a clear, prorated upgrade path for existing \"GM Pro\" and \"Worldforge Pro\" subscribers.\
    \
    ### **Capítulo 23: El Segundo Gran Lanzamiento - La Plataforma Unificada Vorpal**\
    **Objetivo Estratégico:** Ejecutar una campaña a gran escala para anunciar la transformación de Vorpal en una plataforma de juego online completa.\
    \
    #### **La Estrategia de Posicionamiento en el Mercado**\
    - [ ] Develop new marketing materials (website copy, ads, press releases) that consistently use the tagline: \"Vorpal: The world's most integrated roleplaying platform.\"\
    - [ ] Focus all messaging on the key differentiator: the seamless workflow from world-building to gameplay.\
    \
    #### **La Campaña de Lanzamiento**\
    - [ ] Produce high-quality video demonstrations of the complete, integrated workflow.\
    - [ ] Collaborate with TTRPG influencers for sponsored streams and reviews showcasing the unified platform.\
    - [ ] Plan and execute a launch-day promotion to incentivize new subscriptions and upgrades to the \"Ultimate\" tier.\
    \
    ## Época V: Inteligencia y Dominancia del Mercado\
    \
    ### Operaciones de la Pista Cero:\
     La Pista Cero es ahora un Equipo de Negocio Completo, con roles definidos para marketing, operaciones, finanzas y estrategia, asegurando la dominancia del mercado a largo plazo.\
    \
    ---\
    \
    ### **Ritual de Época V: El Bucle de Inteligencia Competitiva**\
    - [ ] Evaluate the cost, quality, and API policies of leading AI models (e.g., GPT series, Claude series, open-source alternatives) for both text and image generation.\
    - [ ] Analyze sentiment in the TTRPG community regarding AI in creative tools, identifying key ethical concerns and user desires.\
    - [ ] Review the usage data of the experimental \"NPC Name Generator\" to quantify user demand for more advanced AI features.\
    - [ ] Use these findings to create a strategic, ethical, and demand-driven roadmap for AI integration.\
    \
    ### **Capítulo 24: La Infraestructura de la Inteligencia - El Núcleo Neuronal de Vorpal**\
    **Objetivo Estratégico:** Construir la base técnica, ética y económica para la integración de la IA a gran escala.\
    \
    #### **24.4 El Andamiaje Legal y Ético de la IA**\
    - [ ] Draft and publish a clear \"AI Acceptable Use Policy\" and \"AI Data Policy.\"\
    - [ ] Ensure these policies transparently explain how anonymized data is used for model improvement and define the intellectual property rights of AI-generated content.\
    \
    #### **La Arquitectura de APIs de IA**\
    - [ ] Develop an internal \"AI Gateway\" service that acts as an abstraction layer between the Vorpal application and various third-party AI APIs.\
    - [ ] Design the gateway to allow for easy switching of AI providers or models with minimal code changes in the core application.\
    \
    #### **El Modelo Económico de \"Tokens\"**\
    - [ ] Implement a backend system to track the token consumption (cost) of every AI API call made by a user.\
    - [ ] Design a \"credit\" system for users, where subscriptions include a monthly allotment of AI credits, with options to purchase more.\
    \
    #### **La Política de Datos y Ética**\
    - [ ] Implement strict data anonymization processes for any data used to fine-tune models.\
    - [ ] Integrate content filters and safety mechanisms into the AI Gateway to prevent the generation of harmful or prohibited content.\
    \
    ### **Capítulo 25: Pista de Worldforge (v3.0) - El Socio Creativo (\"Motor Génesis\")**\
    **Objetivo Estratégico:** Transformar Worldforge de una herramienta de documentación a un socio de brainstorming activo.\
    \
    #### **La Implementación del Diálogo Creativo**\
    - [ ] Develop a chat-based UI within Worldforge that allows users to brainstorm ideas with an AI.\
    - [ ] Implement the logic to parse the AI's structured output and automatically populate new Worldforge Fichas (e.g., \"Create a faction of desert elves\" -> generates a Faction ficha).\
    \
    #### **La Generación de Contenido Aumentado**\
    - [ ] Add \"Generate Details\" buttons within specific fields of Worldforge Fichas.\
    - [ ] Implement contextual prompts that use the existing data in the ficha to generate relevant details (e.g., generate street names for a city ficha).\
    \
    #### **El Taller del Artista Conceptual**\
    - [ ] Integrate an image generation AI service via the AI Gateway.\
    - [ ] Develop a UI in Worldforge for users to write prompts and generate concept art for their worlds, characters, and locations.\
    \
    ### **Capítulo 26: Pista del GM (v3.0) - El Asistente de Improvisación (\"Motor de Improvisación\")**\
    **Objetivo Estratégico:** Otorgar al GM \"superpoderes\" de improvisación durante el juego.\
    \
    #### **El Generador de Entidades en Tiempo Real**\
    - [ ] Build a tool accessible from the VTT interface for the GM to generate a complete monster or NPC ficha (stats, description, abilities) with a single prompt.\
    - [ ] Ensure the generated ficha is immediately usable within the VTT and Campaign Codex.\
    \
    #### **El \"Pincel\" Narrativo**\
    - [ ] Implement quick-action buttons in the VTT for generating descriptive text for locations, environments, and sensory details (\"Describe a spooky forest\").\
    \
    ### **Capítulo 27: Pista del Jugador (v4.0) - El Aumento de la Inmersión (\"Motor de Persona\")**\
    **Objetivo Estratégico:** Utilizar la IA para ayudar a los jugadores a conectarse más profundamente con sus personajes.\
    \
    #### **El Taller del Personaje**\
    - [ ] Develop an AI-powered assistant in the character creation process that helps generate backstories, personality traits, and character voices based on user inputs.\
    \
    #### **El Sugeridor de Acciones**\
    - [ ] Implement an optional, player-controlled feature that analyzes the character's traits and the current game context to suggest potential actions or lines of dialogue.\
    \
    ### **Capítulo 28: La Convergencia Definitiva - El VTT Aumentado por IA**\
    **Objetivo Estratégico:** Unificar todas las herramientas de IA en la experiencia de juego en vivo.\
    \
    #### **La Interfaz de IA Unificada**\
    - [ ] Design and implement a single, consolidated AI panel within the VTT for the GM, providing access to all generation tools without leaving the game screen.\
    \
    #### **La Sinergia de los Motores**\
    - [ ] Create and refine the end-to-end workflow: a GM brainstorms an NPC with the \"Motor Génesis,\" generates its stats with the \"Motor de Improvisación,\" generates its portrait with the \"Taller del Artista,\" and drags it onto the VTT as a functional token, all within seconds.\
    \
    #### **28.3 El Onboarding para la IA (\"El Viaje del Creador Aumentado\")**\
    - [ ] Develop a new set of interactive tutorials specifically for the AI features.\
    - [ ] Create guides and tooltips on \"prompt engineering\" to teach users how to get the best results from the generative tools.\
    \
    ### **Capítulo 29: La Frontera Final - \"The Oracle Engine\" y el Ecosistema Auto-mejorado**\
    **Objetivo Estratégico:** Abrir el mercado del juego en solitario y establecer una plataforma que aprende y mejora por sí misma.\
    \
    #### **El Desarrollo del \"Oracle Engine\"**\
    - [ ] Implement the core logic for an AI to act as a GM, using pre-made modules from the Marketplace as its source material.\
    - [ ] Develop a new \"Solo Play\" mode in the application that allows a single player to interact with the Oracle Engine.\
    - [ ] Evolve the engine to eventually run custom adventures using a GM's Worldforge data.\
    \
    #### **El Bucle de Retroalimentación de IA**\
    - [ ] Design and build an architecture for collecting anonymized, aggregated data on game interactions and outcomes (e.g., encounter difficulty ratings, popular plot hooks).\
    - [ ] Develop a system to use this data to fine-tune the AI models, continuously improving the quality and balance of its generations over time.\
    \
    #### **29.3 La Gobernanza de la Comunidad y la IA**\
    - [ ] Establish a formal charter for a new \"Vorpal Community Council.\"\
    - [ ] Invite top-tier creators ('Leyenda' level) and veteran GMs to join the council.\
    - [ ] Institute a regular meeting cadence for the council to provide feedback and advise on the ethical and functional roadmap of Vorpal's AI tools.",