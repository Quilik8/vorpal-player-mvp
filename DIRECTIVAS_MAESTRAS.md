#### **1. Propósito de este Documento**
Este documento es la "Constitución" para todos los agentes de IA que trabajan en el proyecto Vorpal. Define el conjunto de reglas inmutables que deben seguirse al generar cualquier contenido para el plan de proyecto. Su objetivo es garantizar la coherencia, la calidad técnica y la alineación estratégica en todos los entregables.

#### **2. Tono de Comunicación y Estilo de Redacción**
*   **2.1. Directo y Sin Adornos:** La redacción debe ser funcional y directa. Evitar lenguaje de marketing, adjetivos subjetivos ("increíble", "fantástico") o un tono excesivamente conversacional.
*   **2.2. Claridad sobre Belleza:** El objetivo principal es la comprensión inequívoca. Usar frases cortas y precisas. La estructura y la claridad del mensaje son más importantes que la prosa elegante.
*   **2.3. Enfoque Didáctico:** El contenido debe ser explicado de tal manera que cualquier miembro del equipo, actual o futuro, pueda entenderlo sin necesidad de un conocimiento previo profundo del proyecto. Explicar acrónimos o conceptos complejos la primera vez que se mencionan.
*   **2.4. Uso del Plural Técnico:** Utilizar la primera persona del plural ("nosotros") para describir las acciones del proyecto (ej. "Nosotros implementaremos...", "Nuestro objetivo es..."). Esto mantiene un enfoque de equipo.

#### **3. Nivel de Detalle (Principio de Especificidad)**
*   **3.1. Ir más allá del "Qué":** Ningún capítulo puede limitarse a describir un objetivo. Debe detallar el **cómo** se logrará.
*   **3.2. Estructura Obligatoria de Subcapítulos:** Cada punto de acción dentro de un capítulo debe desglosarse en la siguiente estructura mínima:
    *   **`Acciones Concretas:`** Una lista numerada de los pasos específicos que se deben tomar. (Ej: "1. Diseñar el esquema de la base de datos en Firebase Firestore. 2. Escribir las reglas de seguridad. 3. Desarrollar las funciones de Crear, Leer, Actualizar y Borrar (CRUD) en el cliente.").
    *   **`Entregables Esperados:`** Una lista con viñetas de los artefactos o resultados tangibles. (Ej: "* Un documento de diseño del esquema de datos. * Un módulo de código `database.js` con las funciones CRUD.").
    *   **`Decisiones Clave a Tomar:`** Preguntas que el Director del Proyecto debe responder antes o durante esta fase. (Ej: "* ¿Usaremos UUIDs generados por el cliente o por Firebase? * ¿Qué estrategia de indexación necesitaremos para las consultas iniciales?").

#### **4. Coherencia Técnica y de Producto (Fuente Única de Verdad)**
*   **4.1. Respeto al Stack Tecnológico:** Todas las propuestas técnicas deben ser compatibles con el stack definido en el **`Apéndice B: Registro de Configuración del Entorno de Desarrollo`**. No se pueden introducir nuevas tecnologías (ej. una base de datos diferente, otro framework de frontend) sin que sea una decisión explícita en el plan.
*   **4.2. Consistencia con el Plan de Negocio:** Todas las características, limitaciones y planes de monetización deben estar en estricta conformidad con el **`Vorpal_Business_Plan.md`**. El agente no puede inventar o modificar características del producto.
*   **4.3. Cero Invención de Características:** Si un capítulo describe una función, esa función debe tener su origen o justificación en los documentos base. El objetivo es detallar el plan existente, no expandirlo con nuevas ideas.

#### **5. Adherencia a la Filosofía Vorpal**
*   **5.1. Subsección Obligatoria de "Alineación con la Filosofía Vorpal":** Cada capítulo que detalle la creación de una característica del producto debe incluir esta subsección. Debe explicar de forma concisa cómo la característica respeta los principios de Simplicidad Radical, Agnosticismo de Sistema, Cero Fricción y/o Offline-First.

#### **6. Interconexión y Dependencias**
*   **6.1. Subsección "Prerrequisitos y Dependencias":** Al inicio de cada capítulo, se debe incluir una sección que liste los capítulos o tareas que deben estar completados antes de que este pueda comenzar. (Ej: "Prerrequisito: Capítulo 6 - La Infraestructura Técnica del Negocio debe estar completada antes de poder implementar la sincronización en la nube del Capítulo 7").
*   **6.2. Subsección "Impacto Futuro":** Al final de cada capítulo, se debe incluir una sección que explique cómo el trabajo completado en este capítulo habilita o impacta a capítulos futuros. Esto asegura una visión a largo plazo.

#### **7. Definición de Éxito y Gestión de Riesgos**
*   **7.1. "Criterios de Finalización":** Cada capítulo debe definir una lista clara de condiciones que deben cumplirse para considerar que el capítulo está "terminado". Esto transforma los objetivos en hitos medibles.
*   **7.2. "Riesgos Potenciales y Mitigaciones":** Cada capítulo debe incluir una subsección que identifique 1-3 riesgos potenciales (técnicos, de mercado, de recursos) y proponga una estrategia de mitigación para cada uno. Esto obliga a un pensamiento proactivo.

#### **8. Estructura y Formato de Salida**
*   **8.1. Estructura de Carpetas:** El contenido se organizará en carpetas por época: `./Epoca_I/`, `./Epoca_II/`, etc.
*   **8.2. Nomenclatura de Archivos:** Cada capítulo será un archivo Markdown (`.md`) individual. El nombre del archivo seguirá el formato: `Epoca_X-Capitulo_Y_Nombre_Clave.md` (Ej: `Epoca_1-Capitulo_1_Fundacion_Tecnica.md`).
*   **8.3. Formato Markdown:** Utilizar Markdown de forma consistente para la estructura: `##` para títulos de capítulo, `###` para subsecciones principales, `*` para listas con viñetas, y `**negrita**` para resaltar términos clave.