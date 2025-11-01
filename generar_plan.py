import os
import re
from dotenv import load_dotenv

# Importaciones de CrewAI y LangChain
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# --- FASE DE CONFIGURACIÓN ---
print("Iniciando la configuración del script...")

# 1. Cargar las variables de entorno (tu clave de API de Google)
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: La variable 'GOOGLE_API_KEY' no se encontró en el archivo .env.")
    exit()

# 2. Configurar el modelo de lenguaje (LLM) que usarán los agentes
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        verbose=True,
        temperature=0.5,
        google_api_key=api_key
    )
    print("-> [ÉXITO] Modelo de lenguaje (LLM) configurado.")
except Exception as e:
    print(f"ERROR: No se pudo inicializar el LLM. Detalles: {e}")
    exit()

# --- FUNCIONES DE AYUDA ---

def leer_archivo(nombre_archivo):
    """Función para leer el contenido de un archivo de forma segura."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"ADVERTENCIA: No se encontró el archivo '{nombre_archivo}'. Su contexto no será utilizado.")
        return ""

def guardar_archivo(ruta_carpeta, nombre_archivo, contenido):
    """Función para guardar contenido en un archivo, creando la carpeta si no existe."""
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
    with open(ruta_completa, 'w', encoding='utf-8') as f:
        f.write(contenido)
    print(f"-> Archivo guardado: {ruta_completa}")

def normalizar_nombre(titulo):
    """Convierte un título de capítulo en un nombre de archivo y carpeta válidos."""
    # Extraer Época y número de capítulo de forma robusta
    match_epoca = re.search(r'Época\s+([IVXLCDM]+)', titulo, re.IGNORECASE)
    epoca_id = match_epoca.group(1) if match_epoca else 'Desconocida'
    
    match_cap = re.search(r'(?:Capítulo\s+|(\d+)\.-Análisis)\s*(\d+)', titulo)
    cap_num = match_cap.group(2) if match_cap and match_cap.group(2) else (match_cap.group(1) if match_cap else 'X')

    # Limpiar el título para el nombre del archivo
    nombre_limpio = re.sub(r'[^a-zA-Z0-9\s-]', '', titulo)
    nombre_limpio = re.sub(r'\s+', '_', nombre_limpio) # Reemplazar espacios con guiones bajos
    partes_nombre = nombre_limpio.split('_')
    # Tomar las primeras 3-4 palabras significativas para el nombre del archivo
    nombre_corto = '_'.join(partes_nombre[3:7]) if len(partes_nombre) > 6 else '_'.join(partes_nombre[3:])

    carpeta = f"Epoca_{epoca_id}"
    archivo = f"Epoca_{epoca_id}-Capitulo_{cap_num}_{nombre_corto}.md"
    
    return carpeta, archivo


# --- CARGA DE CONTEXTO ---
print("\nCargando archivos de contexto...")
directivas_contenido = leer_archivo('DIRECTIVAS_MAESTRAS.md')
business_plan_contenido = leer_archivo('Vorpal_Business_Plan.md')
principios_diseno_contenido = leer_archivo('Principios de diseño.md')
blueprint_wolrdforge_contenido = leer_archivo('Blueprint base wolrdforge.md')
guia_contenido = leer_archivo('guia Vorpal para estructura.md')

if not directivas_contenido or not guia_contenido:
    print("ERROR: Los archivos 'DIRECTIVAS_MAESTRAS.md' y 'guia Vorpal para estructura.md' son esenciales. Saliendo.")
    exit()
print("-> [ÉXITO] Todos los archivos de contexto cargados.")

# --- DEFINICIÓN DE AGENTES (La Crew) ---
print("\nDefiniendo el equipo de agentes de IA...")

# Agente 1: El que entiende el panorama general
contextualizador = Agent(
    role='Contextualizador Estratégico',
    goal='Leer el texto de un capítulo específico y todos los documentos de referencia, y luego compilar un paquete de contexto conciso para el resto del equipo.',
    backstory='Eres el bibliotecario del proyecto Vorpal. Tu dominio de todos los documentos es absoluto. Tu función es asegurar que ningún agente trabaje sin el contexto completo y las directivas claras.',
    llm=llm, verbose=True
)

# Agente 2: El que define el 'QUÉ' y el 'PORQUÉ'
arquitecto_producto = Agent(
    role='Arquitecto de Producto',
    goal="Definir los objetivos estratégicos de un capítulo, su alineación con la filosofía Vorpal, los criterios de finalización y sus dependencias.",
    backstory='Eres un jefe de producto obsesionado con la coherencia y la visión estratégica. Traduces la estrategia en objetivos claros y medibles.',
    llm=llm, verbose=True
)

# Agente 3: El que define el 'CÓMO'
planificador_tecnico = Agent(
    role='Planificador Técnico',
    goal="Detallar las acciones técnicas concretas, los entregables esperados y las decisiones clave a tomar para un capítulo, respetando el stack tecnológico del proyecto.",
    backstory='Eres un ingeniero de software senior pragmático y metódico. Conviertes los objetivos de producto en un plan de acción ejecutable.',
    llm=llm, verbose=True
)

# Agente 4: El que se prepara para los problemas
analista_riesgos = Agent(
    role='Analista de Riesgos',
    goal="Identificar los riesgos potenciales (técnicos, de mercado, de recursos) para un capítulo y proponer estrategias de mitigación claras.",
    backstory='Eres un estratega veterano con una habilidad especial para anticipar problemas. Tu trabajo es asegurar que el proyecto esté preparado para cualquier eventualidad.',
    llm=llm, verbose=True
)

# Agente 5: El que une todo y le da formato
sintetizador_redactor = Agent(
    role='Sintetizador-Redactor',
    goal="Recibir las piezas de los otros agentes y ensamblarlas en un único documento Markdown coherente, bien estructurado y formateado según las directivas maestras.",
    backstory='Eres un editor técnico meticuloso. No creas contenido nuevo, sino que lo perfeccionas y estructuras. Eres el control de calidad final.',
    llm=llm, verbose=True, allow_delegation=False
)

# Agente 6: El Archivista del Sistema
archivista = Agent(
    role='Archivista del Sistema',
    goal="Tomar el texto final del Redactor y el título original del capítulo para guardarlo en la ubicación correcta con el nombre de archivo correcto.",
    backstory='Eres un autómata de sistemas, infalible en la organización de archivos. Tu única función es guardar el trabajo finalizado.',
    llm=llm, verbose=True, allow_delegation=False
)
print("-> [ÉXITO] Equipo de 6 agentes definido.")

# --- PROCESO PRINCIPAL ---
print("\nIniciando el proceso de automatización...")

# Dividir la guía en capítulos.
capitulos = re.split(r'\n(?=\d+\.-Análisis Detallado)', guia_contenido)
if len(capitulos) <= 1:
    capitulos = re.split(r'\n(?=Capítulo\s+\d+)', guia_contenido) # Intento alternativo de división

if len(capitulos) <= 1:
    print("ERROR: No se pudieron encontrar secciones de capítulo en 'guia Vorpal para estructura.md'. Revisa el formato.")
    exit()

# Bucle principal para procesar cada capítulo
for i, texto_capitulo in enumerate(capitulos):
    if not texto_capitulo.strip() or "Análisis Detallado" not in texto_capitulo:
        continue

    titulo_capitulo = texto_capitulo.strip().split('\n')[0]
    print(f"\n=============================================")
    print(f"Procesando Capítulo {i}: {titulo_capitulo}")
    print(f"=============================================")

    # Crear la "Crew" para este capítulo
    crew_capitulo = Crew(
        agents=[contextualizador, arquitecto_producto, planificador_tecnico, analista_riesgos, sintetizador_redactor, archivista],
        tasks=[],
        process=Process.sequential,
        verbose=2
    )

    # Definir las tareas dinámicamente
    task_contexto = Task(
        description=f"Analiza el siguiente texto del capítulo '{titulo_capitulo}' y todos los documentos de referencia para crear un resumen contextual completo. Texto del capítulo: '{texto_capitulo}'",
        agent=contextualizador,
        expected_output="Un documento de texto con el resumen del capítulo, sus objetivos principales y las directivas más relevantes para su desarrollo."
    )
    
    # ... (El resto de las tareas se definen aquí, pero por simplicidad para la primera prueba, podemos empezar con una tarea simple)
    # Por ahora, vamos a simplificar para la primera ejecución y solo generar el contenido completo
    
    task_completa = Task(
        description=f"Toma el texto del capítulo '{titulo_capitulo}' y, usando el contexto de TODOS los documentos proporcionados (Directivas, Business Plan, etc.), detallalo completamente. Debes seguir la estructura especificada en las DIRECTIVAS_MAESTRAS.md (Acciones Concretas, Entregables, Riesgos, etc.).",
        agent=sintetizador_redactor,
        context=[task_contexto], # El redactor usa el contexto del primer agente
        expected_output="El contenido completo y final del capítulo en formato Markdown."
    )

    task_guardado = Task(
        description=f"Toma el texto Markdown generado y el título original '{titulo_capitulo}'. Calcula la ruta y el nombre del archivo y guarda el contenido.",
        agent=archivista,
        context=[task_completa], # El archivista usa el resultado del redactor
        expected_output="Una confirmación de que el archivo ha sido guardado, incluyendo la ruta del archivo."
    )

    # Añadir tareas a la Crew
    crew_capitulo.tasks.extend([task_contexto, task_completa, task_guardado])

    # Ejecutar la Crew
    resultado_final = crew_capitulo.kickoff(inputs={
        'directivas_maestras': directivas_contenido,
        'plan_de_negocio': business_plan_contenido,
        'principios_de_diseno': principios_diseno_contenido,
        'blueprint_wolrdforge': blueprint_wolrdforge_contenido
    })
    
    print(f"--- Resultado final para '{titulo_capitulo}' ---")
    print(resultado_final)

print("\n=============================================")
print("PROCESO DE GENERACIÓN COMPLETADO.")
print("Revisa las nuevas carpetas 'Epoca_X' para ver los archivos .md detallados.")
print("=============================================")